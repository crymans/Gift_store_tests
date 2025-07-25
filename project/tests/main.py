from .user import User
from .purchase import Purchase, PURCHASE
from .gift import Gift, GIFTS
from .case import Case, CASES
import requests
import time, asyncio, logging
from .logger import create_logger




url = 'http://127.0.0.1:8000'
body = 'user=%7B%22id%22%3A971495895%2C%22first_name%22%3A%22%D0%A1%20%D0%B0%20%D1%88%20%D0%B0%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22crymans%22%2C%22language_code%22%3A%22ru%22%2C%22is_premium%22%3Atrue%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2FvFbVYnhG2nFxhrRcZQupOywRrxTbLcWcmixGxd1xa8I.svg%22%7D&chat_instance=4015797708649060653&chat_type=group&auth_date=1752835753&signature=8BSQiMcn8Fmb7fE3jqZ2rHfTl0YIDG7_QPnaSREbxrfckmCuYKKDEZ16sLjQPEeGUkr9W55x-LvJRlQPAs1_Cg&hash=012f66914c01e490dc9842dfba4e2714e1a3b7dcddeb844ec73f237772cf8ba6'
headers = {'user-data':body}

async def start():
    await create_logger('api_test')
    log = logging.getLogger('api_test')

    res = {
            'gift_create':[await Gift.create(requests, url, headers, gift) for gift in GIFTS][0],
            'user_before':await User.create(requests, url, headers),
            'case_create':[await Case.create(requests, url, headers, cas) for cas in CASES][0],
            'purchase_create': [await Purchase.create(requests, url, headers, pur) for pur in PURCHASE][0],
            'spin':await Case.spin(requests, url, 1, headers),
            'user_gifts': await Gift.user_giifts(requests, url, headers),
            'sell_gift': await Gift.sell(requests, url, headers, 1),
            'user_after':await User.create(requests, url, headers),
            'all_purchase': await Purchase.get_all(requests, url, headers),
            'all_gifts': await Gift.get_all(requests, url, headers),
        }
    for key, value in res.items():
        try:
            if value.status_code == 200:
                log.info(f'{key} : {value.json()}')
            else:
                log.error(f'{key} ERROR {value.json()}')
        except:
            pass


if __name__ == '__main__':
    asyncio.run(start())