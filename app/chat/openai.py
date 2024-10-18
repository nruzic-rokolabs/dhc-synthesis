from typing import Sequence
from typing_extensions import Annotated, TypedDict

from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, trim_messages
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages

from .models import AIService, ConversationInputMessage


# LLM model
model = ChatOpenAI(model="gpt-3.5-turbo")


# Define prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You talk like a pirate. Answer all questions to the best of your ability in {language}.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Define prompt trimmer
trimmer = trim_messages(
    max_tokens=65,
    strategy="last",
    token_counter=model,
    include_system=True,
    allow_partial=False,
    start_on="human",
)


# Application state
class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    language: str


# Define a new graph
workflow = StateGraph(state_schema=State)


# Define the function that calls the model
def call_model(state: State):
    chain = prompt | model
    trimmed_messages = trimmer.invoke(state["messages"])
    response = chain.invoke(
        {"messages": trimmed_messages, "language": state["language"]}
    )
    return {"messages": [response]}


# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)


# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)


# Simple conversation helper
def converse(thread_id: str, message_in: str):
    messages_in = [HumanMessage(message_in)]
    for chunk, metadata in app.stream({
            "messages": messages_in,
            "language": "Croatian"
        }, {
            "configurable": {
                "thread_id": thread_id
            }
        },
        stream_mode="messages"
    ):
        print(f"chunk: {chunk}")
        print(f"metad: {metadata}")
        if isinstance(chunk, AIMessage):
            yield chunk.content


print(">>>>>>>>>>>>>>>>>>> ChatGPT connector initialized!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


# Connector's application interface implementation
class OpenAIService(AIService):

    def simple_streaming_conversation(self, message: ConversationInputMessage) -> str:
        for chunk in converse(str(message.thread_id), message.message):
            yield chunk

