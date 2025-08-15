import aiohttp
import asyncio
from typing import List

async def check_subdomain(session: aiohttp.ClientSession, url: str) -> bool:
    try:
        async with session.get(url, timeout=5, ssl=False) as response:
            return response.status < 400
    except:
        return False

async def scan_subdomains(domain: str, wordlist: str = "wordlists/subdomains.txt") -> List[str]:
    found = []
    try:
        with open(wordlist, 'r') as f:
            subdomains = [f"http://{line.strip()}.{domain}" for line in f]
        
        async with aiohttp.ClientSession() as session:
            tasks = [check_subdomain(session, url) for url in subdomains]
            results = await asyncio.gather(*tasks)
            found = [subdomains[i] for i, success in enumerate(results) if success]
    except Exception as e:
        print(f"[!] Error: {e}")
    return found