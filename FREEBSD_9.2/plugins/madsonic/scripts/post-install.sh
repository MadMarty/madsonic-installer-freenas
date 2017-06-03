#!/bin/sh

madsonic_pbi_path=/usr/pbi/madsonic-$(uname -m)

${madsonic_pbi_path}/bin/python2.7 ${madsonic_pbi_path}/madsonicUI/manage.py syncdb --migrate --noinput
