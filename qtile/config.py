import os
import subprocess

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, ScratchPad, DropDown, Group, Key, Match, Screen
from libqtile.lazy import lazy

from libqtile import hook
from libqtile import extension

from theme import catppuccin

mod = "mod4"
terminal = "kitty"
browser = "firefox"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "bracketright", lazy.screen.next_group(), desc="Next Group"),
    Key([mod], "bracketleft", lazy.screen.prev_group(), desc="Previous Group"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "f", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle Floating"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod],
        "p",
        lazy.run_extension(
            extension.DmenuRun(
                font="JetBrainsMono Nerd Font",
                fontsize="12",
                dmenu_command="dmenu_run",
                dmenu_height=10,
                dmenu_lines=15,
                background=catppuccin["Base"],
                foreground=catppuccin["Text"],
                selected_background=catppuccin["Surface0"],
                selected_foreground=catppuccin["Text"],
            )
        ),
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("/home/aaditya/.config/qtile/Scripts/bin/raise_xbl"),
        desc="Brightness up",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("/home/aaditya/.config/qtile/Scripts/bin/lower_xbl"),
        desc="Brightness down",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("/home/aaditya/.config/qtile/Scripts/bin/raise_vol"),
        desc="Raise volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("/home/aaditya/.config/qtile/Scripts/bin/lower_vol"),
        desc="Lower volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute 0 toggle"),
        desc="Mute/Unmute Volume",
    ),
    Key(
        [mod],
        "XF86AudioMute",
        lazy.spawn("pactl set-source-mute 0 toggle"),
        desc="Mute/Unmute Mic",
    ),
    Key(
        [mod, "shift"],
        "u",
        lazy.spawn('/usr/bin/betterlockscreen -l --time-format "%I:%M %p"'),
        desc="Lock",
    ),
]

groups = [
    Group(
        "1",
        label="",
        matches=[Match(wm_class="firefox")],
        layout="max",
    ),
    Group(
        "2",
        label="",
        layout="tile",
    ),
    Group(
        "3",
        label="",
        layout="tile",
    ),
    Group(
        "4",
        label="",
        layout="tile",
    ),
    Group(
        "5",
        label="",
        layout="tile",
    ),
    Group(
        "6",
        label="",
        layout="tile",
    ),
    Group(
        "7",
        label="",
        layout="tile",
    ),
    Group(
        "8",
        label="",
        layout="Tile",
    ),
    Group(
        "9",
        label="",
        matches=[Match(wm_class="discord")],
        layout="max",
    ),
    ScratchPad(
        "0",
        [
            DropDown(
                "term", "kitty", width=0.7, height=0.7, x=0.15, y=0.1, opacity=0.8
            ),
        ],
    ),
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
            Key(
                [mod],
                "0",
                lazy.group["0"].dropdown_toggle("term"),
                desc="Kitty ScratchPad",
            ),
        ]
    )

layouts = [
    layout.Tile(
        border_focus=catppuccin["Lavender"],
        border_normal=catppuccin["Crust"],
        border_width=2,
        margin=4,
        margin_on_single=False,
    ),
    layout.Columns(
        border_focus=catppuccin["Lavender"],
        border_normal=catppuccin["Crust"],
        border_width=2,
        margin=4,
        margin_on_single=False,
    ),
    layout.Max(),
    # Layouts:
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",
                    padding=5,
                    fontsize=17,
                    foreground=catppuccin["Blue"],
                    background=catppuccin["Crust"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Surface2"],
                    foreground=catppuccin["Crust"],
                ),
                widget.GroupBox(
                    highlight_method="text",
                    this_current_screen_border=catppuccin["Green"],
                    urgent_alert_method="text",
                    urgent_text=catppuccin["Red"],
                    background=catppuccin["Surface2"],
                    active=catppuccin["Text"],
                    inactive=catppuccin["Surface0"],
                    fontsize=15,
                    disable_drag=True,
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Surface0"],
                    foreground=catppuccin["Surface2"],
                ),
                widget.WindowName(
                    background=catppuccin["Surface0"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Surface0"],
                    foreground=catppuccin["Lavender"],
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/Icons")],
                    scale=0.7,
                    background=catppuccin["Lavender"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Lavender"],
                    foreground=catppuccin["Sapphire"],
                ),
                widget.Clock(
                    format="%I:%M %p",
                    background=catppuccin["Sapphire"],
                    foreground=catppuccin["Mantle"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Sapphire"],
                    foreground=catppuccin["Base"],
                ),
                widget.Systray(
                    background=catppuccin["Base"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                widget.Clock(
                    format="%a %Y-%m-%d",
                    background=catppuccin["Green"],
                    foreground=catppuccin["Mantle"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Green"],
                    foreground=catppuccin["Mantle"],
                ),
                widget.TextBox(
                    text=" ",
                    background=catppuccin["Mantle"],
                    foreground=catppuccin["Red"],
                    fontsize=15,
                    mouse_callbacks={
                        "Button1": lazy.shutdown(),
                    },
                ),
            ],
            24,
            background=catppuccin["Base"],
            foreground=catppuccin["Text"],
        ),
    ),
]

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # xprop
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="flameshot"),
    ],
    border_width=2,
    border_focus=catppuccin["Lavender"],
    border_normal=catppuccin["Crust"],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits;
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])
