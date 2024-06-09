# BPUT Results API

This Flask application provides endpoints to retrieve student details, results, exam information, and SGPA from Biju Patnaik University of Technology (BPUT) results portal.

## Setup

### Prerequisites

- Python 3.6 or later
- Flask
- Requests library

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Arctixinc/BPUT-CheatCode
    cd BPUT-CheatCode
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Export the Flask app:
    ```sh
    export FLASK_APP=app.py  # On Windows use `set FLASK_APP=app.py`
    ```

2. Run the Flask development server:
    ```sh
    flask run
    ```

The application will be available at `http://localhost:5000`.

## API Endpoints

### 1. Get Student Details

**Endpoint:** `/details`  
**Method:** `GET`  
**Query Parameters:**
- `rollno` (required): The roll number of the student.

**Example:**
```sh
curl "http://localhost:5000/details?rollno=2201367065"
```

### 2. Get Results

**Endpoint:** `/results`  
**Method:** `GET`  
**Query Parameters:**
- `rollno` (required): The roll number of the student.
- `semid` (optional, default=`4`): The semester ID.
- `session` (optional, default=`E24`): The session code. Use `E24` for `Even (2023-24)` and `O24` for `Odd (2023-24)`.

**Example:**
```sh
curl "http://localhost:5000/results?rollno=2201367065&semid=4&session=E24"
```

### 3. Get Exam Information

**Endpoint:** `/examinfo`  
**Method:** `GET`  
**Query Parameters:**
- `rollno` (required): The roll number of the student.
- `dob` (optional, default=`2009-07-14`): The date of birth of the student.
- `session` (optional, default=`E24`): The session code. Use `E24` for `Even (2023-24)` and `O24` for `Odd (2023-24)`.

**Example:**
```sh
curl "http://localhost:5000/examinfo?rollno=2201367065&dob=2009-07-14&session=O24"
```

### 4. Get SGPA

**Endpoint:** `/sgpa`  
**Method:** `GET`  
**Query Parameters:**
- `rollno` (required): The roll number of the student.
- `semid` (optional, default=`4`): The semester ID.
- `session` (optional, default=`E24`): The session code. Use `E24` for `Even (2023-24)` and `O24` for `Odd (2023-24)`.

**Example:**
```sh
curl "http://localhost:5000/sgpa?rollno=2201367065&semid=4&session=E24"
```

## Session Codes

To handle the session parameter effectively, use the following codes:

- `E24` for `Even (2023-24)`
- `O24` for `Odd (2023-24)`

## Error Handling

If any error occurs during the request, the API will return a JSON response with an error message:
```json
{
  "error": "Failed to retrieve data: <error message>"
}
```
