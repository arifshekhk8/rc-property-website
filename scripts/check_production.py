"""Validate a synthetic production configuration without connecting to external services.

This checks application settings, not a deployed system. Domain-specific HSTS choices
remain visible release requirements; unexpected warnings fail this check.
"""

import os
import secrets
import sys
from pathlib import Path

os.environ.update(
    DJANGO_SETTINGS_MODULE="config.settings",
    DJANGO_DEBUG="0",
    DJANGO_SECRET_KEY=secrets.token_urlsafe(64),
    DJANGO_ALLOWED_HOSTS="configuration-check.invalid",
    DATABASE_URL="postgresql://configuration-check.invalid/configuration_check",
    DATABASE_SSLMODE="require",
)
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

import django  # noqa: E402
from django.core.checks import WARNING, run_checks  # noqa: E402

django.setup()
issues = run_checks(include_deployment_checks=True)
pending_domain_decisions = {"security.W005", "security.W021"}
unexpected = [
    issue for issue in issues if issue.level >= WARNING and issue.id not in pending_domain_decisions
]
for issue in issues:
    print(f"{issue.id}: {issue.msg}")
if unexpected:
    raise SystemExit(1)
print("Synthetic production checks passed; HSTS subdomain/preload decisions remain launch gates.")
