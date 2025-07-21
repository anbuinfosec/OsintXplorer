import requests

def scan_ip(ip):
    url = f"https://ipwhois.io/widget?ip={ip}&lang=en"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,bn;q=0.8,id;q=0.7,zh-CN;q=0.6,zh;q=0.5",
        "referer": "https://ipwhois.io/",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        result = {
            "IP": data.get("ip", ""),
            "Country": data.get("country", ""),
            "Region": data.get("region", ""),
            "City": data.get("city", ""),
            "ISP": data.get("isp", ""),
            "Latitude": data.get("latitude", ""),
            "Longitude": data.get("longitude", ""),
            "Timezone": data.get("timezone", {}).get("name", ""),
            "ASN": data.get("asn", ""),
        }
        return result
    except Exception as e:
        return {"Error": str(e)}
