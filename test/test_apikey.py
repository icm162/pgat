import pip_system_certs.wrapt_requests

from google import genai

import sys    
import os
os.chdir("..")
sys.path.append(os.getcwd())
from utils import file_io_utils as fiu

with open(r".\api_key", "r", encoding="utf8") as reader: 
    api_key = reader.readline()

client = genai.Client(api_key=api_key)

# query = "Please briefly summarize the changes made to the code from the following diff:\n"
query = "请简短总结以下代码差异，并用数字编号排版:\n"

# url = "https://github.com/browser-use/browser-use/pull/845.diff"
# url = "https://github.com/browser-use/browser-use/pull/738.diff"
url = "https://github.com/browser-use/browser-use/pull/980.diff"

# diff_file = client.files.upload(file=r"C:\Users\ziyang.peng\Desktop\845.diff.txt")

diffs = fiu.get_remote_contents(url)
# diff_file = client.files.upload(file=fiu.get_remote_stream(url))
# diff_file = client.files.upload(file=ios, config=)

response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents=[query + diffs]
)

print(response.text)

