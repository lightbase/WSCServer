import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'psycopg2',
    'pyramid_restler',
    'requests',
    'chameleon',
    'ConfigParser'
]

setup(name='WSCServer',
      version='1.1.2b3',
      description='WSCServer',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Programming Language :: Python :: 3.2",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Lightbase',
      author_email='pedro.ricardo@lighbase.com.br',
      url='',
      keywords='rest lightbase json cacic pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='wscserver',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = wscserver:main
      [console_scripts]
      initialize_WSCServer_db = wscserver.scripts.initializedb:main
      """
      )
