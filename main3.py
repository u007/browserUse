from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
import os
import asyncio


async def main():
    location = os.getenv('LOCATION')
    import time
    start_time = time.time()
    
    agent = Agent(
        task=f"get me list of top 10 trending ai keywords and tech news. then research 1st keyword and write a 1000 word article about it. include any meme or emoji or any free images available on the internet. use markdown format. use the keyword as the title of the article. then write the article in markdown at https://www.memonotepad.com/",
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