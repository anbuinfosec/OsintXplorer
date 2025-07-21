import requests

def scan_username(username):
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Medium": f"https://medium.com/@{username}",
        "Dev.to": f"https://dev.to/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Telegram": f"https://t.me/{username}"
    }
    results = {}
    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                results[platform] = f"✅ Found: {url}"
            elif response.status_code == 404:
                results[platform] = "❌ Not Found"
            else:
                results[platform] = f"⚠️ Status Code: {response.status_code}"
        except requests.RequestException:
            results[platform] = "⚠️ Connection Error"
    return results
