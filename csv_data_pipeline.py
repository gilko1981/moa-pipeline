from typing import List, Union, Generator, Iterator
from pydantic import BaseModel
# from schemas import OpenAIChatMessage
import requests
import os
import pandas as pd


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
        # self.df = pd.read_csv('data/titanic.csv')


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
            context = '--------\n'.join([str(s) for s in (user_message, messages, body)])
            # context = self.df.head(3)

            return context if context else "No information found"


if __name__ == '__main__':
    p = Pipeline()
    p.pipe('some message', 'id', [], {})