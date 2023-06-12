import os
from dotenv import load_dotenv
import openai
from openai import Completion
import time

# Load the environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Counter variable to track API calls
api_call_counter = 0

# Set the maximum number of requests
max_requests = 60

def rearrange_css_code(css_code):
    batches = css_code.split('@media')

    # Remove leading/trailing whitespace from batches
    batches = [batch.strip() for batch in batches]

    # Reconstruct the CSS code with re-arranged batches
    rearranged_css_code = ''
    for i, batch in enumerate(batches):
        rearranged_css_code += f'\n/* Batch {i + 1} */\n@media{batch}\n\n'

    return rearranged_css_code.strip()

def generate_css_batches_prompt(css_code):
    prompt = f'CSS Code Batches:\n\n'

    batches = css_code.split('@media')

    for i, batch in enumerate(batches):
        batch_number = i + 1
        prompt += f'Batch {batch_number}:\n```css\n{batch.strip()}\n```\n\n'
        prompt += f'Confirm the completion of Batch {batch_number} by typing "Completed {batch_number} of batch {batch_number}".\n\n'

    return prompt.strip()

def process_user_input(user_input):
    if 'completed' in user_input.lower():
        # Extracting batch number from user input
        completed_batch_number = int(user_input.split()[-2])
        return completed_batch_number

    return None

def main():
    with open('styles.css', 'r') as file:
        css_code = file.read()

    rearranged_css_code = rearrange_css_code(css_code)
    prompt = generate_css_batches_prompt(rearranged_css_code)

    # Counter variable to track the number of requests
    request_counter = 1

    # Make the initial API call
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )

    if 'choices' in response:
        # Access choices if available
        chat_response = response['choices'][0]['text'].strip()
    else:
        # Handle the case when choices are not available
        chat_response = response['text'].strip()

    print(chat_response)
    
    # Check if the maximum number of requests has been reached
    if max_requests == 1:
        print('Maximum number of requests reached. Writing the current progress to updated_styles.css.')
        with open('updated_styles.css', 'w') as updated_css_file:
            updated_css_file.write(rearranged_css_code)
    else:
        for _ in range(1, max_requests):
            # Enter the loop to make additional requests
            while request_counter < max_requests:

                # Increment the request counter
                request_counter += 1
                api_call_counter += 1  # Increment the API call counter

                # Pause for a specific duration between requests
                time.sleep(1)  # Sleep for 1 second

                # Check if the maximum number of requests has been reached
                if request_counter >= max_requests:
                    print('Maximum number of requests reached. Writing the current progress to updated_styles.css.')
                    with open('updated_styles.css', 'w') as updated_css_file:
                        updated_css_file.write(rearranged_css_code)
                    break

    # Print the number of API calls made
    print(f"Number of API calls made: {api_call_counter}")
    
if __name__ == '__main__':
    main()
