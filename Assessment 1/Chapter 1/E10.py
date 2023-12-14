# Create a dictionary for the film "Avengers: Endgame"
film = {
    "Title": "Avengers: Endgame",
    "Director": "Anthony and Joe Russo",
    "Year Released": 2019,
    "Genre": "Superhero",
    "Duration": "3h 2m"
}

# Display the film details using a loop
print("Film Details:")
for key, value in film.items():
    print(f"{key}: {value}")
