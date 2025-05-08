#
# Copyright 2025 Lorenzo Maiuri
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



# FILE ERROR DIALOG CLASS
class welcome_dialog_class ():

    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, main_self):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE WINDOW CONSTRUCTOR
        dialog = Gtk.Builder()

        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        dialog.set_translation_domain('davinci-helper')

        # IMPORTING THE UI FILE THAT REPRESENT THE MAIN WINDOW
        dialog.add_from_file(f"{ui_path}/welcome_dialog.ui")

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
        self.dialog_switch_label = dialog.get_object("dialog_switch_label")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_switch = dialog.get_object("dialog_switch")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.dialog_close_button = dialog.get_object("dialog_close_button")

        # OBTAINING THE MAIN SELF FROM THE MAIN FILE
        self.main_self = main_self

        #-----------------------------------------------------------------------------------------------------

        # LOADING ICON FILE
        self.dialog_icon.set_from_file(f"{icon_path}/davinci_helper_icon.svg")

        # LOADING TITLE TEXT
        self.dialog_title.set_text(_("Thank you for installing\nDaVinci Helper"))
       
        # LOADING SUBTITLE TEXT
        self.dialog_subtitle_1.set_text(_("Thank you for trusting us and installing DaVinci Helper. We hope that this app will make the management of DaVinci Resolve easier for you.\n"))

        # LOADING SUBTITLE TEXT
        self.dialog_subtitle_2.set_text(_("This app is not affiliated in any way with BlackMagic Design, it's only a community project and comes without any guarantees.\n"))

        # LOADING SUBTITLE TEXT
        paragraph_3 = (_('''If you find this app useful and want to improve it please consider helping us <a href=\"https://github.com/H3rz3n/davinci-helper\">developing</a> this app or <a href=\"https://www.paypal.com/donate/?hosted_button_id=CPCG2RFAV82T8\">making a donation</a>  to the project.'''))
        self.dialog_subtitle_3.set_markup(paragraph_3)

        # LOADING SUBTITLE TEXT
        self.dialog_switch_label.set_text(_("Don't show again"))

        # CONNECTING THE SWITCH TRIGGER TO THE SETTINGS CHANGE FUNCTION
        self.dialog_switch.connect("notify::active", self.change_visibility)

        # CONNECTING THE START BUTTON TO THE FUNCTION
        self.dialog_close_button.connect('clicked', lambda button : self.dialog_window.close())

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT CHECKS IF IS NECESSARY TO SHOW THE WELCOME DIALOG
    def check_splash_screen (self):

        #-----------------------------------------------------------------------------------------------------

        # REAGING ONE LINE AT TIME THE SETTINGS LIST
        with open(f"{settings_path}/davinci_helper/davinci_helper_settings", 'r', encoding='utf-8') as file :

            for line in file :

                # CHECKING IF IS NECESSARY TO SHOW THE SPLASH SCREEN
                if line.find("SHOW_WELCOME_SPLASH_SCREEN") != -1 and line.find("TRUE") != -1 :

                    # STARTING THE SPLASH SCREEN
                    self.show_dialog()

                    # SENDING A SIGNAL TO MAIN FUNCTION DO AVOID CONFLICTS
                    return True

        #-----------------------------------------------------------------------------------------------------
    




    # FUNCTION THAT CHANGES THE SETTINGS WHEN THE SWITCH IS TRIGGERED
    def change_visibility (self, switch, status):

        #-----------------------------------------------------------------------------------------------------

        # RESETTING THE COUNTERS
        line_number = 0

        # REAGING ONE LINE AT TIME THE SETTINGS LIST
        with open(f"{settings_path}/davinci_helper/davinci_helper_settings", 'r', encoding='utf-8') as file :

            # ACQUIRING FILE CONTENT    
            file_content = file.readlines()

        #-----------------------------------------------------------------------------------------------------
            
        # READING LINE BY LINE THE FILE DUMP
        for line in file_content :
            
            # FINDING THE VISIBILITY SETTINGS
            if line.find("SHOW_WELCOME_SPLASH_SCREEN = TRUE") != -1 :

                # SETTING THE SPLASH SCREEN AS HIDDEN
                file_content[line_number] = "SHOW_WELCOME_SPLASH_SCREEN = FALSE\n"

                # EXTING THE CICLE IN A SECURE WAY
                break

            elif line.find("SHOW_WELCOME_SPLASH_SCREEN = FALSE") != -1 :

                # SETTING THE SPLASH SCREEN AS VISIBLE
                file_content[line_number] = "SHOW_WELCOME_SPLASH_SCREEN = TRUE\n"

                # EXTING THE CICLE IN A SECURE WAY
                break

            # ADDING 1 TO THE COUNTER
            line_number = line_number + 1

        #-----------------------------------------------------------------------------------------------------

        # OVERWRITING THE PREVIOUS SETTINGS    
        with open(f"{settings_path}/davinci_helper/davinci_helper_settings", 'w', encoding='utf-8') as file :

            # WRITING THE CONTENT INSIDE THE FILE
            file.writelines(file_content)

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT SHOWS THE DIALOG WINDOW
    def show_dialog (self):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING THE WINDOW AND HER CHILDS
        self.dialog_window.present(self.main_self.main_window)

        #-----------------------------------------------------------------------------------------------------