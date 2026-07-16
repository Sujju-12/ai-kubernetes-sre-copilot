from collector.services import get_services

services = get_services("vehicle-login")

print(f"Services Found: {len(services)}")

for service in services:
    print(service)
