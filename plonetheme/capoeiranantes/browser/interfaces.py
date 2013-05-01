from zope import interface
from plone.app.discussion.interfaces import IDiscussionLayer
from collective.galleria.interfaces import IGalleriaLayer


class IThemeSpecific(interface.Interface, IDiscussionLayer, IGalleriaLayer):
    """Marker interface that defines a Zope 3 browser layer."""
