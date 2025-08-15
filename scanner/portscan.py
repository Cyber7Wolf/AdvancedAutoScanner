import nmap

def scan_ports(target: str, ports: str = "21,22,80,443") -> dict:
    scanner = nmap.PortScanner()
    scanner.scan(target, ports=ports)
    return {host: scanner[host] for host in scanner.all_hosts()}