Introduction
============

Theme for new website http://capoeira-nantes.fr

TODO
====

- Add this snippet in collective.oembed.consumer 81 to support offline:

        except URLError,e:
            logger.info(e)

-addthis: report bug:
All pages are broken when I'm working offline.

 Module zope.tales.tales, line 696, in evaluate
   - URL: /Users/toutpt/.buildout/installed_eggs/collective.addthis-1.3.1-py2.6.egg/collective/addthis/addthis.pt
   - Line 15, Column 4
   - Expression: <PythonExpr ('addthis_button_%s' % chicklet.value)>
   - Names:
      {'args': (),
       'container': <ATTopic at /Plone/homepage>,
       'context': <ATTopic at /Plone/homepage>,
       'default': <object object at 0x100288b70>,
       'here': <ATTopic at /Plone/homepage>,
       'loop': {},
       'nothing': None,
       'options': {},
       'repeat': <Products.PageTemplates.Expressions.SafeMapping object at 0x10a907730>,
       'request': <HTTPRequest, URL=http://localhost:8080/Plone/homepage/folder_full_view>,
       'root': <Application at >,
       'template': <Products.Five.browser.pagetemplatefile.ViewPageTemplateFile object at 0x10afee6d0>,
       'traverse_subpath': [],
       'user': <PropertiedUser 'admin'>,
       'view': <Products.Five.viewlet.viewlet.SimpleViewletClass from /Users/toutpt/.buildout/installed_eggs/collective.addthis-1.3.1-py2.6.egg/collective/addthis/addthis.pt object at 0x10afc4ed0>,
       'views': <Products.Five.browser.pagetemplatefile.ViewMapper object at 0x10a22f410>}
  Module zope.tales.pythonexpr, line 59, in __call__
   - __traceback_info__: ('addthis_button_%s' % chicklet.value)
  Module <string>, line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'value'

> /Users/toutpt/.buildout/installed_eggs/collective.addthis-1.3.1-py2.6.egg/collective/addthis/addthis.py(45)chicklets()
-> return results
(Pdb) results
[None, None, None, None, None, None]

Excepected results: having chicklets displayed or at least do not break if
working offline

Charte graphique
----------------

Header:

- bannière: 3 blocs (horaire/lieu[texte], inscription[texte], événements [list 3])
- globalnav: ajouter les icones

Footer:

- liens à la pnr + lien vers le site du japon
- page de mentions légales

JS:

- changer le libellé 'Contenu corrélés' en 'Photos de l'événement' dans la rubrique
agenda.

Page d'accueil
--------------

Carousel (actu)
Appel à rubrique:

- Chansons
- Mouvements
- Grades

Tableau de bords
----------------

ajouter un bloc pour la créa de contenu:

* Ajouter actualité
* Ajouter événement
* Ajouter album photos
