from typing import List


def parse_ports(port_str: str) -> List[int]:
    ports: List[int] = []
    parts = [p.strip() for p in port_str.split(',')]
    for part in parts:
        if '-' in part:
            start, end = part.split('-')
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(part))
    return sorted(set(ports))
