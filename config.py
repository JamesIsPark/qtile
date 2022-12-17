# ______     ______   __     __         ______        ______     ______     __   __     ______   __     ______    #
#/\  __ \   /\__  _\ /\ \   /\ \       /\  ___\      /\  ___\   /\  __ \   /\ "-.\ \   /\  ___\ /\ \   /\  ___\   #
#\ \ \/\_\  \/_/\ \/ \ \ \  \ \ \____  \ \  __\      \ \ \____  \ \ \/\ \  \ \ \-.  \  \ \  __\ \ \ \  \ \ \__ \  #
# \ \___\_\    \ \_\  \ \_\  \ \_____\  \ \_____\     \ \_____\  \ \_____\  \ \_\\"\_\  \ \_\    \ \_\  \ \_____\ #
#  \/___/_/     \/_/   \/_/   \/_____/   \/_____/      \/_____/   \/_____/   \/_/ \/_/   \/_/     \/_/   \/_____/ #

#	Author: Park, James.				   
#	Born: 12/16/22				           
#	Revised:					   
#	Description: This is the main qtile config file that qtile reads from.
#

import os
import subprocess

from libqtile import hook
from libqtile.lazy import lazy

# local files
from conf_keys import *
from conf_layouts import *
from conf_widgets import *


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.layout_change
def _(layout, group):
	for window in group.windows:
		window.floating = False
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])
@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog' or window.window.get_wm_transient_for()):
        window.floating = True
