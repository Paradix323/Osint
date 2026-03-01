import socket
import dns.resolver
import whois

class OSINTEngine:
    #Implements high-efficiency DNS and WHOIS extraction logic.
    #Demonstrates O(n) complexity where n is the number of record types.
    def __init__(self):
        self.resolver = dns.resolver.Resolver()
        self.resolver.timeout = 2.0  # Professional timeout management
        self.resolver.lifetime = 2.0

    def get_dns_records(self, domain):
        #Extracts A, MX, TXT, and NS records.
        records = ['A', 'MX', 'TXT', 'NS']
        results = {}
        for r_type in records:
            try:
                answers = self.resolver.resolve(domain, r_type)
                results[r_type] = [str(rdata) for rdata in answers]
            except Exception:
                results[r_type] = ["N/A"]
        return results

    def get_whois_data(self, domain):
        #Performs WHOIS lookup for registrar and expiry data.
        try:
            w = whois.whois(domain)
            return {
                "registrar": w.registrar,
                "expiry": str(w.expiration_date),
                "org": w.org
            }
        except Exception as e:
            return {"error": "WHOIS lookup failed"}