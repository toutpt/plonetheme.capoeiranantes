from zope import interface
from plone.app.discussion.interfaces import IDiscussionLayer


class IThemeSpecific(interface.Interface, IDiscussionLayer):
    """Marker interface that defines a Zope 3 browser layer."""
