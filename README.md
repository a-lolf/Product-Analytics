# Product Analytics Project (LargeDataset)

## Project Overview
This is a Django-based project designed to manage product data and provide analytics using the `/api/products/analytics/` endpoint. It includes features like:

1. Importing product data from a CSV file.
2. Caching and optimization for analytics queries.
3. Aggregation and filtering of product data.

---

## Features

- **Data Import**: Import product details (ID, name, category, price, stock, and creation date) from a CSV file.
- **Analytics API**: Provides aggregated statistics (e.g., average price, total stock) with optional filtering.
- **Caching**: Results are cached for 5 minutes for performance.
- **Indexing**: Database indexing for optimized query performance.

---

## Installation and Configuration

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- A database (default: SQLite)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/a-lolf/Product-Analytics.git
   cd Product-Analytics
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   Run migrations:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` to verify the project is running.

6. **Import Data**
   Use the management command to import the sample CSV data:
   ```bash
   python manage.py import_products <path_to_csv>
   ```

7. **Test the Analytics API**
   Use tools like Postman or `curl` to test the `/api/products/analytics/` endpoint.

   Example:
   ```bash
   curl --request GET --url 'http://127.0.0.1:8000/api/products/analytics/?category=electronics&max_price=8'
   ```

---

## Caching

- Results are cached for 5 minutes. This can be changed by the `TTL` variable defined in `views.py`
- Cache is invalidated when query parameters change.
