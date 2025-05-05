
# Full Web Application Deployment on AWS (EC2, RDS, S3)

## Overview

This project involves building and deploying a full web application using Amazon Web Services (AWS). The application integrates multiple AWS services, including EC2 for compute, RDS for database management, and S3 for static file hosting.

### Project Components:

1. **EC2 (Elastic Compute Cloud)**: Hosts the backend application (Flask) that interacts with the database.
2. **RDS (Relational Database Service)**: PostgreSQL database to store and manage data.
3. **S3 (Simple Storage Service)**: Hosts the static files (HTML, CSS, JS) of the front-end web application.

### Application Features:

* Simple web application allowing users to **add** and **delete** records in the database.
* The static files are served via an S3 bucket.
* The backend is powered by a Flask app, which communicates with a PostgreSQL database hosted on Amazon RDS.

---

## Prerequisites

Before starting, ensure you have the following:

1. **AWS Account**: You should have an active AWS account with access to EC2, RDS, and S3 services.
2. **Kaggle Dataset**: Download the dataset of your choice in CSV format from Kaggle.

   * Example: Movies dataset - `movies.csv`
3. **AWS CLI**: Ensure that the AWS CLI is installed and configured on your local machine for easy management of AWS resources.

---

## Project Setup

### 1. **Database Setup (RDS - PostgreSQL)**

#### Step 1: Create an RDS PostgreSQL instance

1. Go to the **AWS RDS Console** and launch a new PostgreSQL database instance.
2. Choose **PostgreSQL** as the database engine and follow the wizard to configure the instance.
3. Create a new database named `db_javlonbek` (replace `javlonbek` with your first name).
4. Note the **RDS endpoint** (e.g., `javlon2t11.ct6ei6agkus4.ap-south-1.rds.amazonaws.com`), **username**, and **password**.

#### Step 2: Import CSV Data into PostgreSQL

1. Use tools like **DBeaver** or **psql** to import the downloaded CSV data into the PostgreSQL database.
2. Create a table with the name format `tbl_javlonbek_movies` (replace `javlonbek` with your first name).
3. Ensure the table schema matches the CSV file structure (columns such as `id`, `title`, `genre`, etc.).

---

### 2. **S3 Static Hosting Setup**

#### Step 1: Create an S3 Bucket

1. Go to the **S3 Console** and create a new bucket.
2. Enable **static website hosting** in the bucket settings.
3. Upload your HTML, CSS, and JS files to the S3 bucket.

   * The main HTML file should be named: `index_javlonbek.html` (replace `javlonbek` with your first name).

#### Step 2: Set Permissions

1. Set the bucket policy to make the website publicly accessible.
2. Example bucket policy for public access:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicReadGetObject",
         "Effect": "Allow",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::javlon2t11/*"
       }
     ]
   }
   ```

#### Step 3: Test Static Website

* Access the website via the provided S3 bucket URL (e.g., `http://<javlon2t11.s3-website-ap-south-1.amazonaws.com`).

---

### 3. **EC2 Deployment**

#### Step 1: Launch EC2 Instance

1. Go to the **EC2 Console** and launch a new **Ubuntu EC2 instance**.
2. Attach the **javlon2t11.pem** private key to access the EC2 instance via SSH.
3. Configure security groups to allow inbound traffic on port 80 (HTTP) and port 5000 (if using Flask's default port).

#### Step 2: SSH Access to EC2

1. SSH into the EC2 instance using the following command:

   ```bash
   ssh -i "javlon2t11.pem" ubuntu@javlon2t11.ct6ei6agkus4.ap-south-1.compute.amazonaws.com
   ```

#### Step 3: Install Dependencies

1. Update packages and install necessary dependencies:

   ```bash
   sudo apt update
   sudo apt install python3-pip python3-dev libpq-dev git
   sudo pip3 install flask psycopg2
   ```

#### Step 4: Set Up Flask Backend Application

1. Clone the GitHub repository into the EC2 instance:

   ```bash
   git clone https://github.com/JavlonbekGoziyev/javlon2t11.git
   cd javlon2t11
   ```

2. Configure the **Flask application** (`app.py`) to connect to your RDS PostgreSQL database:

   ```python
   conn = psycopg2.connect(
       host="javlon2t11.ct6ei6agkus4.ap-south-1.rds.amazonaws.com",
       database="db_javlonbek",
       user="postgres",
       password="postgres"
   )
   ```

3. Run the Flask application:

   ```bash
   python3 app.py
   ```

   The app should now be running on the EC2 instance, accessible via `http://<MY-IP, secret>:5000`.

---

### 4. **Frontend (HTML, CSS, JS)**

#### Step 1: Design the Frontend

1. Create a simple frontend with **Add** and **Delete** buttons.
2. The buttons should interact with the backend (Flask) to add and delete data in the PostgreSQL database.

#### Step 2: Upload to S3

1. Upload the static files (HTML, CSS, JS) to the S3 bucket you created earlier.

---

## How to Run the Application

### Local Setup:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/JavlonbekGoziyev/javlon2t11.git
   cd javlon2t11
   ```

2. Install Python dependencies:

   ```bash
   pip install flask psycopg2
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```

4. Open the browser and navigate to `http://localhost:5000`.

### AWS Setup:

1. Access the EC2 instance using SSH.
2. Run the Flask app on the EC2 instance (`python3 app.py`).
3. Open the web application in a browser via `http://<EC2-MY, IP,>:5000`.

---

## Deployment Details

* **EC2 Instance:** The backend application is deployed on an EC2 Ubuntu instance.
* **RDS Database:** PostgreSQL database is hosted on Amazon RDS and connected to the Flask application.
* **S3 Bucket:** Static files (HTML, CSS, JS) are hosted on S3 and served as the frontend.

---

## Links to Deployed Resources

* **S3 Bucket for Static Hosting**: [Link to S3 static website](http://javlon2t11.s3-website-ap-south-1.amazonaws.com)
* **EC2 Application**: [Link to EC2 web app](http://<EC2-IP>:5000)
* **RDS Database**: (Only accessible from EC2 instance)

---

## Tasks to Modify the Web Application

### 1. Change the Name of the Table in the Database.

### 2. Change the Database Name in the RDS Instance.

### 3. Drop a Table from the Database.

### 4. Remove a Column from a Table.

### 5. Update the Web Application to Reflect These Changes.

These tasks will require you to update the database schema and modify the web application to accommodate the changes.

---

## Conclusion

This project demonstrates how to build and deploy a full web application using AWS services like EC2, RDS, and S3. The application allows adding and deleting data from a PostgreSQL database, with static content served via S3 and the backend hosted on EC2.
