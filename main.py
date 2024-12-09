from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
import os
import asyncio


async def main():
    location = os.getenv('LOCATION')
    start_time = asyncio.get_event_loop().time()
    agent = Agent(
        task=f"find all available primary school in near by {location}. get reviews with pros and cons and state if its private or public school, and also get the address and contact number, and price list. get at least 5 schools. if you detect any captcha on screen, pause for 10 seconds and try again. Do not visit any yelp links. If you detect facebook page that prompt login, just click on the x on the dialog to close the login dialog. When prompt for GPS location dialog, chooese precision location. Do not use enquire button.",
        llm=ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv('OPENAI_API_KEY')),
        browser=Browser(BrowserConfig(headless=False)),
    )
    result = await agent.run()
    end_time = asyncio.get_event_loop().time()
    print("-------------")
    print(f"Time spent: {end_time - start_time:.2f} seconds")
    print(result)
    print("-------------")
    print("ended.")    await agent.browser.close()
asyncio.run(main())