from DateTime import DateTime
from plone.app.layout.viewlets import common
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class HeaderBanViewlet(common.ViewletBase):
    """A ban to display things in the header"""

    index = ViewPageTemplateFile('banner.pt')

#    def events(self):
#        """return 3 events sort on start date"""
#        catalog = getToolByName(self.context, 'portal_catalog')
#        query = {'portal_type': 'Event',
#                 'sort_on': 'start',
#                 'sort_order': 'reverse',
#                 'sort_limit': 3}
#        brains = catalog(**query)
#        events = []
#        now = DateTime()
#
#        for brain in brains:
#
#            if brain.start < now:
#                state = 'appened'
#            else:
#                state = 'futur'
#            events.append({'title': brain.Title,
#                           'url': brain.getURL(),
#                           'state': state})
#
#        return events
