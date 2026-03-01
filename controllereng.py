import re
from mainengine import OSINTEngine

class OSINTController:
    def __init__(self):
        self.engine = OSINTEngine()

    def validate_domain(self, domain):
        """Ensures input follows RFC domain naming conventions."""
        pattern = r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, domain) is not None

    def process_investigation(self, domain):
        if not self.validate_domain(domain):
            return {"error": "Invalid Domain Format"}
        
        dns_data = self.engine.get_dns_records(domain)
        whois_data = self.engine.get_whois_data(domain)
        
        return {"dns": dns_data, "whois": whois_data}