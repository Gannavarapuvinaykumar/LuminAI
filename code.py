import streamlit as st
import cohere
from PIL import Image

# Set up the Cohere client
co = cohere.Client("9gvaFI6EOI4AMrWhkYGdI4QgYOK5rLS6lk2RRkLu")  # Replace with your actual Cohere API key

# Load the logo image from the local directory
logo_path = "C:/Users/ganna/Downloads/Telegram Desktop/logo.png"  # Change this to the path where your logo is stored
logo_image = Image.open(logo_path)

# Display the logo at the top of the app with a custom width
st.image(logo_image, width=150)  # Adjust the width as needed

# Title for the Streamlit app
st.title("LuminAI - AI Code Assistant")

# Custom CSS and JavaScript for styling and animations
st.markdown("""<style>/* Your existing CSS code */</style>""", unsafe_allow_html=True)

# Input prompt section with instructions
st.subheader("Problem Statement")
st.write("Describe the coding problem you want to solve, and the AI will generate code for it.")
prompt = st.text_area(
    "Problem Description:",
    placeholder="Example: Write a Python program to find prime numbers between a range."
)

# Parameter controls for Cohere generation
st.subheader("Model Parameters")
max_tokens = st.slider("Max Tokens", min_value=10, max_value=500, value=100, step=10)
temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)

# Button to generate code with ripple effect
if st.button("Generate Code", key="generate-btn"):
    with st.spinner("Generating code... Please wait."):
        try:
            # Generate code using the Cohere API
            response = co.generate(
                prompt=prompt,
                model="command-xlarge-nightly",
                max_tokens=max_tokens,
                temperature=temperature,
                k=0,
                p=0.1,
                frequency_penalty=0,
                presence_penalty=0,
                stop_sequences=["###"],
                return_likelihoods="NONE"
            )

            # Extract the generated code and remove unwanted data
            generated_code = response.generations[0].text.strip()

            # If the response contains unwanted data (like API call information or extra text),
            # make sure to clean it or adjust the API's settings accordingly.

            # Display the generated code in a collapsible section with fade-in animation
            if generated_code:
                with st.expander("View Generated Code"):
                    st.code(generated_code, language='python')  # Properly format the code
            else:
                st.error("No code generated. Please check your input and try again.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
