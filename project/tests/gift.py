import requests

GIFTS = [
    {
        'telegram_id': 0,
        'uniq': 1,
        'name': 'B-Day Candle',
        'bg_color': 'Shamrock Green',
        'img': 'img',
        'video': 'video',
        'cost': 270
    }
]

class Gift:
    @classmethod
    async def create(cls, req:requests, url:str, headers:dict, gift_data:dict):
        ans = req.post(f'{url}/gift/add', json=gift_data, headers=headers)
        return ans
    @classmethod
    async def user_giifts(cls, req:requests, url:str, headers:dict):
        ans = req.get(f'{url}/gift/user_gifts', headers=headers)
        return ans
    @classmethod
    async def sell(cls, req:requests, url:str, headers:dict, gift_id:int):
        ans = req.post(f'{url}/gift/sell', json=gift_id, headers=headers)
        return ans
    @classmethod
    async def get_all(cls, req:requests, url:str, headers:dict):
        ans = req.get(f'{url}/gift/available_gifts', headers=headers)
        return ans