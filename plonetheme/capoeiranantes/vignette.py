from zope.component import adapts
from zope.interface import implements

from Products.Archetypes import public as atapi
from Products.ATContentTypes.interfaces import IATEvent, IATNewsItem

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender, \
    IBrowserLayerAwareExtender

# Your add-on browserlayer
from plonetheme.capoeiranantes.browser.interfaces import IThemeSpecific

from zope import i18nmessageid
_ = i18nmessageid.MessageFactory('collective.azindexpage')
from Products.ATContentTypes import ATCTMessageFactory as _p


class ExtensionImageField(ExtensionField, atapi.ImageField):
    """MultiLingual LinesField"""


class ExtensionStringField(ExtensionField, atapi.StringField):
    """text"""


class VignetteExtender(object):
    """This extender just add a new field to all content types
    """

    # We use both orderable and browser layer aware sensitive properties
    implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)

    # Don't do schema extending unless our add-on product is installed on Plone
    layer = IThemeSpecific

    fields = [
        ExtensionImageField("image",
            schemata="default",
            required=True,
            widget=atapi.ImageWidget(
              label=_p(u'label_news_image', default=u'Image'),
              description=_(u"This image should have 765px with"),
              show_content_type=False
            ),
        ),
        ExtensionStringField("imageCaption",
            required=False,
            schemata="default",
            widget=atapi.StringWidget(
              label=_p(u'label_image_caption', default=u'Image Caption'),
              size=40
            ),
        )
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        """ Manipulate the order in which fields appear.

        @param schematas: Dictonary of schemata name -> field lists

        @return: Dictionary of reordered field lists per schemata.
        """
        return schematas

    def getFields(self):
        """
        @return: List of new fields we contribute to content.
        """
        return self.fields
