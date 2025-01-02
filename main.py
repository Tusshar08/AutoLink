import streamlit as st
from few_shots import FewShotPosts
from post_generator import generate_post


# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish", "Hindi", "Assamese"]


# Main app layout
def main():
    st.subheader("AutoLink: AI-Generated LinkedIn Posts")

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Subject", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Post Length", options=length_options)

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Preferred Language", options=language_options)



    # Generate Button
    if st.button("Compose Post"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.write(post)


# Run the app
if __name__ == "__main__":
    main()