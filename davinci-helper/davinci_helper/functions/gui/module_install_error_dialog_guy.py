
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
class module_install_error_dialog_class ():

    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, last_function_self, logs):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE WINDOW CONSTRUCTOR
        dialog = Gtk.Builder()

        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        dialog.set_translation_domain('davinci-helper')

        # IMPORTING THE UI FILE THAT REPRESENT THE MAIN WINDOW
        dialog.add_from_file(f"{ui_path}/module_install_error_dialog.ui")

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
        self.dialog_log_revealer = dialog.get_object("dialog_log_revealer")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_log = dialog.get_object("dialog_log")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_close_button = dialog.get_object("dialog_close_button")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_log_button = dialog.get_object("dialog_log_button")

        #-----------------------------------------------------------------------------------------------------

        # LOADING ICON FILE
        self.dialog_icon.set_from_file(f"{icon_path}/function_icons/error.svg")

        # LOADING TITLE TEXT
        self.dialog_title.set_text(_("There are some missing modules"))

        # LOADING SUBTITLE TEXT
        self.dialog_subtitle.set_text(_("There was an error installing the Moviepy python module.\nPlease check the logs to have more details."))

        # LOADING SUBTITLE TEXT
        self.dialog_log.set_text(logs)

        
        # CONNECTING THE BUTTON TO THE FUNCTION
        self.dialog_close_button.connect('clicked', lambda button : self.dialog_window.close())

        # CONNECTING THE BUTTON TO THE FUNCTION
        self.dialog_log_button.connect('clicked', self.show_logs)

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT SHOWS THE DIALOG WINDOW
    def show_dialog (self, last_function_self):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING THE WINDOW AND HER CHILDS
        self.dialog_window.present(last_function_self.main_self.main_window)

        #-----------------------------------------------------------------------------------------------------



    



    # FUNCTION THAT AND MANAGES THE SHOW/HID MECHANISM
    def show_logs (self, button):

        #-----------------------------------------------------------------------------------------------------

        # ACQUIRING VIBILITY STATUS OF THE OBJECT
        current_visibility = self.dialog_log_revealer.get_reveal_child()

        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF THE OBJECT IS VISIBLE
        if current_visibility == True :

            # HIDING THE OBJECT
            self.dialog_log_revealer.set_reveal_child(False)

            # CHANGING BUTTON LABEL
            self.dialog_log_button.set_label(_("Show logs"))

        else :

            # SHOWING THE OBJECT
            self.dialog_log_revealer.set_reveal_child(True)

            # CHANGING BUTTON LABEL
            self.dialog_log_button.set_label(_("Hide logs"))

        #-----------------------------------------------------------------------------------------------------