import requests

def get_direct_link(terabox_url):
    try:
        api_url = "https://terabox-api.vercel.app/api"
        response = requests.get(api_url, params={"link": terabox_url})
        if response.status_code == 200:
            data = response.json()
            return data['data'][0]['dlink']
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None