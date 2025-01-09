# ResumeProcessor

## Setup Instructions

1. Clone the repository:
    ```bash
    https://github.com/Arpreetkhare/Resume-Processor.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up PostgreSQL and configure `DATABASES` in `ResumeProcessor/settings.py`.

4. Create a `.env` file with your OpenAI API key:
    ```text
    OPENAI_API_KEY=your-openai-api-key
    ```

5. Run database migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the server:
    ```bash
    python manage.py runserver
    ```

