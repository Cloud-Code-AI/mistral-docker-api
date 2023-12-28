from fastapi import FastAPI
import json
import time
import llama_cpp
from pydantic import BaseModel
import uvicorn
from typing import (
    List,
    Optional,
    Union,
)

app = FastAPI()

llm = llama_cpp.Llama(
    model_path="./models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    chat_format="llama-2"
    )

class InputQuery(BaseModel):
    messages: list
    temperature: float = 0.2
    top_p: float = 0.95
    stream: bool = False
    stop: Optional[Union[str, List[str]]] = []
    seed: Optional[int] = None
    max_tokens: Optional[int] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/infer")
def query_llm(query: InputQuery):
    start = time.time()
    print("Started Processing: ")
    outputs = llm.create_chat_completion(
        messages=query.messages,
        temperature=query.temperature,
        top_p=query.top_p,
        stream=query.stream,
        stop=query.stop,
        seed=query.seed,
        max_tokens=query.max_tokens,
    )
    print("Final Output input: ", time.time() - start)
    return {"resp": outputs}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
