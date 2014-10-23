import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'laconicurls.testrunner.settings'
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)
import django

from django.test.utils import get_runner
from django.conf import settings

def runtests():
    if hasattr(django, 'setup'):
        django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['laconicurls'])
    sys.exit(bool(failures))
