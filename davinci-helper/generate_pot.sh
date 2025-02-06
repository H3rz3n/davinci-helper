#!/bin/bash 


# 1) Percorso del file POT
POT_FILE="locale/davinci-helper.pot"

# 2) Rimuove il file POT esistente (sovrascrive completamente)
rm -f "$POT_FILE"

# 3) Estrazione file Python
PY_FILES=$(find davinci_helper -name "*.py")
if [[ -n "$PY_FILES" ]]; then
    xgettext \
        --from-code=UTF-8 \
        --language=Python \
        --keyword=_ \
        --keyword=N_ \
        --output="$POT_FILE" \
        $PY_FILES
fi

# 4) Estrazione dai .ui
UI_FILES=$(find data/ui -name "*.ui")
for ui in $UI_FILES; do
    intltool-extract --type=gettext/glade "$ui"
    UI_TEMP="$ui.h"
    if [[ -f "$UI_TEMP" ]]; then
        xgettext \
            --from-code=UTF-8 \
            --language=C \
            --keyword=_ \
            --keyword=N_ \
            -j -o "$POT_FILE" \
            "$UI_TEMP"
        rm -f "$UI_TEMP"
    fi
done

# 5) Estrazione dai .desktop
DESKTOP_FILES=$(find data/desktop -name "*.desktop")
for desk in $DESKTOP_FILES; do
    intltool-extract --type=gettext/keys "$desk"
    DESK_TEMP="$desk.h"
    if [[ -f "$DESK_TEMP" ]]; then
        xgettext \
            --from-code=UTF-8 \
            --keyword=_ \
            --keyword=N_ \
            -j -o "$POT_FILE" \
            "$DESK_TEMP"
        rm -f "$DESK_TEMP"
    fi
done

# 6) Estrazione da eventuali .xml / .policy
XML_FILES=$(find data -name "*.xml" -o -name "*.policy")
for xml in $XML_FILES; do
    intltool-extract --type=gettext/xml "$xml"
    XML_TEMP="$xml.h"
    if [[ -f "$XML_TEMP" ]]; then
        xgettext \
            --from-code=UTF-8 \
            --keyword=_ \
            --keyword=N_ \
            -j -o "$POT_FILE" \
            "$XML_TEMP"
        rm -f "$XML_TEMP"
    fi
done

# 7) Output finale
echo "Nuovo file POT generato ex novo: $POT_FILE"
