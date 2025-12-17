from dotenv import load_dotenv
import json
import os
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from openai import OpenAI


# load the secret file and FastApi router
load_dotenv()
router = APIRouter()

# instantize the client and point to hugging face router
client = OpenAI(
  base_url="https://router.huggingface.co/v1",
  api_key=os.getenv("HF_TOKEN"),
)

# handle the post request from the frontend
@router.post("/")
async def generate_playlist(request: Request):
  body = await request.json()
  genre = body.get("genre")
  if not genre:
      return JSONResponse(status_code=400, content={"error": "Genre is required"})

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
          Generate exactly 5 songs for the {genre} genre."""
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