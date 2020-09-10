#!/bin/bash

 HISTCONTROL=ignoreboth
 HISTFILE=~/.zsh_history
 set -o history

 COMMAND=$(history | sed 's/\s:\s[0-9]\+\:[0-9];//g' | sed '$d' | sort -rn | dmenu -l 10 -fn 15 | awk '{$1=""; print $0}')

 if [ -n "$COMMAND" ]; then
     echo $COMMAND | tr '\n' ' ' | xclip -selection clipboard
 fi
