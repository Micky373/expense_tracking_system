# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server. It allows users to track, categorize, and manage their expenses efficiently.

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## Setup Instructions

Follow these steps to get the Expense Management System up and running on your local machine:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/yourusername/expense-management-system.git](https://github.com/yourusername/expense-management-system.git)
    cd expense-management-system
    ```

2.  **Create a `.env` file:**

    Navigate to the project root directory and create a `.env` file.

    ```bash
    touch .env
    ```

3.  **Inside the `.env` file insert the following, replacing the placeholders with your actual database credentials:**

    ```
    DATABASE_USER="Your username"
    DATABASE_PASSWORD="Your password"
    ```

    **Important:** Ensure you have a MySQL database set up and replace the placeholder values with your database details.

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    This command will install all the necessary Python libraries listed in the `requirements.txt` file for both the frontend and backend.

5.  **Run the FastAPI server:**

    Navigate to the `backend` directory and run the following command:

    ```bash
    cd backend
    uvicorn server:app --reload
    ```

    This will start the FastAPI backend server. The `--reload` flag enables automatic reloading of the server upon code changes, which is helpful during development. You'll typically see the server running on `http://127.0.0.1:8000`.

6.  **Run the Streamlit app:**

    Open a new terminal, navigate to the `frontend` directory, and run the following command:

    ```bash
    cd frontend
    streamlit run app.py
    ```

    This will launch the Streamlit frontend application in your web browser. You'll usually find it running on `http://localhost:8501`.

## Contributing

We welcome contributions to make this expense management system even better! If you have any ideas, bug fixes, or feature requests, please feel free to:

1.  Fork the repository.
2.  Create a new branch for your changes (`git checkout -b feature/your-feature` or `git checkout -b bugfix/your-fix`).
3.  Make your changes and commit them (`git commit -am 'Add some feature'`).
4.  Push to the branch (`git push origin feature/your-feature`).
5.  Open a pull request.

## Author

- GitHub: [@Micky](https://github.com/Micky373)

- LinkedIn: [Michael Tamirie](https://www.linkedin.com/in/michaeltamirie/)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/Micky373/spam_classifier/issues).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- Special thanks to [CodeBasics Team](https://codebasics.io/)