from typing import Iterable, Tuple

Result = Tuple[str, int, bool, str]


def print_results(results: Iterable[Result]) -> None:
    for ip, port, status, banner in sorted(results):
        state = "open" if status else "closed"
        line = f"{ip}:{port} {state}"
        if banner:
            line += f" | {banner}"
        print(line)
