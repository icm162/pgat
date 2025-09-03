import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent, ChatGoogle #, ChatOpenAI

with open(r"..\\api_key", "r", encoding="utf8") as reader: 
    api_key = reader.readline()

browser_task = "Find the number of stars of the browser-use repo"

async def main():
    agent = Agent(
        task=browser_task,
        llm=ChatGoogle(model="gemini-2.5-flash", api_key=api_key),
        # llm=ChatOpenAI(model="",api_key=api_key),
    )
    await agent.run()

asyncio.run(main())

