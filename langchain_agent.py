from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

import utils
from abstract_agent import AbstractAgent

# Note: there is an experimental autogpt API
# from langchain_experimental.autonomous_agents.autogpt.agent import AutoGPT


class LangChainAgent(AbstractAgent):
    def __init__(self):
        keys = utils.get_keys()
        llm = OpenAI(openai_api_key=keys.openai)
        tools = load_tools(["serpapi", "llm-math"], llm=llm, serpapi_api_key=keys.serp)
        self._agent = initialize_agent(
            tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
        )

    def run(self, market: str) -> bool:
        objective = utils.get_market_prompt(market)
        result_str = self._agent.run(objective)
        return utils.parse_result_to_boolean(result_str)
