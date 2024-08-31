## BackupMonitor

This is a simple Python application that retrieves backup status information from a MariaDB database and displays it in an easy-to-understand format.  

**Features:**

* **Get Backup Status:** The application fetches backup details based on the provided start and end dates. 
* **User Interface (HTML):** Utilizes Flask framework to render HTML templates for displaying results (a more interactive frontend could be added). 
* **SQL Queries:**  Provides an example of fetching data from a database using SQL queries.

**Installation:**

1. Make sure you have Python installed on your system.
2. Install the necessary packages: `pip install flask mariadb`
3. Create a Flask application using a basic setup
(for detailed guide, see [https://flask.palletsprojects.com/en/2.3.x/quickstart/]).

**How to Run:**

* Save the code as a Python file (e.g., `backup_tracker.py`)
* In your terminal, navigate to the folder where you saved the file. 
* Run the application using: `python backup_tracker.py` 


**Running on Development Server (Debug Mode):**

This project uses Flask's development server in debug mode, enabling hot reloading if changes are made to the code.

To start the server, run `python backup_tracker.py`.  The server will automatically be running and available at http://127.0.0.1:5000/ (replace this with your desired IP address or hostname). 



**Note:** 


* Ensure you have MariaDB database credentials (host, username, password) defined in the code.
* Modify `index()` function to include data fetching logic for specific jobs and their status, such as "success" or "failed", based on your requirements.

 **Github Repository Link:** https://gitlab.com/python515015/dr-backupmonitor.git

