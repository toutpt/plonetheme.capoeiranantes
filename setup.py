from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plonetheme.capoeiranantes',
      version=version,
      description="An installable diazo theme for Plone 4",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        ],
      keywords='',
      author='JeanMichel FRANCOIS aka toutp',
      author_email='toutpt@gmail.com',
      url='https://github.com/toutpt/plonetheme.capoeiranantes',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'plone.app.themingplugins',
          # -*- Extra requirements: -*-
          'Products.Collage',
          'Products.PloneFormGen',
          'collective.addthis',
          'collective.collage.portlets',
          'collective.galleria',
          'collective.googleanalytics',
          'collective.quickupload',
          'collective.dewplayer',
          'collective.oembed',
          'collective.portlet.actions',
          'collective.portlet.oembed',
          'collective.portlet.embed',
          'collective.seo',
          'collective.masonry',
          'webcouturier.dropdownmenu',
          'plone.app.transmogrifier',
          'iw.rejectanonymous',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
