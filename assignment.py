import sqlalchemy as db
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import JSONB
import json
import psycopg2
import argparse
import gitlab

def create_database(database, user, password, host, port):
    postgres_conn = psycopg2.connect(
        dbname='postgres',
        user=user,
        password=password,
        host=host,
        port=port
    )
    postgres_conn.autocommit = True
    postgres_cursor = postgres_conn.cursor()
    try:
        postgres_cursor.execute(f'CREATE DATABASE {database}')
        print(f"Database '{database}' created successfully!")
    except psycopg2.Error as e:
        print(f"Error creating database: {e}")
    postgres_cursor.close()
    postgres_conn.close()

def fetch_data(api_key):
    gl = gitlab.Gitlab('https://gitlab.boon.com.au', private_token=api_key)  # Base URL for GitLab
    try:
        groups = gl.groups.list()
        return [group.attributes for group in groups]
    except gitlab.exceptions.GitlabGetError as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='GitLab API Data Fetcher')
    parser.add_argument('--api-key', type=str, required=True, help='Your GitLab Private Token')
    parser.add_argument('--db-name', type=str, default='assignment', help='Database name')
    parser.add_argument('--db-user', type=str, default='postgres', help='Database user')
    parser.add_argument('--db-password', type=str, default='password', help='Database password')
    parser.add_argument('--db-host', type=str, default='localhost', help='Database host')
    parser.add_argument('--db-port', type=str, default='5432', help='Database port')
    args = parser.parse_args()

    create_database(args.db_name, args.db_user, args.db_password, args.db_host, args.db_port)

    DATABASE_URL = f'postgresql+psycopg2://{args.db_user}:{args.db_password}@{args.db_host}:{args.db_port}/{args.db_name}'
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    # Fetch data from the API
    groups = fetch_data(args.api_key)
    if not groups:
        return

    # Define attributes for the Group class
    attributes = {
        '__tablename__': 'groups',
        'id': Column(Integer, primary_key=True)
    }

    # Dynamically add columns based on JSON keys
    for key, value in groups[0].items():
        if key == 'id':
            continue
        elif isinstance(value, bool):
            column = Column(Boolean)
        elif isinstance(value, int):
            column = Column(Integer)
        elif isinstance(value, str):
            column = Column(String)
        elif isinstance(value, dict):
            column = Column(JSONB)
        else:
            column = Column(Text)

        attributes[key] = column

    # Create the Group class with dynamic attributes
    Group = type('Group', (Base,), attributes)

    # Create the table
    Base.metadata.create_all(engine)

    # Insert data into the table dynamically
    for group_data in groups:
        for key, value in group_data.items():
            if isinstance(value, dict):
                group_data[key] = json.dumps(value)

        group_instance = Group()
        for key, value in group_data.items():
            setattr(group_instance, key, value)
        session.add(group_instance)

    session.commit()
    print("Data inserted successfully!")

if __name__ == '__main__':
    # Run the project with the following command in the terminal:
    # python assignment.py --api-key xeDpxei6UqEk5WUFSj85 --db-name assignment31 --db-user postgres --db-password password --db-host localhost --db-port 5432
    main()
