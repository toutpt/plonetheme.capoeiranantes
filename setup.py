from setuptools import setup, find_packages

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
          'plone.api',
          'plone.app.themingplugins',
          'Pillow',
          'Products.PloneFormGen',
          'collective.addthis',
          'collective.baseline',
          'collective.ckeditor',
          'collective.contentleadimage',
          'collective.contentrules.imaging',
          'collective.contentrules.yearmonth',
          'collective.dewplayer',
          'collective.footerportletmanager',
          'collective.galleria',
          'collective.googleanalytics',
          'collective.js.fitvids',
          'collective.js.nivoslider',
          'collective.masonry',
          'collective.metarobots',
          'collective.oembed',
          'collective.portlet.actions',
          'collective.portlet.embed',
          'collective.portlet.fancyboxgallery',
          'collective.portlet.nivoslider',
          'collective.portlet.oembed',
          'collective.quickupload',
          'collective.recaptcha',
          'collective.seo',
          'webcouturier.dropdownmenu',
          'plone.formwidget.recaptcha',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
