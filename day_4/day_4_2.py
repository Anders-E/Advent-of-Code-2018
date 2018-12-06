from sys import stdin
import re

TIME_REGEX = re.compile(r"\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.*)")
GUARD_REGEX = re.compile(r"#(\d*)")

def generate_minutes_asleep():
    minutes_asleep = {}
    current_guard = 0
    snoozy_time = None

    for line in sorted(stdin.readlines()):
        groups = TIME_REGEX.match(line).groups()
        minute = int(groups[4])
        msg = groups[5]
    
        if msg[0] == 'f': # falls asleep
            snoozy_time = minute
        elif msg[0] == 'w': # wakes up
            if not current_guard in minutes_asleep:
                minutes_asleep[current_guard] = [0] * 60
            for i in range(snoozy_time, minute):
                minutes_asleep[current_guard][i] += 1
        else:
            current_guard = int(GUARD_REGEX.search(msg).group(1))
    
    return minutes_asleep

def get_sleepiest_guard_and_minute(minutes_asleep):
    sleepiest_minute = 0
    sleepiest_guard = 0
    max_snooze = 0
    
    for guard, minutes in minutes_asleep.items():
        for i, minute in enumerate(minutes):
            if minute > max_snooze:
                sleepiest_minute = i
                sleepiest_guard = guard
                max_snooze = minute
    
    return sleepiest_guard, sleepiest_minute

minutes_asleep = generate_minutes_asleep()
guard, minute = get_sleepiest_guard_and_minute(minutes_asleep)

print(guard * minute)
