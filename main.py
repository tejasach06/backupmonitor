from flask import Flask, render_template, request
import mariadb
from datetime import date

db_ip_addr = "127.0.0.1"
db_user_id = "root"
db_password = "password"
db_name = "DR_backup"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # connect to mariadb database
    conn = mariadb.connect(
        host= db_ip_addr,
        user= db_user_id,
        password= db_password,
        database= db_name' 
    )
    # create cursor object
    cursor = conn.cursor()

    # Get Start date and end date from user
    start_date = request.form.get('start_date', date.today().strftime("%Y-%m-%d"))
    end_date = request.form.get('end_date', date.today().strftime("%Y-%m-%d"))

    # Execute a SQL query to fetch data
    query = '''SELECT j.job_name, jr.start_time, jr.end_time, jr.status FROM jobs j LEFT JOIN job_runs jr ON j.job_id = jr.job_id AND DATE(jr.start_time) = %s AND DATE(jr.end_time) = %s'''
    cursor.execute(query, (start_date, end_date))
    rows = cursor.fetchall()
    column_names = [c[0] for c in cursor.description]

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Pass the column names and rows to the template
    return render_template('index.html', column_names=column_names, rows=rows, start_date=start_date, end_date=end_date)

if __name__ == '__main__':
    app.run(debug=True)


