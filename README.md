# mistral-docker-api
GGUF mistral model deployed as container using Docker.

## Setup

You need to download the model and store it in `models/` folder. 

Current code assusmes you have a model in following format: `models/mistral-7b-instruct-v0.2.Q4_K_M.gguf`.

You can download the above model at https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

Once you have all the files setup, build the docker image using

```docker build . --tag mistral-api```

Optionally you can fetch the pre built image using the following command:

```docker pull cloudcodeai/mistral-quantized-api```

and run the api using
```
docker run -p 8000:8000 mistral-api
```

## API

Inference runs at /infer endpoint.

Sample Request:
```
URL : http://localhost:8000/infer

Input: 
{
    "messages": [
        {"role": "user", "content": "Whats the value of pi?"}
    ]
}

Output:
{
    "resp": {
        "id": "chatcmpl-80b66d39-a218-428f-9b96-6072f0e6d074",
        "object": "chat.completion",
        "created": 1703743185,
        "model": "./models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": " The value of Pi is a mathematical constant that represents the ratio of a circle's circumference to its diameter. Its approximate value is 3.1415926535897932384626433832795028841. This value was calculated through mathematical computations and has been verified to many decimal places using various mathematical methods. However, it is an irrational number, which means its decimal representation goes on infinitely without repeating. Therefore, we can only know its value approximated to a certain degree of precision."
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 18,
            "completion_tokens": 128,
            "total_tokens": 146
        }
    }
}
```

Additionally you can pass following parameters in your input query:

```
class InputQuery(BaseModel):
    messages: list
    temperature: float = 0.2
    top_p: float = 0.95
    stream: bool = False
    stop: Optional[Union[str, List[str]]] = []
    seed: Optional[int] = None
    max_tokens: Optional[int] = None

```
