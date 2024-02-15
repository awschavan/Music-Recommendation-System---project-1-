# Import necessary libraries
import streamlit as st
import pandas as pd

# Load dataset
data = pd.read_csv("spotify_dataset.csv")

# Function to recommend similar songs
def recommend_similar_songs(input_song):
    # Find the genre of the input song
    input_genre = data[data['song_name'] == input_song]['genre'].iloc[0]
    # Find songs with similar genres
    similar_songs = data[data['genre'] == input_genre][['song_name', 'genre', 'track_href']]
    # Shuffle the DataFrame and select a random sample of 100 songs
    similar_songs_sample = similar_songs.sample(n=100)  # Set random_state for reproducibility
    return similar_songs_sample

# Streamlit app
def main():
    st.title('Song Recommendation System')
    
    # Input field for song name
    song_name = st.text_input("Enter a song name:")
    
    if st.button("Recommend"):
        if song_name:
            # Recommendations
            recommendations = recommend_similar_songs(song_name)
            if not recommendations.empty:
                st.write("Top 100 recommended songs similar to", song_name, "with similar genre:")
                st.table(recommendations)
            else:
                st.write("Sorry, no recommendations found for", song_name)
        else:
            st.write("Please enter a song name.")

if __name__ == "__main__":
    main()