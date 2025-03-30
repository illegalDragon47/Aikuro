from pydantic import Field

from app.agent.browser import BrowserAgent
from app.config import config
from app.prompt.browser import NEXT_STEP_PROMPT as BROWSER_NEXT_STEP_PROMPT
from app.prompt.aikuro import NEXT_STEP_PROMPT, SYSTEM_PROMPT
from app.tool import Terminate, ToolCollection
from app.tool.browser_use_tool import BrowserUseTool
from app.tool.python_execute import PythonExecute
from app.tool.str_replace_editor import StrReplaceEditor


class Aikuro(BrowserAgent):
    """
    ┌─────────────────────────────────────────┐
    │  Aikuro: Enterprise AI Solution Suite   │
    └─────────────────────────────────────────┘

    A robust enterprise-grade agent designed to solve complex business challenges
    through systematic planning and efficient execution.

    Extends the BrowserAgent with a comprehensive set of professional tools,
    including Python execution, web research, document management, and data analysis
    to address sophisticated enterprise requirements.

    Built with enhanced enterprise capabilities.
    """

    name: str = "Aikuro"
    description: str = (
        "📊 Enterprise-grade AI solution for transforming business requirements into actionable deliverables 🔧"
    )

    system_prompt: str = SYSTEM_PROMPT.format(directory=config.workspace_root)
    next_step_prompt: str = NEXT_STEP_PROMPT

    max_observe: int = 10000
    max_steps: int = 20

    # Enterprise toolkit for comprehensive business solutions
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            PythonExecute(), BrowserUseTool(), StrReplaceEditor(), Terminate()
        )
    )

    async def think(self) -> bool:
        """Process current state and strategically determine next actions based on context analysis."""
        # Store reference configuration
        original_prompt = self.next_step_prompt

        # Analyze recent interaction patterns for context-aware response
        recent_messages = self.memory.messages[-3:] if self.memory.messages else []
        browser_in_use = any(
            "browser_use" in msg.content.lower()
            for msg in recent_messages
            if hasattr(msg, "content") and isinstance(msg.content, str)
        )

        if browser_in_use:
            # Implement browser-specific protocol when appropriate
            self.next_step_prompt = BROWSER_NEXT_STEP_PROMPT

        # Execute core reasoning algorithm
        result = await super().think()

        # Restore standard operating parameters
        self.next_step_prompt = original_prompt

        return result
