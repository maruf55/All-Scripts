#!/usr/bin/env python3
import argparse
import re
from urllib.parse import urlparse

def clean_domain(raw_domain: str) -> str:
    """
    Normalize a domain: remove http(s)://, www., and trailing slashes.
    """
    if raw_domain.startswith("http://") or raw_domain.startswith("https://"):
        parsed = urlparse(raw_domain)
        domain = parsed.netloc
    else:
        domain = raw_domain

    if domain.startswith("www."):
        domain = domain[4:]

    return domain.lower().strip()


def extract_domains(text: str, parent_domain: str):
    """
    Extract unique domains and subdomains for a given parent domain.
    """
    domain_pattern = re.compile(
        rf"(?:https?://)?(?:www\.)?([a-zA-Z0-9_-]+\.)*{re.escape(parent_domain)}"
    )

    domains = set()
    for match in re.finditer(domain_pattern, text):
        cleaned = clean_domain(match.group(0))
        domains.add(cleaned)

    return sorted(domains)


def main():
    parser = argparse.ArgumentParser(
        description="🔍 Extract unique domains and subdomains from a text file for a given parent domain.\n\n"
                    "Examples:\n"
                    "  python3 extract_domains.py example.com data.txt\n"
                    "  python3 extract_domains.py mysite.org urls.txt\n",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "parent_domain",
        help="Parent domain to match against (e.g., 'example.com').\n"
             "All subdomains of this domain will also be extracted."
    )

    parser.add_argument(
        "input_file",
        help="Path to a text file containing raw URLs, domains, or mixed text.\n"
             "The script will scan the file and extract matching domains."
    )

    args = parser.parse_args()

    # Read input file
    with open(args.input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Extract domains
    domains = extract_domains(text, args.parent_domain)

    # Print results
    if domains:
        print("\n".join(domains))
    else:
        print(f"No domains found for parent: {args.parent_domain}")


if __name__ == "__main__":
    main()
