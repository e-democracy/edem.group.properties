# coding=utf-8
from __future__ import absolute_import, unicode_literals
from gs.group.privacy.visibility import GroupVisibility
from edem.skin.interfaces import IEDemGroupProperties
from gs.group.properties.change import ChangePropertiesForm
from gs.content.form.base.utils import enforce_schema
from gs.content.form.base import disabled_text_widget
from zope.formlib import form


class EDemChangePropertiesForm(ChangePropertiesForm):
    def __init__(self, context, request):
        ChangePropertiesForm.__init__(self, context, request)
        enforce_schema(self.context, IEDemGroupProperties)
        self.groupVisibility = GroupVisibility(self.groupInfo)
        self.__form_fields = None
        self.label = u'Change Group Properties'

    @property
    def form_fields(self):
        if self.__form_fields is None:
            form_fields = \
                form.Fields(IEDemGroupProperties, render_context=True)
            if self.groupVisibility.isPublic:
                form_fields['mshipCriterion'].custom_widget = \
                    disabled_text_widget
            self.__form_fields = form_fields
        return self.__form_fields
