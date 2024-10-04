#
# Copyright 2024 Lorenzo Maiuri
# Published under GPL-3.0 license
# GitHub : https://github.com/H3rz3n/davinci-helper
#

#-----------------------------------------------------------------------------------------------------

# SECTION 1 : DEFAULT FUNCTION UI
# SECTION 2 : LOADING UI
# SECTION 3 : PROGRESS BAR UI

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, gi, os, threading, gettext, locale, subprocess, re, fcntl

# RICHIESTA DELLE VERSIONI DI GTK ED ADWAITA
# REQUESTING THE CHOOSEN VERSION OF GTK AND ADWAITA
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

# IMPORTO I MODULI NECESSARI
# IMPORTING THE NECESSARY MODULES
from gi.repository import Gtk, Adw, Gdk, Pango, Gio, GLib

#-----------------------------------------------------------------------------------------------------

# NOT STANDARD MODULES IMPORT
from .file_size_warning_dialog_gui import file_size_warning_dialog_class
from .converter_dialog_gui import converter_dialog_class
from .module_install_error_dialog_guy import module_install_error_dialog_class
from .loading_gui import loading_class

from ..logic import conversion_settings

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



# DEFINING TEMPLATE PATH
@Gtk.Template(filename=f"{ui_path}/function_5.ui")

# CREATING TEMPLATE CLASS TO EDIT WIDGET
class function_5_class (Gtk.ScrolledWindow):
    
    #-----------------------------------------------------------------------------------------------------

    # DEFINING TEMPLATE NAME
    __gtype_name__ = "Function5"

    #-----------------------------------------------------------------------------------------------------
    
    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_container_1 = Gtk.Template.Child("converter_container_1")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_icon = Gtk.Template.Child("converter_icon")
    
    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_title = Gtk.Template.Child("converter_title")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_subtitle = Gtk.Template.Child("converter_subtitle")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_file_list_container = Gtk.Template.Child("converter_file_list_container")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_video_quality_dropdown = Gtk.Template.Child("converter_video_quality_dropdown")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_audio_quality_dropdown = Gtk.Template.Child("converter_audio_quality_dropdown")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_entry = Gtk.Template.Child("converter_entry")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_entry_button = Gtk.Template.Child("converter_entry_button")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_start_button = Gtk.Template.Child("converter_start_button")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_load_files_button = Gtk.Template.Child("converter_load_files_button")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_delete_files_button = Gtk.Template.Child("converter_delete_files_button")

    #-----------------------------------------------------------------------------------------------------

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_container_2 = Gtk.Template.Child("converter_container_2")

    #-----------------------------------------------------------------------------------------------------

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_container_3 = Gtk.Template.Child("converter_container_3")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_progressbar_label = Gtk.Template.Child("converter_progressbar_label")

    # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
    converter_progressbar = Gtk.Template.Child("converter_progressbar")

    #-----------------------------------------------------------------------------------------------------





    # IMPORTING ATTRIBUTES FROM PARENT CLASS
    def __init__(self, main_window):
        super().__init__()

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE MAIN WINDOW SELF OBJECT
        self.main_self = main_window

        # EXECUTING THE SECURE CLOSE FUNCTION BEFORE CLOSING THE APP
        self.main_self.main_window.connect("close-request", self.on_destroy_button_clicked)

        # CREATING A PLACEHOLDER FOR THE FFMPEG PROCESS
        self.ffmpeg_process = None

        #-----------------------------------------------------------------------------------------------------
    
        # LOADING ICON FILE
        self.converter_icon.set_from_file(f"{icon_path}/main_icons/function_5.svg")

        # LOADING TITLE TEXT
        self.converter_title.set_text(_("DaVinci Video Converter"))

        # LOADING TITLE TEXT
        self.converter_subtitle.set_text(_("Exported video settings"))

        # CONNECTING THE BUTTON TO THE FUNCTION
        self.converter_entry_button.connect('clicked', self.open_output_folder_dialog)

        # CONNECTING THE BUTTON TO THE FUNCTION
        self.converter_delete_files_button.connect('clicked', self.flush_file_list)

        # CONNECTING THE BUTTON TO THE FUNCTION
        self.converter_load_files_button.connect('clicked', self.open_file_dialog)

        # CONNECTING THE BUTTON TO THE FUNCTION
        self.converter_start_button.connect('clicked', self.on_convert_button_clicked)

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE LOADING UI
        self.loading_class = loading_class()

        # SETTING THE LOADING UI INSIDE THE CONTAINER
        self.converter_container_2.append(self.loading_class)

        #-----------------------------------------------------------------------------------------------------
        
        # SETTING THE CONVERTION SUBTITLE
        self.converter_progressbar_label.set_text(_("The time needed to complete this task will vary\non your computer and network performance."))

        #-----------------------------------------------------------------------------------------------------







    # FUNCTION THAT RESET THE UI WHEN THE PAGE IS NOT SHOWED
    def reset_ui (self):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING DEFAULT SECTION
        self.converter_container_1.set_visible(True)

        # HIDING LOADING SECTION
        self.converter_container_2.set_visible(False)

        #-----------------------------------------------------------------------------------------------------

        # HIDING ANIMATION REVEALER
        self.main_self.function_5_content_revealer.set_reveal_child(False)

        # CLEANING FILE LIST
        self.converter_file_list_container.remove_all()

        # CLEANING OUTPUT ENTRY
        self.converter_entry.set_text("")

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT HIDE THE PREVIOUS UI AND DISABLE THE SIDEBAR BUTTONS
    def start_loading (self):

        #-----------------------------------------------------------------------------------------------------

        # HIDING DEFAULT SECTION
        self.converter_container_1.set_visible(False)

        # SHOWING LOADING SECTION
        self.converter_container_2.set_visible(True)

        # HIDING AFTER SCRIPT SECTION
        self.converter_container_3.set_visible(False)

        #-----------------------------------------------------------------------------------------------------

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
        self.converter_container_2.set_visible(False)

        # SHOWING LOADING SECTION
        self.converter_container_1.set_visible(True)

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT OPEN THE FILE CHOOSER DIALOG WINDOW
    def open_output_folder_dialog(self,widget):

        #-----------------------------------------------------------------------------------------------------

        # CREATING THE FILE CHOOSER DIALOG WINDOW
        file_dialog = Gtk.FileDialog.new()

        # MAKING THE WINDOW MODAL
        file_dialog.set_modal(True)

        # SETTING THE WINDOW TITLE
        file_dialog.set_title(_("Select the converted videos output folder"))
        
        # PRINTING TO SCREEN THE FILE CHOOSER DIALOG WINDOW, USING AS PARAMETERS
        # THE FUNCTION WINDOW (SO IT'S SETTED AS PARENT), NONE AND THE FUNCTION TO EXECUTE AFTER THE USER SELECT THE FILE
        file_dialog.select_folder(
            parent=self.main_self.main_window,  
            cancellable=None,
            callback=self.get_output_folder_dialog_output
        )

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT IS EXECUTED WHEN A FILE IS CHOOSED
    def get_output_folder_dialog_output(self, file_dialog, result):

        #-----------------------------------------------------------------------------------------------------
        
        # ALWAYS EXECUTE THIS EXCEPT IF THERE ARE ERROS
        try:

            # ACQUIRING THE OBJECT OF THE FILE SELECTED
            folder = file_dialog.select_folder_finish(result)

            # ACQUIRING THE PATH OF FILE SELECTED
            folder_path = folder.get_path()

            # LOADING THE FOLDER PATH OF THE SELECTED FOLDER IN THE FOLDER PATH TEXT FIELD
            self.converter_entry.set_text(folder_path)

        # EXECUTE THIS IF THERE ARE ERRORS
        except GLib.Error as e:

            # PRINTING IN THE TERMINAL THE ERROR MESSAGE
            print(f"Dismissed by the user: {e.message}")

        #-----------------------------------------------------------------------------------------------------







    # FUNCTION THAT OPEN THE FILE CHOOSER DIALOG WINDOW
    def open_file_dialog(self,widget):

        #-----------------------------------------------------------------------------------------------------

        # CREATING THE FILE CHOOSER DIALOG WINDOW
        file_dialog = Gtk.FileDialog.new()

        # MAKING THE WINDOW MODAL
        file_dialog.set_modal(True)

        # SETTING THE WINDOW TITLE
        file_dialog.set_title(_("Select the files to convert"))

        # ACQUIRING THE OPTION TO FILTER THE FILE TYPE THAT THE USER CAN CHOSE
        video_filter = Gtk.FileFilter()

        # SETTING THE SELECTABLE FILE TYPE NAME
        video_filter.set_name("Video files")

        # SETTING THE SELECTABLE FILE TYPE EXTENSION
        video_filter.add_pattern("*.mov")

        # SETTING THE SELECTABLE FILE TYPE EXTENSION
        video_filter.add_pattern("*.mp4")

        # SETTING THE SELECTABLE FILE TYPE EXTENSION
        video_filter.add_pattern("*.mkv")

        # SETTING THE SELECTABLE FILE TYPE EXTENSION
        video_filter.add_pattern("*.avi")
        
        # SETTING THE FILTER IN THE FILE CHOOSER DIALOG WINDOW
        file_dialog.set_default_filter(video_filter)
        
        # PRINTING TO SCREEN THE FILE CHOOSER DIALOG WINDOW, USING AS PARAMETERS
        # THE FUNCTION WINDOW (SO IT'S SETTED AS PARENT), NONE AND THE FUNCTION TO EXECUTE AFTER THE USER SELECT THE FILE
        file_dialog.open_multiple(
            parent=self.main_self.main_window,  
            cancellable=None,
            callback=self.on_files_selected
        )
        
        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL ADD TO THE LIST THE PATH OF THE USER-SELECTED FILES
    def on_files_selected(self, file_dialog, response):

        #-----------------------------------------------------------------------------------------------------

         # ALWAYS EXECUTE THIS EXCEPT IF THERE ARE ERROS
        try:

            # GETTING THE FILES LIST
            file_list = file_dialog.open_multiple_finish(response)

            #-----------------------------------------------------------------------------------------------------
            
            # ITERATING FOR EVERY FILE INSIDE THE FILE LIST
            for file in file_list:

                # GETTING THE FILE PATH
                file_path = file.get_path()

                # STARTING THE FUNCTION TO ADD THE ROW TO THE LISTBOX AND PASSING IT THE FILE PATH
                self.add_row(file_path)

        # EXECUTE THIS IF THERE ARE ERRORS OR THE OPERATION IS DISMISSED BY THE USER
        except GLib.Error as e:

            # PRINTING IN THE TERMINAL THE ERROR MESSAGE
            print(f"File dialog message : {e.message}")
        
        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL CREATE AND ADD TO THE LIST THE FILE ITEM
    def add_row (self, file_path):

        #-----------------------------------------------------------------------------------------------------

        # CREATING THE LISTBOX ROW
        list_box_row = Gtk.ListBoxRow()

        # CREATING THE MAIN BOX OF THE ROW
        row_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5, hexpand="True")

        # CREATING THE FILE NAME LABEL
        row_label = Gtk.Label(label=f"{file_path}", xalign=0, halign="start", hexpand="True")

        # CREATING THE ROW BUTTON
        row_button = Gtk.Button(icon_name="user-trash-symbolic",  halign="end")

        #-----------------------------------------------------------------------------------------------------

        # SETTING THE CSS OF THE BUTTON
        row_button.get_style_context().add_class("flat")
        row_button.get_style_context().add_class("circular")

        # CONNECTING THE BUTTON'S CLICKED EVENT TO THE REMOVE_ROW FUNCTION
        row_button.connect("clicked", self.on_row_remove_button_clicked, list_box_row)

        #-----------------------------------------------------------------------------------------------------

        # ADDING THE OBJECT TO THE CONTAINER
        row_box.append(row_label)

        # ADDING THE OBJECT TO THE CONTAINER
        row_box.append(row_button)

        # ADDING THE OBJECT TO THE CONTAINER
        list_box_row.set_child(row_box)

        #-----------------------------------------------------------------------------------------------------

        # ADDING THE OBJECT TO THE CONTAINER
        self.converter_file_list_container.append(list_box_row)

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL REMOVE FROM THE FILE LIST THE SELECTED FILE
    def on_row_remove_button_clicked (self, button, list_box_row):

        #-----------------------------------------------------------------------------------------------------

        # REMOVING THE ROW FROM THE FILE LIST
        self.converter_file_list_container.remove(list_box_row)

        #-----------------------------------------------------------------------------------------------------







    # FUNCTION THAT WILL FLUSH THE ENTIRE FILE LIST
    def flush_file_list (self, button):

        #-----------------------------------------------------------------------------------------------------

        # REMOVING ALL THE ITEMS FROM THE LIST
        self.converter_file_list_container.remove_all()

        #-----------------------------------------------------------------------------------------------------







    # FUNCTION THAT WILL READ THE TEXT FROM THE FILE LIST
    def read_file_list_path (self):

        #-----------------------------------------------------------------------------------------------------

        # RESETTING THE COUNTERS
        self.file_path_list = []
        index = 0

        #-----------------------------------------------------------------------------------------------------

        # THIS CODE WILL LOOP UNTIL WE TRIGGER THE EXIT CONDITION
        while True:

            #-----------------------------------------------------------------------------------------------------

            # GETTING THE ROW FROM THE LISTBOX CONTAINER USING THE INDEX
            row = self.converter_file_list_container.get_row_at_index(index)

            #-----------------------------------------------------------------------------------------------------

            # IF THE ROW DOESN'T EXIST, EXIT THE LOOP
            if row is None:

                # EXITING THE WHILE LOOP
                break
            
            #-----------------------------------------------------------------------------------------------------

            # GETTING THE CONTENT OF THE ROW
            container = row.get_child()
            
            # GETTING THE FIRST CHILD OF THE ROW CONTAINER
            child = container.get_first_child()

            # EXEC THIS CODE UNTIL THERE ARE NO MORE CHILD INSIDE THE CONTAINER
            while child is not None:
                
                # CHECKING IF THE CHILD IS GTKLABEL
                if isinstance(child, Gtk.Label):

                    # EXTRACTING THE TEXT FROM THE GTKLABEL
                    self.file_path_list.append(child.get_text())

                # CHECKING THE NEXT CHILD OF THE CONTAINER
                child = child.get_next_sibling()
            
            # ADDING ONE TO THE INDEX COUNTER
            index += 1
        
        # RETURNING THE FILE LIST
        return self.file_path_list
        
        #-----------------------------------------------------------------------------------------------------    



    # FUNCTION THAT WILL START WHEN THE CONVERT BUTTON IS CLICKED
    def on_convert_button_clicked (self, button):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE FILE PATH LIST FROM THE UI
        self.file_path_list = self.read_file_list_path()

        # OBTAINING THE FILE PATH FROM THE TEXT FIELD
        output_path = self.converter_entry.get_text()

        # CHECKING IF THE FILE LIST OR THE OUTPUT FOLDER ENTRY ARE EMPTY
        if not self.file_path_list or not output_path :
            
            # CHECKING IF THE FILE LIST IS EMPTY
            if not self.file_path_list and not output_path :

                # SETTING THE ERROR FOR THE DIALOG
                error_type="Missing_Video_And_Output"
                placeholder = None

                # GETTING THE DIALOG CLASS
                self.converter_dialog_class = converter_dialog_class(self, error_type, placeholder)

                # SHOWING THE FILE SIZE WARNING
                self.converter_dialog_class.show_dialog(self)

            elif not self.file_path_list :

                # SETTING THE ERROR FOR THE DIALOG
                error_type="Missing_Video"
                placeholder = None

                # GETTING THE DIALOG CLASS
                self.converter_dialog_class = converter_dialog_class(self, error_type, placeholder)

                # SHOWING THE FILE SIZE WARNING
                self.converter_dialog_class.show_dialog(self)

            elif not output_path :

                # SETTING THE ERROR FOR THE DIALOG
                error_type="Missing_Output"
                placeholder = None

                # GETTING THE DIALOG CLASS
                self.converter_dialog_class = converter_dialog_class(self, error_type, placeholder)

                # SHOWING THE FILE SIZE WARNING
                self.converter_dialog_class.show_dialog(self)

        else :

            # CHECKING IF THE NECESSARY PYTHON MODULES ARE INSTALLED 
            self.check_python_modules()

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL CHECK IF THE NECESSARY PYTHON MODULES ARE INSTALLED
    def check_python_modules (self):

        #-----------------------------------------------------------------------------------------------------

        # LAUNCHING THE FUNCTION THAT WILL INSTAL THE NECESSARY PYTHON MODULES IF IS NEEDED
        check_module = subprocess.run("python /usr/lib/python*/site-packages/davinci_helper/functions/logic/install_python_modules.py", shell=True, capture_output=True, text=True)

        # CHECKING IF THERE ARE ANY ERRORS
        if check_module.returncode == 1 :

            # GETTING THE DIALOG CLASS
            self.module_install_error_dialog_class = module_install_error_dialog_class(self, check_module.stdout)

            # SHOWING THE FILE SIZE WARNING
            self.module_install_error_dialog_class.show_dialog(self)
            

        else :
            
            # STARTING THE LOADING FUNCTION
            self.start_loading()

            # SHOWING THE FILE SIZE WARNING DIALOG
            # STARTING IN ANOTHER THREAD THE FUNCTION SCRIPT TO AVOID UI CRASH
            threading.Thread(target=self.getting_ffmpeg_file_settings).start()

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL CALCULATE THE TOTAL CONVERTED FILE WEIGHT AND THE FFMPEG SETTINGS FOR EACH FILE
    def getting_ffmpeg_file_settings (self):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE SELECTED VIDEO QUALITY
        self.video_quality = self.converter_video_quality_dropdown.get_selected()

        # GETTING THE SELECTED AUDIO QUALITY
        self.audio_quality = self.converter_audio_quality_dropdown.get_selected()

        #-----------------------------------------------------------------------------------------------------

        # CALCULATING THE NEEDED DISK SPACE TO COMPLETE THE CONVERSION
        self.video_settings_list, self.audio_settings, self.total_file_weight, self.unsupported_file_list, self.duration_list = conversion_settings.calculate_disk_space(self.file_path_list, self.video_quality, self.audio_quality)

        #-----------------------------------------------------------------------------------------------------

        # ON PROCESS END UPDATE THE GUI
        GLib.idle_add(self.checking_for_unsupported_files)

        #-----------------------------------------------------------------------------------------------------







    # FUNCTION THAT WILL CHECK IF THERE ARE SOME UNSUPPORTED FILES TO REMOVE
    def checking_for_unsupported_files (self):

        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF THERE ARE UNSUPPORTED FILES
        if self.unsupported_file_list != []:

            # SETTING THE ERROR FOR THE DIALOG
            error_type="Unsupported_Files"

            # GETTING THE DIALOG CLASS
            self.converter_dialog_class = converter_dialog_class(self, error_type, self.unsupported_file_list)

            # CONNECTING THE START BUTTON TO THE FUNCTION
            self.converter_dialog_class.dialog_continue_button.connect('clicked', lambda button : self.remove_unsupported_files())

            # SHOW UNSUPORTED FILE DIALOG
            self.converter_dialog_class.show_dialog(self)

        #-----------------------------------------------------------------------------------------------------

        else :

            # HIDING THE LOADING UI
            self.stop_loading()

            # SHOW FILE SIZE WARNING DIALOG
            self.show_file_size_warning_dialog()
        
        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL REMOVE THE UNSUPPORTED FILE FROM THE LIST OF THE FILE THAT WILL BE CONVERTED
    def remove_unsupported_files (self):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE NUMBER OF FILES INSIDE THE LIST
        index = len(self.file_path_list) - 1

        #-----------------------------------------------------------------------------------------------------

        # GOING BACKWARDS THROUGH THE LIST
        while index >= 0:

            # GETTING THE FILE LIST ELEMENT
            i_file = self.file_path_list[index]

            # SCROLLING DOWN THE UNSUPPORTED FILE LIST
            for u_file in self.unsupported_file_list:

                # CHECKING IF THERE IS A MATCH BETWEEN FILE LIST ELEMENT AND UNSUPPORTED FILE LIST ELEMENT
                if i_file == u_file:

                    # REMOVING THE UNSUPPORTED FILE FROM THE FILE LIST
                    self.file_path_list.pop(index)

                    # REMOVING THE CORRESPONDING ROW IN THE UI
                    row = self.converter_file_list_container.get_row_at_index(index)
                    self.converter_file_list_container.remove(row)

            # DECREMENTING THE INDEX TO MOVE TO THE PREVIOUS ELEMENT
            index -= 1

        #-----------------------------------------------------------------------------------------------------

        # CALCULATING THE NEEDED DISK SPACE TO COMPLETE THE CONVERSION
        self.video_settings_list, self.audio_settings, self.total_file_weight, self.unsupported_file_list, self.duration_list = conversion_settings.calculate_disk_space(self.file_path_list, self.video_quality, self.audio_quality)

        #-----------------------------------------------------------------------------------------------------

        # HIDING THE LOADING UI
        self.stop_loading()

        #-----------------------------------------------------------------------------------------------------

        # CLOSING THE DIALOG WINDOW
        self.converter_dialog_class.dialog_window.close()

        # SHOW FILE SIZE WARNING DIALOG
        self.show_file_size_warning_dialog()

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL SHOW THE FILE SIZE WARNING DIALOG
    def show_file_size_warning_dialog (self):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE DIALOG CLASS
        self.file_size_warning_dialog_class = file_size_warning_dialog_class(self, self.total_file_weight)

        # CONNECTING THE BUTTON TO THE FUNCTION
        self.file_size_warning_dialog_class.dialog_continue_button.connect('clicked', lambda button : self.conversion_function())

        # SHOWING THE FILE SIZE WARNING
        self.file_size_warning_dialog_class.show_dialog(self)

        #-----------------------------------------------------------------------------------------------------







    # FUNCTION THAT WILL SHOW THE PROGRESS BAR
    def show_progress_bar (self):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING DEFAULT SECTION
        self.converter_container_1.set_visible(False)

        # HIDING LOADING SECTION
        self.converter_container_3.set_visible(True)

        #-----------------------------------------------------------------------------------------------------

        # DISABLING MENU BUTTON
        self.main_self.main_window_menu_button.set_sensitive(False)

        # DISABLING SIDEBAR BUTTONS
        self.main_self.main_window_sidebar_menu.set_sensitive(False)

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL HIDE THE PROGRESS BAR
    def hide_progress_bar (self):

        #-----------------------------------------------------------------------------------------------------

        # SHOWING DEFAULT SECTION
        self.converter_container_1.set_visible(True)

        # HIDING LOADING SECTION
        self.converter_container_3.set_visible(False)

        #-----------------------------------------------------------------------------------------------------

        # DISABLING MENU BUTTON
        self.main_self.main_window_menu_button.set_sensitive(True)

        # DISABLING SIDEBAR BUTTONS
        self.main_self.main_window_sidebar_menu.set_sensitive(True)

        #-----------------------------------------------------------------------------------------------------







    # FUNCTION THAT WILL START THE FILE CONVERSION
    def conversion_function (self):
        
        #-----------------------------------------------------------------------------------------------------

        # CLOSING THE DIALOG WINDOW
        self.file_size_warning_dialog_class.dialog_window.close()

        #-----------------------------------------------------------------------------------------------------

        # SHOWING THE PROGRESS BAR INTEFACE
        self.show_progress_bar()

        # GETTING THE FILE NAME WITHOUT THE PATH
        threading.Thread(target=self.start_conversion).start()

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL TRIGGER THE CONVERT FUNCTION THE FIRST TIME
    def start_conversion(self):

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE TOTAL FILE NUMBER
        self.file_number = len(self.file_path_list) - 1

        # DEFINING THE IDEX
        self.index = 0

        #-----------------------------------------------------------------------------------------------------

        # STARTING THE FILE CONVERSION FUNCTION
        self.convert_file()

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL CONVERT THE FILES
    def convert_file(self):
        
        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF THERE ARE FILE TO CONVERT
        if self.index > self.file_number :

            # EXECUTE THE AFTER CONVERSION FUNCTION
            GLib.idle_add(self.process_end)

            # ENDING THE LAST EXECUTION OF UPDATE CHECK
            return 

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE INPUT FILE NAME WITHOUT EXTENSION
        self.file_name_no_ext = os.path.splitext(os.path.basename(self.file_path_list[self.index]))[0]

        # GETTING THE INPUT FILE NAME EXTENSION
        self.file_name_ext = os.path.splitext(os.path.basename(self.file_path_list[self.index]))[1]

        # GETTING THE INPUT FILE NAME
        self.file_name = os.path.basename(self.file_path_list[self.index])

        # GETTING THE INPUT FILE PATH
        self.file_path = os.path.dirname(self.file_path_list[self.index])

        # DEFINING THE OUTPUT FILE NAME
        self.output_file_name = f"{self.file_name_no_ext}_converted.mov"

        # OBTAINING THE FILE PATH FROM THE TEXT FIELD
        self.output_path = self.converter_entry.get_text()

        #-----------------------------------------------------------------------------------------------------

        # SETTING THE FILE THAT IS CURRENTLY CONVERTING IN THE PROGRESS BAR
        GLib.idle_add(self.converter_progressbar.set_text, (_("Converting the file : {self.file_name}")).format(file_name=self.file_name))

        #-----------------------------------------------------------------------------------------------------

        # DEFINING THE FFMPEG COMMAND
        command = f"ffmpeg -i '{self.file_path_list[self.index]}' -progress pipe:1 -c:v dnxhd {self.video_settings_list[self.index]} -c:a {self.audio_settings} -y '{self.output_path}/{self.output_file_name}'"

        # STARTING THE CONVERSION OF THE FILE
        self.ffmpeg_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True, bufsize=1)

        #-----------------------------------------------------------------------------------------------------

        # MAKING THE READING OF OUTPUT OF THE PROCESS NOT BLOCKING
        fd = self.ffmpeg_process.stdout.fileno()
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

        #-----------------------------------------------------------------------------------------------------

        # LAUNCHING THE CHECK OF THE CONVERSION STATE / WHEN GO TO THE NEXT FILE EVERY 1000MS
        GLib.timeout_add(10, self.update_progress)

        #-----------------------------------------------------------------------------------------------------







    # FUNCTION THAT WILL CHECK THE CONVERSION STATE AND WILL TRIGGER THE CONVERSION OF THE NEXT FILE
    def update_progress(self):

        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF THE FILE CONVERSION HAS ENDED
        if self.ffmpeg_process.poll() is not None:

            #-----------------------------------------------------------------------------------------------------

            # PRINTING THE NAME OF THE FINISHED FILES
            print(_("Finished processing the file : {self.file_name}").format(file_name=self.file_name))
            
            # SETTING THE PROGRESS BAR TO 100
            GLib.idle_add(self.converter_progressbar.set_fraction, 1.0)

            # SETTING THE PROGRESS BAR TEXT
            GLib.idle_add(self.converter_progressbar.set_text, _(f"{self.file_name} - 100%"))
            
            # ADDING ONE TO THE INDEX TO GO TO THE NEXT FILE
            self.index += 1

            #-----------------------------------------------------------------------------------------------------

            # EXECUTING THE CONVERT FILE FUNCTION AGAIN AFTER A DELAY OF 500MS, IF THERE ARE OTHERS FILE THEY WILL BE CONVERTED
            # OTHERWISE WILL BE TRIGGERED THE EXIT FUNCTION AND THIS FUNCTION WILL NOT BE REPATED 
            GLib.timeout_add(500, self.reset_progress_bar_and_convert_next_file)

            # RETURNING FALSE TO END THE LAST EXECUTION OF THE UPDATE CHECK
            return False


        #-----------------------------------------------------------------------------------------------------

        # CHECK IF THERE IS OUTPUT FROM FFMPEG
        try:

            # GETTING THE FFMPEG OUTPUT
            output = self.ffmpeg_process.stdout.readline()

        except BlockingIOError:

            # SETTING THE OUTPUT AS NONE IF IS ABSENT
            output = None

        # CHECKING IF THE OUTPUT HAS BEEN ACQUIRED
        if output:

            # READING THE FFMPEG LOG LINE BY LINE
            for line in output.splitlines():

                # CHECK IF THE LOG LINE CONTAINS THE PROCESSED TIME OUTPUT
                if "out_time_ms=" in line:
                    
                    # GETTING THE FFMPEG PROCESSED TIME OUTPUT
                    match = re.search(r"out_time_ms=(\d+)", line)

                    # CHECKING IF THE MATCH HAS BEEN ACQUIRED
                    if match:
                        
                        # EXTRACTING THE VALUE FROM THE OBJECT
                        out_time_ms = int(match.group(1))

                        # CALCULATING THE PROGRESS USING THE FORMULA "PARTIAL ELABORATED TIME / FILE DURATION"
                        progress = out_time_ms / (self.duration_list[self.index] * 1_000_000)  # Calculate progress

                        # SETTING THE PROGRESS BAR %
                        GLib.idle_add(self.converter_progressbar.set_fraction, progress)

                        # SETTING THE PROGRESS BAR TEXT
                        GLib.idle_add(self.converter_progressbar.set_text, _(f"{self.file_name} - {progress * 100:.2f}%"))




        #-----------------------------------------------------------------------------------------------------

        # RETURNING TRUE TO TRIGGER THE FUNCTION TO CONTINUE CHECK THE STATUS
        return True

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL RESET THE PROGRESS BAR AND START THE NEXT FILE CONVERSION
    def reset_progress_bar_and_convert_next_file(self):

        # RESETTING THE BAR %
        GLib.idle_add(self.converter_progressbar.set_text, (_(f"Starting with the next file...")))

        # SETTING THE PROGRESS BAR TEXT
        GLib.idle_add(self.converter_progressbar.set_fraction, 0.0)

        # LAUNCHING AGAIN THE CONVERT FILE
        self.convert_file()



    # FUNCTION THAT WILL BE EXECUTED WHEN THE CONVERSION ENDS AND WILL SHOW THE EXIT DIALOG
    def process_end (self):

        #-----------------------------------------------------------------------------------------------------

        # HIDING THE PROGRESS BAR INTEFACE
        self.hide_progress_bar()

        #-----------------------------------------------------------------------------------------------------

        # SETTING THE ERROR FOR THE DIALOG
        error_type="Video_Output"

        # GETTING THE DIALOG CLASS
        self.converter_dialog_class = converter_dialog_class(self, error_type, self.unsupported_file_list)

        # SHOW UNSUPORTED FILE DIALOG
        self.converter_dialog_class.show_dialog(self)

        #-----------------------------------------------------------------------------------------------------



   



    # FUNCTION THAT WILL END THE FFMPEG PROCESS IF IS STILL IN BACKGROUND WHEN THE WINDOWS IS CLOSED
    def on_destroy_button_clicked(self, widget):
        
        #-----------------------------------------------------------------------------------------------------

        # CHECKING IF THE FFMPEG PROCESS IS STILL RUNNING
        if self.ffmpeg_process and self.ffmpeg_process.poll() is None:
            
            # SETTING THE ERROR FOR THE DIALOG
            error_type="Exit_Dialog"

            # GETTING THE DIALOG CLASS
            self.converter_dialog_class = converter_dialog_class(self, error_type, self.unsupported_file_list)

            # CONNECTING THE EXIT BUTTON TO THE FUNCTION
            self.converter_dialog_class.dialog_close_button.connect('clicked', lambda button : self.close_ffmpeg_process())

            # SHOW UNSUPORTED FILE DIALOG
            self.converter_dialog_class.show_dialog(self)

            # STOPPING THE APP CLOSURE
            return True

        else :

            # CLOSING THE APP
            self.main_self.main_window.destroy()

        #-----------------------------------------------------------------------------------------------------



    # FUNCTION THAT WILL END THE FFMPEG PROCES BEFORE CLOSING THE APP
    def close_ffmpeg_process(self):

        #-----------------------------------------------------------------------------------------------------

        # PRINTING THE ACTION
        print("Terminating FFmpeg process...")

        # TERMINATING THE FFMPEG PROCESS
        self.ffmpeg_process.terminate()

        # WAITING THE PROCESS TO END
        try:

            # WAITING THE PROCESS TO END
            self.ffmpeg_process.wait(timeout=5)

            # CLOSING THE APP
            self.main_self.main_window.destroy()
        
        # IF THE TIMEOUT DOES NOT END CORRECTLY
        except subprocess.TimeoutExpired:

            # PRINTING THE ACTION
            print("FFmpeg process didn't terminate, killing it...")

            # FORCE KILLING THE FFMPEG PROCESS
            self.ffmpeg_process.kill()

            # CLOSING THE APP
            self.main_self.main_window.destroy()

        