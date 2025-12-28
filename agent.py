 from transformers import pipeline

generator = pipeline("text-generation", model="gpt2", device=-1)

summarizer = None
translator = None

def text_generation(prompt: str) -> str:
    """Generates general text using GPT-2."""
    return generator(prompt, max_new_tokens=200, do_sample=True, truncation=True)[0]["generated_text"]

def summarize(text: str) -> str:
    """Summarizes text using BART (lazy-loaded)."""
    global summarizer
    if summarizer is None:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

def translate(text: str, language: str = "Georgian") -> str:
    """Translates English to Georgian (lazy-loaded)."""
    global translator
    if language.lower() != "georgian":
        return "Only Georgian translation is supported for now."
    if translator is None:
        translator = pipeline("translation_en_to_ka", model="Helsinki-NLP/opus-mt-en-ka")
    return translator(text)[0]['translation_text']

def study_plan(topic: str) -> str:
    """Creates a study plan using GPT-2."""
    prompt = f"Create a detailed study plan for the topic: {topic}"
    return text_generation(prompt)

def calculate(expression: str) -> str:
    """Calculates a math expression safely."""
    try:
        allowed_chars = "0123456789+-*/(). "
        if all(c in allowed_chars for c in expression):
            return str(eval(expression))
        else:
            return "Invalid expression."
    except:
        return "Cannot calculate that expression."

def run_agent(user_input: str) -> str:
    """Decides which tool to use based on keywords in the input."""
    user_lower = user_input.lower()
    
    if "summarize" in user_lower:
        text = user_input.lower().replace("summarize", "").strip()
        return summarize(text)
    elif "translate" in user_lower:   
        text = user_input.lower().replace("translate", "").strip()
        return translate(text)
    elif "study plan" in user_lower:
        text = user_input.lower().replace("study plan", "").strip()
        return study_plan(text)
    elif "calculate" in user_lower:
        expr = user_lower.replace("calculate", "").strip()
        return calculate(expr)
    else: 
        return text_generation(user_input)
