from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from playlist_api import router as playlist_router
import os

app = FastAPI()

# CORS so frontend can make calls to the backend
app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:5173"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# mount the playlist router from the playlist_api
app.include_router(playlist_router, prefix="/api/playlist_api")

# Start the server (run with uvicorn)
if __name__ == "__main__":
  import uvicorn
  port = int(os.environ.get("PORT", 3000))
  uvicorn.run(app, host="0.0.0.0", port=port)
