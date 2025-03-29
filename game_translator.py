from langchain_core.messages import HumanMessage, SystemMessage

class GameTranslator:
    def __init__(self, llm, propmt) -> None:
        self.llm = llm
        self.propmt = propmt
        self.messages = [
            SystemMessage(propmt)
        ]
        pass

    def clear_history(self):
        """Clear the conversation history and reset to initial state."""
        self.messages = [
            SystemMessage(self.propmt)
        ]

    def translate(self, text) -> str:
        self.messages.append(
            HumanMessage(text)
        )
        response = self.llm.invoke(self.messages)
        return response.content