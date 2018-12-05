from sys import stdin
import datetime
import re

regex = re.compile(r"\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.*)")
guard_regex = re.compile(r"^([wf])|Guard #(\d*)")

current_guard = 0

for line in stdin.readlines():
    groups = regex.match(line).groups()
    y, m, d, h, s = map(int, groups[:5])
    timestamp = datetime.datetime(y, m, d, h, s)
    msg = groups[5]
    msg_match = guard_regex.match(msg)
    if (msg_match.group(2)):
        current_guard = msg_match.group(2)

