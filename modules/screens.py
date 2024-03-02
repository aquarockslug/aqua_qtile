from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

light_grey = "#CAC9CA"
dark_grey = "#969696"
text_grey = "#777777"
purple = "#C930AE"
dark_purple = "#8D1BB8"

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(padding=3, linewidth=0, background=light_grey),
                widget.GroupBox(
                    highlight_method="line",
                    this_screen_border=purple,
                    this_current_screen_border=purple,
                    active=purple,
                    inactive=dark_grey,
                    background=light_grey,
                    fontsize=24,
                ),
                widget.Prompt(),
                widget.Sep(foreground=text_grey),
                widget.Spacer(length=5),
                widget.WindowName(foreground=purple, fmt="{}", fontsize=24),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Sep(foreground=text_grey),
                widget.Systray(icon_size=30),
                # widget.Wlan(foreground=text_grey),
                # widget.Battery(foreground="#848e96"),
                # widget.Backlight(foreground="#848e96"),
                # widget.Net(foreground=text_grey),
                # widget.DF(foreground=text_grey),
                volume,
                widget.Sep(foreground=text_grey),
                widget.Clock(
                    format="  %m-%d %a %I:%M %p  ",
                    background=dark_grey,
                    foreground=purple,
                    fontsize=24,
                ),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground=dark_grey,
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(terminal + " -e yay -Syu")
                    },
                    background=purple,
                ),
                widget.TextBox(
                    text="",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            os.path.expanduser("~/.config/rofi/powermenu.sh")
                        )
                    },
                    background=purple,
                    foreground="#e39378",
                ),
            ],
            48,  # height in px
            background=dark_grey,  # background color
        ),
    ),
]
