from libqtile import bar, widget
from libqtile.config import Screen

from defaults import *
from scripts.ordinaldate import custom_date



widget_defaults = dict(
    font="sans",
    fontsize=12,
    foreground=colors["light0"]
)

screens = [
    Screen(
        top=bar.Bar(
            [
            widget.Spacer(length=5),
            widget.GroupBox(
                padding=0,
                active=colors['light0'],
                borderwidth=4,
                inactive=colors['light4'],
                this_current_screen_border=colors['neutral_red'],
                this_screen_border=colors['neutral_red'],
                other_screen_border='#00000000',
                other_current_screen_border='#00000000',
                fontsize=14,
                highlight_method='line',
                highlight_color=['00000000', '00000000']
            ),
            widget.Sep(
                padding=10,
                **widget_defaults    
            ),
            widget.CurrentLayoutIcon(
                padding = 5,
                scale=0.7,
                foreground=colors["light0"]
            ),
            widget.CurrentLayout(
                **widget_defaults
            ),
            widget.Spacer(),
            widget.GenPollText(
	            func=custom_date,
	            update_interval=1,
                **widget_defaults
            ),
            widget.Spacer(),
            widget.Net(
                **widget_defaults
            ),
            widget.Sep(**widget_defaults),
            widget.PulseVolume(**widget_defaults),
            widget.Sep(**widget_defaults),
            widget.QuickExit(
                default_text='[X]',
                **widget_defaults
            ),
            widget.Spacer(length=5),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            [
            widget.Spacer(length=5),
            widget.GroupBox(
                padding=0,
                active=colors['light0'],
                borderwidth=4,
                inactive=colors['light4'],
                this_current_screen_border=colors['neutral_red'],
                this_screen_border=colors['neutral_red'],
                other_screen_border='#00000000',
                other_current_screen_border='#00000000',
                fontsize=14,
                highlight_method='line',
                highlight_color=['00000000', '00000000']
            ),
            widget.CurrentLayoutIcon(
                padding = 10,
                scale=0.7
            ),
            widget.CurrentLayout(
                **widget_defaults
            ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]
