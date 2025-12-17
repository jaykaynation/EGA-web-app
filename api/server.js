import express from 'express';
import dotenv from 'dotenv';
import cors from 'cors';
import playlistRouter from './playlist_api.js'; // the POST handler

// load environ variables
dotenv.config();

const app = express();

//enable cors so frontend can request to backend
app.use(cors({
  origin: 'http://localhost:5173'
}));

// parse the JSON requests here
app.use(express.json());

// mount the playlist route here
app.use('/api/playlist_api', playlistRouter);

// start the server here
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
