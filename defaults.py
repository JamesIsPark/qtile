# ______     ______   __     __         ______  
#/\  __ \   /\__  _\ /\ \   /\ \       /\  ___\
#\ \ \/\_\  \/_/\ \/ \ \ \  \ \ \____  \ \  __\
# \ \___\_\    \ \_\  \ \_\  \ \_____\  \ \_____\
#  \/___/_/     \/_/   \/_/   \/_____/   \/_____/

#	Author: Park, James.				   
#   Name: defaults.py
#	Born: 12/17/22						           
#	Revised:		
#   Description: This file is meant to stand as the main hub for basic setting changes.
import os
from libqtile.config import Group

###################### COLOR SETTINGS ###################### 
colors = {
    'dark0_hard': '#1d2021',
    'dark0': '#282828',
    'dark0_soft': '#32302f',
    'dark1': '#3c3836',
    'dark2': '#504945',
    'dark3': '#665c54',
    'dark4': '#7c6f64',
    'dark4_256': '#7c6f64',

    'gray_245': '#928374',
    'gray_244': '#928374',

    'light0_hard': '#f9f5d7',
    'light0': '#fbf1c7',
    'light0_soft': '#f2e5bc',
    'light1': '#ebdbb2',
    'light2': '#d5c4a1',
    'light3': '#bdae93',
    'light4': '#a89984',
    'light4_256': '#a89984',

    'bright_red': '#fb4934',
    'bright_green': '#b8bb26',
    'bright_yellow': '#fabd2f',
    'bright_blue': '#83a598',
    'bright_purple': '#d3869b',
    'bright_aqua': '#8ec07c',
    'bright_orange': '#fe8019',

    'neutral_red': '#cc241d',
    'neutral_green': '#98971a',
    'neutral_yellow': '#d79921',
    'neutral_blue': '#458588',
    'neutral_purple': '#b16286',
    'neutral_aqua': '#689d6a',
    'neutral_orange': '#d65d0e',

    'faded_red': '#9d0006',
    'faded_green': '#79740e',
    'faded_yellow': '#b57614',
    'faded_blue': '#076678',
    'faded_purple': '#8f3f71',
    'faded_aqua': '#427b58',
    'faded_orange': '#af3a03',
}


###################### CONSTANTS ###################### 
TERMINAL = "kitty"

HOME = os.path.expanduser('~')

##### KEYBINDING CONSTANTS #####
MOD = "mod4"

LAYOUT_LEFT = "h"
LAYOUT_RIGHT = "l"
LAYOUT_DOWN = "j"
LAYOUT_UP = "k"

LAYOUT_NEXT = "space"

LAYOUT_RESET = "n"

NEXT_GROUP = "period"
PREV_GROUP = "comma"

groups = [Group(i) for i in "123456"]
