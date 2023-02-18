from django.test import TestCase

# Create your tests here.
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django5Others.settings')
    import django
    django.setup()
