# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
import os
logger = logging.getLogger('macronux')

from macronux_lib import Window
from macronux.AboutMacronuxDialog import AboutMacronuxDialog
from macronux.PreferencesMacronuxDialog import PreferencesMacronuxDialog

# See macronux_lib.Window.py for more details about how this class works
class MacronuxWindow(Window):
    __gtype_name__ = "MacronuxWindow"

    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(MacronuxWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutMacronuxDialog
        self.PreferencesDialog = PreferencesMacronuxDialog

        # Code for other initialization actions should be added here.
        self.initialisebutton = self.builder.get_object("initialisebutton")
        # self.rmallbutton = self.builder.get_object("rmallbutton")
        self.addfirefox = self.builder.get_object("addfirefox")
        self.removefirefox = self.builder.get_object("removefirefox")
        self.addterminal = self.builder.get_object("addterminal")
        self.removeterminal = self.builder.get_object("removeterminal")
        self.addcalc = self.builder.get_object("addcalc")
        self.removecalc = self.builder.get_object("removecalc")
        self.addmusicplayer = self.builder.get_object("addmusicplayer")
        self.removemusicplayer = self.builder.get_object("removemusicplayer")
        self.addwriter = self.builder.get_object("addwriter")
        self.removewriter = self.builder.get_object("removewriter")
        self.addimpress = self.builder.get_object("addimpress")
        self.removeimpress = self.builder.get_object("removeimpress")
        self.addgedit = self.builder.get_object("addgedit")
        self.removegedit = self.builder.get_object("removegedit")
        self.addsublime = self.builder.get_object("addsublime")
        self.removesublime = self.builder.get_object("removesublime")


    def on_initialisebutton_clicked(self, widget):
    	homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
    	f1 = open(lol,'w')
    	f1.write('import os\n')
    	f1.close()
    	os.system("mkdir "+homedir+"/.config/autostart")
		dir = homedir+'/.config/autostart/strtup.desktop'
		f = open(dir, 'w')
		f.write('[Desktop Entry]\n')
		f.write('Type=Application\n')
		f.write('Exec=python ')
		f.write(homedir)
		f.write('/lol.py\n')
		f.write('Hidden=false\nNoDisplay=false\nX-GNOME-Autostart-enabled=true\nName[en_IN]=Macronux Startup Service\n')
		f.write('Name=Macronux Startup Service\nComment[en_IN]=\nComment=Testing mode ON\n')
		f.close()



	# def on_rmallbutton_clicked(self, widget):
 #        print "Removed All!"
 #        homedir = os.environ['HOME']
 #    	lol = homedir+'/lol.py'
 #        f = open(lol, "r")
 #        lines = f.readlines()
 #        f.close()
 #        f1 = open(lol, "w")
 #        for line in lines:
 #            if 'os.system(' in line:
 #                pass
 #            else:
 #                f1.write(line)
 #        f1.close()



    def on_addfirefox_clicked(self, widget):
        print "Firefox Added!"
    	homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "a")
        f.write("os.system('firefox &')\n")
        f.close()


    def on_removefirefox_clicked(self, widget):
        print "Firefox Removed!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "r")
        lines = f.readlines()
        f.close()
        f1 = open(lol, "w")
        for line in lines:
            if 'firefox' in line:
                pass
            else:
                f1.write(line)
        f1.close()

    def on_addterminal_clicked(self, widget):
        print "Terminal Added!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "a")
        f.write("os.system('gnome-terminal &')\n")
        f.close()


    def on_removeterminal_clicked(self, widget):
        print "Terminal Removed!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "r")
        lines = f.readlines()
        f.close()
        f1 = open(lol, "w")
        for line in lines:
            if 'gnome-terminal' in line:
                pass
            else:
                f1.write(line)
        f1.close()

    def on_addcalc_clicked(self, widget):
        print "Calc Added!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "a")
        f.write("os.system('gnome-calculator &')\n")
        f.close()


    def on_removecalc_clicked(self, widget):
        print "Calc Removed!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "r")
        lines = f.readlines()
        f.close()
        f1 = open(lol, "w")
        for line in lines:
            if 'gnome-calculator' in line:
                pass
            else:
                f1.write(line)
        f1.close()

    def on_addmusicplayer_clicked(self, widget):
        print "Music Player Added!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "a")
        f.write("os.system('rhythmbox &')\n")
        f.close()


    def on_removemusicplayer_clicked(self, widget):
        print "Music Player Removed!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "r")
        lines = f.readlines()
        f.close()
        f1 = open(lol, "w")
        for line in lines:
            if 'rhythmbox' in line:
                pass
            else:
                f1.write(line)
        f1.close()


    def on_addwriter_clicked(self, widget):
        print "Writer Added!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "a")
        f.write("os.system('libreoffice --writer &')\n")
        f.close()


    def on_removewriter_clicked(self, widget):
        print "Writer Removed!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "r")
        lines = f.readlines()
        f.close()
        f1 = open(lol, "w")
        for line in lines:
            if 'writer' in line:
                pass
            else:
                f1.write(line)
        f1.close()


    def on_addimpress_clicked(self, widget):
        print "Impress Added!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "a")
        f.write("os.system('libreoffice --impress &')\n")
        f.close()


    def on_removeimpress_clicked(self, widget):
        print "Impress Removed!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "r")
        lines = f.readlines()
        f.close()
        f1 = open(lol, "w")
        for line in lines:
            if 'impress' in line:
                pass
            else:
                f1.write(line)
        f1.close()        


    def on_addgedit_clicked(self, widget):
        print "gedit Added!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "a")
        f.write("os.system('gedit &')\n")
        f.close()


    def on_removegedit_clicked(self, widget):
        print "gedit Removed!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "r")
        lines = f.readlines()
        f.close()
        f1 = open(lol, "w")
        for line in lines:
            if 'gedit' in line:
                pass
            else:
                f1.write(line)
        f1.close()        

    def on_addsublime_clicked(self, widget):
        print "sublime Added!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "a")
        f.write("os.system('subl &')\n")
        f.close()


    def on_removesublime_clicked(self, widget):
        print "sublime Removed!"
        homedir = os.environ['HOME']
    	lol = homedir+'/lol.py'
        f = open(lol, "r")
        lines = f.readlines()
        f.close()
        f1 = open(lol, "w")
        for line in lines:
            if 'subl' in line:
                pass
            else:
                f1.write(line)
        f1.close()        
