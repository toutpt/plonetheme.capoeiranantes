from Products.Five.browser import BrowserView


class HomePageView(BrowserView):
    """Home page"""

    def items(self):
        brains = self.context.queryCatalog()
        items = []

        for brain in brains:
            items.append({'title': brain.Title,
                    'description': brain.Description,
                    'url': brain.getURL(),
                    'imgurl': brain.getURL() + '/image'})

        return items
