import requests


PURCHASE = [
    {
        'purchase_type': 'star',
        'inner_star': 100,
        'price': 100,
        'gift_name': 'Gazy Dai'
    },
]

class Purchase:
    @classmethod
    async def create(cls, req:requests, url:str, headers:dict,  purchase_data:dict):
        ans = req.post(f'{url}/purchase/add', json=purchase_data, headers=headers)
        return ans
    @classmethod
    async def get_all(cls, req:requests, url:str, headers:dict, type_p:str='star'):
        ans = req.get(f'{url}/purchase/all?purchase_type={type_p}', headers=headers)
        return ans
    @classmethod
    async def logs(cls, req:requests, url:str, headers:dict):
        ans = req.get(f'{url}/purchase/logs', headers=headers)
        return ans