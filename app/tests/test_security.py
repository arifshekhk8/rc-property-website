import os
import secrets
import subprocess
import sys
from pathlib import Path

from django.test import SimpleTestCase, TestCase


class ConfigurationBoundaryTests(SimpleTestCase):
    def production_environment(self):
        env = os.environ.copy()
        for key in [
            "DJANGO_DEBUG",
            "DJANGO_SECRET_KEY",
            "DJANGO_ALLOWED_HOSTS",
            "DATABASE_URL",
            "DATABASE_SSLMODE",
        ]:
            env.pop(key, None)
        env.update(
            DJANGO_SECRET_KEY=secrets.token_urlsafe(64),
            DJANGO_ALLOWED_HOSTS="configuration-check.invalid",
            DATABASE_URL="postgresql://configuration-check.invalid/configuration_check",
            DATABASE_SSLMODE="require",
        )
        return env

    def import_wsgi(self, env):
        return subprocess.run(
            [sys.executable, "-c", "import config.wsgi"],
            cwd=Path(__file__).resolve().parents[1],
            env=env,
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )

    def test_wsgi_defaults_to_production_and_refuses_missing_secrets(self):
        env = self.production_environment()
        env.pop("DJANGO_SECRET_KEY")
        response = self.import_wsgi(env)
        self.assertNotEqual(response.returncode, 0)
        self.assertIn("DJANGO_SECRET_KEY is required", response.stderr)

    def test_production_refuses_unsafe_configuration(self):
        cases = [
            ({"DJANGO_SECRET_KEY": "short"}, "strong, unique production"),
            ({"DJANGO_SECRET_KEY": "x" * 64}, "strong, unique production"),
            ({"DJANGO_ALLOWED_HOSTS": ""}, "explicit production DJANGO_ALLOWED_HOSTS"),
            ({"DJANGO_ALLOWED_HOSTS": "*"}, "explicit production DJANGO_ALLOWED_HOSTS"),
            ({"DATABASE_URL": ""}, "PostgreSQL DATABASE_URL is required"),
            ({"DATABASE_URL": "sqlite:///local.sqlite3"}, "must identify PostgreSQL"),
            ({"DATABASE_SSLMODE": "disable"}, "PostgreSQL requires TLS"),
        ]
        for overrides, expected in cases:
            with self.subTest(fields=list(overrides)):
                response = self.import_wsgi({**self.production_environment(), **overrides})
                self.assertNotEqual(response.returncode, 0)
                self.assertIn(expected, response.stderr)

    def test_valid_production_configuration_loads_without_connecting_to_a_database(self):
        self.assertEqual(self.import_wsgi(self.production_environment()).returncode, 0)


class ResponsePrivacyTests(TestCase):
    def test_staff_and_account_routes_have_strict_script_policy_and_no_store(self):
        for path in ["/staff/", "/account/login/"]:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertIn("script-src 'self';", response["Content-Security-Policy"])
                self.assertEqual(response["Cache-Control"], "no-store, private")

    def test_forms_and_validation_errors_are_not_cacheable(self):
        for language in ["en", "bn"]:
            for page in ["contact", "inquiry"]:
                path = f"/{language}/{page}/"
                with self.subTest(path=path):
                    self.assertEqual(self.client.get(path)["Cache-Control"], "no-store, private")
                    response = self.client.post(path, {"phone": "invalid"})
                    self.assertEqual(response.status_code, 422)
                    self.assertEqual(response["Cache-Control"], "no-store, private")
                    self.assertEqual(response.wsgi_request.sensitive_post_parameters, "__ALL__")
