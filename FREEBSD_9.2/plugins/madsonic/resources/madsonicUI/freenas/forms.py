import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from madsonicUI.freenas import models, utils

class MadsonicForm(forms.ModelForm):

    class Meta:
        model = models.Madsonic
        widgets = {
            'madsonic_max_memory': forms.widgets.TextInput(),
            'madsonic_port': forms.widgets.TextInput(),
        }
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(MadsonicForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(MadsonicForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.madsonic_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('madsonic_enable="YES"\n')

        conf_dir = os.path.join(utils.madsonic_etc_path, "madsonic")
        settingsfile = os.path.join(conf_dir, "config.ini")
        settings = {}

        for field in obj._meta.local_fields:
            if field.attname not in utils.madsonic_settings:
                continue
            info = utils.madsonic_settings.get(field.attname)
            value = getattr(obj, field.attname)
            _filter = info.get("filter")
            if _filter:
                settings[info.get("field")] = _filter(value)
            else:
                settings[info.get("field")] = value

        madsonic_ssl = str(obj.madsonic_ssl).lower()
        with open(settingsfile, 'w') as f:
            f.write('MADSONIC_MAX_MEMORY="%d"\n' % (obj.madsonic_max_memory, ))
            f.write('MADSONIC_SSL="%s"\n' % (madsonic_ssl, ))
            f.write('MADSONIC_PORT="%d"\n' % (obj.madsonic_port, ))
            f.write('MADSONIC_CONTEXT_PATH="%s"' % (obj.madsonic_context_path, ))

        os.system(os.path.join(utils.madsonic_pbi_path, "tweak-rcconf"))
