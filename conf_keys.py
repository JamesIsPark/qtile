# ______     ______   __     __         ______  
#/\  __ \   /\__  _\ /\ \   /\ \       /\  ___\
#\ \ \/\_\  \/_/\ \/ \ \ \  \ \ \____  \ \  __\
# \ \___\_\    \ \_\  \ \_\  \ \_____\  \ \_____\
#  \/___/_/     \/_/   \/_/   \/_____/   \/_____/

#	Author: Park, James.				   
#   Name: keybindings.py
#	Born: 12/16/22						           
#	Revised:		
#   Description: This is the keybindings for all spawn commands and keybinds/mouse bindings

from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

# Local Files
from defaults import *

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([MOD, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([MOD, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([MOD, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([MOD, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([MOD, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([MOD, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [MOD, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch TERMINAL"),
    # Toggle between different layouts as defined below
    Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([MOD], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn a command using a prompt widget"),


    # New Keybinds
     Key([MOD], "m", lazy.window.toggle_floating())

]

for i in groups:
    keys.extend(
        [
            # MOD1 + letter of group = switch to group
            Key(
                [MOD],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # MOD1 + shift + letter of group = switch to & move focused window to group
            #Key(
            #    [MOD, "shift"],
            #    i.name,
            #    lazy.window.togroup(i.name, switch_group=True),
            #    desc="Switch to & move focused window to group {}".format(i.name),
            #),
            # Or, use below if you prefer not to switch to that group.
            # MOD1 + shift + letter of group = move focused window to group
             Key([MOD, "shift"], i.name, lazy.window.togroup(i.name),
                 desc="move focused window to group {}".format(i.name)),
        ]
    )

# Drag floating layouts.
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]