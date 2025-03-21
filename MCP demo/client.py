from mcp import ClientSession, StdioServerParameters, types
from mcp.client.sse import sse_client




# Optional: create a sampling callback
async def handle_sampling_message(
    message: types.CreateMessageRequestParams,
) -> types.CreateMessageResult:
    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(
            type="text",
            text="Hello, world! from model",
        ),
        model="gpt-3.5-turbo",
        stopReason="endTurn",
    )


async def run():
    async with sse_client("http://localhost:8000/sse") as (read, write):
        async with ClientSession(
            read, write, sampling_callback=handle_sampling_message
        ) as session:
            # Initialize the connection
            await session.initialize()

            # List available prompts
            prompts = await session.list_prompts()
            print(prompts)
            # # Get a prompt
            # prompt = await session.get_prompt(
            #     "example-prompt", arguments={"arg1": "value"}
            # )

            # List available resources
            resources = await session.list_resources()
            print(resources)
            # List available tools
            tools = await session.list_tools()
            print(tools)
            # # Read a resource
            # content, mime_type = await session.read_resource("file://some/path")

            # # Call a tool
            result = await session.call_tool("add", arguments={"a" : 1,"b": 2})
            print(result.content[0].text)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())