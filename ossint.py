import argparse
import sys
from core import social, email_scan, phone_scan, domain_scan, ip_scan, metadata_scan
from report.json_report import save_json_report
from report.pdf_report import save_pdf_report
from utils.helpers import progress_bar, print_results
from utils.banner import print_banner
from utils.color import cyan, green

def run_osint(email=None, phone=None, ip=None, domain=None, username=None, file=None, output="both"):
    print_banner()
    print(cyan("\n[+] Starting OSINT scan..."))

    result = {}

    if email:
        for em in email:
            progress_bar(f"Scanning Email {em}", 30)
            result.setdefault("Email Scan", {}).update({em: email_scan.scan_email(em)})

    if phone:
        for ph in phone:
            progress_bar(f"Scanning Phone {ph}", 30)
            result.setdefault("Phone Scan", {}).update({ph: phone_scan.scan_number(ph)})

    if ip:
        for ipp in ip:
            progress_bar(f"Scanning IP {ipp}", 30)
            result.setdefault("IP Scan", {}).update({ipp: ip_scan.scan_ip(ipp)})

    if domain:
        for dm in domain:
            progress_bar(f"Scanning Domain {dm}", 30)
            result.setdefault("Domain Scan", {}).update({dm: domain_scan.scan_domain(dm)})

    if username:
        for usr in username:
            progress_bar(f"Scanning Social {usr}", 30)
            result.setdefault("Social Media Scan", {}).update({usr: social.scan_username(usr)})

    if file:
        for f in file:
            progress_bar(f"Scanning Metadata {f}", 30)
            result.setdefault("Metadata", {}).update({f: metadata_scan.scan_file(f)})

    print_results(result)

    if output in ("json", "both"):
        save_json_report(result)
    if output in ("pdf", "both"):
        save_pdf_report(result)

    print(green("\n[+] Scan complete. Reports saved."))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced OSINT CLI Tool")
    parser.add_argument("--email", "-e", nargs="+", help="Target email address(es)")
    parser.add_argument("--phone", "-p", nargs="+", help="Target phone number(s)")
    parser.add_argument("--ip", "-i", nargs="+", help="Target IP address(es)")
    parser.add_argument("--domain", "-d", nargs="+", help="Target domain name(s)")
    parser.add_argument("--username", "-u", nargs="+", help="Target username(s)")
    parser.add_argument("--file", "-f", nargs="+", help="Image/file(s) for metadata analysis")
    parser.add_argument("--output", "-o", choices=["json", "pdf", "both"], default="both", help="Output report format")
    args = parser.parse_args()

    if not any([args.email, args.phone, args.ip, args.domain, args.username, args.file]):
        parser.print_help()
        sys.exit(1)

    run_osint(**vars(args))
