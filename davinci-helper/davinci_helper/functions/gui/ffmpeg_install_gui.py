#
# Copyright 2024 Lorenzo Maiuri
# Published under GPL-3.0 license
# GitHub : https://github.com/H3rz3n/davinci-helper
#

#-----------------------------------------------------------------------------------------------------

# SECTION 0 : (OPTIONAL) INSTALL FFMPEG UI
# SECTION 1 : DEFAULT FUNCTION UI
# SECTION 2 : LOADING UI
# SECTION 3 : AFTER FUNCTION EXEC UI

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

from ..logic import setting_management

#-----------------------------------------------------------------------------------------------------

# DEFINING UI FILES PATH
ui_path = os.path.join("/usr/share/davinci-helper/data/ui")

# DEFINING ICON FILES PATH
icon_path = os.path.join("/usr/share/davinci-helper/data/icons")

# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale")

#-----------------------------------------------------------------------------------------------------

# ASSOCIATE THE NAME OF THE TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE LOCALE MODULE
locale.bindtextdomain('davinci-helper', locale_path)

# ASSOCIATE THE NAME OF TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE GETTEXT MODULE
gettext.bindtextdomain('davinci-helper', locale_path)

# TELLING GETTEXT WHICH FILE TO USE FOR THE TRANSLATION OF THE APP
gettext.textdomain('davinci-helper')

# TELLING GETTEXT THE TRANSLATE SIGNAL
_ = gettext.gettext

#-----------------------------------------------------------------------------------------------------



# DEFINING TEMPLATE PATH
@Gtk.Template(filename=f"{ui_path}/ffmpeg_install.ui")

# CREATING TEMPLATE CLASS TO EDIT WIDGET
class ffmpeg_install_class (Gtk.ScrolledWindow):
    
    #-----------------------------------------------------------------------------------------------------

    # DEFINING TEMPLATE NAME
    __gtype_name__ = "ffmpeg_install"

    #-----------------------------------------------------------------------------------------------------

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_container = Gtk.Template.Child("section_1_container")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_icon = Gtk.Template.Child("section_1_icon")
    
    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_title = Gtk.Template.Child("section_1_title")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_install_button = Gtk.Template.Child("section_1_install_button")

    #-----------------------------------------------------------------------------------------------------

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_2_container = Gtk.Template.Child("section_2_container")

    #-----------------------------------------------------------------------------------------------------

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_3_container = Gtk.Template.Child("section_3_container")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_3_icon = Gtk.Template.Child("section_3_icon")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_3_title = Gtk.Template.Child("section_3_title")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_3_subtitle = Gtk.Template.Child("section_3_subtitle")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_3_log_revealer = Gtk.Template.Child("section_3_log_revealer")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_3_log = Gtk.Template.Child("section_3_log")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_3_start_button = Gtk.Template.Child("section_3_start_button")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_3_log_button = Gtk.Template.Child("section_3_log_button")

    #-----------------------------------------------------------------------------------------------------





    # IMPORTING ATTRIBUTES FROM PARENT CLASS
    def __init__(self, main_window):
        super().__init__()

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE MAIN WINDOW SELF OBJECT
        self.main_self = main_window

        #-----------------------------------------------------------------------------------------------------

        # LOADING ICON FILE
        self.section_1_icon.set_from_file(f"{icon_path}/main_icons/ffmpeg_icon.jpg")

        # LOADING TITLE TEXT
        self.section_1_title.set_text(_("Install FFMPEG\nto use this feature"))

        # CONNECTING THE INFO BUTTON TO THE FUNCTION
        self.section_1_install_button.connect('clicked', self.start_script)

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE LOADING UI
        self.loading_class = loading_class()

        # SETTING THE LOADING UI INSIDE THE CONTAINER
        self.section_2_container.append(self.loading_class)

        #-----------------------------------------------------------------------------------------------------

        # CONNECTING THE LOG BUTTON TO THE FUNCTION
        self.section_3_log_button.connect('clicked', self.show_logs)

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT RESET THE UI WHEN THE PAGE IS NOT SHOWED
    def reset_ui (self):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING DEFAULT SECTION
        self.section_1_container.set_visible(True)

        # HIDING LOADING SECTION
        self.section_2_container.set_visible(False)

        # HIDING FINAL SECTION
        self.section_3_container.set_visible(False)

        #-----------------------------------------------------------------------------------------------------

        # CLOSING LOG BOX
        self.section_3_log_revealer.set_reveal_child(False)

        # RESETTING BUTTON LABEL
        self.section_3_log_button.set_label(_("Show logs"))

        # HIDING ANIMATION REVEALER
        self.main_self.function_5_content_revealer.set_reveal_child(False)

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT HIDE THE PREVIOUS UI AND DISABLE THE SIDEBAR BUTTONS
    def start_loading (self):

        #-----------------------------------------------------------------------------------------------------

        # HIDING DEFAULT SECTION
        self.section_1_container.set_visible(False)

        # SHOWING LOADING SECTION
        self.section_2_container.set_visible(True)

        # HIDING AFTER SCRIPT SECTION
        self.section_3_container.set_visible(False)

        #-----------------------------------------------------------------------------------------------------
        
        # HIDING THE OBJECT
        self.section_3_log_revealer.set_reveal_child(False)

        # DISABLING MENU BUTTON
        self.main_self.main_window_menu_button.set_sensitive(False)

        # DISABLING SIDEBAR BUTTONS
        self.main_self.main_window_sidebar_menu.set_sensitive(False)

        # STARTING THE SPINNER
        self.loading_class.start_spinner()

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT HIDE THE LOADING UI
    def stop_loading (self):

        #-----------------------------------------------------------------------------------------------------

        # ENABLING MENU BUTTON
        self.main_self.main_window_menu_button.set_sensitive(True)

        # ENABLING SIDEBAR BUTTONS
        self.main_self.main_window_sidebar_menu.set_sensitive(True)

        # STOPPING THE SPINNER
        self.loading_class.stop_spinner()

        #-----------------------------------------------------------------------------------------------------
        
        # HIDING DEFAULT SECTION
        self.section_2_container.set_visible(False)

        # SHOWING LOADING SECTION
        self.section_3_container.set_visible(True)

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT LAUNCH THE FUNCTION SCRIPT
    def script_launch (self):

        #-----------------------------------------------------------------------------------------------------

        # LAUNCHING THE FUNCTION SCRIPT
        function_script = subprocess.run("pkexec python /usr/lib/python*/site-packages/davinci_helper/functions/logic/install_ffmpeg.py", shell=True, capture_output=True, text=True)

        #-----------------------------------------------------------------------------------------------------

        # ON PROCESS END UPDATE THE GUI
        GLib.idle_add(self.after_script_end, function_script)

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT STARTS THE FUNCTION SCRIPT AND LAUNCH THE UI FUNCTIONS
    def start_script (self, button):
        
        #-----------------------------------------------------------------------------------------------------

        # STARTING THE LOADING FUNCTION
        self.start_loading()

        #-----------------------------------------------------------------------------------------------------

        # STARTING IN ANOTHER THREAD THE FUNCTION SCRIPT TO AVOID UI CRASH
        threading.Thread(target=self.script_launch).start()

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT LAUNCH THE NEW UI AFTER THE SCRIPT END
    def after_script_end (self, function_script):

        #-----------------------------------------------------------------------------------------------------

        # ENDING THE LOADING FUNCTION AND SHOWING FINAL UI
        self.stop_loading()

        # CHECKING IF THERE ARE ANY ERRORS TO CHAGE THE UI OUTPUT
        self.check_return_code(function_script)

        #-----------------------------------------------------------------------------------------------------


    


    # FUNCTION THAT CHECKS IF THERE ARE ANY ERROR CODES IN THE SCRIPT OUTPUT
    def check_return_code (self, function_script):

        #-----------------------------------------------------------------------------------------------------

        # LOADING THE LOG TEXTS INSIDE THE LOGS CONTAINER
        self.section_3_log.set_text(f"{function_script.stdout} \n {function_script.stderr}")

        # CHECKING IF THE FUNCTION HAS NO ERRORS
        if function_script.returncode == 0 :

            # CHANGING THE SETTINGS TO FLAG FFMPEG AS INSTALLED
            setting_management.flag_ffmpeg_as_installed()
            
            # SHOWING THE SUCCESS SCREEN
            self.show_success()
        
        else :

            # SHOWING THE ERROR SCREEN
            self.show_error(function_script)

        #-----------------------------------------------------------------------------------------------------




    
    # FUNCTION THAT SHOWS THE SUCCESS SCREEN
    def show_success (self):

        #-----------------------------------------------------------------------------------------------------

        # LOADING THE ICON FILE
        self.section_3_icon.set_from_file(f"{icon_path}/function_icons/success.svg")

        # LOADING TITLE TEXT
        self.section_3_title.set_text(_("FFMPEG was successfully installed"))

        # LOADING THE SUBTITLE TEXT
        self.section_3_subtitle.set_text(_("FFMPEG has been correctly installed inside the system.\nNow you can start using DaVinci Video Convert."))

        # SETTING THE START BUTTON LABEL
        self.section_3_start_button.set_label(_("Go to DaVinci Video Converter"))

        # SETTING THE START BUTTON FUNCTION
        self.section_3_start_button.connect('clicked', self.show_davinci_converter)

        #-----------------------------------------------------------------------------------------------------
    




    # FUNCTION THAT SHOWS THE ERROR SCREEN
    def show_error (self, function_script):

        #-----------------------------------------------------------------------------------------------------

        # LOADING THE ICON FILE
        self.section_3_icon.set_from_file(f"{icon_path}/function_icons/error.svg")

        # LOADING TITLE TEXT
        self.section_3_title.set_text(_("There was an error installing FFMPEG"))

        # SETTING THE START BUTTON LABEL
        self.section_3_start_button.set_label("Start again")

        # SETTING THE START BUTTON FUNCTION
        self.section_3_start_button.connect('clicked', self.start_script)

        #-----------------------------------------------------------------------------------------------------

        # CHECKING ERROR CODE 1
        if function_script.returncode == 1 :

            # LOADING THE SUBTITLE TEXT
            self.section_3_subtitle.set_text(_("There was an error while adding the RPM Fusion repository to your system.\nPlease check the logs to have more details."))

        #-----------------------------------------------------------------------------------------------------

        # CHECKING ERROR CODE 2
        elif function_script.returncode == 2 :

            # LOADING THE SUBTITLE TEXT
            self.section_3_subtitle.set_text(_("There was an error installing FFMPEG from the RPM Fusion repository.\nPlease check the logs to have more details."))
    
        #-----------------------------------------------------------------------------------------------------

        # CHECKING ERROR CODE 3
        elif function_script.returncode == 3 :

            # LOADING THE SUBTITLE TEXT
            self.section_3_subtitle.set_text(_("There was an error swapping FFMPEG lite with\nFFMPEG full from the RPM Fusion repository.\nPlease check the logs to have more details."))
    
        #-----------------------------------------------------------------------------------------------------

        # CHECKING ERROR CODE 4
        elif function_script.returncode == 4 :

            # LOADING THE SUBTITLE TEXT
            self.section_3_subtitle.set_text(_("There was an error installing the required codecs\nand libraries from the RPM Fusion repository\nPlease check the logs to have more details."))
    
        #-----------------------------------------------------------------------------------------------------

        # CHECKING ERROR CODE 5
        elif function_script.returncode == 5 :

            # LOADING THE SUBTITLE TEXT
            self.section_3_subtitle.set_text(_("There was an error updating the multimedia group\nPlease check the logs to have more details."))
    
        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF WAS IMPOSSIBILE TO START THE FUNCTION DUE TO MISSING ROOT PERMISSION
        elif function_script.stdout == "" :

             # LOADING TITLE TEXT
            self.section_3_title.set_text(_("You need to be an admin to use this function"))

            # LOADING THE SUBTITLE TEXT
            self.section_3_subtitle.set_text(_("It was impossible to start this function because you didn't give the necessary root permission for his execution. Try again giving the root permission."))

            # HIDING THE LOG BUTTON BECAUSE IS UNECESSARY
            self.section_3_log_button.set_visible(False)

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT AND MANAGES THE SHOW/HID MECHANISM
    def show_logs (self, button):

        #-----------------------------------------------------------------------------------------------------

        # ACQUIRING VIBILITY STATUS OF THE OBJECT
        current_visibility = self.section_3_log_revealer.get_reveal_child()

        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF THE OBJECT IS VISIBLE
        if current_visibility == True :

            # HIDING THE OBJECT
            self.section_3_log_revealer.set_reveal_child(False)

            # CHANGING BUTTON LABEL
            self.section_3_log_button.set_label(_("Show logs"))

        else :

            # SHOWING THE OBJECT
            self.section_3_log_revealer.set_reveal_child(True)

            # CHANGING BUTTON LABEL
            self.section_3_log_button.set_label(_("Hide logs"))

        #-----------------------------------------------------------------------------------------------------




    
    # FUNCTION THAT WILL SHOW DAVINCI VIDEO CONVERTER AFTER A SUCCESSFULL FFMPEG CHECK
    def show_davinci_converter (self, button):

        #-----------------------------------------------------------------------------------------------------

        # CHANGING THE UI TO SHOW
        self.main_self.choose_default_ui()

        #-----------------------------------------------------------------------------------------------------