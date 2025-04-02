from mcp import ClientSession
from mcp.client.sse import sse_client


async def run():
    async with sse_client("http://0.0.0.0:8000/sse") as streams:  # Connect to the server
        async with ClientSession(*streams) as session:
            await session.initialize()
        # How to list tool and call tool

            tools = await session.list_tools()
            print("Available tools:", tools)

            #call a tool
            result = await session.call_tool("add", arguments={"a":5, "b":3})
            print("5 + 3 =", result.content[0].text)


        # How to call a resource and list resources
            resources = await session.list_resources()
            print("Available resources:", resources)

            #call a resource
            resources = await session.read_resource("resource://some_static_resource")
            print("Static Resource:", resources.contents[0].text)

            resources = await session.read_resource("resource://test")
            print("Dynamic Resource:", resources.contents[0].text)  

        # How to call a prompt and list prompts
            prompts = await session.list_prompts()
            print("Available prompts:", prompts)

            #call a prompt
            prompt = await session.get_prompt("review_code", arguments={"code":"print('Hello World!')"})
            print("Review Code prompt:", prompt)

            result = await session.get_prompt("debug_error", arguments={"error":"syntax error: invalid Syntax"})
            print("Debug Error prompt:", prompt)






if __name__ == "__main__":
    import asyncio
    asyncio.run(run())            



# llm_response = completion_api(message[], tools=[])

# if llm_response contains tool_call:
#     await session.call_tool(tool_call, arguments={"a":4,   "b":5})
