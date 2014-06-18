# -*- coding: utf-8 -*-
"""Migration steps for theming.toolkit.core"""

# zope imports
from plone.registry.interfaces import IRegistry
from theming.toolkit.core.interfaces import IToolkitSettings
from zope.component import getUtility

PROFILE_ID = 'profile-theming.toolkit.core":default'


def migrate_to_1001(context):
    """Migrate from 1000 to 1001.

    * Update the IToolkitSettings registry settings.
    """
    registry = getUtility(IRegistry)
    registry.registerInterface(IToolkitSettings)
