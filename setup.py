from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='theming.toolkit.color',
      version=version,
      description="A product that allows to change a set of theme colors in it's configuration.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Jens Krause',
      author_email='jens@propertyshelf.com',
      url='http://propertyshelf.com/',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['theming', 'theming.toolkit'],
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      
      extras_require={
          'test': ['plone.app.testing',]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
