# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from Products.EasyNewsletter.testing import (
    PRODUCTS_EASYNEWSLETTER_FUNCTIONAL_TESTING,
    PRODUCTS_EASYNEWSLETTER_INTEGRATION_TESTING,
)
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = PRODUCTS_EASYNEWSLETTER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.newsletter = api.content.create(container=self.portal, type='Newsletter', id='newsletter')

    def test_unsubscribe_form_is_registered(self):
        view = getMultiAdapter(
            (self.newsletter, self.portal.REQUEST),
            name='unsubscribe-form'
        )
        self.assertTrue(view.__name__ == 'unsubscribe-form')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in unsubscribe-form'
        # )

    def test_unsubscribe_form_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal, self.portal.REQUEST),
                name='unsubscribe-form'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = PRODUCTS_EASYNEWSLETTER_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
