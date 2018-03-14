# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

import logging
logger = logging.getLogger('macronux')

from macronux_lib.AboutDialog import AboutDialog

# See macronux_lib.AboutDialog.py for more details about how this class works.
class AboutMacronuxDialog(AboutDialog):
    __gtype_name__ = "AboutMacronuxDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutMacronuxDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

