from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
import os
import asyncio


async def main():
    location = os.getenv('LOCATION')
    start_time = asyncio.get_event_loop().time()
    agent = Agent(
        task=f"goto phitomas.com, and submit an enquiry to the contact form to tell them this is a ai bot using the browser agent. randomise my name and set email to jamestan@phitomas.com. Randomise or select 1st option for industry and product.",
        llm=ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv('OPENAI_API_KEY')),
        browser=Browser(BrowserConfig(headless=False)),
    )
    result = await agent.run()
    end_time = asyncio.get_event_loop().time()
    print("-------------")
    print(result)
    print("-------------")
    print(f"Time spent: {end_time - start_time:.2f} seconds")
    print("ended.")
    await agent.browser.close()
asyncio.run(main())