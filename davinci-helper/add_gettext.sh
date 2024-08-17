#!/bin/bash
find davinci_helper data -name "*.py" -o -name "*.ui" -o -name "*.xml" -o -name "*.desktop" | xargs xgettext -j -o locale/davinci-helper.pot

msgmerge -U locale/it/LC_MESSAGES/davinci-helper.po locale/davinci-helper.pot