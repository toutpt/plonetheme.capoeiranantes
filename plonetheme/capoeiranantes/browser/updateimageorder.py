import logging

from Products.Five.browser import BrowserView

logger=  logging.getLogger('capoeira')


def getdateint(image):
    exif = image.getEXIF()
    for key in exif:
        if 'date' not in key.lower():
            continue
        date = exif[key]
        if len(date) != 19:
            logger.info('a date with len != 19: %s' % data)
            continue
        #we keep month and the rest
        try:
            intdate = int(date[5:].replace(':', '').replace(' ',''))
        except ValueError:
            continue
        return intdate
    return -1


def cmp(a, b):
    return int.__cmp__(getdateint(a), getdateint(b))


def getObject(brain):
    return brain.getObject()


def getId(brain):
    return brain.getId


class UpdateImageOrder(BrowserView):
    """update image order on picture taken"""

    def __call__(self):
        trace = []
        bids = self.context.objectIds()

        brains = self.context.getFolderContents()
        images = map(getObject, brains)
        exif_sorted = sorted(images, cmp=cmp)

        for image in images:
            id = image.getId()
            new_position = exif_sorted.index(image)

            trace.append('id: %s -> position %s' % (id, new_position))
            self.context.moveObjectToPosition(id, new_position)

        return u" -- ".join(trace)
