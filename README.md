# Codex Training Nmap Clone

This repository contains a simple network scanner inspired by `nmap`.
It provides basic TCP port scanning and optional banner grabbing.

## Usage

```
python -m nmap_clone <target> [-p PORTS] [--banner] [--timeout SECONDS] [--verbose] [--workers N]
```

- **target**: IP address, CIDR (e.g. `192.168.1.0/24`) or range (`192.168.1.1-192.168.1.10`)
- **-p / --ports**: Ports to scan, e.g. `80`, `20-25`, `80,443,8080`
- **--banner**: Enable banner grabbing
- **--timeout**: Connection timeout (default 1.0s)
- **--verbose**: Verbose logging
- **--workers**: Number of parallel workers (default 100)

Example:

```
python -m nmap_clone 192.168.1.1 -p 22,80 --banner
```
