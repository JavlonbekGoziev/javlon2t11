import psycopg2
import csv

db_host = "javlon2t.ct6ei6agkus4.ap-south-1.rds.amazonaws.com"
db_name = "db_javlonbek"
db_user = "postgres"
db_password = "postgres"

# Connect to the PostgreSQL database
conn = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_password)
cursor = conn.cursor()

# Function to import data from CSV
def import_movies_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            title, genre, year = row
            cursor.execute(
                "INSERT INTO movies (title, genre, year) VALUES (%s, %s, %s)",
                (title, genre, year)
            )
    conn.commit()
    print(f"Imported {cursor.rowcount} movies.")

# Call the function with the path to your CSV file
import_movies_from_csv('movies.csv')

# Close the connection
cursor.close()
conn.close()
