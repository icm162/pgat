from google import genai
import os

print(os.path.abspath(r".\api_key"))
with open(r"..\\api_key", "r", encoding="utf8") as reader: api_key = reader.readline()

print(api_key)

# client = genai.Client(api_key="AIzaSyD4WKyxKgdU-vJLPidKBe1pELP9rMMjeGQ")

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
# )

# print(response.text)

