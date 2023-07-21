import httpx

from settings import INSTAGRAM_CUSTOM_USER_HEADER


async def get_photos_url(username: str, count: int) -> list:
    base_url = 'https://www.instagram.com'
    url = f'{base_url}/api/v1/feed/user/{username}/username/?count=10'
    headers = {
        'referer': f'https://www.instagram.com/{username}/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': 'Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-full-version-list': 'Chromium";v="112.0.5615.165", "Google Chrome";v="112.0.5615.165", "Not:A-Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '"5.4.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
        'x-requested-with': 'XMLHttpRequest'
    }
    headers.update(INSTAGRAM_CUSTOM_USER_HEADER)

    photos = []
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        items = data['items']
        photos.extend(item['image_versions2']['candidates'][0]['url'] for item in items)

        if not items:
            return []

        if len(items) > count:
            return photos[:count]

        instagram_user_pk: str = data['user']['pk']

        while len(photos) < count and data['more_available']:
            url = f'{base_url}/api/v1/feed/user/{instagram_user_pk}/?count=10&max_id={data["next_max_id"]}'
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            items = data['items']
            photos.extend(item['image_versions2']['candidates'][0]['url'] for item in items)
        return photos[:count]
