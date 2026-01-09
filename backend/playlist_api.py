from dotenv import load_dotenv
import json
import os
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from openai import OpenAI
import re
import unicodedata


# load the secret file and FastApi router
load_dotenv()
router = APIRouter()

api_key = os.getenv("HF_TOKEN")
  
if not api_key:
  raise ValueError("HF_TOKEN ENVIRONMENT VARIABLE IS MISSING")
  
client = OpenAI(
  base_url="https://router.huggingface.co/v1",
  api_key=api_key,
)

# this function will sanitize the genre input
def sanitize_genre(genre_value: str) -> str:
  # normalize unicode
  genre_value = unicodedata.normalize("NFC", genre_value)

  # remove scripts, collapse genre and aggresively truncate
  script_chars = r'[{}\[\]()<>"\'`\\|;:]'
  genre_value = re.sub(script_chars, '', genre_value)
  genre_value = re.sub(r'\s+', ' ', genre_value).strip()
  genre_value = genre_value[:50]

  print('Sanitized the genre input:', genre_value)  
  return genre_value

# handle the post request from the frontend
@router.post("/")
async def generate_playlist(request: Request):
  body = await request.json()

  raw_genre = body.get("genre")

  # Type check
  if not isinstance(raw_genre, str):
    return JSONResponse(status_code=400, content={"error": "GENRE MUST BE A STRING"})

  # implement the sanitization function
  safe_genre = sanitize_genre(raw_genre)
  if safe_genre != raw_genre:
    print('Scripts detected in the genre input', raw_genre)
    return JSONResponse(status_code=400, content={"error": f"There was something wrong with the input {raw_genre}"})

  safe_genre = safe_genre.strip()
  
  if not safe_genre:
    return JSONResponse(status_code=400, content={"error": "GENRE CANNOT BE EMPTY"})

  if len(safe_genre) > 50:
    return JSONResponse(status_code=400, content={"error": "GENRE TOO LONG (MAX 50 CHARS)"})

  # Allowed chars: letters, numbers, spaces, hyphens, apostrophes (basic sanitization)
  if not re.match(r"^[a-zA-Z0-9\s\-']+$", safe_genre):
    return JSONResponse(status_code=400, content={"error": "Invalid characters in genre"})


  # call to the hugging face ai model
  try:
    completion = client.chat.completions.create(
      model="deepseek-ai/DeepSeek-V3.2:novita",  # FIX: find valid :provider suffix
      messages=[
        {
          "role": "user",
          "content": f"""Respond EXCLUSIVELY with valid JSON. NO explanations, NO markdown, NO extra text before/after. Output ONLY:

          {{
            "songs": [
              {{"title": "Example Title", "artist": "Example Artist"}},
              {{"title": "Another", "artist": "Another"}}
              // 3 more for total 5
            ]
          }}
          Generate exactly 5 songs for the {safe_genre} genre."""
          }
      ],

      temperature=0, 
      max_tokens=512,
    )

    #hold the result from the model in this variable
    content = completion.choices[0].message.content.strip()

    # print the response from the ai model to the backend server just in case it add more text and we can't handle the output correclty at the frontend
    print("\n=== RAW MODEL OUTPUT START ===")
    print(repr(content))  # repr() shows escapes, newlines, exact bytes
    print("=== RAW MODEL OUTPUT END ===\n")

    # Basic parse/validation fallback if model hallucinated
    try:
      playlist = json.loads(content)
    except json.JSONDecodeError:
      raise ValueError("Model returned invalid JSON")

    #return the result from the ai model to the front end as a json object
    return JSONResponse(status_code=200, content=playlist)

  # handle the error if the call to the hugging face ai model did not succeed
  except Exception as err:
    print("Hugging Face API error:", str(err))
    return JSONResponse(
      status_code=500,
      content={"error": "Failed to generate playlist", "details": str(err)},
    )