#
# Copyright 2024 Lorenzo Maiuri
# Published under GPL-3.0 license
# GitHub : https://github.com/H3rz3n/davinci-helper
#

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, gi, os, threading, gettext, locale, subprocess

# REQUESTING THE VERSION OF GTK AND ADWAITA
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

# IMPORTING THE NECESSARY MODULES
from gi.repository import Gtk, Adw, Gdk, Pango, Gio, GLib

#-----------------------------------------------------------------------------------------------------

# NOT STANDARD MODULES IMPORT
from .functions.gui.welcome_dialog_gui import welcome_dialog_class
from .functions.gui.settings_management_dialog_gui import setting_management_dialog_class
from .functions.gui.check_update_dialog_gui import check_update_dialog_class
from .functions.gui.about_dialog_gui import about_dialog_class

from .functions.gui.start_screen_gui import start_screen_class
from .functions.gui.function_1_gui import function_1_class
from .functions.gui.function_2_gui import function_2_class
from .functions.gui.function_3_gui import function_3_class
from .functions.gui.function_4_gui import function_4_class
from .functions.gui.function_5_gui import function_5_class
from .functions.gui.ffmpeg_install_gui import ffmpeg_install_class

from .functions.logic.setting_management import check_settings_existence, restore_settings
from .functions.logic.check_update import check_update

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

# IMPORTING THE CSS FILE FOR STYLES DEFINITION
css_provider = Gtk.CssProvider()
css_provider.load_from_path(f'{css_path}/style.css')
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(),css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

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

# DEFINING THE CLASS WHO CREATES AND DISPLAYS THE MAIN WINDOW
class build_main_window(Adw.Application):

    #-----------------------------------------------------------------------------------------------------

    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, **kwargs):

        #-----------------------------------------------------------------------------------------------------

        super().__init__(**kwargs)

        #-----------------------------------------------------------------------------------------------------

        # LINKING TO A FUNCTION THE HAMBURGER MENU ITEM
        reset_settings_action = Gio.SimpleAction.new("reset_settings", None)
        reset_settings_action.connect("activate", self.reset_settings)
        self.add_action(reset_settings_action)

        # LINKING TO A FUNCTION THE HAMBURGER MENU ITEM
        show_about_action = Gio.SimpleAction.new("show_about", None)
        show_about_action.connect("activate", self.show_about_dialog)
        self.add_action(show_about_action)

        #-----------------------------------------------------------------------------------------------------

        # CALLING THE CONNECT FUNCTION USING AS PARAMETERS "ACTIVATE" AND THE MAIN WINDOW CREATOR FUNCTION
        self.connect('activate', self.main_window_activation)

        #-----------------------------------------------------------------------------------------------------





    # STARTING THE FUNCTION THAT CREATES THE MAIN WINDOW AND DIPLAYS IT
    def main_window_activation (self, app):

        #-----------------------------------------------------------------------------------------------------

        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE OF THE MAIN WINDOW
        self.main_window_builder = Gtk.Builder()

        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        self.main_window_builder.set_translation_domain('davinci-helper')

		# IMPORTING THE UI FILE THAT REPRESENT THE MAIN WINDOW
        self.main_window_builder.add_from_file(f"{ui_path}/main.ui")

        # OBTAINING THE MAIN WINDOW AND HER CHILD FROM THE UI FILE
        self.main_window = self.main_window_builder.get_object("main_window")

        # SETTING THE MAIN WINDOW TO CLOSE THE APP AFTER ALL APP WINDOWS ARE CLOSED
        self.main_window.set_application(self)

        #-----------------------------------------------------------------------------------------------------

        # IMPORTING SIDEBAR OBJECTS FROM THE UI FILE
        self.sidebar_ui_import()

        # IMPORTING FUNCTIONS PAGES OBJECTS FROM THE UI FILE
        self.functions_pages_ui_import ()

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_menu_button = self.main_window_builder.get_object("main_window_menu_button")

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE INFO ABOUT THE SYSTEM THEME
        self.style_manager = Adw.StyleManager.get_default()

        # STARTING THE FUNCTION THAT DETECTS THE THEME AND CHAGES THE ICONS EVERY TIME THE THEME IS CHANGED
        self.style_manager.connect("notify::dark", lambda *args: self.apply_current_theme())

        # INITIAL START OF THE DETECT THEME FUNCTION
        self.apply_current_theme()

        #-----------------------------------------------------------------------------------------------------
        
        # GETTING THE SETTING MANAGEMENT DIALOG CLASS
        self.setting_management_dialog_class = setting_management_dialog_class(self)

        # GETTING THE WELCOME SPLASH SCREEN DIALOG CLASS
        self.welcome_dialog_dialog_class = welcome_dialog_class(self)

        # GETTING THE ABOUT DIALOG CLASS
        self.about_dialog_class = about_dialog_class(self)

        #-----------------------------------------------------------------------------------------------------

        # GETTING START SCREEN UI
        self.start_screen_class = start_screen_class(self)

        # GETTING THE FUNCTION UI
        self.function_1_class = function_1_class(self)

        # GETTING THE FUNCTION UI
        self.function_2_class = function_2_class(self)

        # GETTING THE FUNCTION UI
        self.function_3_class = function_3_class(self)

        # GETTING THE FUNCTION UI
        self.function_4_class = function_4_class(self)

        # GETTING THE FUNCTION UI
        self.function_5_class = function_5_class(self)

        # GETTING THE FUNCTION UI
        self.ffmpeg_install_class = ffmpeg_install_class(self)

        #-----------------------------------------------------------------------------------------------------

        # SETTING THE SIDEBAR MENU TEXT LABELS
        self.sidebar_label_setting()

        # LOADING THE PAGE CONTENT INSIDE THE STACK PAGES
        self.load_page_content()

        #-----------------------------------------------------------------------------------------------------

        # CONNECTING THE SIDEBAR ITEM LIST TO THE FUNCTION THAT STARTS THE CORRECT FUNCTION FOR EVERY ITEM
        self.main_window_sidebar_menu.connect("row-selected", self.on_row_selected)

        #-----------------------------------------------------------------------------------------------------

        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        self.main_window.present()

        #-----------------------------------------------------------------------------------------------------

        # SETTING THE WELCOME SPLASH SCREEN WINDOW TO LAUNCH THE UPDATE CHECK AFTER THE WINDOW IS CLOSED
        self.welcome_dialog_dialog_class.dialog_window.connect("closed", lambda window: threading.Thread(target=self.start_update_check).start())

        # CHECKING IF IS NECESSARY TO SHOW THE SPLASH SCREEN AND STARTING IT
        splash_screen_presence = self.welcome_dialog_dialog_class.check_splash_screen()

        # CHECKING IF THE SPLASH SCREEN HAS BEEN LAUNCHED TO CORRECTLY LAUNCH THE UPDATE CHECK
        if splash_screen_presence != True :

            # STARTING THE UPDATE CHECK
            threading.Thread(target=self.start_update_check).start()
        
        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT IMPORTS THE FUNCTIONS PAGES OBJECTS FROM THE UI FILE
    def functions_pages_ui_import (self):

        #-----------------------------------------------------------------------------------------------------

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_function_stack = self.main_window_builder.get_object("main_window_function_stack")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.function_1_content_revealer = self.main_window_builder.get_object("function_1_content_revealer")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.function_2_content_revealer = self.main_window_builder.get_object("function_2_content_revealer")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.function_3_content_revealer = self.main_window_builder.get_object("function_3_content_revealer")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.function_4_content_revealer = self.main_window_builder.get_object("function_4_content_revealer")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.function_5_content_revealer = self.main_window_builder.get_object("function_5_content_revealer")

        #-----------------------------------------------------------------------------------------------------

    # FUNCTION THAT IMPORTS THE SIDEBAR MENU OBJECTS FROM THE UI FILE
    def sidebar_ui_import (self):

        #-----------------------------------------------------------------------------------------------------

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_sidebar_menu = self.main_window_builder.get_object("main_window_sidebar_menu")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_sidebar_icon_1 = self.main_window_builder.get_object("main_window_sidebar_icon_1")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_sidebar_icon_2 = self.main_window_builder.get_object("main_window_sidebar_icon_2")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_sidebar_icon_3 = self.main_window_builder.get_object("main_window_sidebar_icon_3")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_sidebar_icon_4 = self.main_window_builder.get_object("main_window_sidebar_icon_4")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_sidebar_icon_5 = self.main_window_builder.get_object("main_window_sidebar_icon_5")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_sidebar_label_1 = self.main_window_builder.get_object("main_window_sidebar_label_1")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_sidebar_label_2 = self.main_window_builder.get_object("main_window_sidebar_label_2")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_sidebar_label_3 = self.main_window_builder.get_object("main_window_sidebar_label_3")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_sidebar_label_4 = self.main_window_builder.get_object("main_window_sidebar_label_4")

        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_sidebar_label_5 = self.main_window_builder.get_object("main_window_sidebar_label_5")


        #-----------------------------------------------------------------------------------------------------
    
    # FUNCTION THAT DETECT EVERY THEME CHANGE AND SWITCH THE ICONS ACCORDING TO IT
    def apply_current_theme (self):

        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF THE SYSTEM IS USING THE DARK MODE
        if self.style_manager.get_dark():

            # SETTING THE WHITE ICON FOLDER FOR DARK MODE
            mode_path = "dark_mode"

        else :
            
            # SETTING THE DARK ICON FOLDER FOR WHITE MODE
            mode_path = "white_mode"

        #-----------------------------------------------------------------------------------------------------

        # SETTING THE SIDEBAR ICON
        self.main_window_sidebar_icon_1.set_from_file(f"{icon_path}/{mode_path}/function_1.svg")

        # SETTING THE SIDEBAR ICON
        self.main_window_sidebar_icon_2.set_from_file(f"{icon_path}/{mode_path}/function_2.svg")

        # SETTING THE SIDEBAR ICON
        self.main_window_sidebar_icon_3.set_from_file(f"{icon_path}/{mode_path}/function_3.svg")

        # SETTING THE SIDEBAR ICON
        self.main_window_sidebar_icon_4.set_from_file(f"{icon_path}/{mode_path}/function_4.svg")

        # SETTING THE SIDEBAR ICON
        self.main_window_sidebar_icon_5.set_from_file(f"{icon_path}/{mode_path}/function_5.svg")

        #-----------------------------------------------------------------------------------------------------



        



    # FUNCTION THAT WILL SET THE SIDERBAR MENU TEXT LABEL
    def sidebar_label_setting (self):

        #-----------------------------------------------------------------------------------------------------

        # LOADING SIDEBAR TEXT
        self.main_window_sidebar_label_1.set_text(_("Install missing dependencies"))

        # LOADING SIDEBAR TEXT
        self.main_window_sidebar_label_2.set_text(_("Launch DaVinci Resolve installer"))

        # LOADING SIDEBAR TEXT
        self.main_window_sidebar_label_3.set_text(_("Apply post installation fix"))

        # LOADING SIDEBAR TEXT
        self.main_window_sidebar_label_4.set_text(_("Check and install GPU drivers"))

        # LOADING SIDEBAR TEXT
        self.main_window_sidebar_label_5.set_text(_("DaVinci Video Converter"))

        #-----------------------------------------------------------------------------------------------------

    # FUNCTION THAT WILL ADD THE CONTENT INSIDE THE STACK PAGES
    def load_page_content (self):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE FUNCTION UI CONTAINER
        self.start_screen_content_container = self.main_window_builder.get_object("start_screen_content_container")

        # SETTING THE FUNCTION UI INSIDE THE CONTAINER
        self.start_screen_content_container.append(self.start_screen_class)

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE FUNCTION UI CONTAINER
        self.function_1_content_container = self.main_window_builder.get_object("function_1_content_container")

        # SETTING THE FUNCTION UI INSIDE THE CONTAINER
        self.function_1_content_container.append(self.function_1_class)

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE FUNCTION UI CONTAINER
        self.function_2_content_container = self.main_window_builder.get_object("function_2_content_container")

        # SETTING THE FUNCTION UI INSIDE THE CONTAINER
        self.function_2_content_container.append(self.function_2_class)

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE FUNCTION UI CONTAINER
        self.function_3_content_container = self.main_window_builder.get_object("function_3_content_container")

        # SETTING THE FUNCTION UI INSIDE THE CONTAINER
        self.function_3_content_container.append(self.function_3_class)

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE FUNCTION UI CONTAINER
        self.function_4_content_container = self.main_window_builder.get_object("function_4_content_container")

        # SETTING THE FUNCTION UI INSIDE THE CONTAINER
        self.function_4_content_container.append(self.function_4_class)

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE FUNCTION UI CONTAINER
        self.function_5_content_container = self.main_window_builder.get_object("function_5_content_container")

        #-----------------------------------------------------------------------------------------------------

    # FUNCTION THAT WILL START THE UPDATE CHECK
    def start_update_check (self):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE REMOTE GITHUB INFO
        version_exist, version_number, version_changelog, app_version = check_update()

        # STARTING THE UPDATE CHECK ON APP STARTUP
        GLib.idle_add(self.check_update_on_start, version_exist, version_number, version_changelog)

        #-----------------------------------------------------------------------------------------------------






    # FUNCTION THAT WILL RESET THE APP SETTINGS AND WILL SHOWS A DIALOG
    def reset_settings (self, action, test):

        #-----------------------------------------------------------------------------------------------------

        # STARTING THE FUNCTION THAT RESTORES THE DEFAULT SETTINGS
        restore_settings()
        
        # SHOWING THE DIALOG WINDOW
        self.setting_management_dialog_class.show_dialog()

        #-----------------------------------------------------------------------------------------------------
    
    # FUNCTION THAT WILL SHOW THE ABOUT THIS APP DIALOG
    def show_about_dialog (self, action, test):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING THE DIALOG WINDOW
        self.about_dialog_class.show_dialog(self)

        #-----------------------------------------------------------------------------------------------------







    # FUNCTION THAT WILL CHECK THE PRESENCE OF UPDATES EVERYTIME THE APP IS STARTED
    def check_update_on_start (self, version_exist, version_number, version_changelog):

        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF A NEW VERSION IS AVAILABLE
        if version_exist == True :

            # GETTING THE DIALOG CLASS
            self.check_update_dialog_class = check_update_dialog_class(self, version_number, version_changelog)

            # SHOWING THE DIALOG
            self.check_update_dialog_class.show_dialog()

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT RECEIVES THE INPUT FROM THE SIDEBAR LIST AND STARTS THE CORRECT FUNCTION FOR EVERY ITEM
    def on_row_selected(self, listbox, row):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE LAST USED FUNCTION
        previous_function_name = self.main_window_function_stack.get_visible_child_name()

        # GETTING THE ROW ID OF THE PRESSED ROW
        row_id = row.get_index()

        #-----------------------------------------------------------------------------------------------------

        # DEFINING WHICH ROWS HAS BEEN PRESSED
        if row_id == 0:

            # SETTING THE FUNCTION INTERFACE TO SHOW
            function_name = "function_1"

        elif row_id == 1:
                
            # SETTING THE FUNCTION INTERFACE TO SHOW
            function_name = "function_2"

        elif row_id == 2:
                
            # SETTING THE FUNCTION INTERFACE TO SHOW
            function_name = "function_3"

        elif row_id == 3:
   
            # SETTING THE FUNCTION INTERFACE TO SHOW
            function_name = "function_4"

        elif row_id == 5:

            # SETTING THE FUNCTION INTERFACE TO SHOW
            function_name = "function_5"

            # CHECKING WHICH UI SHOW
            self.choose_default_ui()

        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF IS NECESSARY TO HIDE AND RESET THE FUNCTION
        if (previous_function_name != function_name) and (previous_function_name != "start_screen") :

            # HIDING AND RESETTING PREVIOUS FUNCTION
            self.hide_and_reset_previous_function(previous_function_name)

        #-----------------------------------------------------------------------------------------------------

        # SHOWING FUNCTION
        self.show_function_page(function_name)

        #-----------------------------------------------------------------------------------------------------





    
    # FUNCTION THAT WILL CHECK WHICH UI SHOW WHEN THE FUNCTION IS STARTED
    def choose_default_ui (self):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE PRESENCE OF PREVIOUS UI LOADED INSIDE THE CONTAINER
        function_content = self.function_5_content_container.get_first_child()

        # CHECKING WHICH INTERFACE WAS PREVIOUSLY LOADED
        if function_content == self.ffmpeg_install_class :
            
            # REMOVING THE PREVIOUS INTERFACE
            self.function_5_content_container.remove(self.ffmpeg_install_class)

        elif function_content == self.function_5_class :

            # REMOVING THE PREVIOUS INTERFACE
            self.function_5_content_container.remove(self.function_5_class)

        #-----------------------------------------------------------------------------------------------------

        # REAGING ONE LINE AT TIME THE SETTINGS LIST
        with open(f"{settings_path}/davinci_helper/davinci_helper_settings", 'r', encoding='utf-8') as file :

            for line in file :

                # CHECKING WHICH UI IS NECESSARY TO SHOW
                if line.find("FFMPEG_INSTALLED = FALSE") != -1 :

                    # SETTING THE FFMPEG INSTALL UI INSIDE THE CONTAINER
                    self.function_5_content_container.append(self.ffmpeg_install_class)
                    break

                elif line.find("FFMPEG_INSTALLED = TRUE") != -1 :

                    # SHOWING THE DEFAULT PAGE UI
                    
                    self.function_5_content_container.append(self.function_5_class)
                    break

        #-----------------------------------------------------------------------------------------------------


        


    # FUNCTION THAT HIDES AND RESETS THE PREVIOUS USED FUNCTION
    def hide_and_reset_previous_function (self, previous_function_name):

        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF IS NEEDED THE SPECIAL CODE FOR FUNCTION 5 
        if previous_function_name == "function_5" :

            # RESETTING FUNCTION 5 UI
            self.function_5_class.reset_ui()

            # RESETTING FFMPEG INSTALL UI
            self.ffmpeg_install_class.reset_ui()

        else :

            # CONSTRUCTING THE ATTRIBUTE NAME DYNAMICALLY
            previous_function_class_name = f"{previous_function_name}_class"

            # GETTING THE ATTRIBUTE DYNAMICALLY
            previous_function = getattr(self, previous_function_class_name)

            # RESETTING THE PREVIOUS UI
            previous_function.reset_ui()

        #-----------------------------------------------------------------------------------------------------

        # CONSTRUCTING THE ATTRIBUTE NAME DYNAMICALLY
        previous_function_revealer_name = f"{previous_function_name}_content_revealer"

        # GETTING THE ATTRIBUTE DYNAMICALLY
        previous_function_content_revealer = getattr(self, previous_function_revealer_name)

        # HIDING THE PREVIOUS INTERFACE WITH AN ANIMATION
        previous_function_content_revealer.set_reveal_child(False)

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT SHOWS THE SELECTED FUNCTION
    def show_function_page (self, function_name):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING THE FUNCTION PAGE
        self.main_window_function_stack.set_visible_child_name(function_name)

        # CONSTRUCTING THE ATTRIBUTE NAME DYNAMICALLY
        function_revealer_name = f"{function_name}_content_revealer"

        # GETTING THE ATTRIBUTE DYNAMICALLY
        function_content_revealer = getattr(self, function_revealer_name)

        # SHOWING THE INTERFACE WITH AN ANIMATION
        function_content_revealer.set_reveal_child(True)

        #-----------------------------------------------------------------------------------------------------
   




    #-----------------------------------------------------------------------------------------------------


   




# APP STARTING FUNCTION
def main():

    #-----------------------------------------------------------------------------------------------------

    # STARTING THE FUNCTION THAT CHECKS IF THE SETTINGS EXIST
    check_settings_existence()

    # ASSIGNING THE APP ID AND COPY OF THE MAIN WINDOW CLASS IN A VARIABLE
    app_gui = build_main_window(application_id="com.davinci.helper.app")

    # STARTING THE MAIN WINDOW
    app_gui.run(sys.argv)

    #-----------------------------------------------------------------------------------------------------







#-----------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # STARTING THE SCRIPT
    main()

