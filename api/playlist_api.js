import express from 'express';
import { OpenAI } from "openai";


const router = express.Router();

router.post('/', async (req, res) => {
  const { genre } = req.body;   // get genre from frontend

  if (!genre) return res.status(400).json({ error: "Genre is required" });

  // use this try block to make the call to hugging face and process the response
  try {
    const client = new OpenAI({
	    baseURL: "https://router.huggingface.co/v1",
	    apiKey: process.env.hfApiKey,
    });

    const chatCompletion = await client.chat.completions.create({
	    model: "deepseek-ai/DeepSeek-V3.2:novita",
      messages: [
        {
        role: "user",
        content: `You are a playlist generator. Always respond with ONLY valid JSON in this exact format, no extra text, explanations, or markdown:

          {
            "songs": [
              {"title": "Song Title", "artist": "Artist Name"},
              ...
            ]
          }
            Generate exactly 5 songs for the ${genre} genre. Do not number them or add reasons.`,
        },
      ],
    });

    const playlist = chatCompletion.choices[0].message

    return res.status(200).json({ playlist });

  } catch (err) {
    console.error("Hugging Face API error:", err.response?.data || err.message);

    // send full details to frontend for debugging
    return res.status(500).json({
      error: "Failed to generate playlist",
      details: err.response?.data || err.message
    });
  }
});

export default router;