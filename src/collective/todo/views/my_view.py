# -*- coding: utf-8 -*-

from collective.todo import _
from Products.Five.browser import BrowserView


class MyView(BrowserView):

    def __call__(self):
        return _(u'This view works!')
