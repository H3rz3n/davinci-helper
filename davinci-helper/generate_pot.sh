#!/bin/bash 

find davinci_helper data -name "*.py" -o -name "*.ui" -o -name "*.xml" -o -name "*.desktop" | xargs xgettext -o locale/davinci-helper.pot

# 7) Output finale
echo "Nuovo file POT generato ex novo: $POT_FILE"
