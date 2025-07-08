from openai import OpenAI
client = OpenAI()

prompt = ""
while prompt != "STOP":
    prompt = input("Enter prompt.")
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ]
    )
    print(completion.choices[0].message.content)