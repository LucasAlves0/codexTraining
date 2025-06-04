from ipaddress import ip_network, ip_address
from typing import List


def generate_ips(target: str) -> List[str]:
    target = target.strip()
    if '/' in target:
        net = ip_network(target, strict=False)
        return [str(ip) for ip in net.hosts()]
    if '-' in target:
        start_str, end_str = target.split('-')
        start = int(ip_address(start_str))
        end = int(ip_address(end_str))
        return [str(ip_address(i)) for i in range(start, end + 1)]
    return [target]
