import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # You can also use "gpt2-medium", "gpt2-large", etc.
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Move the model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_response(input_text):
    # Encode the input text
    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)

    # Generate a response from the model
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode the response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Simple user interface
print("Chatbot: Hi! I'm a chatbot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = generate_response(user_input)
    print("Chatbot:", response)
