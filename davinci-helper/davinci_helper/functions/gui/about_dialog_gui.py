#
# Copyright 2024 Lorenzo Maiuri
# Published under GPL-3.0 license
# GitHub : https://github.com/H3rz3n/davinci-helper
#

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, gi, os, threading, gettext, locale, subprocess

# RICHIESTA DELLE VERSIONI DI GTK ED ADWAITA
# REQUESTING THE CHOOSEN VERSION OF GTK AND ADWAITA
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

# IMPORTO I MODULI NECESSARI
# IMPORTING THE NECESSARY MODULES
from gi.repository import Gtk, Adw, Gdk, Pango, Gio, GLib

#-----------------------------------------------------------------------------------------------------

# NOT STANDARD MODULES IMPORT
from ..logic import app_info

#-----------------------------------------------------------------------------------------------------

# DEFINING UI FILES PATH
ui_path = os.path.join("/usr/share/davinci-helper/data/ui")

# DEFINING ICON FILES PATH
icon_path = os.path.join("/usr/share/davinci-helper/data/icons")

# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale")

#-----------------------------------------------------------------------------------------------------

# ASSOCIA IL NOME DEL DIZIONARIO DI TRADUZIONE AL FILE CORRISPONDENTE PER IL MODULO LOCALE
# ASSOCIATE THE NAME OF THE TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE LOCALE MODULE
locale.bindtextdomain('davinci-helper', locale_path)

# ASSOCIA IL NOME DEL DIZIONARIO DI TRADUZIONE AL FILE CORRISPONDENTE PER IL MODULO GETTEXT
# ASSOCIATE THE NAME OF TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE GETTEXT MODULE
gettext.bindtextdomain('davinci-helper', locale_path)

# COMUMICO A GETTEXT QUALE FILE USARE PER TRADURRE IL PROGRAMMA
# TELLING GETTEXT WHICH FILE TO USE FOR THE TRANSLATION OF THE APP
gettext.textdomain('davinci-helper')

# COMUNICO A GETTEXT IL SEGNALE DI TRADUZIONE
# TELLING GETTEXT THE TRANSLATE SIGNAL
_ = gettext.gettext

#-----------------------------------------------------------------------------------------------------



# FILE ERROR DIALOG CLASS
class about_dialog_class ():

    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, last_function_self):

        #-----------------------------------------------------------------------------------------------------

        # CREATING THE ABOUT DIALOG WINDOW
        self.dialog_window = Adw.AboutDialog()

        # SETTING THE APP NAME
        self.dialog_window.set_application_name(app_info.app_name)

         # SETTING THE APP VERSION
        self.dialog_window.set_version(app_info.app_version)

        # SETTING THE APP ICON
        self.dialog_window.set_application_icon(app_info.app_icon)

        # SETTING THE APP WEBSITE
        self.dialog_window.set_website(app_info.app_website)

        # SETTING THE APP DEVELOPER
        self.dialog_window.set_developer_name(app_info.app_developers)

        # SETTING THE APP CONTRIBUTORS
        self.dialog_window.set_developers(app_info.app_contributors)

        # SETTING THE APP TRANSLATOR
        self.dialog_window.set_translator_credits(app_info.app_translator)

        # SETTING THE APP LICENSE
        self.dialog_window.set_license(app_info.app_license)

        # SETTING THE APP ISSUES URL
        self.dialog_window.set_issue_url(app_info.app_issue_url)

        # SETTING THE APP COPYRIGHT
        self.dialog_window.set_copyright(app_info.app_copyright)

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT SHOWS THE DIALOG WINDOW
    def show_dialog (self, last_function_self):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING THE WINDOW AND HER CHILDS
        self.dialog_window.present(last_function_self.main_window)

        #-----------------------------------------------------------------------------------------------------
