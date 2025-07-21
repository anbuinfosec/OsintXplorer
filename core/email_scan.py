import re

def scan_email(email):
    result = {}

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    result["Valid Format"] = bool(re.match(pattern, email))

    if result["Valid Format"]:
        domain = email.split('@')[1]
        result["Domain"] = domain
        result["MX Record Check"] = f"https://mxtoolbox.com/SuperTool.aspx?action=mx:{domain}"
        result["Breach Check"] = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    else:
        result["Error"] = "Invalid email format"

    return result
