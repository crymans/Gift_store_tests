import requests, json

CASES = [
    {
        'name': 'name',
        'cost': 0,
        'img': 'img',
        'video': 'video',
        'quality': 'common',
        'gifts': "{'1':1000}"
    }
]


class Case:

    @classmethod
    async def create(cls, req:requests, url:str, headers:dict, case_data):
        ans = req.post(f'{url}/case/add', json=case_data, headers=headers)
        return ans

    @classmethod
    async def spin(cls, req:requests, url:str, case_id:str, headers:dict):
        ans = req.post(f'{url}/case/spin', json=case_id, headers=headers)
        return ans