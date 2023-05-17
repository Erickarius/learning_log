# Learning Log

This repository contains the source code for the Learning Log application. The Learning Log is a web-based journal that allows users to record and organize their learning progress. It is built using Python and Django.

## Website

The Learning Log website is accessible at [https://learning-log-by-eryk.herokuapp.com/](https://learning-log-by-eryk.herokuapp.com/). Visit the website to use the application and track your learning journey.

## Features

- User registration and authentication
- Create, read, update, and delete learning topics
- Add and manage entries for each topic
- Timestamped entries to track learning progress
- User-friendly interface for easy navigation

## Installation

To run the Learning Log application locally, follow these steps:

1. Clone the repository: `git clone https://github.com/Erickarius/learning_log.git`
2. Navigate to the project directory: `cd learning_log`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For macOS/Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Apply database migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

Open your web browser and go to [http://localhost:8000/](http://localhost:8000/) to access the Learning Log application locally.

## Contributing

Contributions to the Learning Log project are welcome. If you find a bug or have suggestions for improvement, please open an issue in the GitHub repository.
