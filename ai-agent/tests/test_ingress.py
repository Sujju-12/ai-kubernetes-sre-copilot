from collector.ingress import get_ingresses

ingresses = get_ingresses("vehicle-login")

print(f"Ingresses : {len(ingresses)}")

for ingress in ingresses:
    print(ingress)
