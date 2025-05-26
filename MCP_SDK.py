from mcp.server.fastmcp import FastMCP     ## Import FastMCP class to build the server

mcp = FastMCP("Weather Service")           ## Create a FastMCP server instance with the name "Weather Service"


@mcp.tool()                                ## Register this function as a tool that can be called by external agents
def get_weather(location: str) -> str:     ## Define a function that takes a location string and returns weather info
    return f"Weather in {location}: Sunny, 72°F"  ## Return a string with the location inserted using an f-string


@mcp.resource("weather://{location}")      ## Register this function as a resource endpoint accessed via a URI
def weather_resource(location: str) -> str:## Define a function that handles requests to weather://{location}
    return f"Weather data for {location}: Sunny, 72°F" ## Return weather info as a formatted string resource


@mcp.prompt()                              ## Register this function as a prompt that returns a natural language query
def weather_report(location: str) -> str:  ## Define a function that returns a prompt for an LLM to generate a report
    return f"You are a weather reporter. Weather report for {location}?" ## Create a prompt including the location


if __name__ == "__main__":                 ## This ensures the server only runs if the script is executed directly
    mcp.run()                              ## Starts the FastMCP server to listen for tool, resource, and prompt calls

