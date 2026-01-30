import re

WEEK_SECONDS = 604800

with open("schedule.txt", "r", encoding="utf-8") as f:
    content = f.read()

def add_week(match):
    return f"<t:{int(match.group(1)) + WEEK_SECONDS}:R>"

updated = re.sub(r"<t:(\\d+):R>", add_week, content)

with open("schedule.txt", "w", encoding="utf-8") as f:
    f.write(updated)

print("Updated schedule +1 week")