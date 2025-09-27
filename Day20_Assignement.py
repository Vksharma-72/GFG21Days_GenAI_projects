from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio
import os
import sys

from dotenv import load_dotenv

load_dotenv()

from browser_use import Agent
API_KEY = os.getenv("GOOGLE_API_KEY")

async def main():
    # Instantiate the Google Gemini model
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=API_KEY)
    task = "Search Google for 'what is browser automation' and tell me the top 3 results"
    agent = Agent(
        task=task, 
        llm=llm
    )

    try:
        # Run the agent
        history = await agent.run()

        # Extract the content as text
        result_text = ""
        for item in history:
            if 'extracted_content' in item and item['extracted_content']:
                result_text += item['extracted_content'] + "\n"

        # Print results
        print("=== Agent Results ===")
        print(result_text)

        # Save to txt file
        with open("browser_use_results.txt", "w", encoding="utf-8") as f:
            f.write(result_text)

        print("Results saved to browser_use_results.txt")

    except Exception as e:
        print("Error running agent:", e)


if __name__ == "__main__":
	asyncio.run(main())