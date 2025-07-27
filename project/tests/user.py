import requests

class User:
    @classmethod
    async def create(cls, req:requests, url:str, headers:dict):
        ans = req.post(f'{url}/user/', headers=headers)
        return ans
    
    @classmethod
    async def leaderboard(cls, req:requests, url:str, headers:dict):
        ans = req.get(f'{url}/user/leaderboard', headers=headers)
        return ans
    @classmethod
    async def bot_income_gift(cls, req:requests, url:str, headers:dict):
        ans = req.post(f'{url}/bot/income_gift', headers=headers)
        return ans

