# 🌐 Gemini Translator App

A simple and elegant web application built with Python and Streamlit that uses Google's Gemini 1.5 Flash model to translate text from any language into English.

![Gemini Translator App: https://gemini-instructor-lk1612dzaxv3okurtbwfaa.streamlit.app/

---

##  Features

- **Simple Interface**: A clean and intuitive user interface powered by Streamlit.
- **Real-time Translation**: Get instant translations for your text.
- **Powered by Gemini**: Utilizes the speed and power of Google's `gemini-1.5-flash` model for accurate and fast results.
- **Easy to Set Up**: Get the application running locally in just a few steps.

---

##  Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8 or higher
- A Google AI API Key. You can get one from [Google AI Studio](https://aistudio.google.com/).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://your-repository-url/gemini-translator-app.git
    cd gemini-translator-app
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
    - Create a file named `.env` in the root of your project directory.
    - Add your Google AI API key to the `.env` file like this:
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

1.  Enter the text you wish to translate into the text box.
2.  Click the "Translate" button.
3.  The English translation will appear below.

---

## 🛠️ Technologies Used

- **Python**: The core programming language.
- **Streamlit**: For creating and running the web application.
- **Google Generative AI SDK**: To interact with the Gemini API.
- **python-dotenv**: To manage environment variables securely.

