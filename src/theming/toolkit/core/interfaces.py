# -*- coding: utf-8 -*-
"""Interface definitions."""

# zope imports
from zope import schema
from zope.interface import Interface

# local imports
from theming.toolkit.core.i18n import _


class IToolkitSettings(Interface):
    """Global theming.toolkit settings.
    This describes records stored in the configuration registry and obtainable
    via plone.registry.
    """

    theme_leadcolor = schema.TextLine(
        default=u"",
        required=True,
        title=_(
            u"label_toolkit_theme_leadcolor",
            default=u"The main color for this theme.",
        )
    )
