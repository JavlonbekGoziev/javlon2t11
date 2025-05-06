# Final Project: Full Web Application Deployment on AWS (EC2, RDS, S3)

## 📌 Project Overview

This project is a full-stack web application deployed on Amazon Web Services. It uses:

* **Amazon EC2**: to host the backend application
* **Amazon RDS (PostgreSQL)**: to manage and store data
* **Amazon S3**: to host static frontend files

---

## 🧱 Components

### 1. PostgreSQL Database (RDS)

* **Dataset Source**: Downloaded from [Kaggle](https://www.kaggle.com/datasets)
* **Database name**: `db_javlonbek`
* **Table name**: `movies`
* **Imported Using**: `psql` / `DBeaver`
* The table structure matches the CSV schema from Kaggle

### 2. Static Frontend (S3)

* **S3 bucket**: Publicly accessible, configured for static website hosting
* **Main HTML file**: `index_javlonbek.html.html`
* Contains **Add** and **Delete** buttons
* Communicates with the backend via HTTP

### 3. Backend Server (EC2)

* Hosted on **Ubuntu EC2 instance**
* Built using **Flask (Python)**
* Communicates with **RDS PostgreSQL**
* Listens to HTTP requests to **Add/Delete** data from the database

---

## 🚀 Deployment Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JavlonbekGoziev/javlon2t11.git
cd movies
```

### 2. Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure `app.py`

Update DB credentials:

```python
host = "javlon2t.ct6ei6agkus4.ap-south-1.rds.amazonaws.com"
database = "db_javlonbek"
user = "postgres"
password = "postgres"
```

### 4. Run Backend on EC2

```bash
python app.py
```

Accessible at: `http://13.201.90.1:5000`

### 5. Upload Static Files to S3

* Upload `index_javlonbek.html.html`, `styles.css`, and JS files
* Set bucket to public
* Enable **Static Website Hosting**

Accessible at:
`[http://<your-bucket-name>.s3-website-<region>.amazonaws.com](http://javlonbek-bucket.s3-website-us-east-1.amazonaws.com
)`


## 🧪 Features

* ✅ Static homepage hosted on **S3**
* ✅ Connects to **RDS PostgreSQL**
* ✅ **Add/Delete** buttons modify DB content
* ✅ Data is stored permanently in RDS
* ✅ Accessible from public IP or S3 URL

---

## 📁 Project Structure

```
Movies/
├── app.py
├── requirements.txt
├── import_data.py
├── templates/
│   └── index_javlonbek.html.html
├── static/
│   ├── styles.css
│   └── script.js
└── README.md
```

---

## 🧪 Defense Tasks (Sample)

You will be asked to:

1. Rename the table
2. Change the DB name
3. Drop a table
4. Remove a column
5. Update the app to reflect changes

You must show your app continues to work after each task.

---

## 🔗 Deployed Links

* **Frontend (S3)**: [Click here](http://javlonbek-bucket.s3-website-us-east-1.amazonaws.com)
* **Backend (EC2 IP)**: `http://13.201.90.1:5000`
* **Database (RDS)**: Connected privately — shown during defense

---

## ✅ Completion Criteria

| Requirement                          | Status |
| ------------------------------------ | ------ |
| S3 Static Hosting                    | ✅      |
| PostgreSQL RDS Connection            | ✅      |
| EC2 Backend Deployment               | ✅      |
| Add/Delete Buttons Functioning       | ✅      |
| Code and Instructions in GitHub Repo | ✅      |

---

## 🧠 Notes

* Use your **first name** in all naming (e.g., `db_javlonbek`, `index_javlonbek.html.html`, etc.)
* Public access and proper security groups are configured
* RDS instance must allow EC2 connection

---

## 📬 Contact

Project by **Javlonbek**
Feel free to reach out via GitHub for any questions or improvements.

