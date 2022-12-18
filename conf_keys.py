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

from libqtile.config import Click, Drag, Key, Group
from libqtile.lazy import lazy

# Local Files
from defaults import *

#    # New Keybinds
#     Key([MOD], "m", lazy.window.toggle_floating())

class Keybindings:
    keys = []

    def create_layout_keys(self):
        # switch between windows
        layout_move_left = Key([MOD], LAYOUT_LEFT, lazy.layout.left(), desc="Move focus to left")
        layout_move_right = Key([MOD], LAYOUT_RIGHT, lazy.layout.right(), desc="Move focus to right")
        layout_move_down = Key([MOD], LAYOUT_DOWN, lazy.layout.down(), desc="Move focus down")
        layout_move_up = Key([MOD], LAYOUT_UP, lazy.layout.up(), desc="Move focus up")
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        layout_swap_left = Key([MOD, "shift"], LAYOUT_LEFT, lazy.layout.shuffle_left(), desc="Move window to the left")
        layout_swap_right = Key([MOD, "shift"], LAYOUT_RIGHT, lazy.layout.shuffle_right(), desc="Move window to the right")
        layout_swap_down = Key([MOD, "shift"], LAYOUT_DOWN, lazy.layout.shuffle_down(), desc="Move window down")
        layout_swap_up = Key([MOD, "shift"], LAYOUT_UP, lazy.layout.shuffle_up(), desc="Move window up")
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        layout_grow_left = Key([MOD, "control"], LAYOUT_LEFT, lazy.layout.grow_left(), desc="Grow window to the left")
        layout_grow_right = Key([MOD, "control"], LAYOUT_RIGHT, lazy.layout.grow_right(), desc="Grow window to the right")
        layout_grow_down = Key([MOD, "control"], LAYOUT_DOWN, lazy.layout.grow_down(), desc="Grow window down")
        layout_grow_up = Key([MOD, "control"], LAYOUT_UP, lazy.layout.grow_up(), desc="Grow window up")
        layout_grow_normalize = Key([MOD], LAYOUT_RESET, lazy.layout.normalize(), desc="Reset all window sizes")
        # Toggle to new layout
        layout_toggle_next = Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts")

        self.keys += [layout_move_left, layout_move_right, layout_move_down, layout_move_up, layout_swap_left,
        layout_swap_right, layout_swap_down, layout_swap_up, layout_grow_left, layout_grow_right, layout_grow_down,
        layout_grow_up, layout_grow_normalize, layout_toggle_next]
    # end method
    
    def create_group_keys(self): 
        for i in groups:
            group_key = Key([MOD], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name))
            move_window_key = Key([MOD, "shift"], i.name, lazy.window.togroup(i.name), desc="move focused window to group {}".format(i.name))
            self.keys += [group_key, move_window_key]
        # end loop
    # end method

    def create_spawn_keys(self):
        spawn_terminal = Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch TERMINAL")
        spawn_launcher = Key([MOD], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn a command using a prompt widget")
        self.keys += [spawn_terminal, spawn_launcher]
    # end method

    def create_system_keys(self):
        window_kill = Key([MOD], "w", lazy.window.kill(), desc="Kill focused window")
        qtile_restart = Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload the config")
        qtile_quit = Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile")
        self.keys += [window_kill, qtile_restart, qtile_quit]
    # end method
    
    def init_keys(self):
        self.create_layout_keys()
        self.create_spawn_keys()
        self.create_system_keys()
        self.create_group_keys()
        
        return self.keys
    # end method
# end class

class Mouse:
    def init_mouse(self):
        mouse = [
            Drag([MOD], "Button1", lazy.window.set_position_floating(),
                 start=lazy.window.get_position()),
            Drag([MOD], "Button3", lazy.window.set_size_floating(),
                 start=lazy.window.get_size()),
            Click([MOD], "Button2", lazy.window.bring_to_front())
        ]
        return mouse
    # end method
# end class