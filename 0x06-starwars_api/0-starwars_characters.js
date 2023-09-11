#!/usr/bin/node

const request = require('request-promise');

async function getCharacterNames (movieId) {
  try {
    // Fetch movie details from the API
    const movieResponse = await request(`https://swapi-api.hbtn.io/api/films/${movieId}`);
    const movie = JSON.parse(movieResponse);

    // Extract character URLs from the movie details
    const characterURLs = movie.characters;

    // Fetch character details and print names
    for (const characterURL of characterURLs) {
      const characterResponse = await request(characterURL);
      const character = JSON.parse(characterResponse);
      process.stdout.write(character.name + '\n');
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command-line argument.');
} else {
  getCharacterNames(movieId);
}
