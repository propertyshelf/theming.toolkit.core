# -*- coding: utf-8 -*-
"""Theming toolkit Settings Control Panel."""

# zope imports
from plone.app.registry.browser import controlpanel
from z3c.form import field
#from collective.z3cform.colorpicker.colorpicker import ColorpickerFieldWidget
#from collective.z3cform.colorpicker.colorpickeralpha import ColorpickerAlphaFieldWidget

# local imports
from theming.toolkit.core.i18n import _
from theming.toolkit.core.interfaces import IToolkitSettings


class ToolkitSettingsEditForm(controlpanel.RegistryEditForm):
    """Theming toolkit Settings Form"""

    schema = IToolkitSettings
    label = _(u"heading_toolkit_settings", u"Propertyshelf Theming Toolkit Settings")
    fields = field.Fields(IToolkitSettings)
    #fields['theme_leadcolor'].widgetFactory = ColorpickerFieldWidget

    def updateFields(self):
        super(ToolkitSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(ToolkitSettingsEditForm, self).updateWidgets()


class ToolkitSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Theming toolkit Settings Control Panel"""

    form = ToolkitSettingsEditForm