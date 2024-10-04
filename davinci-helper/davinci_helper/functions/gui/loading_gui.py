#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
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

# DEFINING CSS FILES PATH
css_path = os.path.join("/usr/share/davinci-helper/data/css")

# DEFINING UI FILES PATH
ui_path = os.path.join("/usr/share/davinci-helper/data/ui")

# DEFINING ICON FILES PATH
icon_path = os.path.join("/usr/share/davinci-helper/data/icons")

# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale")

# DEFINING SETTINGS FILES PATH
home_dir = os.path.expanduser("~")
settings_path = os.path.join(f"{home_dir}/.config/davinci_helper")

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



# DEFINING TEMPLATE PATH
@Gtk.Template(filename=f"{ui_path}/loading.ui")

# CREATING TEMPLATE CLASS TO EDIT WIDGET
class loading_class (Gtk.Grid):
    
    #-----------------------------------------------------------------------------------------------------

    # DEFINING TEMPLATE NAME
    __gtype_name__ = "Loading"

    #-----------------------------------------------------------------------------------------------------
    
    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    loading_spinner = Gtk.Template.Child("loading_spinner")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    loading_text = Gtk.Template.Child("loading_text")




    # IMPORTING ATTRIBUTES FROM PARENT CLASS
    def __init__(self):
        super().__init__()

        #-----------------------------------------------------------------------------------------------------

        # SETTING THE TEXT
        self.loading_text.set_text(_("The time needed to complete this task will vary on your computer and network performance."))

        #-----------------------------------------------------------------------------------------------------




   
    # FUNCTION THAT STARTS THE SPINNER
    def start_spinner (self):

        #-----------------------------------------------------------------------------------------------------

        # STARTING THE SPINNER
        self.loading_spinner.start()

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT STOPS THE SPINNER
    def stop_spinner(self):

        #-----------------------------------------------------------------------------------------------------

        # STOPPING THE SPINNER
        self.loading_spinner.stop()

        #-----------------------------------------------------------------------------------------------------
    

