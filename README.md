# CSS Code Batching Script

This script processes CSS code in batches using the OpenAI API. It splits the CSS code into batches based on the `@media` rule, sends the batches to the OpenAI API for processing, and re-arranges the completed batches. The script is written in Python.

## Prerequisites

Before running the script, ensure that you have the following:

- Python 3.x installed
- The required Python packages: `dotenv`, `openai`, and `time`
- An OpenAI API key

## Installation

1. Clone the repository

```
git clone https://github.com/dev-alt/gpt-rewriteCSS.git
```

2. Install the required Python packages:

```
pip install dotenv openai
```

3. Create a `.env` file in the root directory of the repository and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Place your CSS code in a file named `styles.css` in the root directory.

2. Run the script:

```
python script.py
```

3. The script will split the CSS code into batches, send them to the OpenAI API for processing, and re-arrange the completed batches.

4. If the maximum number of requests is set to 1 (default), the current progress will be written to `updated_styles.css`.

5. If the maximum number of requests is greater than 1, the script will make additional API requests with a rate limit of 1 request per second. After the specified number of requests, the current progress will be written to `updated_styles.css`.

6. The number of API calls made will be displayed at the end.

## Customization

- To change the maximum number of requests, modify the `max_requests` variable in the `script.py` file.

- To change the OpenAI engine, max tokens, or temperature for API requests, modify the corresponding parameters in the `openai.Completion.create` method in the `script.py` file.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The script utilizes the [OpenAI API](https://openai.com/) for natural language processing.

- The CSS code batching algorithm is inspired by the requirements of a specific use case.
