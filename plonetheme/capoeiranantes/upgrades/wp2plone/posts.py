from zope import interface
from zope import component

from collective.transmogrifier.transmogrifier import Transmogrifier
from collective.transmogrifier import interfaces

def import_posts(context):
    transmogrifier = Transmogrifier(context)
    transmogrifier("wp2plone-posts")

class PostSection(object):
    interface.classProvides(interfaces.ISectionBlueprint)
    interface.implements(interfaces.ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.transmogrifier = transmogrifier
        self.name = name
        self.options = options
        self.previous = previous

    def __iter__(self):

        for item in self.previous:
            self.constructor(item)

            yield item

    def constructor(self, item):
        import pdb;pdb.set_trace()
        item['title']=item['post_title']
        item['text'] =item['post_content']

        if item['post_type'] == "page":
            item['_path']="/archives/page/%s"%item['post_name']
            item['_type']='Document'
        
        elif item['post_type'] == "post":
            item['_path']="/archives/post/%s"%item['post_name']
            item['_type']='Document'

        return item
