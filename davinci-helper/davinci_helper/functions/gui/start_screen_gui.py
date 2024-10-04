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
from .loading_gui import loading_class

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
settings_path = os.path.join(f"{home_dir}/.config")

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
@Gtk.Template(filename=f"{ui_path}/start_screen.ui")

# CREATING TEMPLATE CLASS TO EDIT WIDGET
class start_screen_class (Gtk.ScrolledWindow):
    
    #-----------------------------------------------------------------------------------------------------

    # DEFINING TEMPLATE NAME
    __gtype_name__ = "start_screen"

    #-----------------------------------------------------------------------------------------------------
    
    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_container = Gtk.Template.Child("section_1_container")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_icon = Gtk.Template.Child("section_1_icon")
    
    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_title = Gtk.Template.Child("section_1_title")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_subtitle_1 = Gtk.Template.Child("section_1_subtitle_1")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_function_1_button = Gtk.Template.Child("section_1_function_1_button")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_function_2_button = Gtk.Template.Child("section_1_function_2_button")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_function_3_button = Gtk.Template.Child("section_1_function_3_button")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_function_4_button = Gtk.Template.Child("section_1_function_4_button")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_function_5_button = Gtk.Template.Child("section_1_function_5_button")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_function_1_button_icon = Gtk.Template.Child("section_1_function_1_button_icon")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_function_2_button_icon = Gtk.Template.Child("section_1_function_2_button_icon")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_function_3_button_icon = Gtk.Template.Child("section_1_function_3_button_icon")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_function_4_button_icon = Gtk.Template.Child("section_1_function_4_button_icon")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_function_5_button_icon = Gtk.Template.Child("section_1_function_5_button_icon")

    #-----------------------------------------------------------------------------------------------------



    # IMPORTING ATTRIBUTES FROM PARENT CLASS
    def __init__(self, main_self):
        super().__init__()

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE MAIN WINDOW SELF OBJECT
        self.main_self = main_self

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE INFO ABOUT THE SYSTEM THEME
        self.style_manager = Adw.StyleManager.get_default()

        # STARTING THE FUNCTION THAT DETECTS THE THEME AND CHAGES THE ICONS EVERY TIME THE THEME IS CHANGED
        self.style_manager.connect("notify::dark", lambda *args: self.apply_current_theme())

        # INITIAL START OF THE DETECT THEME FUNCTION
        self.apply_current_theme()

        #-----------------------------------------------------------------------------------------------------

        # LOADING ICON FILE
        self.section_1_icon.set_from_file(f"{icon_path}/davinci_helper_icon.svg")

        # LOADING TITLE TEXT
        self.section_1_title.set_text(_("Welcome to DaVinci Helper"))

        # LOADING TITLE TEXT
        self.section_1_subtitle_1.set_text(_("The best tool for managing DaVinci Resolve on Linux"))

        # CONNECTING THE ICON BUTTON TO THE FUNCTION
        self.section_1_function_1_button.connect('clicked', lambda button : self.main_self.show_function_page("function_1"))

        # CONNECTING THE ICON BUTTON TO THE FUNCTION
        self.section_1_function_2_button.connect('clicked', lambda button : self.main_self.show_function_page("function_2"))

        # CONNECTING THE ICON BUTTON TO THE FUNCTION
        self.section_1_function_3_button.connect('clicked', lambda button : self.main_self.show_function_page("function_3"))

        # CONNECTING THE ICON BUTTON TO THE FUNCTION
        self.section_1_function_4_button.connect('clicked', lambda button : self.main_self.show_function_page("function_4"))

        # CONNECTING THE ICON BUTTON TO THE FUNCTION
        self.section_1_function_5_button.connect('clicked', lambda button : (self.main_self.choose_default_ui(), self.main_self.show_function_page("function_5")))

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT DETECT EVERY THEME CHANGE AND SWITCH THE ICONS ACCORDING TO IT
    def apply_current_theme (self):

        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF THE SYSTEM IS USING THE DARK MODE
        if self.main_self.style_manager.get_dark():

            # SETTING THE WHITE ICON FOLDER FOR DARK MODE
            mode_path = "dark_mode"

        else :
            
            # SETTING THE DARK ICON FOLDER FOR WHITE MODE
            mode_path = "white_mode"

        #-----------------------------------------------------------------------------------------------------

        # SETTING THE SIDEBAR ICON
        self.section_1_function_1_button_icon.set_from_file(f"{icon_path}/{mode_path}/function_1.svg")

        # SETTING THE SIDEBAR ICON
        self.section_1_function_2_button_icon.set_from_file(f"{icon_path}/{mode_path}/function_2.svg")

        # SETTING THE SIDEBAR ICON
        self.section_1_function_3_button_icon.set_from_file(f"{icon_path}/{mode_path}/function_3.svg")

        # SETTING THE SIDEBAR ICON
        self.section_1_function_4_button_icon.set_from_file(f"{icon_path}/{mode_path}/function_4.svg")

        # SETTING THE SIDEBAR ICON
        self.section_1_function_5_button_icon.set_from_file(f"{icon_path}/{mode_path}/function_5.svg")

        #-----------------------------------------------------------------------------------------------------    