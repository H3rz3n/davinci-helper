#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licensa CC-BY-NC-SA
# Published under CC-BY-NC-SA license
#   

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale, re

#-----------------------------------------------------------------------------------------------------

# DEFINISCO I PERCORSI DEI FILE DI TRADUZIONE
# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale")

# DEFINISCO I PERCORSI DEI FILE CON GLI ELENCHI DELLE GPU SUPPORTATE
# DEFINING THE SUPPORTED GPU LIST FILE 
gpu_database_path = os.path.join("/usr/share/davinci-helper/data/gpu_support")

#-----------------------------------------------------------------------------------------------------

# ASSOCIA IL NOME DEL DIZIONARIO DI TRADUZIONE AL FILE CORRISPONDENTE PER IL MODULO LOCALE
# ASSOCIATE THE NAME OF TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE LOCALE MODULE
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



# FUNZIONE CHE INDIVIDUA IL PRODUTTORE DELLA GPU
# FUNCTION THAT FINDS THE GPU VENDOR
def find_gpu_vendor ():

    #-----------------------------------------------------------------------------------------------------

    # ACQUISICO IL PRODUTTORE DELLA GPU
    # ACQUIRING THE GPU VENDOR
    gpu_lspci = subprocess.Popen("lspci | grep -i vga", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
    gpu_lspci_output, gpu_lspci_error = gpu_lspci.communicate()

    # RENDO MINUSCONI TUTTI I CARATTERI DELLA STRINGA
    # MAKING LOWERCASE ALL THE STRING CHARACTER
    gpu_lspci_output = gpu_lspci_output.lower()

    # AZZERO IL CONTATORE
    # RESETTING THE COUNTER
    gpu_vendor = ""

    #-----------------------------------------------------------------------------------------------------

    # CONTROLLO SE L'AZIENDA PRODUTTRICE È NVIDIA
    # CHECKING IF THE VENDOR IS NVIDIA
    if gpu_lspci_output.find("nvidia") != -1 :

        # SALVO IL PRODUTTORE DELLA GPU
        # SAVING THE GPU VENDOR
        gpu_vendor = " nvidia"
    
    # CONTROLLO SE L'AZIENDA PRODUTTRICE È AMD
    # CHECKING IF THE VENDOR IS AMD
    if gpu_lspci_output.find("amd") != -1 :

        # SALVO IL PRODUTTORE DELLA GPU
        # SAVING THE GPU VENDOR
        gpu_vendor =  gpu_vendor + " amd"

    # CONTROLLO SE L'AZIENDA PRODUTTRICE È INTEL
    # CHECKING IF THE VENDOR IS INTEL
    if gpu_lspci_output.find("intel") != -1 :

        # SALVO IL PRODUTTORE DELLA GPU
        # SAVING THE GPU VENDOR
        gpu_vendor =  gpu_vendor + " intel"

    #-----------------------------------------------------------------------------------------------------

    # TOLGO LI SPAZI IN ECCESSO DALLA STRINGA
    # DELETING START AND END SPACES FROM THE STRING
    gpu_vendor = gpu_vendor.strip()

    # RIMANDO AL PROGRAMMA IL NOME DEI PRODUTTORI E L'OUTPUT DI LSPCI
    # RETURNING TO THE APP THE VENDOR NAMES AND THE LSPCI OUTPUT
    return gpu_lspci_output, gpu_vendor

    #-----------------------------------------------------------------------------------------------------





# FUNZIONE CHE ESTRAE IL NOME DELLA GPU DA LSPCI
# FUNCTION THAT EXTRACTS GPU NAME FROM LSPCI
def extract_gpu_model_name(gpu_lspci):

    #-----------------------------------------------------------------------------------------------------

    # ESTRAGGO IL NOME DELLA GPU CONTENUTO TRA LE PARENTESI [ ]
    # EXTRACTING THE GPU FROM THE [ ] BRACKETS
    gpu_model_name_list = re.findall(r'\[(.*?)\]', gpu_lspci)

    # RIMANDO AL PROGRAMMA IL NOME DEL MODELLO DI GPU
    # RETURNING TO THE APP THE GPU MODEL NAME
    return gpu_model_name_list

    #-----------------------------------------------------------------------------------------------------





# FUNZIONE CHE ESTRAE IL NOME NUMERICO DELLA GPU DA LSPCI
# FUNCTION THAT EXTRACTS THE NUMERIC GPU NAME FROM LSPCI
def extract_gpu_model_number (gpu_lspci):

    #-----------------------------------------------------------------------------------------------------

    # ESTRAGGO IL NOME DELLA GPU CONTENUTO TRA LE PARENTESI [ ]
    # EXTRACTING THE GPUS FROM THE [ ] BRACKETS
    square_brackets_output = re.findall(r'\[(.*?)\]', gpu_lspci)

    # AZZERO LA LISTA DEI NOMI NUMERICI DELLE GPU
    # RESETTING THE NUMERIC GPUS NAMES LIST
    gpu_model_number_list = []

    # ESTRAGGO I NOMI NUMERI DELLE GPU
    # EXTRACTING THE NUMERIC GPUS NAMES
    for item in square_brackets_output :

        gpu_model_number_list.extend(re.findall(r'\d+',item))

    # RIMANDO AL PROGRAMMA IL NOME NUMERICO DEL MODELLO DI GPU
    # RETURNING TO THE APP THE GPU NUMERIC MODEL NAME
    return gpu_model_number_list

    #-----------------------------------------------------------------------------------------------------





# FUNZIONE CHE AVVIA LA RICERCA DEL MODELLO DELLA GPU IN USO
# FUNCTION THAT START THE RESERCH OF WHICH GPU MODEL IS IN USE
def start_gpu_support_search(gpu_vendor, gpu_model_name_list, gpu_model_number_list):

    #-----------------------------------------------------------------------------------------------------

    # AZZERO I CONTATORI
    # RESETTING THE COUNTERS
    gpu_supported_nvidia = False
    gpu_supported_amd = False
    gpu_supported_intel = False

    #-----------------------------------------------------------------------------------------------------

    # CONTROLLO SE L'AZIENDA PRODUTTRICE È NVIDIA
    # CHECKING IF THE VENDOR IS NVIDIA
    if gpu_vendor.find("nvidia") != -1 :

        # CONTROLLO SE LA GPU È SUPPORTATA
        # CHECKING IF THE GPU IS SUPPORTED
        gpu_supported_nvidia = check_nvidia_gpu_support(gpu_model_name_list, gpu_model_number_list)
    
    # CONTROLLO SE L'AZIENDA PRODUTTRICE È AMD
    # CHECKING IF THE VENDOR IS AMD
    if gpu_vendor.find("amd") != -1 :

        # CONTROLLO SE LA GPU È SUPPORTATA
        # CHECKING IF THE GPU IS SUPPORTED
        gpu_supported_amd = check_amd_gpu_support(gpu_model_name_list, gpu_model_number_list)

    # CONTROLLO SE L'AZIENDA PRODUTTRICE È INTEL
    # CHECKING IF THE VENDOR IS INTEL
    if gpu_vendor.find("intel") != -1 :

        # CONTROLLO SE LA GPU È SUPPORTATA
        # CHECKING IF THE GPU IS SUPPORTED
        gpu_supported_intel = check_intel_gpu_support(gpu_model_name_list ,gpu_model_number_list)

    #-----------------------------------------------------------------------------------------------------

    # RIMANDO AL PROGRAMMA SE LE GPU SONO SUPPORTATE
    # RETURNING TO THE APP IF THE GPUs ARE SUPPORTED  
    return gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel

    #-----------------------------------------------------------------------------------------------------

        



# FUNZIONE CHE CERCA SE LA GPU NVIDIA È COMPATIBILE
# FUNCTION THAT FINDS IF THE NVIDIA GPU IS COMPATIBLE
def check_nvidia_gpu_support (gpu_model_name_list, gpu_model_number_list):
    
    #-----------------------------------------------------------------------------------------------------

    # AZZERO I CONTATORI
    # RESETTING THE COUNTERS
    gpu_supported_nvidia = False

    #-----------------------------------------------------------------------------------------------------

    # CONTROLLO SE ALMENO UNA DELLE GPU TROVATE NEL SISTEMA CORRISPONDE AD UNA GPU COMPATIBILE
    # CHECKING IF ANY OF THE FOUND GPU IN THE SYSTEM IS COMPATIBLE

    # TROVO IL NOME DELLA GPU CORRISPONDENTE ALLA NUMERO DELLA GPU COMPATIBILE
    # FINDING THE GPU NAME ASSOCIETED TO THE COMPATIBLE GPU NUMERIC NAME

    # È NECESSARIO FARE QUESTO CONTROLLO INCROCIATO POICHÈ FILTRANDO LE PARENTESI QUADRE [ ] È POSSIBILE TROVARE STRINGHE NON CONSONE, GRAZIE AMD
    # IT IS NECESSARY TO DO THIS CROSS CHECK BECAUSE FILTERING THE SQUARE BRACKETS [ ] MAY FIND INCORRECT STRINGS, THANK YOU AMD

    # SCORRO LA LISTA DEI NOMI GPU
    # SLIDING THE GPU NAME LIST
    for gpu_name in gpu_model_name_list :

        # SCORRO LA LISTA DEI NOMI NUMERICI DELLE GPU
        # SLIDING THE GPU NUMERIC NAME LIST
        for gpu_number in gpu_model_number_list :

            # LEGGO LA LISTA DELLE GPU COMPATIBILI RIGA PER RIGA 
            # REAGING ONE LINE AT TIME THE COMPATIBLE GPU LIST
            with open(f"{gpu_database_path}/nvidia_support.txt", 'r', encoding='utf-8') as file :
                for line in file:

                    # CONTROLLO SE IL NOME DELLA GPU È PRESENTE NELLA LISTA DELLE GPU SUPPORTATE E SE COMBACIA CON IL NUMERO DI GPU TROVATO COMPATIBILE
                    # CHECKING IF THE GPU NAME IS PRESENT INSIDE THE SUPPORTED GPU LIST AND IF IT MATCHES THE GPU NUMERIC NAME FOUND AS COMPATIBLE
                    if ((gpu_name.find("gtx") != -1 or gpu_name.find("rtx") != -1 or gpu_name.find("quadro") != -1) and (line.find("GTX") != -1 or line.find("RTX") != -1 or line.find("QUADRO") != -1)) and line.find(gpu_number) != -1 :

                        # STAMPO IL MODELLO DI GPU TROVATO COME COMPATIBILE
                        # PRINTING THE GPU MODEL FOUND AS COMPATIBLE
                        print("")
                        print(_(f"Has been found a compatible Nvidia GPU : {gpu_name.upper()}"))
                        print("")

                        # IMPOSTO COME TROVATA UNA GPU COMPATIBILE NVIDIA
                        # SETTING AD FOUND A SUPPORTED NVIDIA GPU
                        gpu_supported_nvidia = True

                        # ESCO DAL CICLO IN MODO SICURO
                        # EXTING THE CICLE IN A SECURE WAY
                        break

    #-----------------------------------------------------------------------------------------------------

    # RIMANDO AL PROGRAMMA SE SONO STATE TROVATE GPU SUPPORTATE
    # RETURNING TO THE APP IF THERE ARE SUPPORTED GPUs 
    return gpu_supported_nvidia

    #-----------------------------------------------------------------------------------------------------           

        



# FUNZIONE CHE CERCA SE LA GPU AMD È COMPATIBILE
# FUNCTION THAT FINDS IF THE AMD GPU IS COMPATIBLE
def check_amd_gpu_support (gpu_model_name_list, gpu_model_number_list):

    #-----------------------------------------------------------------------------------------------------

    # AZZERO I CONTATORI
    # RESETTING THE COUNTERS
    gpu_supported_amd = False
    
    #-----------------------------------------------------------------------------------------------------

    # CONTROLLO SE ALMENO UNA DELLE GPU TROVATE NEL SISTEMA CORRISPONDE AD UNA GPU COMPATIBILE
    # CHECKING IF ANY OF THE FOUND GPU IN THE SYSTEM IS COMPATIBLE

    # TROVO IL NOME DELLA GPU CORRISPONDENTE ALLA NUMERO DELLA GPU COMPATIBILE
    # FINDING THE GPU NAME ASSOCIETED TO THE COMPATIBLE GPU NUMERIC NAME

    # È NECESSARIO FARE QUESTO CONTROLLO INCROCIATO POICHÈ FILTRANDO LE PARENTESI QUADRE [ ] È POSSIBILE TROVARE STRINGHE NON CONSONE, GRAZIE AMD
    # IT IS NECESSARY TO DO THIS CROSS CHECK BECAUSE FILTERING THE SQUARE BRACKETS [ ] MAY FIND INCORRECT STRINGS, THANK YOU AMD
    
    # SCORRO LA LISTA DEI NOMI GPU
    # SLIDING THE GPU NAME LIST
    for gpu_name in gpu_model_name_list :

        # SCORRO LA LISTA DEI NOMI NUMERICI DELLE GPU
        # SLIDING THE GPU NUMERIC NAME LIST
        for gpu_number in gpu_model_number_list :
            
            # LEGGO LA LISTA DELLE GPU COMPATIBILI RIGA PER RIGA 
            # REAGING ONE LINE AT TIME THE COMPATIBLE GPU LIST
            with open(f"{gpu_database_path}/amd_support.txt", 'r', encoding='utf-8') as file :
            
                for line in file:
                    
                    # CONTROLLO SE IL NOME DELLA GPU È PRESENTE NELLA LISTA DELLE GPU SUPPORTATE E SE COMBACIA CON IL NUMERO DI GPU TROVATO COMPATIBILE
                    # CHECKING IF THE GPU NAME IS PRESENT INSIDE THE SUPPORTED GPU LIST AND IF IT MATCHES THE GPU NUMERIC NAME FOUND AS COMPATIBLE
                    if ((gpu_name.find("rx") != -1 or gpu_name.find("vega") != -1) and (line.find("RX") != -1 or line.find("VEGA") != -1 )) and line.find(gpu_number) != -1 :

                        # STAMPO IL MODELLO DI GPU TROVATO COME COMPATIBILE
                        # PRINTING THE GPU MODEL FOUND AS COMPATIBLE
                        print("")
                        print(_(f"Has been found a compatible AMD GPU : {gpu_name.upper()}"))
                        print("")

                        # IMPOSTO COME TROVATA UNA GPU COMPATIBILE AMD
                        # SETTING AD FOUND A SUPPORTED AMD GPU
                        gpu_supported_amd = True

                        # RIMANDO AL PROGRAMMA SE SONO STATE TROVATE GPU SUPPORTATE
                        # RETURNING TO THE APP IF THERE ARE SUPPORTED GPUs 
                        return gpu_supported_amd

                        # ESCO DAL CICLO IN MODO SICURO
                        # EXTING THE CICLE IN A SECURE WAY
                        break
                    
            
    #-----------------------------------------------------------------------------------------------------
    
    # RIMANDO AL PROGRAMMA SE SONO STATE TROVATE GPU SUPPORTATE
    # RETURNING TO THE APP IF THERE ARE SUPPORTED GPUs 
    return gpu_supported_amd

    #-----------------------------------------------------------------------------------------------------
    




# FUNZIONE CHE CERCA SE LA GPU INTEL È COMPATIBILE
# FUNCTION THAT FINDS IF THE INTEL GPU IS COMPATIBLE
def check_intel_gpu_support (gpu_model_name_list, gpu_model_number_list):
    
    #-----------------------------------------------------------------------------------------------------

    # AZZERO I CONTATORI
    # RESETTING THE COUNTERS
    gpu_supported_intel = False

    #-----------------------------------------------------------------------------------------------------

    # CONTROLLO SE ALMENO UNA DELLE GPU TROVATE NEL SISTEMA CORRISPONDE AD UNA GPU COMPATIBILE
    # CHECKING IF ANY OF THE FOUND GPU IN THE SYSTEM IS COMPATIBLE

    # TROVO IL NOME DELLA GPU CORRISPONDENTE ALLA NUMERO DELLA GPU COMPATIBILE
    # FINDING THE GPU NAME ASSOCIETED TO THE COMPATIBLE GPU NUMERIC NAME

    # È NECESSARIO FARE QUESTO CONTROLLO INCROCIATO POICHÈ FILTRANDO LE PARENTESI QUADRE [ ] È POSSIBILE TROVARE STRINGHE NON CONSONE, GRAZIE AMD
    # IT IS NECESSARY TO DO THIS CROSS CHECK BECAUSE FILTERING THE SQUARE BRACKETS [ ] MAY FIND INCORRECT STRINGS, THANK YOU AMD

    # SCORRO LA LISTA DEI NOMI GPU
    # SLIDING THE GPU NAME LIST
    for gpu_name in gpu_model_name_list :

        # SCORRO LA LISTA DEI NOMI NUMERICI DELLE GPU
        # SLIDING THE GPU NUMERIC NAME LIST
        for gpu_number in gpu_model_number_list :

            # LEGGO LA LISTA DELLE GPU COMPATIBILI RIGA PER RIGA 
            # REAGING ONE LINE AT TIME THE COMPATIBLE GPU LIST
            with open(f"{gpu_database_path}/intel_support.txt", 'r', encoding='utf-8') as file :
                for line in file:

                    # CONTROLLO SE IL NOME DELLA GPU È PRESENTE NELLA LISTA DELLE GPU SUPPORTATE E SE COMBACIA CON IL NUMERO DI GPU TROVATO COMPATIBILE
                    # CHECKING IF THE GPU NAME IS PRESENT INSIDE THE SUPPORTED GPU LIST AND IF IT MATCHES THE GPU NUMERIC NAME FOUND AS COMPATIBLE
                    if ((gpu_name.find("arc") != -1 ) and (line.find("ARC") != -1 )) and line.find(gpu_number) != -1 :

                        # STAMPO IL MODELLO DI GPU TROVATO COME COMPATIBILE
                        # PRINTING THE GPU MODEL FOUND AS COMPATIBLE
                        print("")
                        print(_(f"Has been found a compatible Intel GPU : {gpu_name.upper()}"))
                        print("")

                        # IMPOSTO COME TROVATA UNA GPU COMPATIBILE INTEL
                        # SETTING AD FOUND A SUPPORTED INTEL GPU
                        gpu_supported_intel = True

                        # ESCO DAL CICLO IN MODO SICURO
                        # EXTING THE CICLE IN A SECURE WAY
                        break

    #-----------------------------------------------------------------------------------------------------

    # RIMANDO AL PROGRAMMA SE SONO STATE TROVATE GPU SUPPORTATE
    # RETURNING TO THE APP IF THERE ARE SUPPORTED GPUs 
    return gpu_supported_intel

    #-----------------------------------------------------------------------------------------------------





# FUNZIONE CHE STAMPA IL MESSAGGIO DI ERRORE IN CASO LE GPU NON SIA SUPPORTATE
# FUNCTION THAT PRINTS THE ERROR MESSAGE IF THE APP HAS NOT FOUND A COMPATIBLE GPU
def check_supported_gpu_presence(gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel):

    #-----------------------------------------------------------------------------------------------------

    # CONTROLLO SE NESSUNA GPU È COMPATIBILE
    # CHECKING IF THERE ISN'T A COMPATIBLE GPU
    if gpu_supported_nvidia == False and gpu_supported_amd == False and gpu_supported_intel == False :

        # STAMPO IL MESSAGGIO DI ERRORE
        # PRINTING THE ERROR MESSAGE
        print("")
        print(_("DEBUG : Has not been found any supported GPU inside your system. If you know that you have a DaVinci Resolve compatible GPU, please open an issue and paste this error code on the project GitHub page :"))
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(3)
    
    #-----------------------------------------------------------------------------------------------------





# FUNZIONE CHE AGGIUNGE IL REPOSITORY RPM FUSION
# FUNCTION THAT ADDS THE RPM FUSION REPOSITORY
def add_repository():

    #-----------------------------------------------------------------------------------------------------

    # ACQUISISCO SE È GIÀ INSTALLATO IL DRIVER PROPRIETARIO NVIDIA
    # ACQUIRING IF IS ALREADY INSTALLED THE PROPRIETARY NVIDIA DRIVER
    rpm_fusion_repo_check = subprocess.Popen("dnf repolist", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
    rpm_fusion_repo_check_output, rpm_fusion_repo_check_err = rpm_fusion_repo_check.communicate()

    # CONTROLLO SE È GIÀ INSTALLATO IL DRIVER PROPRIETARIO NVIDIA
    # CHECKING IF IS ALREADY INSTALLED THE PROPRIETARY NVIDIA DRIVER
    if rpm_fusion_repo_check_output.find("rpmfusion") != -1:

        # STAMPO IL MESSAGGIO
        # PRINTING THE MESSAGE
        print("")
        print(_("The RPM Fusion repository was already added to the system, there was no need to add it."))
        print("")

    else :
    
        # AGGIUNGGO IL REPOSITORY RPM FUSION
        # ADDING THE RPM FUSION REPOSITORY
        adding_repo = subprocess.Popen("dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
        adding_repo_output, adding_repo_error = adding_repo.communicate()

        # CONTROLLO CHE DAVINCI RESOLVE SIA INSTALLATO
        # CHECKING IF DAVINCI RESOLVE IS INSTALLED
        if adding_repo_error != None :

            # STAMPO IL MESSAGGIO DI ERRORE
            # PRINTING THE ERROR MESSAGE
            print("")
            print(_("DEBUG : It was impossible to add the RPM Fusion Free and Non-Free repository. Check your network connection and try again or add it by yourself."))
            print("")
            print(_("Please open an issue and paste this error code on the project GitHub page :"))
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")
            exit(1)

        else :

            # STAMPO IL MESSAGGIO DI OPERAZIONE RIUSCITA
            # PRINTING THE SUCCESSFUL STATE
            print("")
            print(_("Successfully added the RPM Fusion Free and Non-Free repository."))
            print("")

    #-----------------------------------------------------------------------------------------------------





# FUNZIONE CHE AVVIA LA CORRETTA INSTALLAZIONE DEI DRIVER DELLA GPU
# FUNCTION THAT STARTS THE CORRECT GPU DRIVER INSTALLATION
def start_driver_install(gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel):

    #-----------------------------------------------------------------------------------------------------

    # CONTROLLO QUALI DRIVER BISOGNA INSTALLARE ED AVVIO LA GIUSTA FUNZIONE DI INSTALLAZIONE
    # CHECKING WHICH DRIVER NEEDS TO BE INSTALLED AND STARTING THE CORRECT INSTALLATION FUNCTION
    if gpu_supported_nvidia == True :

        # AVVIO L'INSTALLAZIONE DEI DRIVER
        # STARTING THE DRIVER INSTALLATION
        install_nvidia_driver()

    if gpu_supported_amd == True :

        # AVVIO L'INSTALLAZIONE DEI DRIVER
        # STARTING THE DRIVER INSTALLATION
        install_amd_driver()

    if gpu_supported_intel == True :

        # AVVIO L'INSTALLAZIONE DEI DRIVER
        # STARTING THE DRIVER INSTALLATION
        install_intel_driver()

    
    #-----------------------------------------------------------------------------------------------------





# FUNZIONE CHE AVVIA L'INSTALLAZIONE DEI DRIVER NVIDIA
# FUNCTION THAT STARTS THE NVIDIA DRIVER INSTALLATION
def install_nvidia_driver():

    #-----------------------------------------------------------------------------------------------------

    # ACQUISISCO SE È GIÀ INSTALLATO IL DRIVER PROPRIETARIO NVIDIA
    # ACQUIRING IF IS ALREADY INSTALLED THE PROPRIETARY NVIDIA DRIVER
    nvidia_driver_check = subprocess.Popen("dnf list installed | grep akmod-nvidia", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
    nvidia_driver_check_output, nvidia_driver_check_err = nvidia_driver_check.communicate()

    # CONTROLLO SE È GIÀ INSTALLATO IL DRIVER PROPRIETARIO NVIDIA
    # CHECKING IF IS ALREADY INSTALLED THE PROPRIETARY NVIDIA DRIVER
    if nvidia_driver_check_output.find("akmod-nvidia") != -1:

        # STAMPO IL MESSAGGIO
        # PRINTING THE MESSAGE
        print("")
        print(_("The proprietary Nvidia GPU driver was already installed on the system, there was no need to install it."))
        print("")

    else :

        # INSTALLO IL DRIVER PROPRIETARIO NVIDIA
        # INSTALLING THE NVIDIA PROPRIETARY DRIVER  
        nvidia_driver_install = subprocess.Popen("dnf install -y akmod-nvidia", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
        nvidia_driver_install_output, nvidia_driver_install_error = nvidia_driver_install.communicate()

        # CONTROLLO SE CI SONO STATI ERRORI
        # CHECKING IF THERE WERE ERRORS
        if nvidia_driver_install_error != None :

            # STAMPO IL MESSAGGIO DI ERRORE
            # PRINTING THE ERROR MESSAGE
            print("")
            print(_("DEBUG : It was impossible to install the proprietary Nvidia GPU driver. Check your network connection and try again or install it by yourself."))
            print("")
            print(_("Please open an issue and paste this error code on the project GitHub page :"))
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")            
            exit(1)

        else :

            # STAMPO IL MESSAGGIO DI OPERAZIONE RIUSCITA
            # PRINTING THE SUCCESSFUL STATE
            print("")
            print(_("Successfully installed the proprietary Nvidia GPU driver."))
            print("")

    #-----------------------------------------------------------------------------------------------------





# FUNZIONE CHE AVVIA L'INSTALLAZIONE DEI DRIVER GPU AMD
# FUNCTION THAT STARTS THE AMD GPU DRIVER INSTALLATION
def install_amd_driver():

    #-----------------------------------------------------------------------------------------------------
    
    print("")
    print(_("DEBUG : It was impossible to install the drivers for your GPU because is currently not supported by this app. "))
    print("")
    print(_("If you know that your GPU is supported by DaVinci Resolve please open an issue on the project GitHub page :"))
    print("https://github.com/H3rz3n/davinci-helper/issues")
    print("")
    exit(2)
    
    #-----------------------------------------------------------------------------------------------------






# FUNZIONE CHE AVVIA L'INSTALLAZIONE DEI DRIVER GPU INTEL
# FUNCTION THAT STARTS THE INTEL GPU DRIVER INSTALLATION
def install_intel_driver():

   #-----------------------------------------------------------------------------------------------------
    
    print("")
    print(_("DEBUG : It was impossible to install the drivers for your GPU because is currently not supported by this app. "))
    print("")
    print(_("If you know that your GPU is supported by DaVinci Resolve please open an issue on the project GitHub page :"))
    print("https://github.com/H3rz3n/davinci-helper/issues")
    print("")
    exit(2)
    
    #-----------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------
#----------------------------------------------  MAIN ------------------------------------------------
#-----------------------------------------------------------------------------------------------------

# AVVIO LA FUNZIONE CHE INDIVIDUA IL PRODUTTORE DELLA GPU
# STARTING THE FUNCTION THAT FINDS THE GPU VENDOR
gpu_lspci, gpu_vendor = find_gpu_vendor()

# ACQUISICO IL NOME DEL MODELLO DELLA GPU
# ACQUIRING GPU MODEL NAME
gpu_model_name_list = extract_gpu_model_name(gpu_lspci)

# ACQUISICO IL NOME DEL MODELLO DELLA GPU
# ACQUIRING GPU MODEL NAME
gpu_model_number_list = extract_gpu_model_number(gpu_lspci)

# AVVIO LA FUNZIONE CHE INDIVIDUA IL MODELLO DELLA GPU
# STARTING THE FUNCTION THAT FINDS THE GPU MODEL
gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel = start_gpu_support_search(gpu_vendor, gpu_model_name_list, gpu_model_number_list)

# AVVIO LA FUNZIONE CHE CONTROLLA SE NON SONO STATE TROVATE GPU COMPATIBILI
# STARTING THE FUNCTION THAT CHECKS IF THERE ARE NOT BEEN FOUND COMPATIBLE GPUs
check_supported_gpu_presence(gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel)

# AVVIO LA FUNZIONE CHE AGGIUNGE IL REPOSITORY DI RPM FUSION
# STARTING THE FUNCTION THAT ADDS THE RPM FUSION REPOSITORY
add_repository()

# AVVIO LA FUNZIONE CHE INSTALLA I DRIVER GPU NECESSARI
# STARTING THE FUNCTION THAT INSTALLS THE NECESSARY GPU DRIVERS
start_driver_install(gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel)










