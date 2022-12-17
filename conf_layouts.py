# ______     ______   __     __         ______  
#/\  __ \   /\__  _\ /\ \   /\ \       /\  ___\
#\ \ \/\_\  \/_/\ \/ \ \ \  \ \ \____  \ \  __\
# \ \___\_\    \ \_\  \ \_\  \ \_____\  \ \_____\
#  \/___/_/     \/_/   \/_/   \/_____/   \/_____/

#	Author: Park, James.				   
#   Name: layouts.py
#	Born: 12/16/22				           
#	Revised:		
#   Description: This file holds the layout configurations for the main qtile config file

from libqtile import layout
from libqtile.config import Match

# Local Files
from defaults import *

layout_defaults = {
            "border_width": 2,
            "margin": 8,
            "border_focus": colors["faded_blue"],
            "border_normal": colors["dark0"]}

layouts = [
    layout.Max(**layout_defaults),
    layout.MonadTall(**layout_defaults),
    #layout.floating.Floating(**layout_defaults),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)