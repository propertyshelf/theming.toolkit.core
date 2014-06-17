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

    show_headerplugin = schema.Bool(
        default=False,
        required=False,
        title=_(
            u"label_show_header_plugin",
            default=u"Show Social Header Viewlet",
        ),
    )

    headerplugin_code =schema.Text(
        description=PMF(
            u'help_plugin_code',
            default=u'Please enter the Social Header Plugin Code.',
        ),
        required=False,
        title=PMF(u'label_plugin_code', default=u'Social Plugins Code'),
    )

    show_title_contact = schema.Bool(
        default=False,
        required=False,
        title=_(
            u"label_show_header_plugin",
            default=u"Show Site title & contact viewlet",
        ),
    )

    contact_code =schema.TextLine(
        default=u"",
        required=False,
        title=_(
            u"label_toolkit_contact_code",
            default=u"Contact Info for Website header",
        )      
    )

    show_featuredNavigation = schema.Bool(
        default=False,
        required=False,
        title=_(
            u"label_show_featuredNavigation",
            default=u"Show the featured Navigation",
        ),
    )

    featuredNavigation_taglist =schema.Text(
        default=u"featured navigation, Featured Navigation",
        description=PMF(
            u'help_plugin_code',
            default=u'Please enter a comma seperated list of category tags to identify Pages& Folders for featured navigation',
        ),
        required=False,
        title=PMF(u'label_featuredNavigation_taglist', default=u'Tag list featured Navigation'),
    )

    show_featuredListingSlider = schema.Bool(
        default=True,
        required=False,
        title=_(
            u"label_show_featuredListingSlider",
            default=u"Activate or deactivate the MLS featured Listing Slider globally",
        ),
    )

    display_featuredListingSlider_aboveContent = schema.Bool(
        default=True,
        required=False,
        title=_(
            u"label_FLS_abovecontent",
            default=u"Show featuredListingSlider above content.",
        ),
    )

    display_featuredListingSlider_belowContent = schema.Bool(
        default=True,
        required=False,
        title=_(
            u"label_FLS_belowcontent",
            default=u"Show featuredListingSlider below content.",
        ),
    )

    featuredListingSlider_ItemList =schema.TextLine(
        default=u"",
        required=False,
        title=_(
            u"label_FLS_offset",
            default=u"Add a list of Listings",
        )      
    )

    featuredListingSlider_Limit =schema.TextLine(
        default=u"",
        required=False,
        title=_(
            u"label_FLS_limit",
            default=u"Limit the amount of shown listings ",
        )      
    )

    featuredListingSlider_offset =schema.TextLine(
        default=u"",
        required=False,
        title=_(
            u"label_FLS_offset",
            default=u"Set a global offset for the Listing Items in the List",
        )      
    )


    featuredListingSliderJS =schema.Text(
        default=u"<script>alert('FeaturedListingSlider on its way');</script>",
        description=PMF(
            u'help_FLS_code',
            default=u'The global default JavaScript code for initialising the FeaturedListingSlider. This setting can be replaced by the local galery settings',
        ),
        required=False,
        title=PMF(u'label_featuredListingSliderJS', default=u'Default JS to start'),
    )