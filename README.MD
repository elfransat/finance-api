# Finance API Built with FastAPI

A FastAPI application for processing loan applications, validating applicant information, and generating loan offers.

## Overview

This system processes loan applications by:

1. Collecting applicant personal and financial information
2. Validating application data against predefined criteria
3. Automatically rejecting invalid applications with specific reasons
4. Generating appropriate loan offers for valid applications
5. Managing the application status through its lifecycle

## Project Structure

```
app/
├── db/
│   ├── database.py         # Database connection and operations
│   └── models.py           # SQLModel data models
├── enums.py                # Enum definitions for application states
├── main.py                 # FastAPI application entry point
├── routes/
│   └── application_routes.py # API endpoints
├── services/
│   ├── application/
│   │   ├── application_service.py  # Main application logic
│   │   └── application_validator.py # Validation logic
│   └── bidding/
│       └── bidding_service.py  # Loan bidding logic
```

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip

### Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/finance-api.git
cd finance-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # if running unix based system
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following variables:
```
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=finance_api
```

5. Create the database:
```bash
createdb finance_api
```

## Running the Application

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

### API Documentation

After starting the server, access the Swagger UI documentation at:
- http://localhost:8000/docs

## API Endpoints

### Create Application
- **URL**: `/application/create`
- **Method**: `POST`
- **Request Body**: JSON object with applicant and application details

Example request:
```json
{
  "applicant": {
    "first_name": "John",
    "last_name": "Doe",
    "age": 35,
    "employment_status": "EMPLOYED",
    "address": "123 Main St",
    "postcode": "00100",
    "phone_number": "0501234567",
    "income": 45000,
    "ssn": "010190-123A"
  },
  "application": {
    "requested_amount": 15000,
    "requested_maturity": 24,
    "purpose": "EXPANSION"
  }
}
```

Note: Finnish SSN format is DDMMYY-XXXZ where:
- DDMMYY is the date of birth
- XXX is an individual number
- Z is a control character

Valid examples include:
- `010190-123A` (male, born on Jan 1, 1990)
- `010203-456B` (female, born on Jan 2, 2003)

### Get Application
- **URL**: `/application/{application_id}`
- **Method**: `GET`
- **Response**: Application details including status and any loan offer

## Business Rules

### Application Rejection Criteria

Applications are automatically rejected if any of the following conditions are met:
- Request amount less than 1000
- Invalid SSN format
- Maturity less than 6 months
- Unemployed applicant
- Applicant income less than 20000
- Applicant age under 18
- Loan purpose is to avoid bankruptcy

### Bidding Rules

Maximum loan offers are determined by:
- Default maximum: 50,000
- Reduced to 20,000 for loans with maturity less than 12 months
- Reduced to 10,000 for self-employed applicants
- Reduced to 10,000 for applicants with income less than 40,000