#!/bin/bash

# Trova e compila tutti i file .po in tutte le sottocartelle
find locale -name "*.po" | while read -r po_file; do
    # Determina la cartella di destinazione per il file .mo
    mo_file="${po_file%.po}.mo"
    
    # Compila il file .po in .mo
    msgfmt "$po_file" -o "$mo_file"
    
    echo "Compilato: $po_file -> $mo_file"
done