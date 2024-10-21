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
class file_size_warning_dialog_class ():

    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, last_function_self, disk_space):

        #-----------------------------------------------------------------------------------------------------

        # ROUNDING THE TAKED DISK SPACE
        disk_space_r = round(disk_space, 2)

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE WINDOW CONSTRUCTOR
        dialog = Gtk.Builder()

        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        dialog.set_translation_domain('davinci-helper')

        # IMPORTING THE UI FILE THAT REPRESENT THE MAIN WINDOW
        dialog.add_from_file(f"{ui_path}/file_size_warning_dialog.ui")

        # OBTAINING THE MAIN WINDOW AND HER CHILD FROM THE UI FILE
        self.dialog_window = dialog.get_object("dialog_window")

        #-----------------------------------------------------------------------------------------------------
        
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_icon = dialog.get_object("dialog_icon")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_title = dialog.get_object("dialog_title")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_subtitle_1 = dialog.get_object("dialog_subtitle_1")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_subtitle_2 = dialog.get_object("dialog_subtitle_2")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_subtitle_3 = dialog.get_object("dialog_subtitle_3")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_continue_button = dialog.get_object("dialog_continue_button")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_cancel_button = dialog.get_object("dialog_cancel_button")

        #-----------------------------------------------------------------------------------------------------

        # LOADING ICON FILE
        self.dialog_icon.set_from_file(f"{icon_path}/function_icons/warning.svg")

        # LOADING TITLE TEXT
        self.dialog_title.set_text(_("This will need a lot of space !"))

        # LOADING SUBTITLE TEXT
        self.dialog_subtitle_1.set_text(_("The conversion of the files using the DNxHD/HR encoder will make new files fully compatible with DaVinci Resolve Free.\n\nThe use of these uncompressed sources will make your editing experience faster, but it will take a lot of disk space.\n"))

        # LOADING SUBTITLE TEXT
        self.dialog_subtitle_2.set_text(_("The estimated disk space needed to convert the files is :\n{space_placeholder}GB\n").format(space_placeholder = disk_space_r))

        # LOADING SUBTITLE TEXT
        self.dialog_subtitle_3.set_markup(_("If you want to use less disk space please consider using\nlower video and audio settings."))

        
        # CONNECTING THE BUTTON TO THE FUNCTION
        self.dialog_cancel_button.connect('clicked', lambda button : self.dialog_window.close())

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT SHOWS THE DIALOG WINDOW
    def show_dialog (self, last_function_self):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING THE WINDOW AND HER CHILDS
        self.dialog_window.present(last_function_self.main_self.main_window)

        #-----------------------------------------------------------------------------------------------------