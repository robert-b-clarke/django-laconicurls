import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-laconicurls',
    version='0.1.0',
    packages=['laconicurls'],
    include_package_data=True,
    license='BSD License',
    description='A generic url shortner for content in a Django ORM',
    long_description=README,
    url='http://redanorak.co.uk/',
    author='Robert Clarke',
    author_email='rob@redanorak.co.uk',
    test_suite='laconicurls.runtests.runtests',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Development Status :: 4 - Beta',
    ],
)
