# Smart Space Itinerary Web App

This project is a Flask-based web application that provides users with a personalized space travel itinerary based on their responses to a quiz. The app helps users discover which planet—Jupiter, Mars, or Saturn—best matches their preferences for a space adventure.

## Features

- **Homepage:** Introduction to Infinite Horizons, a fictional space travel agency.
- **Quiz:** Users answer a series of questions about their preferences and interests in space travel.
- **Smart Recommendation:** Based on quiz answers, the app recommends the most suitable planet and displays a themed success page.
- **Planets Page:** Learn more about Jupiter, Mars, and Saturn, and navigate directly to their respective pages.
- **Database:** Stores quiz responses using SQLite via the CS50 SQL library.

## Project Structure

- `app.py` — Main Flask application and routing logic.
- `templates/` — HTML templates for layout, quiz, planets, and result pages.
- `static/` — Static files such as images (not included here, but referenced in templates).
- `questionnaire.db` — SQLite database for storing quiz responses.

## How It Works

1. Users visit the homepage and can start the quiz.
2. The quiz consists of several multiple-choice questions.
3. Upon submission, the app analyzes the answers and determines which planet best fits the user's preferences.
4. The user is shown a result page with information and imagery for their recommended destination.

## Getting Started

1. **Clone the repository and install dependencies:**
    ```sh
    pip install flask cs50
    ```

2. **Set up the database:**
    - Ensure `questionnaire.db` exists with the appropriate schema:
      ```sql
      CREATE TABLE questionnaire (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          Question1 INTEGER,
          Question2 INTEGER,
          Question3 INTEGER,
          Question4 INTEGER,
          Question5 INTEGER,
          Question6 INTEGER,
          Question7 INTEGER
      );
      ```

3. **Run the application:**
    ```sh
    flask run
    ```

4. **Open your browser and go to:**
    ```
    http://127.0.0.1:5000/
    ```

## Notes

- All HTML templates are in the `templates/` folder.
- Static images referenced in the templates should be placed in a `static/` directory.
- The quiz logic and planet recommendation are handled in [`app.py`](app.py).

## License

This project is for educational purposes.