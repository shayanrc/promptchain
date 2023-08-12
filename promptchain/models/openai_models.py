import openai

from promptchain import Message, Transform, Chain

openai.api_key = "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"

class LLM(Transform):
    def __init__(self, model, temperature=0.91, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0):
        super().__init__({'model': model, 'temperature': temperature, 'max_tokens': max_tokens, 'top_p': top_p, 'frequency_penalty': frequency_penalty, 'presence_penalty': presence_penalty})

    def __call__(self, obj):
        if isinstance(obj, Chain):
            # Perform the language model transformation here
            print(self.value)
            messages = [node.value for node in obj.nodes if isinstance(node, Message)]
            
            api_response = openai.ChatCompletion.create(**{**self.value, "messages":messages})
            return Message(**api_response.choices[0]['message'])

        elif isinstance(obj, Message):
            api_response = openai.ChatCompletion.create(**{**self.value, "messages":[obj.value]})
            return Message(**api_response.choices[0]['message'])

        else:
            super()(obj)