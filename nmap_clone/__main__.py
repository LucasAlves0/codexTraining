from .cli_parser import parse_args
from .ip_utils import generate_ips
from .port_utils import parse_ports
from .scanner_engine import scan_targets
from .output_formatter import print_results
from .logger import setup_logger


def main() -> None:
    args = parse_args()
    logger = setup_logger(args.verbose)
    ips = generate_ips(args.target)
    ports = parse_ports(args.ports)
    logger.debug(f"Scanning IPs: {ips}")
    logger.debug(f"Ports: {ports}")
    results = scan_targets(
        ips,
        ports,
        timeout=args.timeout,
        banner=args.banner,
        workers=args.workers,
    )
    print_results(results)


if __name__ == "__main__":
    main()
