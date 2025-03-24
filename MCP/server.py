
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.requests import Request
import uvicorn
from starlette.routing import  Route
from mcp.server.sse import SseServerTransport

mcp = FastMCP("ai_hello_world")
# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


app = mcp._mcp_server
sse = SseServerTransport("/messages")

async def handle_sse(request:Request):
    async with sse.connect_sse(request.scope, request.receive, request._send) as streams:
        await app.run(streams[0], streams[1], app.create_initialization_options())

async def handle_messages(request:Request):
    await sse.handle_post_message(request.scope, request.receive, request._send)

starlette_app = Starlette(
    routes=[
        Route("/sse", endpoint=handle_sse),
        Route("/messages", endpoint=handle_messages, methods=["POST"]),
    ]
)
uvicorn.run(starlette_app)