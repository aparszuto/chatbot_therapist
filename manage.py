#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_therapist.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Nie można zaimportować Django. Upewnij się, że jest zainstalowane i dostępne w Twoim wirtualnym środowisku."
        ) from exc
    execute_from_command_line(sys.argv)