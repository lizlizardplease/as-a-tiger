import requests
import asyncio
import aiofiles
import aiohttp


async def process_urls(song):
    with open("urls.txt", 'r') as file:
        urls = (line.strip() for line in file)
        tasks = [look_up_url(url, song) for url in urls]
        await asyncio.gather(*tasks)


async def look_up_url(url, song):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/search?q={song}") as response:
            if response.status == 200:
                print("Запрос выполнен успешно")
            else:
                print("Ошибка при выполнении запроса")
            #print(await response.text())

asyncio.run(process_urls('Лиза'))