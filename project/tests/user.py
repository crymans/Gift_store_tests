import requests

class User:
    @classmethod
    async def create(cls, req:requests, url:str, headers:dict):
        ans = req.post(f'{url}/user/', headers=headers)
        return ans

