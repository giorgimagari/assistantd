from transformers import pipeline

generator = pipeline("text-generation", model="gpt2", device=-1)

def text_generation(prompt: str) -> str:
    """Generates text based on prompt."""
    return generator(prompt, max_new_tokens=300, do_sample=True, truncation=True)[0]["generated_text"]

def summarize(text: str) -> str:
    """Summarizes long text."""
    prompt = f"Summarize this text in detail:\n{text}"
    return text_generation(prompt)

def translate(text: str, language: str = "Georgian") -> str:
    """Translates text to another language."""
    prompt = f"Translate this text to {language}:\n{text}"
    return text_generation(prompt)

def study_plan(topic: str) -> str:
    """Creates a detailed study plan for a topic."""
    prompt = f"Create a detailed study plan for the topic: {topic}"
    return text_generation(prompt)

def calculate(expression: str) -> str:
    """Calculates a math expression."""
    try:
        return str(eval(expression))
    except:
        return "Cannot calculate that expression."


def agent(user_input: str) -> str:
    """Decides which tool to use based on keywords in the input."""
    user_lower = user_input.lower()
    
    if "summarize" in user_lower:
        return summarize(user_input)
    elif "translate" in user_lower:   
        return translate(user_input)
    elif "study plan" in user_lower:
        return study_plan(user_input)
    elif "calculate" in user_lower:
        expr = user_lower.replace("calculate", "").strip()
        return calculate(expr)
    else: 
        return text_generation(user_input)

if __name__ == "__main__":
    print("General Purpose Study Assistant running. Type 'exit' to quit.\n")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        response = agent(user_input)
        print("\nAgent Response:\n", response + "\n" + "-"*60 + "\n")
