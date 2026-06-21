# Python & SQLite Integration Pipeline

## Overview
This project demonstrates a lightweight, production-ready database integration using Python and SQLite. It automates the creation of a local database, sets up a structured `Employees` table, and handles secure data insertion and management using native SQL commands.

## Features
* **Automated Database Provisioning:** Automatically initializes a local database file (`company_data.db`) if it does not exist.
* **SQL Automation:** Executes relational database operations including `CREATE TABLE`, `DELETE`, and parameterized `INSERT INTO` queries through Python's `sqlite3` module.
* **Data Integrity & Security:** Utilizes parameterized queries (`executemany`) to prevent SQL injection and ensures safe termination of database connections.

## Tech Stack
* **Language:** Python 3.x
* **Database:** SQLite3 (Built-in standard library)

## How to Run
1. Clone the repository.
2. Run the `main.py` script.
3. The local database `company_data.db` will be generated with populated records.
