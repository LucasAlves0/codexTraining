import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Simple Nmap clone")
    parser.add_argument("target", help="Target IP, CIDR or range")
    parser.add_argument(
        "-p",
        "--ports",
        default="1-1024",
        help="Ports to scan: single, comma list or range (default 1-1024)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="Connection timeout in seconds (default 1.0)",
    )
    parser.add_argument(
        "--banner",
        action="store_true",
        help="Enable banner grabbing",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose output",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=100,
        help="Number of parallel workers (default 100)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(args)
