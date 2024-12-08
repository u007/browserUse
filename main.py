from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig

import asyncio

async def main():
    agent = Agent(
        task="find all available primary school nearby kinrara mas apartment, and get their reviews with proos and cons and state if its private or public school, and also get their address and contact number, and price list. get at least 5 schools. if you detect any captcha on screen, pause for 10 seconds and try again.",
        llm=ChatOpenAI(model="gpt-4o-mini"),
        browser=Browser(BrowserConfig(headless=False)),
    )
    result = await agent.run()
    print("-------------")
    print(result)
    print("-------------")
    print("ended.")
    await agent.browser.close()

asyncio.run(main())
