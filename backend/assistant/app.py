import os
import time
from dotenv import load_dotenv
import openai


# Load environment variables
load_dotenv()

# Initialize API clients
sambanova_api_key = os.getenv("SAMBANOVA_API_KEY")
sambanova_client = openai.OpenAI(
    api_key=sambanova_api_key,
    base_url="https://api.sambanova.ai/v1"
)


def create_analysis_prompt(article_text):
    return f"""
    You are an AI assistant specializing in analyzing text for gender bias and providing actionable feedback. Review the following article for any biased language or tone and suggest inclusive alternatives.

    Article:
    {article_text}

    For each biased or potentially exclusive sentence, provide:
    - Original sentence
    - Suggested correction
    - Explanation of why the change improves neutrality and inclusivity.

    If no bias is detected, respond with "No suggestions necessary."
    """


def get_sambanova_response(article_text):
    start_time = time.time()
    prompt = create_analysis_prompt(article_text)

    response = sambanova_client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        top_p=0.1
    )

    end_time = time.time()
    response_text = response.choices[0].message.content.strip()

    suggestions = []
    lines = response_text.splitlines()

    current_suggestion = {}

    for line in lines:
        if line.startswith("Original sentence:"):
            if current_suggestion:
                suggestions.append(current_suggestion)
            current_suggestion = {'original_sentence': line.split(": ", 1)[1].strip()}
        elif line.startswith("Suggested correction:"):
            current_suggestion['suggested_correction'] = line.split(": ", 1)[1].strip()
        elif line.startswith("Explanation:"):
            current_suggestion['explanation'] = line.split(": ", 1)[1].strip()

    if current_suggestion:
        suggestions.append(current_suggestion)

    return {
        'suggestions': suggestions,
        'no_suggestions_message': "No suggestions necessary." in response_text
    }
