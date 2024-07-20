# https://ai.google.dev/gemini-api/docs/models/gemini#gemini-1.5-flash
# gemini-1.5-flash
# Audio, images, video, and text
# Free:
# 15 RPM
# 1 million TPM
# 1,500 RPD

import os
# import pathlib
import textwrap
import google.generativeai as genai

# from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Write a story about a AI and magic")
response_to_markdown = to_markdown(response.text)

# print(response.text)
print(response_to_markdown)
