import requests
import asyncio
from datetime import datetime
from colorama import Fore


class RequestSiteController:
    @staticmethod
    async def req(site) -> str or None:
        r = requests.get(site)
        print(Fore.BLUE + f"Requisicao em {datetime.now()}")
        await asyncio.sleep(0.01)
        if r.status_code:
            print("Sucesso!")
            return r.content
        print("Falha na requisição")
        return None
