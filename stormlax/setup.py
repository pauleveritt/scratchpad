
from setuptools import setup, find_packages
import os
import sys

requires = [
    'pyramid',
    'setuptools',
    'nose',
    'WebTest',
    'waitress',
    ]

if sys.version_info[:2] < (2, 7):
    requires.append('unittest2')

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='stormlax',
    version='0.1',
    description='Sports League Stuff',
    long_description=README + '\n\n' +  CHANGES,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    author='Paul Everitt',
    author_email='pauleveritt@me.com',
    keywords='web pylons pyramid',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    test_suite='stormlax',
    install_requires=requires,
    entry_points="""
    [paste.app_factory]
    main = stormlax:main
    """,
    )
