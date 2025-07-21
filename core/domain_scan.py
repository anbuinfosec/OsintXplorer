import whois

def scan_domain(domain):
    try:
        w = whois.whois(domain)
        return {
            "Registrar": w.registrar,
            "Creation Date": str(w.creation_date),
            "Expiration Date": str(w.expiration_date),
            "Name Servers": w.name_servers,
            "Status": w.status
        }
    except Exception as e:
        return {"Error": str(e)}
