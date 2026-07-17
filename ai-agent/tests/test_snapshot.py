from collector.snapshot import build_snapshot


def main():

    snapshot = build_snapshot("vehicle-login")

    print("=" * 60)
    print("Pods        :", len(snapshot.pods))
    print("Deployments :", len(snapshot.deployments))
    print("Services    :", len(snapshot.services))
    print("Ingresses   :", len(snapshot.ingresses))
    print("Events      :", len(snapshot.events))
    print("Nodes       :", len(snapshot.nodes))
    print("=" * 60)


if __name__ == "__main__":
    main()
