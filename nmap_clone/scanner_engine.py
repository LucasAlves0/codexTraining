from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Iterable, List, Tuple

from .tcp_scan import tcp_connect


Result = Tuple[str, int, bool, str]


def scan_targets(
    ips: Iterable[str],
    ports: Iterable[int],
    *,
    timeout: float = 1.0,
    banner: bool = False,
    workers: int = 100,
) -> List[Result]:
    tasks = []
    results: List[Result] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for ip in ips:
            for port in ports:
                tasks.append(
                    executor.submit(tcp_connect, ip, port, timeout=timeout, banner=banner)
                )
        for future in as_completed(tasks):
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                results.append(("error", 0, False, str(exc)))
    return results
