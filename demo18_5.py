import asyncio

import aiohttp

from demo17_2 import BASE_URL,save_flag,main,show

async def get_flag(cc):
	url='{}/{cc}/{cc}.gif'.format(BASE_URL,cc=cc.lower())
	async with aiohttp.request('GET',url) as r:
		image = await r.read()
	return image

async def download_one(cc):
	image = await get_flag(cc)
	show(cc)
	save_flag(image,cc.lower()+'.gif')
	return cc

def download_many(cc_list):
	loop = asyncio.get_event_loop()
	to_do = [download_one(cc) for cc in cc_list]
	wait_coro = asyncio.wait(to_do)
	loop.run_until_complete(wait_coro)
	loop.close()

if __name__=='__main__':
	main(download_many)