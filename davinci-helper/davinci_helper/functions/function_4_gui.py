#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licensa GPL-3.0
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, gi, os, subprocess, threading, locale, gettext

# RICHIESTA DELLE VERSIONI DI GTK ED ADWAITA
# REQUESTING THE CHOOSEN VERSION OF GTK AND ADWAITA
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

# IMPORTO I MODULI NECESSARI
# IMPORTING THE NECESSARY MODULES
from gi.repository import Gtk, Adw, Gdk, Pango, Gio, GLib

#-----------------------------------------------------------------------------------------------------

# DEFINISCO I PERCORSI DEI FILE IMMAGINE
# DEFINING IMAGES FILES PATH
icon_path = os.path.join("/usr/share/davinci-helper/data/icons")

# DEFINISCO I PERCORSI DEI FILE UI
# DEFINING UI FILES PATH
ui_path = os.path.join("/usr/share/davinci-helper/data/ui")

# DEFINISCO I PERCORSI DEI FILE DI TRADUZIONE
# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale")

# DEFINISCO I PERCORSI DEI FILE DI IMPOSTAZIONE
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



# DEFINISCO LA CLASSE CHE PERMETTE LA CREAZIONE E MESSA SCHERMO DELLA FINESTRA DELLA FUNZIONE 4
# DEFINING THE CLASS WHO CREATES AND DISPLAYS THE FUNCTION 4 WINDOW
class build_function_4 ():

    # IMPORTO GLI ATTRIBUTI E METODI DALLA CLASSE MADRE UTILIZZANDO LA FUNZIONE INIT E LA SUPERCLASSE
    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, parent):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE
        function_4_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        function_4_window_builder.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA
		# IMPORTING THE UI FILE THAT REPRESENT THE WINDOW
        function_4_window_builder.add_from_file(f"{ui_path}/function_4.ui")
        
        # OTTENGO LA FINESTRA ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE WINDOW AND HER CHILD FROM THE UI FILE
        self.function_4_window = function_4_window_builder.get_object("function_4_window")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.function_4_window.set_transient_for(parent)

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.icon = function_4_window_builder.get_object("function_4_icon")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.title_text = function_4_window_builder.get_object("function_4_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.subtitle_scrollable_container = function_4_window_builder.get_object("function_4_subtitle_scrollable_container")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.sub_title_text = function_4_window_builder.get_object("function_4_sub_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.log_scrollable_container = function_4_window_builder.get_object("function_4_log_scrollable_container")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.log_text_viewer = function_4_window_builder.get_object("function_4_log_text_viewer")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.button_box = function_4_window_builder.get_object("function_4_button_box")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.log_button = function_4_window_builder.get_object("function_4_log_button")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.exit_button = function_4_window_builder.get_object("function_4_exit_button")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.spinner_box = function_4_window_builder.get_object("function_4_spinner_box")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.waiting_text = function_4_window_builder.get_object("function_4_waiting_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.spinner = function_4_window_builder.get_object("function_4_spinner")

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO IL BUFFER DAL CAMPO DI TESTO
        # OBTAINING THE BUFFER FROM THE TEXT FIELD
        self.log_text_viewer_buffer = self.log_text_viewer.get_buffer()

        # CHIUDO LA FINESTRA DELLA FUNZIONE 4 ALLA PRESSIONE DEL BOTONE
        # CLOSE THE FUNCTION 4 WINDOW WHEN THE BUTTON IS PRESSED
        self.exit_button.connect('clicked', lambda button: self.function_4_window.destroy())

        # AVVIO LA FUNZIONE CHE MOSTRA I LOG
        # STARTING THE FUNCTION THAT SHOWS THE LOGS
        self.log_button.connect('clicked', self.show_logs)

        # IMPOSTO IL TESTO ATTESA
        # SETTING THE WAITING TEXT
        self.waiting_text.set_text(_("The time needed to complete the operation will vary\ndepending on on your computer and network performance"))

        # ACQUISISCO L'OGGETTO DELLA FINESTRA MADRE
        # ACQUIRING MAIN WINDOW OBJECT
        self.parent = parent
        
        #-----------------------------------------------------------------------------------------------------






    # FUNZIONE CHE AVVIA LO SCRIPT DELLA FUNZIONE 4
    # FUNCTION THAT STARTS THE FUNCTION 4 SCRIPT
    def start_function (self):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE CHE CONTROLLA SE È NECESSARIO MOSTRARE L'AVVISO
        # STARTING THE FUNCTION THAT CHEKS IF IS NECESSARY TO SHOW THE WARNING
        start_splash_screen = self.check_splash_screen()

        if start_splash_screen == True :

            # AVVIO LA FUNZIONE CHE MOSTRA LA FINESTRA DI SPLASH SCREEN
            # STARTING THE FUNCTION THAT SHOWS THE SPLASH SCREEN
            self.show_splash_screen()

        else :

            # AVVIO LA FUNZIONE CHE AVVIA IL CONTROLLO E L'INSTALLAZIONE DEI DRIVER GPU
            # STARTING FUNCTION THAT CHECKS AND INSTALLS THE GPU DRIVERS
            self.start_function_4(self)
        
        #-----------------------------------------------------------------------------------------------------




    
    # FUNZIONE CHE ESEGUE CON PERMESSI DI AMMINISTRATORE LO SCRIPT DELLA FUNZIONE 4
    # FUNCTION THAT EXEC AS AMMINISTRATOR THE FUNCTION 4 SCRIPT
    def install_gpu_driver (self) :

        #-----------------------------------------------------------------------------------------------------

        # ESECUZIONE CON PERMESSI DI ROOT DELLO SCRIPT DELLA FUNZIONE 4
        # EXECUTING AS ROOT THE FUNCTION 4 SCRIPT
        function_4_log = subprocess.Popen("pkexec python /usr/lib/python*/site-packages/davinci_helper/functions/function_4.py",shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        function_4_log_output, function_4_log_err = function_4_log.communicate()

        # AL COMPLETAMENTO DEL PROCESSO AGGIORNO LA GUI
        # ON PROCESS END UPDATE THE GUI
        GLib.idle_add(self.on_task_complete, function_4_log, function_4_log_output, function_4_log_err )

        #-----------------------------------------------------------------------------------------------------

        



    # FUNZIONE CHE RIPRISTINA LA FINESTRA DELLA FUNZIONE 2 UNA VOLTA CHIUSO IL WIZARD DI INSTALLAZIONE ED AVVIA IL POP-UP PER EVENTUALI ERRORI
    # FUNCTION THAT RESTORE THE FUNCTION 2 WINDOW ONCE THE INSTALLATION WIZARD IS CLOSED AND STARTS THE ERROR POP-UP IF IS NEED
    def on_task_complete(self, function_4_log, function_4_log_output, function_4_log_err):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO DELLA FUNZIONE CHE NASCONDE LA ROTELLA DI CARICAMENTO
        # STARTING THE FUNCTION THAT HIDES THE LOADING WHEEL
        self.hide_spinner()

        # AVVIO DELLA FUNZIONE CHE CONTROLLA LA PRESENZA DI ERRORI NEI LOG E CARICA IL TESTO NEL BUFFER
        # STARTING THE FUNCTION THAT CHECKS IF THERE ARE ANY ERRORS IN THE LOGS AND LOADS THE TEXT TO THE TEXT BUFFER
        self.check_and_load_log_text(function_4_log, function_4_log_output, function_4_log_err)
        
        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE NASCONDE GLI ELEMENTI DELL'INTERFACCIA LASCIANDO SOLO LA ROTELLA DI CARICAMENTO
    # FUNCTION THAT HIDES ALL THE UI ELEMENTS AND SHOWS ONLY THE LOADING WHEEL
    def show_spinner (self):

        #-----------------------------------------------------------------------------------------------------

        # NASCONDO L'ICONA
        # HIDING THE ICON
        self.icon.set_visible(False)

        # NASCONDO IL TESTO DI TITOLO
        # HIDING THE TITLE TEXT
        self.title_text.set_visible(False)

        # NASCONDO IL CONTENITORE DEL TESTO DI SOTTOTITOLO
        # HIDING THE SCROLLABLE SUBTITLE TEXT CONTAINER
        self.subtitle_scrollable_container.set_visible(False)

        # NASCONDO IL BOX DEI BOTTONE DI USCITA E DI LOG
        # HIDING THE EXIT AND LOG BUTTONS BOX
        self.button_box.set_visible(False)

        #-----------------------------------------------------------------------------------------------------

        # MOSTRO IL BOX DELLO SPINNER
        # SHOWING THE SPINNER BOX
        self.spinner_box.set_visible(True)

        # AVVIO LO SPINNER
        # STARTING THE SPINNER
        self.spinner.start()

        #-----------------------------------------------------------------------------------------------------




    
    # FUNZIONE CHE NASCONDE LA ROTELLA DI CARICAMENTO E MOSTRA TUTTI GLI ALTRI ELEMENTI DELL'INTERFACCIA
    # FUNCTION THAT HIDES THE LOADING WHEEL AND SHOW ALL THE UI ITEMS
    def hide_spinner(self):
        #-----------------------------------------------------------------------------------------------------
        
        # MOSTRO L'ICONA
        # SHOWING THE ICON
        self.icon.set_visible(True)

        # MOSTRO IL TESTO DI TITOLO
        # SHOWING THE TITLE TEXT
        self.title_text.set_visible(True)

        # MOSTRO IL CONTENITORE DEL TESTO DI SOTTOTITOLO
        # SHOWING THE SCROLLABLE SUBTITLE TEXT CONTAINER
        self.subtitle_scrollable_container.set_visible(True)

        # MOSTRO IL BOX DEI BOTTONE DI USCITA E DI LOG
        # SHOWING THE EXIT AND LOG BUTTONS BOX
        self.button_box.set_visible(True)

        #-----------------------------------------------------------------------------------------------------

        # NASCONDO IL BOX DELLO SPINNER
        # HIDING THE SPINNER BOX
        self.spinner_box.set_visible(False)

        # FERMO LO SPINNER
        # STOPPING THE SPINNER
        self.spinner.stop()

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE CONTROLA LA PRESENZA DI ERRORI NEI LOG E CARICA IL TESTO NEL BUFFER
    # FUNCTION THAT CHECKS IF THERE ARE ANY ERRORS IN THE LOGS AND LOADS THE TEXT IN THE TEXT BUFFER
    def check_and_load_log_text (self, function_4_log, function_4_log_output, function_4_log_err):

        #-----------------------------------------------------------------------------------------------------
        
        # CONTROLLO SE LO SCRIPT HA PRODOTTO ERRORI
        # SEARCHING IF THE SCRIPT HAS RETURNED ANY ERROR
        if function_4_log.returncode == 1 :

            # RACCOLGO I LOG IN UNICA VARIABILE
            # JOINING THE LOGS AS A ONE VARIABLE
            log_output = str(function_4_log_output) + str(function_4_log_err)

            # OTTENGO CIÒ CHE È STATO PRECEDENTEMENTE CARICATO NEL BUFFER DEL TESTO
            # OBTAINING WHAT WAS PREVIOUSLY ADDED TO THE TEXT BUFFER
            end_iter = self.log_text_viewer_buffer.get_end_iter()

            # AGGIUNGO IL NUOVO TESTO AL BUFER DEL TESTO
            # ADDING NEW TEXT TO THE TEXT BUFFER
            self.log_text_viewer_buffer.insert(end_iter, log_output)

            # AVVIO LA FUNZIONE CHE RIPORTA LA PRESENZA DI ERRORI
            # STARTING THE FUNCTION THAT SHOWS THE ERRORS
            self.show_error()

            # STAMPO NEL TERMINALE I MESSAGGI DI OUTPUT E DI ERRORE
            # PRINTING INSIDE THE TERMINAL THE OUTPUT AND ERROR MESSAGGES
            print(function_4_log_output)
        
        elif function_4_log.returncode == 2 :

            # RACCOLGO I LOG IN UNICA VARIABILE
            # JOINING THE LOGS AS A ONE VARIABLE
            log_output = str(function_4_log_output) + str(function_4_log_err)

            # OTTENGO CIÒ CHE È STATO PRECEDENTEMENTE CARICATO NEL BUFFER DEL TESTO
            # OBTAINING WHAT WAS PREVIOUSLY ADDED TO THE TEXT BUFFER
            end_iter = self.log_text_viewer_buffer.get_end_iter()

            # AGGIUNGO IL NUOVO TESTO AL BUFER DEL TESTO
            # ADDING NEW TEXT TO THE TEXT BUFFER
            self.log_text_viewer_buffer.insert(end_iter, log_output)

            # AVVIO LA FUNZIONE CHE RIPORTA LA PRESENZA DI UN AVVISO
            # STARTING THE FUNCTION THAT SHOWS A WARNING
            self.show_warning()

            # STAMPO NEL TERMINALE I MESSAGGI DI OUTPUT E DI ERRORE
            # PRINTING INSIDE THE TERMINAL THE OUTPUT AND ERROR MESSAGGES
            print(function_4_log_output)

        elif function_4_log.returncode == 3 :

            # RACCOLGO I LOG IN UNICA VARIABILE
            # JOINING THE LOGS AS A ONE VARIABLE
            log_output = str(function_4_log_output) + str(function_4_log_err)

            # OTTENGO CIÒ CHE È STATO PRECEDENTEMENTE CARICATO NEL BUFFER DEL TESTO
            # OBTAINING WHAT WAS PREVIOUSLY ADDED TO THE TEXT BUFFER
            end_iter = self.log_text_viewer_buffer.get_end_iter()

            # AGGIUNGO IL NUOVO TESTO AL BUFER DEL TESTO
            # ADDING NEW TEXT TO THE TEXT BUFFER
            self.log_text_viewer_buffer.insert(end_iter, log_output)

            # AVVIO LA FUNZIONE CHE RIPORTA LA PRESENZA DI UN ERRORE PER GPU NON SUPPORTATA
            # STARTING THE FUNCTION THAT SHOWS AN ERROR FOR UNSUPPORTED GPU
            self.show_error_unsupported()

            # STAMPO NEL TERMINALE I MESSAGGI DI OUTPUT E DI ERRORE
            # PRINTING INSIDE THE TERMINAL THE OUTPUT AND ERROR MESSAGGES
            print(function_4_log_output)

        elif function_4_log_output.find("Request dismissed") != -1 :
            
            # NASCONDO IL BOTTONE PER MOSTRARE I LOG
            # HIDING THE SHOW LOG BUTTON
            self.log_button.hide()

            # AVVIO LA FUNZIONE CHE MOSTRA L'ERRORE DI MANCANZA DEI PERMESSI DI AMMINISTRATORE
            # STARTING THE FUNCTION THAT SHOW THE ERROR ABOUT THE LACK OF ADMIN PERMISSION
            self.show_permission_error()

            # STAMPO NEL TERMINALE I MESSAGGI DI OUTPUT E DI ERRORE
            # PRINTING INSIDE THE TERMINAL THE OUTPUT AND ERROR MESSAGGES
            print(function_4_log_output)

        else :

            # OTTENGO CIÒ CHE È STATO PRECEDENTEMENTE CARICATO NEL BUFFER DEL TESTO
            # OBTAINING WHAT WAS PREVIOUSLY ADDED TO THE TEXT BUFFER
            end_iter = self.log_text_viewer_buffer.get_end_iter()

            # AGGIUNGO IL NUOVO TESTO AL BUFER DEL TESTO
            # ADDING NEW TEXT TO THE TEXT BUFFER
            self.log_text_viewer_buffer.insert(end_iter, function_4_log_output)

            # AVVIO LA FUNZIONE CHE RIPORTA LO STATO DI SUCCESSO
            # STARTING THE FUNCTION THAT SHOWS THE SUCCESS STATE
            self.show_success()

            # STAMPO NEL TERMINALE I MESSAGGI DI OUTPUT E DI ERRORE
            # PRINTING INSIDE THE TERMINAL THE OUTPUT AND ERROR MESSAGGES
            print(function_4_log_output)

        #-----------------------------------------------------------------------------------------------------




    # FUNZIONE CHE MOSTRA L'ICONA ED IL TESTO IN CASO DI ASSENZA DI ERRORI NELLO SCRIPT
    # FUNCTION THAT SHOW THE ICON AND TEXT IF THE SCRIPT DOESN'T HAVE ANY ERRORS
    def show_success (self):

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA DI IN CASO SUCCESSO
        # LOADING THE ICON FILE IN CASE OF SUCCESS
        self.icon.set_from_file(f"{icon_path}/function_icons/success.svg")

        # CARICO IL TESTO DEL TITOLO DI IN CASO SUCCESSO
        # LOADING TITLE TEXT IN CASE OF SUCCESS
        self.title_text.set_text(_("The GPU drivers have been installed successfully"))

        # CARICO IL TESTO DEL SOTTOTITOLO IN CASO DI SUCCESSO
        # LOADING THE SUBTITLE TEXT IN CASE OF SUCCESS
        self.sub_title_text.set_text(_("Your GPU drivers have been correctly installed\nand now the GPU is supported by DaVinci Resolve."))

        #-----------------------------------------------------------------------------------------------------
    




    # FUNZIONE CHE MOSTRA L'ICONA ED IL TESTO IN CASO DI DI ERRORI NELLO SCRIPT
    # FUNCTION THAT SHOW THE ICON AND TEXT IF THE SCRIPT RETURN ANY ERRORS
    def show_error (self):

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA DI IN CASO ERRORE
        # LOADING THE ICON FILE IN CASE OF ERROR
        self.icon.set_from_file(f"{icon_path}/function_icons/error.svg")

        # CARICO IL TESTO DEL TITOLO DI IN CASO ERRORE
        # LOADING TITLE TEXT IN CASE OF ERROR
        self.title_text.set_text(_("There was an error installing the GPU drivers"))

        # CARICO IL TESTO DEL SOTTOTITOLO IN CASO DI ERRORE
        # LOADING THE SUBTITLE TEXT IN CASE OF ERROR
        self.sub_title_text.set_text(_("There was an error installing the GPU drivers. Please check the logs to have more details"))

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE MOSTRA L'ICONA ED IL TESTO IN CASO LO SCRIPT RIPORTI UN AVVERTIMENTO
    # FUNCTION THAT SHOW THE ICON AND TEXT IF THE SCRIPT RETURN A WARNING
    def show_warning (self):

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA DI IN CASO AVVISO
        # LOADING THE ICON FILE IN CASE OF WARNING
        self.icon.set_from_file(f"{icon_path}/function_icons/warning.svg")

        # CARICO IL TESTO DEL TITOLO DI IN CASO AVVISO
        # LOADING TITLE TEXT IN CASE OF WARNING
        self.title_text.set_text(_("Your GPU is currently not supported by this app"))

        # CARICO IL TESTO DEL SOTTOTITOLO IN CASO DI AVVISO
        # LOADING THE SUBTITLE TEXT IN CASE OF WARNING
        self.sub_title_text.set_text(_("It was impossible to install the drivers for your GPU\nbecause it is currently not supported by this app."))

        #-----------------------------------------------------------------------------------------------------

    



    # FUNZIONE CHE MOSTRA L'ICONA ED IL TESTO IN CASO DI DI ERRORI NELLO SCRIPT
    # FUNCTION THAT SHOW THE ICON AND TEXT IF THE SCRIPT RETURN ANY ERRORS
    def show_error_unsupported (self):

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA DI IN CASO ERRORE
        # LOADING THE ICON FILE IN CASE OF ERROR
        self.icon.set_from_file(f"{icon_path}/function_icons/error.svg")

        # CARICO IL TESTO DEL TITOLO DI IN CASO ERRORE
        # LOADING TITLE TEXT IN CASE OF ERROR
        self.title_text.set_text(_("Your GPU is not supported by DaVinci Resolve"))

        # CARICO IL TESTO DEL SOTTOTITOLO IN CASO DI ERRORE
        # LOADING THE SUBTITLE TEXT IN CASE OF ERROR
        self.sub_title_text.set_text(_("It was impossible to install the drivers for your GPU\nbecause it is currently not supported by DaVinci Resolve.\nPlease check the logs for more details."))

        #-----------------------------------------------------------------------------------------------------




    # FUNZIONE CHE MOSTRA L'ICONA ED IL TESTO IN CASO DI DI ERRORI DI PERMESSI NELL'AVVIARE LO SCRIPT
    # FUNCTION THAT SHOW THE ICON AND TEXT IF THE SCRIPT RETURN ANY ERRORS ABOUT START PERMESSION
    def show_permission_error (self):

         #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA DI IN CASO ERRORE
        # LOADING THE ICON FILE IN CASE OF ERROR
        self.icon.set_from_file(f"{icon_path}/function_icons/error.svg")

        # CARICO IL TESTO DEL TITOLO DI IN CASO ERRORE
        # LOADING TITLE TEXT IN CASE OF ERROR
        self.title_text.set_text(_("You need to grant admin permission to use this function"))

        # CARICO IL TESTO DEL SOTTOTITOLO IN CASO DI ERRORE
        # LOADING THE SUBTITLE TEXT IN CASE OF ERROR
        self.sub_title_text.set_text(_("It was impossible to start the function because you didn't give admin permission. Please try again."))

        #-----------------------------------------------------------------------------------------------------



    # FUNZIONE CHE RENDE VISIBILE IL LOG DI ERRORE
    # FUNCTION THAT SHOWS THE ERROR LOGS
    def show_logs (self, widget):

        #-----------------------------------------------------------------------------------------------------

        # ACQUISISCO LO STATO DI VILIBILITÀ DEL CONTENITORE DEI LOG
        # ACQUIRING VIBILITY STATUS OF THE LOG CONTAINER
        current_log_visibility = self.log_scrollable_container.get_visible()

        #-----------------------------------------------------------------------------------------------------

        # ACQUISISCO SE LA FUNZIONE LOG È STATA GIÀ AVVIATA IN PRECEDENZA
        # ACQUIRING IF THE LOG FUNCTION WAS ALREADY STARTED
        if current_log_visibility == True :

            # NASCONDO IL CAMPO DI TESTO DEI LOG
            # HIDING THE LOGS TEXT FIELD
            self.log_scrollable_container.set_visible(False)

        else :

            # RENDO VISIBILE IL CAMPO DI TESTO DEI LOG
            # SHOWING THE LOGS TEXT FIELD
            self.log_scrollable_container.set_visible(True)

        #-----------------------------------------------------------------------------------------------------
        




    # FUNZIONE CHE CONTROLLA SE È NECESSARIO MOSTRARE SPLASH SCREEN
    # FUNCTION THAT CHEKS IF IS NECESSARY TO SHOW THE SPLASH SCREEN
    def check_splash_screen(self):

        #-----------------------------------------------------------------------------------------------------

        # AZZERO I CONTATORI
        # RESETTING THE COUNTERS
        start_splash_screen = False

        # LEGGO LA LISTA DELLE IMPOSTAZIONI RIGA PER RIGA 
        # REAGING ONE LINE AT TIME THE SETTINGS LIST
        with open(f"{settings_path}/davinci_helper_settings", 'r', encoding='utf-8') as file :

            for line in file :

                # CONTROLLO SE È NECESSARIO MOSTRARE SPLASH SCREEN
                # CHECKING IF IS NECESSARY TO SHOW THE SPLASH SCREEN
                if line.find("SHOW_GPU_SPLASH_SCREEN") != -1 and line.find("TRUE") != -1 :

                    # IMPOSTO COME NECESSARIO IL MOSTRARE LA SPLASH SCREEN
                    # SETTING AD NECESSARY TO SHOW THE SPLASH SCREEN
                    start_splash_screen = True
                
        #-----------------------------------------------------------------------------------------------------

        # RESTITUISCO AL PROGRAMMA SE È NECESSARIO MOSTRARE LA SPLASH SCREEN
        # RETURNING TO THE APP IF IS NECESSARY TO SHOW THE SPLASH SCREEN
        return start_splash_screen

        #-----------------------------------------------------------------------------------------------------     





    # FUNZIONE CHE MOSTRA SPLASH SCREEN
    # FUNCTION THAT SHOW THE SPLASH SCREEN
    def show_splash_screen (self):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI 
        # STARTING THE BUILDER FUNCTION TO READ THE UI
        gpu_warning_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        gpu_warning_window_builder.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA
        # IMPORTING THE UI FILE THAT REPRESENT THE WINDOW
        gpu_warning_window_builder.add_from_file(f"{ui_path}/gpu_warning_splash_screen.ui")
        
        # OTTENGO LA FINESTRA ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE WINDOW AND HER CHILD FROM THE UI FILE
        self.gpu_warning_window = gpu_warning_window_builder.get_object("gpu_warning_window")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.gpu_warning_window.set_transient_for(self.parent)

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.gpu_warning_icon = gpu_warning_window_builder.get_object("gpu_warning_icon")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.gpu_warning_title_text = gpu_warning_window_builder.get_object("gpu_warning_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.gpu_warning_sub_title_text = gpu_warning_window_builder.get_object("gpu_warning_sub_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.gpu_warning_no_see_switch = gpu_warning_window_builder.get_object("gpu_warning_no_see_switch")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.gpu_warning_exit_button = gpu_warning_window_builder.get_object("gpu_warning_exit_button")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.gpu_warning_start_function_button = gpu_warning_window_builder.get_object("gpu_warning_start_function_button")

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA
        # LOADING THE ICON FILE
        self.gpu_warning_icon.set_from_file(f"{icon_path}/function_icons/warning.svg")

        # CARICO IL TESTO DEL TITOLO
        # LOADING TITLE TEXT
        self.gpu_warning_title_text.set_text(_("This function is still in BETA"))

        # CARICO IL TESTO DEL SOTTOTITOLO
        # LOADING THE SUBTITLE TEXT
        self.gpu_warning_sub_title_text.set_text(_("This function is currently in a development state and it may not function properly.\nTo finish this part of the software I need your help.\n\nIf you have an AMD GPU or an Intel ARC GPU and are interested in testing GPU drivers or you know how to make them work with DaVinci Resolve,\nplease start a discussion on the GitHub page."))

        # AVVIO LA FUNZIONE CHE CAMBIA LE IMPOSTAZIONI DI VISIBILITÀ DELLA SPLASH SCREEN
        # STARTING THE FUNCTION THAT CHANGES THE VISIBILITY SETTINGS OF THE SPLASH SCREEN
        self.gpu_warning_no_see_switch.connect("notify::active", self.change_spash_screen_status)

        # CHIUDO LA FINESTRA ALLA PRESSIONE DEL BOTONE
        # CLOSING THE WINDOW WHEN THE BUTTON IS PRESSED
        self.gpu_warning_exit_button.connect('clicked', lambda button: self.gpu_warning_window.destroy())

        # AVVIO LA FUNZIONE CHE AVVIA LA FUNZIONE 4
        # STARTING THE FUNCTION THAT STARTS THE FUNCTION 4
        self.gpu_warning_start_function_button.connect('clicked', self.start_function_4_from_spash_screen)

        # MOSTRO LA FINESTRA DI AVVISO
        # SHOWING THE WARNING WINDOW
        self.gpu_warning_window.present()

        #-----------------------------------------------------------------------------------------------------

    



    # FUNZIONE CHE CAMBIA LE IMPOSTAZIONI DI VISIBILITÀ DELLA SPLASH SCREEN
    # FUNCTION THAT CHANGES THE SPLASH SCREEN VISIBILITY SETTINGS
    def change_spash_screen_status(self, widget, status):

        #-----------------------------------------------------------------------------------------------------

        # AZZERO I CONTATORI
        # RESETTING THE COUNTERS
        line_number = 0

        # LEGGO LA LISTA DELLE IMPOSTAZIONI RIGA PER RIGA 
        # REAGING ONE LINE AT TIME THE SETTINGS LIST
        with open(f"{settings_path}/davinci_helper_settings", 'r', encoding='utf-8') as file :

            # ACQUISICO IL CONTENUTO DEL FILE
            # ACQUIRING FILE CONTENT    
            file_content = file.readlines()
        
        # SCORRO IL FILE DUMP RIGA PER RIGA
        # READING LINE BY LINE THE FILE DUMP
        for line in file_content :

            # TROVO L'IMPOSTAZIONE DI VISIBILITÀ
            # FINDING THE VISIBILITY SETTINGS
            if line.find("SHOW_GPU_SPLASH_SCREEN") != -1 and line.find("TRUE") != -1 :

                # IMPOSTO LA SPLASH SCREEN COME NASCOSTA
                # SETTING THE SPLASH SCREEN AS HIDDEN
                file_content[line_number] = "SHOW_GPU_SPLASH_SCREEN = FALSE\n"

                # ESCO DAL CICLO IN MODO SICURO
                # EXTING THE CICLE IN A SECURE WAY
                break

            elif line.find("SHOW_GPU_SPLASH_SCREEN") != -1 and line.find("FALSE") != -1 :

                # IMPOSTO LA SPLASH SCREEN COME VISIBILE
                # SETTING THE SPLASH SCREEN AS VISIBLE
                file_content[line_number] = "SHOW_GPU_SPLASH_SCREEN = TRUE\n"

                # ESCO DAL CICLO IN MODO SICURO
                # EXTING THE CICLE IN A SECURE WAY
                break

            # AUMENTO IL CONTATORE
            # ADDING 1 TO THE COUNTER
            line_number = line_number + 1

        # SOVRASCRIVO LE PRECEDENTI IMPOSTAZIONI
        # OVERWRITING THE PREVIOUS SETTINGS    
        with open(f"{settings_path}/davinci_helper_settings", 'w', encoding='utf-8') as file :

            # SCRIVO IL CONTENUTO NEL FILE
            # WRITING THE CONTENT INSIDE THE FILE
            file.writelines(file_content)
                
        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE AVVIA IL CONTROLLO E L'INSTALLAZIONE DEI DRIVER GPU
    # FUNCTION THAT CHECKS AND INSTALLS THE GPU DRIVERS 
    def start_function_4_from_spash_screen (self, widget):

        #-----------------------------------------------------------------------------------------------------

        # CHIUDO LA FINESTRA DI AVVISO
        # CLOSING THE WARNING WINDOW
        self.gpu_warning_window.destroy()

        # AVVIO LA FUNZIONE CHE AVVIA IL CONTROLLO E L'INSTALLAZIONE DEI DRIVER GPU
        # STARTING FUNCTION THAT CHECKS AND INSTALLS THE GPU DRIVERS
        self.start_function_4(self)

        #-----------------------------------------------------------------------------------------------------


    # FUNZIONE CHE AVVIA IL CONTROLLO E L'INSTALLAZIONE DEI DRIVER GPU
    # FUNCTION THAT CHECKS AND INSTALLS THE GPU DRIVERS
    def start_function_4 (self, widget): 

        #-----------------------------------------------------------------------------------------------------

        # MANDO A SCHERMO LA FINESTRA ED I SUOI CHILD
        # PRINTING TO SCREEN THE WINDOW AND HER CHILDS
        self.function_4_window.present()

        # AVVIO DELLA FUNZIONE CHE MOSTRA LA ROTELLA DI CARICAMENTO
        # STARTING THE FUNCTION THAT SHOWS THE LOADING WHEEL
        self.show_spinner()
        
        # AVVIO DELLA FUNZIONE CHE AVVIA L'INSTALLAZIONE DEI DRIVER GPU
        # STARTING THE FUNCTION THAT STARTS THE GPU DRIVER INSTALLATION
        threading.Thread(target=self.install_gpu_driver).start()

        #-----------------------------------------------------------------------------------------------------