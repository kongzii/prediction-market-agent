from prediction_market_agent.agents.abstract import AbstractAgent


class AlwaysYesAgent(AbstractAgent):
    """
    Save OpenAI API credits. Always say yes!
    """

    def __init__(self):
        pass

    def run(self, objective: str) -> bool:
        return True
