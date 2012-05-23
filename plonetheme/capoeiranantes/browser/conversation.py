from zope.component import queryUtility
from plone.registry.interfaces import IRegistry
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.app.discussion.interfaces import IDiscussionSettings
from Products.Five.browser import BrowserView


class ConversationView(BrowserView):

    def enabled(self):
        context = aq_inner(self.context)

        # Fetch discussion registry
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IDiscussionSettings, check=False)

        # Check if discussion is allowed globally
        if not settings.globally_enabled:
            return False

        # Check if discussion is allowed on the content object
        if getattr(context, "allow_discussion", None) is not None:
            return context.allow_discussion

        # Check if discussion is allowed on the content type
        portal_types = getToolByName(self, 'portal_types')
        document_fti = getattr(portal_types, context.portal_type)
        return document_fti.getProperty('allow_discussion')
