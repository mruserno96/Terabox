import requests

def get_direct_link(terabox_url):
    try:
        api_url = "https://terabox-api.vercel.app/api"
        response = requests.get(api_url, params={"link": terabox_url})
        if response.status_code == 200:
            result = response.json()
            if "data" in result:
                return result['data'][0]['dlink']
        return None
    except Exception as e:
        print(f"[ERROR] Terabox API: {e}")
        return None
