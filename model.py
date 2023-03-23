import openai

speech = """
{input}


###


"""

def key_setter(api_key):
   
    openai.api_key = api_key

class OpenAIModel:
    def __init__(self):
        print("Initialising...")

    def query(self, prompt, myKwargs={}):
        # arguments to send the API
        kwargs = {
            "temperature": 0.6,
            "max_tokens": 1000,
            "best_of": 1,
            "top_p": 1,
            "frequency_penalty": 0.5,
            "presence_penalty": 0.3,
            "stop": ["***"],
        }

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]

        speech = openai.Completion.create(prompt=prompt, model="davinci:ft-personal:speechgen-2023-01-30-01-35-08", **kwargs)["choices"][0][
            "text"
        ].strip()
        return speech


    def model_prediction(self, input, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        key_setter(api_key)
        output = self.query(speech.format(input = input))
        return output
