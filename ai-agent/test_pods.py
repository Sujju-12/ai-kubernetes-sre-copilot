from collector.pods import get_pods


def main():

    pods = get_pods()

    for pod in pods:

        print("=" * 50)
        print(pod)


if __name__ == "__main__":
    main()
