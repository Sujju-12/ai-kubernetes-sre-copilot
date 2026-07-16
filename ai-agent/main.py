import argparse

from cli.diagnose import diagnose


def main():

    parser = argparse.ArgumentParser(
        description="AI Kubernetes SRE Copilot"
    )

    parser.add_argument(
        "--namespace",
        required=True,
        help="Namespace to diagnose"
    )

    args = parser.parse_args()

    diagnose(args.namespace)


if __name__ == "__main__":
    main()
