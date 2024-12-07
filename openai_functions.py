from openai import OpenAI
import instructor

client = OpenAI(api_key="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")

import instructor
instructor.patch(client)

def analyze_image_basic(image_url, prompt):
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {
            "type": "image_url",
            "image_url": {
                "url": image_url,
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    return response.choices[0].message.content



def generate_with_response_model(user_prompt,response_model):

    resut: response_model = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_model=response_model,
        messages=[{"role": "user", "content": user_prompt}]
    )

    return resut




