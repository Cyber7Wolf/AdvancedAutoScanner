# Add at the top
from scanner.report import generate_report
from scanner.subdomain import scan_subdomains
import asyncio

async def test():
    print("Testing subdomain scanner...")
    results = await scan_subdomains("google.com")  # Test with a safe domain
    print(f"Found {len(results)} subdomains: {results}")

asyncio.run(test())

from scanner.portscan import scan_ports

print("\nTesting port scanner...")
ports = scan_ports("scanme.nmap.org")  # Test with Nmap's allowed target
print("Open ports found:", ports)

from scanner.vuln_checks import check_xss, check_sqli

print("\nTesting XSS/SQLi checks...")
print("XSS vulnerable (should be False):", check_xss("https://google.com"))
print("SQLi vulnerable (should be False):", check_sqli("https://google.com"))

try:
    from scanner.vuln_checks import check_xss, check_sqli
    print("\nTesting XSS/SQLi checks...")
    print("XSS vulnerable:", check_xss("https://google.com"))
    print("SQLi vulnerable:", check_sqli("https://google.com"))
except ImportError as e:
    print(f"\nVulnerability checks skipped: {e}")

# Add at the end (before main check)
report_data = {
    'target': args.url,
    'subdomains': subdomains,
    'ports': ports[list(ports.keys())[0]],  # Get first host
    'vulns': {
        'XSS': xss_result,
        'SQLi': sqli_result
    }
}
generate_report(report_data)
print("\n[+] Report generated: scan_report.html & scan_report.pdf")