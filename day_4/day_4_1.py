from sys import stdin
import datetime
import re

"""
for line in stdin.readlines():
    groups = regex.match(line).groups()
    y, m, d, h, s = map(int, groups[:5])
    timestamp = datetime.datetime(y, m, d, h, s)
    msg = groups[5]
    msg_match = guard_regex.match(msg)
    if (msg_match.group(2)):
        current_guard = msg_match.group(2)
"""

regex = re.compile(r"\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.*)")
guard_regex = re.compile(r"#(\d*)")

current_guard = 0
time_asleep = {}
snoozy_time = None
asleep = False

for line in sorted(stdin.readlines()):
    groups = regex.match(line).groups()
    y, m, d, h, s = map(int, groups[:5])
    timestamp = datetime.datetime(y, m, d, h, s)
    msg = groups[5]
    if msg[0] == 'f': # falls asleep
        asleep = True
        snoozy_time = timestamp
    elif msg[0] == 'w': # wakes up
        delta = (timestamp - snoozy_time)
        if current_guard in time_asleep:
            time_asleep[current_guard] += delta.total_seconds()
        else:
            time_asleep[current_guard] = delta.total_seconds()
    else:
        current_guard = int(guard_regex.search(msg).group(1))

most_sleep = 0
snooziest_guard = 0
for guard, time in time_asleep.items():
    if time > most_sleep:
        snooziest_guard = guard

print(snooziest_guard)
