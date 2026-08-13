# CloudX Service Tracker

A deliberately simple Flask CRUD project for learning and interviews.

## What it does

The application stores service requests.

Each record has:
- customer name
- service
- status
- created time

You can:
- Create a request
- Read all requests
- Update request status
- Delete a request

That gives you full CRUD behavior without unnecessary application complexity.

## Run

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open:

http://127.0.0.1:5000

## Current database

SQLite is used locally because it requires no separate database server.

Later in AWS we will replace SQLite with Amazon RDS PostgreSQL or MySQL while keeping the same application concept.

## Interview architecture later

Browser
-> ALB
-> Flask app on EC2
-> RDS

Supporting services:
- Secrets Manager for DB credentials
- KMS encryption
- CloudWatch logs and metrics
- Auto Scaling
- Multi-AZ
- Terraform
- CI/CD
