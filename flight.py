from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
import os
import asyncio


async def main():
    location = os.getenv('LOCATION')
    import time
    start_time = time.time()
    model = "gpt-4o"
    agent = Agent(
        task=f"get me the available flights with return flights california to canada on Jan 15th 2025. sort them by price and return the cheapest one first. Use google flights for this. To set the date, click on departure to set flight date, and click on return to set return date. makesure to select the from and to location when dropdown is presented.",
        llm=ChatOpenAI(model=model, api_key=os.getenv('OPENAI_API_KEY')),
        browser=Browser(BrowserConfig(headless=False)),
    )
    result = await agent.run()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print("-------------")
    print(result)
    print("-------------")
    print(f"model {model} Time elapsed: {elapsed_time:.2f} seconds")
    print("ended.")    # await agent.browser.close()
asyncio.run(main())