# SEO Article Brief Generator

This project is an SEO Article Brief Generator designed to create comprehensive, SEO-optimized briefs for writers tasked with writing articles on specific keywords. The app supports user interactions, generates SEO briefs based on input, and allows for saving and updating conversations.

## Project Structure

- **app.py**: Main entry point of the application.
- **.env**: Environment variables file.
- **pages/**: Directory containing the main pages of the app.
  - **main_page.py**: The main page logic for generating SEO briefs.
  - **manage_conversations.py**: Logic for managing saved conversations.
- **utils/**: Utility functions and modules.
  - **db_utils.py**: Database utility functions.
  - **response_utils.py**: Utility functions related to generating responses and managing the session state.
- **requirements.txt**: Python dependencies.
- **README.md**: Project documentation.

## Getting Started

1. **Clone the repository**:
   ```sh
   git clone <repository_url>
   cd seo_app_v2
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up the environment variables**:
   - Create a .env file in the root directory and add your API key:
     ```
     ANTHROPIC_API_KEY=your_api_key_here
     ```

4. **Run the application**:
   ```sh
   streamlit run app.py
   ```

## Usage

- Navigate to the main page to generate SEO briefs.
- Use the conversation management page to view and delete saved conversations.

## License

This project is licensed under the MIT License.
