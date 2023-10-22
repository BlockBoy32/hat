import streamlit as st
import openai

# Set up the API client
openai.api_key = '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'




def generate_hat_image(adjective):
    # Generate a random hat image based on the selected adjective
    response = openai.Image.create(
        prompt=f"a {adjective} hat",
        n=1,
        size="512x512"
    )
    
    # Get the image URL from the response
    image_url = response['data'][0]['url']
    
    return image_url

# Title
st.title("Random Hat Generator")

# List of adjective to create a variety of hats
adjectives = ["stylish", "vintage", "modern", "elegant", "colorful", "unique"]
# Randomly choose an adjective
selected_adjective = st.selectbox("Choose an adjective for the hat:", adjectives)

# Button to generate a random hat image
if st.button("Generate Hat"):
    image_url = generate_hat_image(selected_adjective)
    st.image(image_url)