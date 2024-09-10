from typing import List, Union, Generator, Iterator
from pydantic import BaseModel
# from schemas import OpenAIChatMessage
import requests
import os
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
# from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

class Pipeline:
    class Valves(BaseModel):
        pass

    def __init__(self):
        # Optionally, you can set the id and name of the pipeline.
        # Best practice is to not specify the id so that it can be automatically inferred from the filename, so that users can install multiple versions of the same pipeline.
        # The identifier must be unique across all pipelines.
        # The identifier must be an alphanumeric string that can include underscores or hyphens. It cannot contain spaces, special characters, slashes, or backslashes.
        # self.id = "wiki_pipeline"
        self.name = "csv_pipeline"
        # Initialize rate limits
        self.valves = self.Valves(**{"OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", "")})
        # self.df = pd.read_csv('/app/titanic.csv')
        self.df = pd.read_csv('/app/titanic.csv')
        # self.llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", api_key=os.getenv('ANTHROPIC_API_KEY'))
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)

    async def on_startup(self):
        # This function is called when the server is started.
        print(f"on_startup:{__name__}")
        pass

    async def on_shutdown(self):
        # This function is called when the server is stopped.
        print(f"on_shutdown:{__name__}")
        pass

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        # This is where you can add your custom pipelines like RAG.
        print(f"pipe:{__name__}")

        if body.get("title", False):
            print("Title Generation")
            return "CSV Pipeline"
        else:
            context = 'lala'
            # context = '--------\n'.join([str(s) for s in (user_message, messages, body)])
            # context = str(self.df.head(3))
    
            # agent = create_pandas_dataframe_agent(self.llm, self.df, agent_type="openai-tools", verbose=True, allow_dangerous_code=True)
            # context = agent.invoke({"input": user_message}).get('output', '')
            

        return context if context else "No information found"


if __name__ == '__main__':
    p = Pipeline()
    print(p.pipe("What's the strongest correlation between any of the headers to survivability in the data", 'id', [], {}))