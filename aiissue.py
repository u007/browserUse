from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
import os
import asyncio


async def main():
    # location = os.getenv('LOCATION')
    import time
    start_time = time.time()
    
    agent = Agent(
        task=f"get me top 5 business related issues with manual field works that requires human intervention to proceed paper work and suggest how ai can help to automate the process",
        llm=ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv('OPENAI_API_KEY')),
        browser=Browser(BrowserConfig(headless=False)),
    )
    result = await agent.run()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print("-------------")
    print(result)
    print("-------------")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print("ended.")    # await agent.browser.close()
asyncio.run(main())