#
# Copyright 2024 Lorenzo Maiuri
# Published under GPL-3.0 license
# GitHub : https://github.com/H3rz3n/davinci-helper
#

#-----------------------------------------------------------------------------------------------------

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
from .file_error_dialog_gui import file_error_dialog_class

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



# DEFINING TEMPLATE PATH
@Gtk.Template(filename=f"{ui_path}/function_2.ui")

# CREATING TEMPLATE CLASS TO EDIT WIDGET
class function_2_class (Gtk.ScrolledWindow):
    
    #-----------------------------------------------------------------------------------------------------

    # DEFINING TEMPLATE NAME
    __gtype_name__ = "Function2"

    #-----------------------------------------------------------------------------------------------------
    
    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_container = Gtk.Template.Child("section_1_container")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_icon = Gtk.Template.Child("section_1_icon")
    
    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_title = Gtk.Template.Child("section_1_title")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_file_entry = Gtk.Template.Child("section_1_file_entry")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_file_button = Gtk.Template.Child("section_1_file_button")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_info_revealer = Gtk.Template.Child("section_1_info_revealer")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_info = Gtk.Template.Child("section_1_info")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_start_button = Gtk.Template.Child("section_1_start_button")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    section_1_info_button = Gtk.Template.Child("section_1_info_button")

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
        self.section_1_icon.set_from_file(f"{icon_path}/main_icons/function_2.svg")

        # LOADING TITLE TEXT
        self.section_1_title.set_text(_("Launch DaVinci Resolve\ninstallation wizard"))

        # LOADING INFO TEXT
        self.section_1_info.set_text(_("This part of the software will ask you to indicate the DaVinci Resolve installer file path, then it will run it with the necessary patch to make it launch properly."))

        # LOADING ENTRY TEXT
        self.section_1_file_entry.set_placeholder_text(_("Please select the 'name.zip' or 'file.run' file to launch the installation wizard of DaVinci Resolve"))

        # CONNECTING THE FILE BUTTON TO THE FUNCTION
        self.section_1_file_button.connect('clicked', self.open_file_dialog)

        # CONNECTING THE INFO BUTTON TO THE FUNCTION
        self.section_1_info_button.connect('clicked', self.show_info)

        # CONNECTING THE START BUTTON TO THE FUNCTION
        self.section_1_start_button.connect('clicked', self.check_and_load_file)

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE LOADING UI
        self.loading_class = loading_class()

        #-----------------------------------------------------------------------------------------------------

        # SETTING THE LOADING UI INSIDE THE CONTAINER
        self.section_2_container.append(self.loading_class)

        #-----------------------------------------------------------------------------------------------------

        # CONNECTING THE LOG BUTTON TO THE FUNCTION
        self.section_3_log_button.connect('clicked', self.show_logs)

        # CONNECTING THE START BUTTON TO THE FUNCTION
        self.section_3_start_button.connect('clicked', self.check_and_load_file)

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

        # CLOSING INFO BOX
        self.section_1_info_revealer.set_reveal_child(False)

        # RESETTING ENTRY TEXT
        self.section_1_file_entry.set_text("")

        # RESETTING BUTTON LABEL
        self.section_1_info_button.set_label(_("Show Info"))

        # HIDING ANIMATION REVEALER
        self.main_self.function_2_content_revealer.set_reveal_child(False)

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT SHOWS THE INFO PARAGRAPH
    def show_info (self, button):
        
        #-----------------------------------------------------------------------------------------------------

        # ACQUIRING VIBILITY STATUS OF THE OBJECT
        current_visibility = self.section_1_info_revealer.get_reveal_child()

        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF THE OBJECT IS VISIBLE
        if current_visibility == True :

            # HIDING THE OBJECT
            self.section_1_info_revealer.set_reveal_child(False)

            # CHANGING BUTTON LABEL
            self.section_1_info_button.set_label(_("Show Info"))

        else :

            # SHOWING THE OBJECT
            self.section_1_info_revealer.set_reveal_child(True)

            # CHANGING BUTTON LABEL
            self.section_1_info_button.set_label(_("Hide info"))

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT OPEN THE FILE CHOOSER DIALOG WINDOW
    def open_file_dialog(self,widget):

        #-----------------------------------------------------------------------------------------------------

        # CREATING THE FILE CHOOSER DIALOG WINDOW
        file_dialog = Gtk.FileDialog.new()

        # MAKING THE WINDOW MODAL
        file_dialog.set_modal(True)

        # SETTING THE WINDOW TITLE
        file_dialog.set_title(_("Select the DaVinci Resolve installer `.zip` or `.run` file"))

        # ACQUIRING THE OPTION TO FILTER THE FILE TYPE THAT THE USER CAN CHOSE
        zip_filter = Gtk.FileFilter()

        # SETTING THE SELECTABLE FILE TYPE NAME
        zip_filter.set_name("Zip Files")

        # SETTING THE SELECTABLE FILE TYPE EXTENSION
        zip_filter.add_pattern("*.zip")

        # SETTING THE SELECTABLE FILE TYPE EXTENSION
        zip_filter.add_pattern("*.ZIP")

        # SETTING THE SELECTABLE FILE TYPE EXTENSION
        zip_filter.add_pattern("*.run")

        # SETTING THE SELECTABLE FILE TYPE EXTENSION
        zip_filter.add_pattern("*.RUN")
        
        # SETTING THE FILTER IN THE FILE CHOOSER DIALOG WINDOW
        file_dialog.set_default_filter(zip_filter)
        
        # PRINTING TO SCREEN THE FILE CHOOSER DIALOG WINDOW, USING AS PARAMETERS
        # THE FUNCTION WINDOW (SO IT'S SETTED AS PARENT), NONE AND THE FUNCTION TO EXECUTE AFTER THE USER SELECT THE FILE
        file_dialog.open(
            parent=self.main_self.main_window,  
            cancellable=None,
            callback=self.get_file_dialog_output
        )

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT IS EXECUTED WHEN A FILE IS CHOOSED
    def get_file_dialog_output(self, file_dialog, result):

        #-----------------------------------------------------------------------------------------------------
        
        # ALWAYS EXECUTE THIS EXCEPT IF THERE ARE ERROS
        try:

            # ACQUIRING THE OBJECT OF THE FILE SELECTED
            file = file_dialog.open_finish(result)

            # ACQUIRING THE PATH OF FILE SELECTED
            file_path = file.get_path()

            # PRINTING THE FILE PATH OF THE SELECTED FILE IN THE FILE PATH TEXT FIELD
            self.section_1_file_entry.set_text(file_path)

        # EXECUTE THIS IF THERE ARE ERRORS
        except GLib.Error as e:

            # PRINTING IN THE TERMINAL THE ERROR MESSAGE
            print(f"Dismissed by the user: {e.message}")

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT CHECKS IF THE FILE IS SUITABLE AND LOAD IT INSIDE THE GTK ENTRY
    def check_and_load_file (self, file_path):

        #-----------------------------------------------------------------------------------------------------

        # OBTAINING THE FILE PATH FROM THE TEXT FIELD
        file_path = self.section_1_file_entry.get_text()

        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF THE FILE PATH IS EMPTY
        if len(file_path) >= 2 :

            #-----------------------------------------------------------------------------------------------------
            
            # ESTABLISHING THE PARAMETERS THAT THE INSTALLATION FILE MUST HAVE
            name_check = ["DaVinci", "Resolve", "Linux"]

            # AZZERAMENTO DELLA VARIABILE DI CONTROLLO E DEL CONTATORE
            # RESETTING THE CONTROL TRIGGER AND THE COUNTER
            check_passed = False
            counter = 0

            # CHECKING IF THE REFERENCE WORDS ARE CONTAINED IN THE FILE NAME
            for word in name_check:
                if word in file_path:
                    counter += 1
                if counter >= 3:
                    check_passed=True

            #-----------------------------------------------------------------------------------------------------

            # CHECKING IF THE NAME CONDITION IS RESPECTED
            if  check_passed == True:

                # LAUNCHING THE LOADING SCREEN
                self.start_loading()

                # STARTING IN ANOTHER THREAD THE FUNCTION SCRIPT TO AVOID UI CRASH
                threading.Thread(target=self.script_launch, args=(file_path,)).start()

            else :
                
                # SETTING THE EXIT ERROR AS "UNSUITABLE FILE"
                error_type = "Unsuitable"

                # GETTING THE DIALOG CLASS
                self.file_error_dialog_class = file_error_dialog_class(self, error_type)

                # SHOWING THE ERROR POP-UP
                self.file_error_dialog_class.show_dialog(self)

            #-----------------------------------------------------------------------------------------------------

        else :

            # SETTING THE EXIT ERROR AS "MISSING FILE"
            error_type = "Missing"

            # GETTING THE DIALOG CLASS
            self.file_error_dialog_class = file_error_dialog_class(self, error_type)

            # SHOWING THE ERROR POP-UP
            self.file_error_dialog_class.show_dialog(self)

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
    def script_launch (self, file_path):

        #-----------------------------------------------------------------------------------------------------

        # LAUNCHING THE FUNCTION SCRIPT
        function_script = subprocess.run(f"python /usr/lib/python*/site-packages/davinci_helper/functions/logic/function_2.py '{file_path}'", shell=True, capture_output=True, text=True)

        #-----------------------------------------------------------------------------------------------------

        # ON PROCESS END UPDATE THE GUI
        GLib.idle_add(self.after_script_end, function_script)

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
            
            # SHOWING THE SUCCESS SCREEN
            self.show_success(function_script)
        
        else :

            # SHOWING THE ERROR SCREEN
            self.show_error(function_script)

        #-----------------------------------------------------------------------------------------------------





    # FUNCTION THAT SHOWS THE SUCCESS SCREEN
    def show_success (self, function_script):

        #-----------------------------------------------------------------------------------------------------

        # LOADING THE ICON FILE
        self.section_3_icon.set_from_file(f"{icon_path}/function_icons/success.svg")

        # LOADING TITLE TEXT
        self.section_3_title.set_text(_("You have successfully started the DaVinci wizard"))

        # LOADING THE SUBTITLE TEXT
        self.section_3_subtitle.set_text(_("You have successfully started the DaVinci Resolve installation wizard.\nNow you can install DaVinci Resolve on your computer."))

        # HIDING THE LOG BUTTON BECAUSE IS USELESS IN THIS CASE
        self.section_3_log_button.set_visible(False)

        #-----------------------------------------------------------------------------------------------------
    




    # FUNCTION THAT SHOWS THE ERROR SCREEN
    def show_error (self, function_script):

        #-----------------------------------------------------------------------------------------------------

        # LOADING THE ICON FILE
        self.section_3_icon.set_from_file(f"{icon_path}/function_icons/error.svg")

        # LOADING TITLE TEXT
        self.section_3_title.set_text(_("There was an error launching the DaVinci wizard"))

        #-----------------------------------------------------------------------------------------------------

        # CHECKING ERROR CODE 1
        if function_script.returncode == 1 :

            # LOADING THE SUBTITLE TEXT
            self.section_3_subtitle.set_text(_("There was an error extracting the DaVinci Resolve installer zip inside the target folder.\nPlease check the logs to have more details."))

        #-----------------------------------------------------------------------------------------------------

        # CHECKING ERROR CODE 2
        
        elif function_script.returncode == 2 :

            # LOADING THE SUBTITLE TEXT
            self.section_3_subtitle.set_text(_("There was an error launching the DaVinci Resolve installation wizard.\nPlease check the logs to have more details."))

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

