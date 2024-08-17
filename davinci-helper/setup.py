#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licensa GPL-3.0
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULES IMPORT
from setuptools import setup, find_packages
import os

#-----------------------------------------------------------------------------------------------------

# FUNZIONE PER LEGGERE IL FILE README
# FUNCTION TO READ THE README FILE
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#-----------------------------------------------------------------------------------------------------

# INIZIO DELLE IMPOSTAZIONI DI SETUP
# SETUP SETTINGS START
setup(
    
    # NOME DEL PROGRAMMA
    # APP NAME
    name="davinci-helper",
    
    # VERSIONE DEL PROGRAMMA
    # APP VERSION
    version="1.0",

    # AUTORE DEL PROGRAMMA
    # APP AUTHOR
    author="Lorenzo Maiuri",

    # INDIRIZZO MAIL DELL'AUTORE
    # AUTHOR EMAIL ADDRESS
    author_email="lorenzo.maiuri@gmail.com",

    # DESCRIZIONE BREVE DEL PROGRAMMA
    # APP SHORT DESCRIPTION
    description=("A helper to help you install DaVinci Resolve."),

    # DESCRIZIONE LUNGA DEL PROGRAMMA
    # APP LONG DESCRIPTION
    long_description=read('README.md'),
    
    # TIPOLOGIA DI TESTO DELLA DESCRIZIONE LUNGA
    # LONG DESCRIPTION TEXT TYPE
    long_description_content_type='text/markdown',

    # LICENZA DI PUBBLICAZIONE
    # PUBBLICATION LICENSE
    license="GPL-3.0",

    # PAROLE CHIAVE
    # KEYWORDS
    keywords="davinci helper tool",

    # INDIRIZZO GITHUB DEL PROGETTO
    # PROJECT GITHUB ADDRESS
    url="https://github.com/H3rz3n/davinci-helper",

    # CLASSIFICAZIONE DEL PROGETTO
    # PROJECT CLASSIFICATION
    classifiers=[
        "Development Status :: 1.0 - Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL-3.0 License",
    ],

    #-----------------------------------------------------------------------------------------------------

    # INCLUSIONE DEI FILE NON ESEGUIBILI
    # NOT EXECUTABLE FILES INCLUSION
    include_package_data=True,

    # POSIZIONE DEI FILE NON ESEGUIBILI
    # NOT EXECUTABLE FILES PATH
    data_files=[
        ('share/davinci-helper/data/css', ['data/css/style-dark.css']),
        ('share/davinci-helper/data/desktop', [
            'data/desktop/com.davinci.helper.app.desktop',
            'data/desktop/com.davinci.helper.app.metainfo.xml',
            'data/desktop/davinci-helper-icon.svg'
        ]),
        ('share/davinci-helper/data/icons/', [
        'data/icons/davinci-helper-icon.svg'
        ]),
        ('share/davinci-helper/data/icons/main_icons', [
            'data/icons/main_icons/F1.svg',
            'data/icons/main_icons/F2.svg',
            'data/icons/main_icons/F3.svg',
            'data/icons/main_icons/F4.svg'
        ]),
        ('share/davinci-helper/data/icons/function_icons', [
            'data/icons/function_icons/error.svg',
            'data/icons/function_icons/success.svg',
            'data/icons/function_icons/warning.svg',
            'data/icons/function_icons/file.svg'
        ]),
        ('share/davinci-helper/data/polkit', [
            'data/polkit/com.davinci.helper.app.rules',
            'data/polkit/com.davinci.helper.app.policy'
        ]),
        ('share/davinci-helper/data/ui', [
            'data/ui/about_window.ui',
            'data/ui/function_1.ui',
            'data/ui/function_2.ui',
            'data/ui/function_3.ui',
            'data/ui/function_4.ui',
            'data/ui/info_function_1.ui',
            'data/ui/info_function_2.ui',
            'data/ui/info_function_3.ui',
            'data/ui/info_function_4.ui',
            'data/ui/error_dialog.ui',
            'data/ui/welcome_messagge_splash_screen.ui',
            'data/ui/gpu_warning_splash_screen.ui',
            'data/ui/check_update.ui',
            'data/ui/reset_settings.ui',
            'data/ui/main_window.ui'
        ]),
        ('share/davinci-helper/data/gpu_support', [
            'data/gpu_support/amd_support.txt',
            'data/gpu_support/intel_support.txt',
            'data/gpu_support/nvidia_support.txt'
        ]),
        ('share/davinci-helper/data/settings', [
            'data/settings/davinci_helper_settings'
        ]),
        ('share/davinci-helper/locale/it/LC_MESSAGES', [
            'locale/it/LC_MESSAGES/davinci-helper.mo'
        ])
    ],

    #-----------------------------------------------------------------------------------------------------

    # VERSIONE MINIMA DI PYTHON RICHIESTA
    # MINUMUN REQUIRMENT PYTHON VERSION
    python_requires='>=3.0',

    # MODULI PYTHON ESEGUIBILI
    # EXECUTABLE PYTHON MODULES
    packages=['davinci_helper', 'davinci_helper/functions'],

    # AVVIO DEL PROGRAMMA
    # APP START
    entry_points={
        "console_scripts": [
            "davinci-helper=davinci_helper.main:main",
        ],
    },
)

#-----------------------------------------------------------------------------------------------------
