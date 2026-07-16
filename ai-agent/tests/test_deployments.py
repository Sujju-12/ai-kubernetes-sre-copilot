from collector.deployments import get_deployments

deployments = get_deployments("vehicle-login")

print("=" * 60)

print(f"Deployments Found: {len(deployments)}")

print("=" * 60)

for deployment in deployments:
    print(deployment)
