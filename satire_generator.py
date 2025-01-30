import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def generate_satire(prompt):
    """Generates satirical content based on a given prompt."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a satirical political commentator."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Error generating satire:", e)
        return None

if __name__ == "__main__":
    print(generate_satire("Write a sarcastic tweet about US politics."))
