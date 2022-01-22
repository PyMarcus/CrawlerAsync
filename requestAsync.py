"""
Pode-se fazer requisicoes usando aiohttp
pip install aiohttp[speedups]
"""
import asyncio
import aiofiles
import aiohttp
import bs4


async def search_links():
    links = list()
    async with aiofiles.open('links.txt') as f:
        async for link in f:
            links.append(link.strip())
    return links


async def request_link(link):
    print("Html de {}".format(link))
    async with aiohttp.ClientSession() as s:
        async with s.get(link) as r:
            r.raise_for_status()
            return await r.text()


def parse_html(html):
    """Pega o título do curso"""
    b = bs4.BeautifulSoup(html, 'html.parser')
    c = b.select_one('title')
    c = c.text.split('|')[0].strip()
    return c


async def main():
    links = await search_links()
    tarefas = []
    for link in links:
        tarefas.append(asyncio.create_task(request_link(link)))
    print("Imprimindo titulos")
    for tarefa in tarefas:
        html = await tarefa
        title = parse_html(html)
        print(title)


def run():
    el = asyncio.get_event_loop()
    el.run_until_complete(main())
    el.close()


if __name__ == '__main__':
    run()
