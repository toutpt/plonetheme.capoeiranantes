from Products.Five.browser import BrowserView


class ChangeType(BrowserView):
    """browser view to change portla_type"""

    def __call__(self):
        new_type = self.request['portal_type']
        self.context.portal_type = new_type
        self.context.reindexObject()
        self.request.response.redirect(self.context.absolute_url())
