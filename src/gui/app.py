import sys
import os

# Add the "src" directory to the Python path
current_dir = os.path.abspath(os.path.dirname(__file__))  # Path to src/gui
src_path = os.path.abspath(os.path.join(current_dir, ".."))  # Path to src
if src_path not in sys.path:
    sys.path.insert(0, src_path)

print("Updated Python Path:", sys.path)  # Debugging the path

import streamlit as st
from newsletter_gen.crew import NewsletterGenCrew


from dotenv import load_dotenv



class NewsletterGenUI:

    def load_html_template(self):
        with open("src/newsletter_gen/config/newsletter_template.html", "r") as file:
            html_template = file.read()

        return html_template

    def generate_newsletter(self, topic, personal_message):
        inputs = {
            "topic": topic,
            "personal_message": personal_message,
            "html_template": self.load_html_template(),
        }
        return NewsletterGenCrew().crew().kickoff(inputs=inputs)

    def newsletter_generation(self):
        if st.session_state.generating:
            # Generate the newsletter
            crew_output = self.generate_newsletter(
                st.session_state.topic, st.session_state.personal_message
            )

            # Ensure it's in the right format (e.g., extract the HTML or serialize it)
            if hasattr(crew_output, "content"):  # Assuming 'content' has the HTML
                st.session_state.newsletter = crew_output.content
            else:
                st.session_state.newsletter = str(crew_output)  # Fallback

        # Display the download button if we have a newsletter
        if st.session_state.newsletter and st.session_state.newsletter != "":
            with st.container():
                st.write("Newsletter generated successfully!")
                st.download_button(
                    label="Download HTML file",
                    data=st.session_state.newsletter,  # Ensure this is str or bytes
                    file_name="newsletter.html",
                    mime="text/html",
                )
            st.session_state.generating = False


    def sidebar(self):
        with st.sidebar:
            st.title("Newsletter Generator")

            st.write(
                """
                To generate a newsletter, enter a topic and a personal message. \n
                Your team of AI agents will generate a newsletter for you!
                """
            )

            st.text_input("Topic", key="topic", placeholder="USA Stock Market")

            st.text_area(
                "Your personal message (to include at the top of the newsletter)",
                key="personal_message",
                placeholder="Dear readers, welcome to the newsletter!",
            )

            if st.button("Generate Newsletter"):
                st.session_state.generating = True

    def render(self):
        st.set_page_config(page_title="Newsletter Generation", page_icon="📧")

        if "topic" not in st.session_state:
            st.session_state.topic = ""

        if "personal_message" not in st.session_state:
            st.session_state.personal_message = ""

        if "newsletter" not in st.session_state:
            st.session_state.newsletter = ""

        if "generating" not in st.session_state:
            st.session_state.generating = False

        self.sidebar()

        self.newsletter_generation()


if __name__ == "__main__":
    NewsletterGenUI().render()
