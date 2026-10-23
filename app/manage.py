#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Management commands default to local development; the WSGI entry defaults secure.
    # Deployment commands must explicitly set DJANGO_DEBUG=0.
    os.environ.setdefault("DJANGO_DEBUG", "1")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
