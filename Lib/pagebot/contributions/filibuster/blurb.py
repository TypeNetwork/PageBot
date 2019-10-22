#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
#    blurb.py
#
import re
from pagebot.contributions.filibuster import blurbwriter, content

class Blurb:
    """The Content is a wrapper around the filibuster BlurbWriter of Erik van
    Blokland and Jonathan Hoefler. There is supposed to be only one instance of
    the writer installed in the system.

    b = Blurb()
    print(b.getBlurb('article'))
    """
    def __init__(self, customContent=None):
        #if customContent is None:
        #    content = customContent

        self.writer = blurbwriter.BlurbWriter(content.content())

    reNoTags = re.compile('\<[^\>]*|([^\<\>]*)')

    def getBlurb(self, ofType, cnt=None, charCnt=None, noTags=True,
            newLines=False):
        """The getBlurb method answers a random generated blurb of type. The
        list of available types can be obtained by calling getBlurbTypes()."""
        content = self.writer.write(ofType)

        # Remove the HTML tags.
        if noTags:
            # If newlines, then replace the <p> by return, before removing all
            # tags.
            if newLines:
                content = content.replace('<p>','').replace('</p>','\n')

            content = str().join(self.reNoTags.findall(content))

        # If word count defined, slice by wordspace.
        if cnt is not None:
            content = str(' ').join(content.split(' ')[:cnt])

        if charCnt is not None and len(content) > charCnt:
            # Shorten the string to the requested amount of glyphs.
            content = self.writer.write(type)[:charCnt].strip()

            while content and not content[-1].lower() in 'abcdefghijklmnopqrstuvwxyz':
                content = content[:-1]

        return content

    def getBlurbTypes(self):
        """Answers a list of names of all types of content blurbs that can can
        be generated by the writer."""
        return self.writer.keywords

# Make the single instance of Blurb.
blurb = Blurb()

if __name__ == '__main__':

    def printString(s):
        try:
            print(s)
        except UnicodeEncodeError:
            start = 0
            for n in range(len(s)):
                try:
                    print('[--]', s[start:n])
                except UnicodeEncodeError:
                    print('****')
                    start = n

    w = blurb
    printString(w.getBlurb('address'))
    printString(w.getBlurb('sports_headline'))
    printString(w.getBlurb('filibuster_about'))
    printString(w.getBlurb('aerospace_headline'))
    printString(w.getBlurb('address'))

    for i in range(10):
        printString(w.getBlurb('politics_euro_headline'))
