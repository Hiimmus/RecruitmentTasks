## Requirements

- Python 3.x
- Django
- babel == 2.16.0
- python-decouple ==3.8
## Installation

1. Clone the repository:

   ```bash
   git clone <REPOSITORY_URL>
   cd RecruitmentTasks
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Activate the virtual environment:
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the main project directory and add your `SECRET_KEY`:

   ```plaintext
   SECRET_KEY='your_secret_key_here'
   ```

5. Running the Application

   To run the application, use the following command:

   ```bash
   python manage.py runserver
