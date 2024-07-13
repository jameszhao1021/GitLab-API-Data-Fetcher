# GitLab API Data Fetcher

This project is a Python script designed to fetch data from the GitLab API and store it in a PostgreSQL database. The script dynamically creates the database schema based on the structure of the JSON data returned by the GitLab API.

## Features

- Connects to the GitLab API using a private token.
- Fetches groups data from the GitLab instance.
- Dynamically creates a PostgreSQL database and table schema based on the fetched data.
- Inserts the fetched data into the PostgreSQL database. 
- Utilises SQLAlchemy for database operations and psycopg2 for database connection.  

## Prerequisites

- Python 3.x
- PostgreSQL database server
- GitLab account with a private token
- Python packages: sqlalchemy, psycopg2, argparse, gitlab 

## Installation

1. Clone the repository:
```
git clone https://github.com/jameszhao1021/GitLab-API-Data-Fetcher.git
cd gitlab-api-data-fetcher
```

2. Install the required Python packages:
```
pip install sqlalchemy psycopg2 argparse python-gitlab
```

## Usage

Run the script:
```
python assignment.py --api-key YOUR_GITLAB_PRIVATE_TOKEN --db-name DATABASE_NAME --db-user DB_USER --db-password DB_PASSWORD --db-host DB_HOST --db-port DB_PORT
```
Github Example:
```
python assignment.py --api-key 123456 --db-name assignment --db-user postgres --db-password password --db-host localhost --db-port 5432
```