from mcp import ClientSession, StdioServerParameters
from typing import Annotated, List
from typing_extensions import TypedDict
from langgraph.graph.message import AnyMessage, add_messages

# Define server parameters (specify path to server script).
server_params = StdioServerParameters(
    command="python",
    args=["mcp_server.py"]
)

# LangGraphs state definition
class State(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]