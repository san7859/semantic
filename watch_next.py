import spacy

def watch_next(description):
    # Load the Spacy model
    nlp = spacy.load('en_core_web_md')

    # Load the movie descriptions from text file into a list
    with open("movies.txt", "r", encoding='utf-8') as file:
        # Read all lines in file & return them as a list of strings
        lines = file.readlines()
        # Create an empty list to store the movie names
        movies = []
        # Loop over each line in the list of lines
        for line in lines:
            movie_description = line.strip()
            # Append movie_description to the list of movies
            movies.append(movie_description)

    # Calculate the similarity scores between each movie and the watched_description
    # Assign empty list to variable 'similarity_scores'
    similarity_scores = []
    # Loop over each movie in the list of movies
    for movie in movies:
        # Calculate the similarity score between the movie description and the current movie using the spaCy model
        similarity_score = nlp(movie).similarity(nlp(description))
        # Append the similarity score to the list of similarity scores
        similarity_scores.append(similarity_score)

    # Find the index of the movie with the highest similarity score
    max_index = similarity_scores.index(max(similarity_scores))

    # Extract the name of the movie with the highest similarity score
    watch_next = movies[max_index].split(':')[0]

    return watch_next

# input description, in this case, Planet Hulk
watched_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

# call 'watch_next' function with 'watched_description' parameter & print recommended
# movie ahead of the text 'Recommendation For Next Movie To Watch:'
print("Recommendation For Next Movie To Watch: " + watch_next(watched_description))
