# -*- coding: utf-8 -*-
"""Theming toolkit Settings Control Panel."""

# zope imports
from plone.app.registry.browser import controlpanel

# local imports
from theming.toolkit.core.i18n import _
from theming.toolkit.core.interfaces import IToolkitSettings


class ToolkitSettingsEditForm(controlpanel.RegistryEditForm):
    """Theming toolkit Settings Form"""

    schema = IToolkitSettings
    label = _(u"heading_toolkit_settings", u"Propertyshelf Theming Toolkit Settings")

    def updateFields(self):
        super(ToolkitSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(ToolkitSettingsEditForm, self).updateWidgets()


class ToolkitSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Theming toolkit Settings Control Panel"""

    form = ToolkitSettingsEditForm