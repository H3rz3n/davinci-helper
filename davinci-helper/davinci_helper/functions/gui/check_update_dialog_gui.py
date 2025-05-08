#
# Copyright 2025 Lorenzo Maiuri
# Published under GPL-3.0 license
# GitHub : https://github.com/H3rz3n/davinci-helper
#

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, gi, os, threading, gettext, locale, subprocess, requests

# RICHIESTA DELLE VERSIONI DI GTK ED ADWAITA
# REQUESTING THE CHOOSEN VERSION OF GTK AND ADWAITA
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

# IMPORTO I MODULI NECESSARI
# IMPORTING THE NECESSARY MODULES
from gi.repository import Gtk, Adw, Gdk, Pango, Gio, GLib

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
class check_update_dialog_class ():

    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, main_self, version_number, version_changelog):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE WINDOW CONSTRUCTOR
        dialog = Gtk.Builder()

        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        dialog.set_translation_domain('davinci-helper')

        # IMPORTING THE UI FILE THAT REPRESENT THE MAIN WINDOW
        dialog.add_from_file(f"{ui_path}/check_update_dialog.ui")

        # OBTAINING THE MAIN WINDOW AND HER CHILD FROM THE UI FILE
        self.dialog_window = dialog.get_object("dialog_window")

        #-----------------------------------------------------------------------------------------------------
        
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_icon = dialog.get_object("dialog_icon")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_title = dialog.get_object("dialog_title")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_subtitle = dialog.get_object("dialog_subtitle")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_changelog = dialog.get_object("dialog_changelog")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_download_button = dialog.get_object("dialog_download_button")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_close_button = dialog.get_object("dialog_close_button")

        # OBTAINING THE MAIN SELF FROM THE MAIN FILE
        self.main_self = main_self

        #-----------------------------------------------------------------------------------------------------

        # LOADING ICON FILE
        self.dialog_icon.set_from_file(f"{icon_path}/davinci_helper_icon.svg")

        # LOADING TITLE TEXT
        self.dialog_title.set_text(_("A new update is available"))

        # LOADING SUBTITLE TEXT
        self.dialog_subtitle.set_text(_("A new version of this app has been found.\nWe recommend you to update it before continue using it."))

        # LOADING CHANGELOG TEXT
        self.dialog_changelog.set_text(version_changelog)

        # CONNECTING THE DOWNLOAD BUTTON TO THE FUNCTION
        self.dialog_download_button.connect('clicked', self.open_github_page)

        # CONNECTING THE CLOSE BUTTON TO THE FUNCTION
        self.dialog_close_button.connect('clicked', lambda button : self.dialog_window.close())

        #-----------------------------------------------------------------------------------------------------


    
    
    
    # FUNCTION THAT OPENS THE LATEST VERSION DOWNLOAD PAGE
    def open_github_page(self, button) :

        #-----------------------------------------------------------------------------------------------------

        # SETTONG THE DOWNLOAD PAGE LINK
        url = "https://github.com/H3rz3n/davinci-helper/releases/latest"

        # USING GIO TO OPEN THE URL IN THE DEFAULT WEB BROWSER
        Gio.AppInfo.launch_default_for_uri(url)

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT SHOWS THE DIALOG WINDOW
    def show_dialog (self):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING THE WINDOW AND HER CHILDS
        self.dialog_window.present(self.main_self.main_window)

        #-----------------------------------------------------------------------------------------------------






