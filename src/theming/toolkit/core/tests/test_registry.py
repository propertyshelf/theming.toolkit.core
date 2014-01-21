# -*- coding: utf-8 -*-
"""Test Registry for theming.toolkit.core."""

# python imports
import unittest2 as unittest

# zope imports
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

# local imports
from theming.toolkit.core.interfaces import IToolkitSettings
from theming.toolkit.core.testing import THEMING_TOOLKIT_CORE_INTEGRATION_TESTING


class TestToolkitRegistry(unittest.TestCase):
    """Registry Test Case for theming.toolkit.core."""
    layer = THEMING_TOOLKIT_CORE_INTEGRATION_TESTING

    def test_registry_registered(self):
        """Test that the settings are registered correctly."""
        registry = getUtility(IRegistry)
        self.assertTrue(registry.forInterface(IToolkitSettings))
