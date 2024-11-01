import os
import time
from dotenv import load_dotenv
import openai
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize API clients
groq_api_key = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=groq_api_key)

sambanova_api_key = os.getenv("SAMBANOVA_API_KEY")
sambanova_client = openai.OpenAI(
    api_key=sambanova_api_key,
    base_url="https://api.sambanova.ai/v1"
)


def create_analysis_prompt(article_text):
    """
    Generate a prompt to detect gender bias and suggest improvements in the article.
    """
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


def get_groq_response(prompt):
    """
    Get a response from the Groq API.
    """
    start_time = time.time()
    response = groq_client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192"
    )
    end_time = time.time()

    response_text = response.choices[0].message.content.strip()
    print("Groq Response:", response_text)
    print(f"Response Time: {end_time - start_time} seconds")
    return response_text


def get_sambanova_response(article_text):
    """
    Get a response from the SambaNova API.
    """
    start_time = time.time()
    messages = [
        {"role": "system",
         "content": "You are an assistant that specializes in analyzing text for gender bias and providing actionable feedback."},
        {"role": "user", "content": f"Please analyze the following article and suggest improvements: '{article_text}'"}
    ]

    response = sambanova_client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=messages,
        temperature=0.1,
        top_p=0.1
    )
    end_time = time.time()

    # Corrected access to the response content
    response_text = response.choices[0].message.content.strip()
    print("SambaNova Response:", response_text)
    print(f"Response Time: {end_time - start_time} seconds")
    return response_text


def analyze_article_for_bias(article_text):
    """
    Analyze the article for gender bias and provide suggestions for improvement.
    """
    prompt = create_analysis_prompt(article_text)

    # Get responses from both APIs for combined insights
    groq_feedback = get_groq_response(prompt)
    sambanova_feedback = get_sambanova_response(article_text)

    # Aggregate responses
    combined_feedback = f"Groq Feedback:\n{groq_feedback}\n\nSambaNova Feedback:\n{sambanova_feedback}"

    return combined_feedback


# Example article for testing
article_text = """
common hazard with critiquing family influencers is that we side-eye them for showing only the cute stuff, and then we critique them as though what they show is all there really is. The latest cycle of virality for Ballerina Farm’s Hannah Neeleman has called into question a lot of what we’ve assumed, but this time, unlike her previous go-rounds in the media, the questions have come from both the press and from Neeleman herself.

I’ve been following Ballerina Farm for years, and I’ve always felt that I kind of knew Neeleman. I knew that shortly after graduating from Juilliard, she had left a ballet career behind to have eight kids in quick succession with her husband, Daniel, whose father owns JetBlue Airways. I knew they sold upscale flour and meat and Frenchified provisions from their huge Utah farm, and I knew she was a dedicated beauty-pageant competitor who competed for Mrs. American 2023 less than two weeks after having her eighth child. But I always thought there was something subtly knowing in her posts about life on the farm. Hannah seems temperamentally low-key, even when she’s in full pageant glam, and that has always made me hope that she’s self-aware about creating content that’s an elaborate charade about status, purity, and simplicity. She follows Alison Roman and Smitten Kitchen, I thought — how trad-pilled could she possibly be?! Then I read the now-viral profile in the Times. Oof.
"""

# Run the analysis
feedback = analyze_article_for_bias(article_text)
print("Final Feedback:\n", feedback)
