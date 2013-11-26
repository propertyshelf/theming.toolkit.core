# -*- coding: utf-8 -*-
"""Interface definitions."""

# zope imports

from Products.CMFPlone import PloneMessageFactory as PMF

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

    show_headerplugin = schema.Bool(
        default=True,
        required=False,
        title=_(
            u"label_show_header_plugin",
            default=u"Show Social Header Viewlet",
        ),
    )

    headerplugin_title = schema.TextLine(
        required=False,
        title=_(
            u'Header Extra Title',
            default=u'Extra Title',
        ),
    )

    headerplugin_code =schema.Text(
        description=PMF(
            u'help_plugin_code',
            default=u'Please enter the Header Plugin Code.',
        ),
        required=False,
        title=PMF(u'label_plugin_code', default=u'Plugin Code'),
    )
