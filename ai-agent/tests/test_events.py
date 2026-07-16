from collector.events import get_events

events = get_events("vehicle-login")

print(f"Events Found: {len(events)}")

for event in events:
    print(event)
