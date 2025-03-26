import random
from phi.agent import Agent
from phi.model.groq import Groq

BASE_INSTRUCTIONS = [
    "Generate a short, lame joke based on the provided topic.",
    "Keep it simple, cheesy, and related to the topic. Make it humorous so that people can enjoy it.",
    "Do not include any explanations, just the joke itself."
]

joke_agent = Agent(
    model=Groq(
        id="qwen-2.5-32b",
        temperature=1.2,
        top_p=0.9,
    ),
    instructions=BASE_INSTRUCTIONS,
    markdown=False
)

def generate_lame_joke(topic, attempt):
    prompt_variations = [
        f"Create a lame joke about {topic}.",
        f"Tell me a cheesy {topic}-related joke, attempt {attempt}.",
        f"What’s a silly joke about {topic}?",
        f"Give me a goofy lame joke involving {topic}.",
        f"Make up a ridiculous joke about {topic}.",
        f"Generate a corny {topic} joke right now."
    ]
    
    prompt = "\n".join(BASE_INSTRUCTIONS) + "\n" + random.choice(prompt_variations)
    print(f"Debug: Prompt sent to model: {prompt}")
    
    response = joke_agent.run(prompt)
    
    if isinstance(response, str):
        joke = response
    elif hasattr(response, 'content'):
        joke = response.content
    else:
        print("Warning: Unexpected response format. Returning raw response.")
        joke = str(response)
    
    return joke.replace("\\n", "\n")