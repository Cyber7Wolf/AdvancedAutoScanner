import pdfkit
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def generate_report(scan_results: dict):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report.html')
    
    html = template.render(
        target=scan_results['target'],
        date=datetime.now().strftime("%Y-%m-%d %H:%M"),
        subdomains=scan_results['subdomains'],
        ports=scan_results['ports'],
        vulns=scan_results['vulns']
    )
    
    with open("scan_report.html", "w") as f:
        f.write(html)
    
    pdfkit.from_file("scan_report.html", "scan_report.pdf")