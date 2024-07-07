#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licensa CC-BY-NC-SA
# Published under CC-BY-NC-SA license
#



# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, gi, os, subprocess, threading

# RICHIESTA DELLE VERSIONI DI GTK ED ADWAITA
# REQUESTING THE CHOOSEN VERSION OF GTK AND ADWAITA
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

# IMPORTO I MODULI NECESSARI
# IMPORTING THE NECESSARY MODULES
from gi.repository import Gtk, Adw, Gdk, Pango, Gio, GLib



# DEFINISCO I PERCORSI DEI FILE UI
# DEFINING UI FILES PATH
ui_path = os.path.join("/usr/share/davinci-helper/data/ui")



# DEFINISCO LA CLASSE CHE PERMETTE LA CREAZIONE E MESSA SCHERMO DELLA FINESTRA DELLA FUNZIONE 1
# DEFINING THE CLASS WHO CREATES AND DISPLAYS THE FUNCTION 1 WINDOW
class build_function_1 ():

    # IMPORTO GLI ATTRIBUTI E METODI DELLA CLASSE MADRE A"DW.APPLICATION" UTILIZZANDO LA FUNZIONE INIT E LA SUPERCLASSE
    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, parent):

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI DELLA FINESTRA INFO 1
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE OF THE INFO WINDOW 1
        function_1_window_builder = Gtk.Builder()
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA INFO 1
		# IMPORTING THE UI FILE THAT REPRESENT THE INFO WINDOW 1
        function_1_window_builder.add_from_file(f"{ui_path}/function_1.ui")
        
        # OTTENGO LA FINESTRA DI INFO 1 ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE INFO WINDOW 1 AND HER CHILD FROM THE UI FILE
        self.function_window_1 = function_1_window_builder.get_object("function_1_window")

        # IMPOSTO LA FINESTRA DI INFO 1 COME FIGLIA DELLA FINESTRA PRINCIPALE
        # SETTING THE INFO WINDOW 1 AD CHILD OF THE MAIN WINDOW
        self.function_window_1.set_transient_for(parent)

        # OTTENGO IL CAMPO DI TESTO DEL TERMINALE DAL FILE UI
        # OBTAINING THE TERMINAL TEXT FIELD FROM THE UI FILE
        self.terminal_textview_1 = function_1_window_builder.get_object("terminal_text_1")
        
        # OTTENGO IL BUFFER DAL CAMPO DI TESTO
        # OBTAINING THE BUFFER FROM THE TEXT FIELD
        self.terminal_textbuffer_1 = self.terminal_textview_1.get_buffer()
        


    # FUNZIONE CHE MANDA A SCHERMO LA FINESTRA
    # FUNCTION THAT DISPLAYS THE WINDOW
    def print_window (self):

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        self.function_window_1.present()

        # AVVIO IL THREAD SEPARATO PER ESEGUIRE LO SCRIPT DELLA FUNZIONE 1
        # STARTING A SEPARETED THREAD TO EXECUTE THE FUNCTION 1 SCRIPT
        function_1_thread = threading.Thread(target=self.execute_function_1())
        function_1_thread.start()


    
    # FUNZIONE CHE ESEGUE CON PERMESSI DI AMMINISTRATORE LO SCRIPT DELLA FUNZIONE 1
    # FUNCTION THAT EXEC AS AMMINISTRATOR THE FUNCTION 1 SCRIPT
    def execute_function_1(self) :

        # ESECUZIONE CON PERMESSI DI ROOT DELLO SCRIPT DELLA FUNZIONE 1
        # EXECUTING AS ROOT THE FUNCTION 1 SCRIPT
        function_1 = subprocess.Popen("pkexec python /usr/lib/python*/site-packages/davinci_helper/functions/function_1.py",shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        function_1_output, function_1_err = function_1.communicate()

        # AGGIUNGO IL TESTO GENERATO DALLA FUNZIONE 1 AL BUFFER DEL CAMPO DI TESTO "TERMINALE"
        # ADDING THE TEXT FROM FUNCTION 1 TO THE TEXT BUFFER OF THE TEXT FIELD "TERMINAL"
        self.add_text(function_1_output)



    # FUNZIONE CHE AVVIA LA FUNZIONE DI AGGIUNTA DEL TESTO
    # FUNCTION THAT STARTS THE ADDING TEXT FUNCTION
    #
    def add_text(self, text):

        # ESEGUO LA FUNZIONE DI AGGIUNTA DEL TESTO AL BUFFER IN MODO SICURO
        # EXECUTING THE FUNCTION TO ADD TEXT TO THE BUFFER IN A SECURE WAY
        GLib.idle_add(self._add_text, text)


    # FUNZIONE CHE AGGIUNGE IL TESTO AL BUFFER
    # FUNCTION THAT ADDS THE TEXT TO THE BUFFER
    def _add_text(self, text):

        # OTTENGO CIÒ CHE È STATO PRECEDENTEMENTE CARICATO NEL BUFFER DEL TESTO
        # OBTAINING WHAT WAS PREVIOUSLY ADDED TO THE TEXT BUFFER
        end_iter = self.terminal_textbuffer_1.get_end_iter()

        # AGGIUNGO IL NUOVO TESTO AL BUFER DEL TESTO
        # ADDING NEW TEXT TO THE TEXT BUFFER
        self.terminal_textbuffer_1.insert(end_iter, text)








            

        

        

        