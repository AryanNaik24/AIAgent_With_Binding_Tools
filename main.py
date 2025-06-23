from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from dotenv import load_dotenv
import asyncio
import os
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage


load_dotenv()






model = ChatOllama(
    model="llama3.1:8b", 
    temperature=0
)




server_params = StdioServerParameters(
    command="npx",
    args=["firecrawl-mcp"],
    env={"FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY")}
)






async def main():
    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(
                model,
                tools,
             
            )
            messages = [{
                "role": "system",
                "content": "You are a helpful assistant that can scrape websites, crawl pages , and exract data using Firecrawl tools. Think step by step and use the appropriate tools to help the user."
            }]

            print("Available tools:",*[tool.name for tool in tools])
            print("-"*60)

            while True :
                user_input = input("\nYou: ")
                if user_input.lower() in ["exit","quit","bye"]:
                    print("Goodbye!")
                    break
                messages.append({"role": "user", "content": user_input[:165000]})
                try:
                    response = await agent.ainvoke({"messages": messages})
                    response2=response.get("messages")[-1]

                    if isinstance(response2, AIMessage):
                        assistant_reply = response2.content
                    else:
                        assistant_reply = str(response)

                    messages.append({"role": "assistant", "content": assistant_reply})
                    print("\nAssistant:", assistant_reply)

                except Exception as e:
                    print(f"Error: {e}")
                    print("Please try again.")
            





if __name__ == "__main__":
    asyncio.run(main())
        
        







