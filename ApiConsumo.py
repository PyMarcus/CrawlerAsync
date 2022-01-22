import aiohttp
import json
import asyncio

async def call(site) -> None:
    """Retorna json da api"""
    async with aiohttp.ClientSession() as session:
        async with session.get(site) as respond:
            valor = await respond.json()
            print(valor)

if __name__ == '__main__':
    api = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    try:
        asyncio.run(call(api))
    except:
        print('Erro ao executar a chamada')





