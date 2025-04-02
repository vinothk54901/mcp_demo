from mcp.server.fastmcp import FastMCP
import math

# Initialize MCP server
mcp = FastMCP("CalculatorServer")

# Define tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first."""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide the first number by the second."""
    if b == 0:
        return float('inf')
    return a / b

#### Resources ####
#Add a static resource
@mcp.resource("resource://some_static_resource")
def get_static_resource() -> str:
    """static resource data"""
    return "Any Static resource can be returned"
#Add a dynamic resource
@mcp.resource("resource://{name}")
def get_dynamic_resource(name: str) -> str:
    """dynamic resource data"""
    return f"Any Dynamic resource can be returned {name}"


### Prompts ###
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Review this code: {code}"

@mcp.prompt()
def debug_error(error: str) -> list[tuple]:
    """Return the square root of a number."""
    return [
        {"user", "I'm seeing this error"},
        {"user",error},
        {"assistant","I'm sorry to hear that. Can you provide more details about the error?"}
    ]


if __name__ == "__main__":
    mcp.run(transport="sse")
