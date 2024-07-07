# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, os, subprocess, threading

# FUNZIONE CHE CERCA QUALI LIBRERIE È NECESSARIO INSTALLARE I FEDORA 38-39-40
# FUNCTION THAT SEARCH WHICH LIBRARIES ARE MISSING IN FEDORA 38-39-40
def fix_dependencies_38_39_40 (library_list_output):
    
    
    # CONTROLLO SE LE LIBRERIE NECESSARIE SONO INSTALLATE
    # CHECKING IF ALL THE LIBRARIES NEEDED ARE INSTALLED
    lib_to_install = ""
    
    # CERCO libxcrypt-compat
    # SEARCHING FOR libxcrypt-compat
    if library_list_output.find('libxcrypt-compat') == -1 :
        lib_to_install = lib_to_install + " libxcrypt-compat"
    
    # CERCO libcurl
    # SEARCHING FOR libcurl
    if library_list_output.find('libcurl') == -1 :
        lib_to_install = lib_to_install + " libcurl"
    
    # CERCO libcurl-devel
    # SEARCHING FOR libcurl-devel
    if library_list_output.find('libcurl-devel') == -1 :
        lib_to_install = lib_to_install + " libcurl-devel"
    
    # CERCO mesa-libGLU
    # SEARCHING FOR mesa-libGLU
    if library_list_output.find('mesa-libGLU') == -1 :
        lib_to_install = lib_to_install + " mesa-libGLU"
    
    # CERCO zlib-ng-compat
    # SEARCHING FOR zlib-ng-compat
    if library_list_output.find('zlib') == -1 :
        lib_to_install = lib_to_install + " zlib"


    # CONTROLLO SE CI SONO DELLE LIBRERIE MANCANTI
    # CHEKING IF THERE ARE MISSING LIBRARIES
    if lib_to_install != "" :

        # ELIMINO LO SPAZIO IN ECCESSO DALLA LISTA DELLE LIBRERIE DA INSTALLARE
        # REMOVE EXCESS SPACE FROM THE LIST OF LIBRARIES TO INSTALL
        lib_to_install = lib_to_install.lstrip(' ')

        # STAMPO LA LISTA DELLE LIBRERIE DA INSTALLARE
        # PRINTING THE LIST OF THE LIBRARIES TO INSTALL
        print("The following libraries will be installed because are missing :", lib_to_install, "\n")

        # ESECUZIONE DELLA FUNZIONE CHE INSTALLA LE LIBRERIE MANCANTI
        # EXECUTION OF THE FUNCTION THAT INSTALL THE MISSING LIBRARIES
        libraries_installation(lib_to_install)
    
    else:

        # STAMPO L'ASSENZA DI LIBRERIE DA INSTALLARE
        # PRINTING THE MISSING OF LIBRARIES TO INSTALL
        print("There are no missing libraries to install, you can now install Davinci Resolve ", "\n")



# FUNZIONE CHE ESEGUE IL COMANDO DI INSTALLAZIONE DELLE LIBRERIE
# FUNCTION THAT INSTALL THE MISSING LIBRARIES IN THE SYSTEM
def libraries_installation (lib_to_install):

    # AGGIORNAMENTO DELLA LISTA PACCHETTI DEI REPOSITORY
    # UPDATING THE REPOSITORY PACKAGES LIST'S
    repo_update = subprocess.Popen("dnf check-update",shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    repo_update_output, repo_update_err = repo_update.communicate()

    # STAMPA NEL TERMINALE IL RISULTATO A SECONDA CHE CI SIANO ERRORI O MENO
    # PRINTING IN THE TERMINAL THE RESULT DEPENDING ON WHETHER THERE ARE ERRORS OR NOT
    if repo_update_err == None:
        print("Updating the source repos :", "\n") 
        print(repo_update_output)
    
    else:
        print("DEBUG : There was an error updating the repository packages list's :", "\n\n", 
        repo_update_err, 
        "\n\nPlease open an issue on the project GitHub page and paste the error code :",
        "\nhttps://github.com/H3rz3n/davinci-helper")

        exit()

    

    # AGGIORNAMENTO DELLA LISTA PACCHETTI DEI REPOSITORY
    # UPDATING THE REPOSITORY PACKAGES LIST'S
    package_install = subprocess.Popen(f"dnf install -y {lib_to_install}",shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    package_install_output, package_install_err = package_install.communicate()

    # STAMPA NEL TERMINALE IL RISULTATO A SECONDA CHE CI SIANO ERRORI O MENO
    # PRINTING IN THE TERMINAL THE RESULT DEPENDING ON WHETHER THERE ARE ERRORS OR NOT
    if package_install_err == None: 
        print(package_install_output)
    
    else:
        print("DEBUG : There was an error installing the missing libraries :", "\n\n", 
        package_install_err, 
        "\n\nPlease open an issue on the project GitHub page and paste the error code :",
        "\nhttps://github.com/H3rz3n/davinci-helper")

        exit()



# FUNZIONE CHE LEGGE LE LIBRERIE INSTALLATE NEL SISTEMA
# FUNCTION THAT READ THE LIST OF THE INSTALLED LIBRARIES
def get_libraries_list ():

    # LETTURA DELLA LISTA DELLE LIBRERIE INSTALLATE
    # READING INSTALLED LIBRARY LIST
    library_list = subprocess.Popen("dnf list installed | grep lib", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    library_list_output, library_list_err = library_list.communicate()

    # STAMPA NEL TERMINALE IL RISULTATO A SECONDA CHE CI SIANO ERRORI O MENO
    # PRINTING IN THE TERMINAL THE RESULT DEPENDING ON WHETHER THERE ARE ERRORS OR NOT
    if library_list_err == None: 

        # RESTITUISCE IL VALORE AL PROGRAMMA
        # RETURNS VALUE TO THE SCRIPT
        return library_list_output

    else:
        print("DEBUG : There was an error reading the library list :", "\n\n", 
        library_list_err,
        "\n\nPlease open an issue on the project GitHub page and paste the error code :",
        "\nhttps://github.com/H3rz3n/davinci-helper")

        exit()



# FUNZIONE CHE CONTROLLA LA VERSIONE DI FEDORA INSTALLATA
# FUNCTION THAT CHECK WHICH VERSION OF FEDORA IS INSTALLED
def check_fedora_version ():
    
    # LETTURA DELLA VERSIONE DI FEDORA INSTALLATA
    # READING WHICH VERSION OF FEDORA IS INSTALLED
    fedora_version = subprocess.Popen("cat /etc/fedora-release", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    fedora_version_output, fedora_version_err = fedora_version.communicate()


    # STAMPA NEL TERMINALE IL RISULTATO A SECONDA CHE CI SIANO ERRORI O MENO
    # PRINTING IN THE TERMINAL THE RESULT DEPENDING ON WHETHER THERE ARE ERRORS OR NOT
    if fedora_version_err == None: 
        
        # STAMPA LA VERSIONE DI FEDORA
        # PRINT THE FEDORA VERSION
        print("You are using", fedora_version_output)

        # RESTITUISCE IL VALORE AL PROGRAMMA
        # RETURNS VALUE TO THE SCRIPT
        return fedora_version_output
        
    else:
        print("DEBUG : There was an error reading what version of Fedora is installed :", "\n\n", 
        fedora_version_err, 
        "\n\nPlease open an issue on the project GitHub page and paste the error code :",
        "\nhttps://github.com/H3rz3n/davinci-helper")

        exit()



#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


# ACQUISISCO LA VERSIONE DI FEDORA UTILIZZATA
# ACQUIRING THE USED VERSION OF FEDORA
fedora_version = check_fedora_version()



# ACQUISISCO LA LISTA DELLE LIBRERIE INSTALLATA
# ACQUIRING THE INSTALLED LIBRARIES LIST
library_list = get_libraries_list()



# CONTROLLO SE È INSTALLATO FEDORA 38
# CHECKING IF IS INSTALLED FEDORA 38
if fedora_version.find("38") != -1 :
    
    # ESECUZIONE DELLA FUNZIONE CHE INSTALLA LE DIPENDENZE MANCANTI
    # EXECUTION OF THE FUNCTION THAT INSTALL THE MISSING DEPENDENCIES
    fix_dependencies_38_39_40(library_list)



# CONTROLLO SE È INSTALLATO FEDORA 39
# CHECKING IF IS INSTALLED FEDORA 39
elif fedora_version.find("39") != -1 :
    
    # ESECUZIONE DELLA FUNZIONE CHE INSTALLA LE DIPENDENZE MANCANTI
    # EXECUTION OF THE FUNCTION THAT INSTALL THE MISSING DEPENDENCIES
    fix_dependencies_38_39_40(library_list)



# CONTROLLO SE È INSTALLATO FEDORA 40
# CHECKING IF IS INSTALLED FEDORA 40
elif fedora_version.find("40") != -1 :

    # ESECUZIONE DELLA FUNZIONE CHE INSTALLA LE DIPENDENZE MANCANTI
    # EXECUTION OF THE FUNCTION THAT INSTALL THE MISSING DEPENDENCIES
    fix_dependencies_38_39_40(library_list)





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

