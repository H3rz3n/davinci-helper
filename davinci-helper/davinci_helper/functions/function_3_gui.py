#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
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



# DEFINISCO LA CLASSE CHE PERMETTE LA CREAZIONE E MESSA SCHERMO DELLA FINESTRA DELLA FUNZIONE 3
# DEFINING THE CLASS WHO CREATES AND DISPLAYS THE FUNCTION 3 WINDOW
class build_function_3 ():

    # IMPORTO GLI ATTRIBUTI E METODI DALLA CLASSE MADRE UTILIZZANDO LA FUNZIONE INIT E LA SUPERCLASSE
    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, parent):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE
        function_3_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        function_3_window_builder.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA
		# IMPORTING THE UI FILE THAT REPRESENT THE WINDOW
        function_3_window_builder.add_from_file(f"{ui_path}/function_3.ui")
        
        # OTTENGO LA FINESTRA ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE WINDOW AND HER CHILD FROM THE UI FILE
        self.function_3_window = function_3_window_builder.get_object("function_3_window")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.function_3_window.set_transient_for(parent)

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.icon = function_3_window_builder.get_object("function_3_icon")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.title_text = function_3_window_builder.get_object("function_3_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.subtitle_scrollable_container = function_3_window_builder.get_object("function_3_subtitle_scrollable_container")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.sub_title_text = function_3_window_builder.get_object("function_3_sub_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.log_scrollable_container = function_3_window_builder.get_object("function_3_log_scrollable_container")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.log_text_viewer = function_3_window_builder.get_object("function_3_log_text_viewer")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.button_box = function_3_window_builder.get_object("function_3_button_box")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.log_button = function_3_window_builder.get_object("function_3_log_button")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.exit_button = function_3_window_builder.get_object("function_3_exit_button")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.spinner_box = function_3_window_builder.get_object("function_3_spinner_box")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.waiting_text = function_3_window_builder.get_object("function_3_waiting_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.spinner = function_3_window_builder.get_object("function_3_spinner")

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO IL BUFFER DAL CAMPO DI TESTO
        # OBTAINING THE BUFFER FROM THE TEXT FIELD
        self.log_text_viewer_buffer = self.log_text_viewer.get_buffer()

        # CHIUDO LA FINESTRA DELLA FUNZIONE 3 ALLA PRESSIONE DEL BOTONE
        # CLOSE THE FUNCTION 3 WINDOW WHEN THE BUTTON IS PRESSED
        self.exit_button.connect('clicked', lambda button: self.function_3_window.destroy())

        # AVVIO LA FUNZIONE CHE MOSTRA I LOG
        # STARTING THE FUNCTION THAT SHOWS THE LOGS
        self.log_button.connect('clicked', self.show_logs)

        # IMPOSTO IL TESTO ATTESA
        # SETTING THE WAITING TEXT
        self.waiting_text.set_text(_("The time needed to complete the operation will vary\ndepending on on your computer and network performance"))

        
        #-----------------------------------------------------------------------------------------------------






    # FUNZIONE CHE AVVIA LO SCRIPT DELLA FUNZIONE 3
    # FUNCTION THAT STARTS THE FUNCTION 3 SCRIPT
    def start_function (self):

        #-----------------------------------------------------------------------------------------------------

        # MANDO A SCHERMO LA FINESTRA ED I SUOI CHILD
        # PRINTING TO SCREEN THE WINDOW AND HER CHILDS
        self.function_3_window.present()

        # AVVIO DELLA FUNZIONE CHE MOSTRA LA ROTELLA DI CARICAMENTO
        # STARTING THE FUNCTION THAT SHOWS THE LOADING WHEEL
        self.show_spinner()
        
        # AVVIO DELLA FUNZIONE CHE AVVIA L'INSTALLAZIONE DELLE DIPENDENZE
        # STARTING THE FUNCTION THAT STARTS THE DEPENDENCIES INSTALLATION
        threading.Thread(target=self.post_installation).start()

        #-----------------------------------------------------------------------------------------------------




    
    # FUNZIONE CHE ESEGUE CON PERMESSI DI AMMINISTRATORE LO SCRIPT DELLA FUNZIONE 3
    # FUNCTION THAT EXEC AS AMMINISTRATOR THE FUNCTION 3 SCRIPT
    def post_installation (self) :

        #-----------------------------------------------------------------------------------------------------

        # ESECUZIONE CON PERMESSI DI ROOT DELLO SCRIPT DELLA FUNZIONE 3
        # EXECUTING AS ROOT THE FUNCTION 3 SCRIPT
        function_3_log = subprocess.Popen("pkexec python /usr/lib/python*/site-packages/davinci_helper/functions/function_3.py",shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        function_3_log_output, function_3_log_err = function_3_log.communicate()

        # AL COMPLETAMENTO DEL PROCESSO AGGIORNO LA GUI
        # ON PROCESS END UPDATE THE GUI
        GLib.idle_add(self.on_task_complete, function_3_log, function_3_log_output, function_3_log_err )

        #-----------------------------------------------------------------------------------------------------

        





    # FUNZIONE CHE RIPRISTINA LA FINESTRA DELLA FUNZIONE 2 UNA VOLTA CHIUSO IL WIZARD DI INSTALLAZIONE ED AVVIA IL POP-UP PER EVENTUALI ERRORI
    # FUNCTION THAT RESTORE THE FUNCTION 2 WINDOW ONCE THE INSTALLATION WIZARD IS CLOSED AND STARTS THE ERROR POP-UP IF IS NEED
    def on_task_complete(self, function_3_log, function_3_log_output, function_3_log_err):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO DELLA FUNZIONE CHE NASCONDE LA ROTELLA DI CARICAMENTO
        # STARTING THE FUNCTION THAT HIDES THE LOADING WHEEL
        self.hide_spinner()

        # AVVIO DELLA FUNZIONE CHE CONTROLLA LA PRESENZA DI ERRORI NEI LOG E CARICA IL TESTO NEL BUFFER
        # STARTING THE FUNCTION THAT CHECKS IF THERE ARE ANY ERRORS IN THE LOGS AND LOADS THE TEXT TO THE TEXT BUFFER
        self.check_and_load_log_text(function_3_log, function_3_log_output, function_3_log_err)
        
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
    def check_and_load_log_text (self, function_3_log, function_3_log_output, function_3_log_err):

        #-----------------------------------------------------------------------------------------------------

        # CONTROLLO SE LO SCRIPT HA PRODOTTO ERRORI
        # SEARCHING IF THE SCRIPT HAS RETURNED ANY ERROR
        if function_3_log.returncode == 1 :

            # RACCOLGO I LOG IN UNICA VARIABILE
            # JOINING THE LOGS AS A ONE VARIABLE
            log_output = str(function_3_log_output) + str(function_3_log_err)

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
            print(function_3_log_output)

        elif function_3_log_output.find("Request dismissed") != -1 :
            
            # NASCONDO IL BOTTONE PER MOSTRARE I LOG
            # HIDING THE SHOW LOG BUTTON
            self.log_button.hide()

            # AVVIO LA FUNZIONE CHE MOSTRA L'ERRORE DI MANCANZA DEI PERMESSI DI AMMINISTRATORE
            # STARTING THE FUNCTION THAT SHOW THE ERROR ABOUT THE LACK OF ADMIN PERMISSION
            self.show_permission_error()

            # STAMPO NEL TERMINALE I MESSAGGI DI OUTPUT E DI ERRORE
            # PRINTING INSIDE THE TERMINAL THE OUTPUT AND ERROR MESSAGGES
            print(function_3_log_output)

        else :

            # OTTENGO CIÒ CHE È STATO PRECEDENTEMENTE CARICATO NEL BUFFER DEL TESTO
            # OBTAINING WHAT WAS PREVIOUSLY ADDED TO THE TEXT BUFFER
            end_iter = self.log_text_viewer_buffer.get_end_iter()

            # AGGIUNGO IL NUOVO TESTO AL BUFER DEL TESTO
            # ADDING NEW TEXT TO THE TEXT BUFFER
            self.log_text_viewer_buffer.insert(end_iter, function_3_log_output)

            # AVVIO LA FUNZIONE CHE RIPORTA LO STATO DI SUCCESSO
            # STARTING THE FUNCTION THAT SHOWS THE SUCCESS STATE
            self.show_success()

            # STAMPO NEL TERMINALE I MESSAGGI DI OUTPUT E DI ERRORE
            # PRINTING INSIDE THE TERMINAL THE OUTPUT AND ERROR MESSAGGES
            print(function_3_log_output)

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
        self.title_text.set_text(_("The DaVinci Resolve post installation\npatch has been applied"))

        # CARICO IL TESTO DEL SOTTOTITOLO IN CASO DI SUCCESSO
        # LOADING THE SUBTITLE TEXT IN CASE OF SUCCESS
        self.sub_title_text.set_text(_("All the operations have been correctly executed inside the DaVinci Resolve installation folder. Now you can proceed to close this window and check if you are using the correct GPU drivers."))

        #-----------------------------------------------------------------------------------------------------
    




    # FUNZIONE CHE MOSTRA L'ICONA ED IL TESTO IN CASO DI ASSENZA DI ERRORI NELLO SCRIPT
    # FUNCTION THAT SHOW THE ICON AND TEXT IF THE SCRIPT DOESN'T HAVE ANY ERRORS
    def show_error (self):

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA DI IN CASO ERRORE
        # LOADING THE ICON FILE IN CASE OF ERROR
        self.icon.set_from_file(f"{icon_path}/function_icons/error.svg")

        # CARICO IL TESTO DEL TITOLO DI IN CASO ERRORE
        # LOADING TITLE TEXT IN CASE OF ERROR
        self.title_text.set_text(_("There was an error patching DaVinci Resolve"))

        # CARICO IL TESTO DEL SOTTOTITOLO IN CASO DI ERRORE
        # LOADING THE SUBTITLE TEXT IN CASE OF ERROR
        self.sub_title_text.set_text(_("There was an error patching DaVinci Resolve. Please check the logs to have more details"))

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
            self.log_button.set_label(_("Show logs"))

        else :

            # RENDO VISIBILE IL CAMPO DI TESTO DEI LOG
            # SHOWING THE LOGS TEXT FIELD
            self.log_scrollable_container.set_visible(True)
            self.log_button.set_label(_("Hide logs"))

        #-----------------------------------------------------------------------------------------------------
        
