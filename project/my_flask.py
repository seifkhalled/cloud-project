from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configurations
db_config = {
    'host': 'db',
    'port': 3306,
    'user': 'root',
    'password': 'Messi2005!',
    'database': 'cloudproject'
}

def connect_to_database():
    """Establishes a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None


@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/inf.html')
def display_student_data_inf():
    """Render the page to display student data."""
    conn = connect_to_database()
    if not conn:
        return render_template('error.html', message="Could not connect to the database.")
    else:
        cursor = conn.cursor()
        try:
            # Execute the query to fetch student data
            cursor.execute("SELECT student_id, name, age, cgpa FROM team")
            student_data = cursor.fetchall()

            # Close the cursor and database connection
            cursor.close()
            conn.close()

            # Render the template with student data
            return render_template('inf.html', student_data=student_data)
        except mysql.connector.Error as e:
            return render_template('error.html', message="Error accessing the database.")

#@app.route('/student_data')
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000,host='0.0.0.0')

   