from setuptools import setup, find_packages

version = '0.1dev'

setup(
    name='jslibs',
    version=version,
    description="Static JS libraries common to Pyramid projects",
    long_description="",
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords='pyramid javascript python',
    author='Paul Everitt',
    author_email='paul@agendaless.com',
    url='http://pypi.python.org/pypi/pyramid_jslibs',
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'psycopg2',
        'simplejson',
        'SQLAlchemy>=0.7.1',
        'ZODB3',
        'zope.component',
        'zope.dublincore',
        'zope.interface',
        'zope.sqlalchemy',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
