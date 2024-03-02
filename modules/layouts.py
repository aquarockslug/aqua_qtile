from libqtile import layout
from libqtile.config import Match

border = dict(
    margin=16, border_focus="#ED1ECD", border_width=7, border_normal="#c0bfc0"
)

layouts = [
    layout.MonadTall(**border),
    layout.MonadWide(**border),
    # layout.VerticalTile(**border),
    # layout.Bsp(**border),
    layout.Matrix(**border),
    # layout.Columns(border_focus_stack="#d75f5f"),
    layout.Max(**border),
    # layout.Stack(**border, num_stacks=2),
    # layout.RatioTile(**border),
    # layout.Tile(**border),
    # layout.TreeTab(**border),
    # layout.Zoomy(**border),
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
