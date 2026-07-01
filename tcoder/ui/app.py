from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Static
from textual.containers import Container, VerticalScroll
from rich.console import RenderableType
from rich.markdown import Markdown
import asyncio

from tcoder.core.models import Message, MessageRole
from tcoder.memory import MemoryManager


class ChatMessage(Static):
    """Widget to display a single chat message."""

    def __init__(self, message: Message):
        super().__init__()
        self.message = message

    def render(self) -> RenderableType:
        role_color = {
            MessageRole.USER: "blue",
            MessageRole.ASSISTANT: "green",
            MessageRole.SYSTEM: "magenta",
            MessageRole.TOOL: "yellow"
        }[self.message.role]

        return f"[bold {role_color}]{self.message.role.value.title()}:[/bold {role_color}]\n{Markdown(self.message.content)}"


class TCODERApp(App):
    """Main TCODER interactive application."""

    CSS = """
    #input-container {
        height: 4;
        dock: bottom;
        padding: 1;
        background: #202020;
    }
    #chat-scroll {
        height: 1fr;
    }
    """

    def __init__(self):
        super().__init__()
        self.memory = MemoryManager()

    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(id="chat-scroll")
        yield Container(Input(placeholder="Type your message here...", id="chat-input"), id="input-container")
        yield Footer()

    def on_mount(self) -> None:
        """Called when app starts."""
        self.query_one("#chat-input", Input).focus()

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle user input submission."""
        user_message = Message(role=MessageRole.USER, content=event.value)
        self.memory.add_message(user_message)

        chat_scroll = self.query_one("#chat-scroll", VerticalScroll)
        chat_scroll.mount(ChatMessage(user_message))

        event.input.value = ""

        # Simulate AI response for now (replace with real provider call later)
        ai_message = Message(role=MessageRole.ASSISTANT, content="This is a test response. I'm TCODER!")
        self.memory.add_message(ai_message)
        chat_scroll.mount(ChatMessage(ai_message))

        await chat_scroll.scroll_end(animate=False)


def run_interactive_ui():
    """Run the TCODER interactive UI."""
    app = TCODERApp()
    app.run()
