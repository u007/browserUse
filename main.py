from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig

import asyncio

async def main():
    agent = Agent(
        task="find all available primary school nearby puchong jaya, malaysia. get reviews with pros and cons and state if its private or public school, and also get the address and contact number, and price list. get at least 5 schools. if you detect any captcha on screen, pause for 10 seconds and try again. Do not visit any yelp links. If you detect facebook page that prompt login, just click on the x on the dialog to close the login dialog. When prompt for GPS location dialog, chooese precision location.",
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
