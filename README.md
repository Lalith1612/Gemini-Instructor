# Gemini Instructor

An AI-powered tutor application built with Python and Streamlit. It uses Google's Gemini 1.5 Flash model to provide clear and concise explanations of complex concepts.

![Professor Gemini App: https://gemini-translator-lk16125xg2ax8hnm62nalq.streamlit.app/

---

##  Features

-   **Expert Explanations**: Get clear, beginner-friendly explanations on any topic you want to learn.
-   **Interactive Learning**: Simply type in a concept and let the AI teach you.
-   **Powered by Gemini**: Leverages the advanced reasoning and language capabilities of Google's `gemini-1.5-flash` model.
-   **Easy to Set Up**: Get the application running on your local machine in just a few steps.

---

##  Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.8 or higher
-   A Google AI API Key. You can get one from [Google AI Studio](https://aistudio.google.com/).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://your-repository-url/professor-gemini-app.git
    cd professor-gemini-app
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required libraries:**
    Create a file named `requirements.txt` with the following content:
    ```
    streamlit
    google-generativeai
    python-dotenv
    ```
    Then, run the following command to install them:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    -   Create a file named `.env` in the root of your project directory.
    -   Add your Google AI API key to the `.env` file like this:
        ```
        GOOGLE_AI_API_KEY="your_actual_google_ai_api_key_here"
        ```

5.  **Run the application:**
    Open your terminal and run the following command:
    ```bash
    streamlit run app.py
    ```
    Your browser should open with the application running!

---

## Usage

1.  Enter the concept or topic you want to learn about into the text area.
2.  Click the "Teach Me!" button.
3.  The AI-generated explanation will appear below.

---

##  Technologies Used

-   **Python**: The core programming language.
-   **Streamlit**: For creating and running the web application.
-   **Google Generative AI SDK**: To interact with the Gemini API.
-   **python-dotenv**: To manage environment variables securely.
