# Excelerate

Easily convert Excel and JSON files.

## Project Structure

- **Backend**: Django REST Framework
- **Frontend**: Vue.js

## Setup Instructions

### Backend

1. **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

### Frontend

1. **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2. **Install dependencies:**
    ```bash
    npm install
    ```

3. **Run the development server:**
    ```bash
    npm run serve
    ```

4. **Access the app:**
    Open [http://localhost:8080](http://localhost:8080) in your browser.

## Usage

1. **Convert Excel to JSON:**
    - Drag and drop an `.xlsx` file or click the "Choose a File" button.
    - Preview the content of the Excel file.
    - Click the download link to get the converted JSON file.

2. **Convert JSON to Excel:**
    - Drag and drop a `.json` file or click the "Choose a File" button.
    - Preview the content of the JSON file.
    - Click the download link to get the converted `.xlsx` file.

## Features

- **Drag and Drop:** Easily drag and drop files for conversion.
- **File Preview:** View a preview of your file before conversion.
- **Progress Bar:** Visual feedback during the conversion process.
- **Responsive UI:** User-friendly interface for seamless interaction.
- **Dual Conversion:** Support for both Excel to JSON and JSON to Excel conversions.

## Technologies Used

- **Backend**:
    - Django
    - Django REST Framework
    - pandas
    - openpyxl
    - django-cors-headers

- **Frontend**:
    - Vue.js 3
    - Axios
    - xlsx

## License

MIT
