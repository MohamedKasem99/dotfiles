from i3pystatus import Status

status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register(
    "clock",
    format="%H %-d %b %X",
)

status.register(
    "xkblayout",
    format="🌐 {name}",
)
# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
# Shows your CPU temperature, if you have a Intel CPU
status.register(
    "temp",
    format="🔥{temp:.0f}°C",
)
status.register(
    "cpu_usage",
    format="🖥️{usage:02}%",
)
status.register(
    "mem",
    format="💾{used_mem:02}/{total_mem:02}GB",
    divisor=1024 ** 3,
)

# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via D-Bus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
# If you don't have a desktop notification demon yet, take a look at dunst:
#   http://www.knopwob.org/dunst/
status.register(
    "battery",
    format="{status} {percentage:.2f}% ⏳{remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=10,
    status={
        "DIS": "⬇️",
        "CHR": "⬆️",
        "FULL": "🟢",
    },
)

# This would look like this:
# Discharging 6h:51m
status.register(
    "battery",
    format="🔋{status}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS": "🟡 Discharging",
        "CHR": "⚡ Charging",
        "FULL": "✅ Bat full",
    },
)
# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register(
    "network",
    interface="enp4s0",
    format_up="{network_graph_recv}{bytes_recv}KB/s",
    format_down="",
)

# Note: requires both netifaces and basiciw (for essid and quality)
status.register(
    "network",
    interface="wlp0s20f3",
    format_up="{essid} {quality:03.0f}% {network_graph_recv}{bytes_recv}KB/s",
)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register(
    "disk",
    path="/",
    format="{used}/{total}G [{avail}G]",
)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register(
    "pulseaudio",
    format="🎶{volume}%",
)

status.register(
    "now_playing",
    status={
        "pause": "⏯️",
        "play": "▶️",
        "stop": "⏹️",
    },
    on_leftclick=["player_command", "PlayPause"],
    on_rightclick=["player_command", "Stop"],
)

status.run()
