import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent, ChatGoogle

with open(r"..\\api_key", "r", encoding="utf8") as reader: api_key = reader.readline()

async def main():
    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=ChatGoogle(model="gemini-2.5-flash",
                       api_key="AIzaSyD4WKyxKgdU-vJLPidKBe1pELP9rMMjeGQ"),
    )
    await agent.run()

asyncio.run(main())

