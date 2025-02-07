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
class file_error_dialog_class ():

    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, last_function_self, error_type):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE WINDOW CONSTRUCTOR
        dialog = Gtk.Builder()

        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        dialog.set_translation_domain('davinci-helper')

        # IMPORTING THE UI FILE THAT REPRESENT THE MAIN WINDOW
        dialog.add_from_file(f"{ui_path}/file_error_dialog.ui")

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
        self.dialog_close_button = dialog.get_object("dialog_close_button")

        #-----------------------------------------------------------------------------------------------------

        # LOADING ICON FILE
        self.dialog_icon.set_from_file(f"{icon_path}/function_icons/warning.svg")

        # LOADING TITLE TEXT
        self.dialog_title.set_text(_("Select a valid file !"))

        # CHECKING WHICH SUBTITLE TEXT HAS TO BE LOADED :
        if error_type == "Missing" :

            # DEFINING SUBTITLE TEXT
            subtitle_text= (_("It seems like you didn't load any file.\nPlease load a valid DaVinci Resolve installer file to continue."))

        elif error_type == "Unsuitable":

            # DEFINING SUBTITLE TEXT
            subtitle_text= (_("It seems like you tried to load an usupported file.\nPlease load a valid DaVinci Resolve installer file to continue.\nIf you have renamed it, remember that the file name must\ncontain the words 'DaVinci', 'Resolve', 'Linux' inside of it\nand it must to have the '.zip' or `.run` extension."))

        # LOADING SUBTITLE TEXT
        self.dialog_subtitle.set_text(subtitle_text)

        # CONNECTING THE START BUTTON TO THE FUNCTION
        self.dialog_close_button.connect('clicked', lambda button : self.dialog_window.close())

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT SHOWS THE DIALOG WINDOW
    def show_dialog (self, last_function_self):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING THE WINDOW AND HER CHILDS
        self.dialog_window.present(last_function_self.main_self.main_window)

        #-----------------------------------------------------------------------------------------------------