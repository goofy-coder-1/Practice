from flask import Flask, render_template_string, request, redirect, url_for
import csv
import os

from functions import fetch_student_brief, delete_student, update_student_detail
from register import StudentBase

app = Flask(__name__)
CSV_FILE = "student_base.csv"

# 1. NEW HOME PAGE TEMPLATE
HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Hostel Portal - Home</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background-color: #f4f4f9; }
        .container { background: white; padding: 40px; display: inline-block; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        p { color: #666; font-size: 18px; }
        .nav-btn { display: inline-block; padding: 12px 24px; background: #007BFF; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; margin-top: 20px; }
        .nav-btn:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Hostel Management System</h1>
        <p>Manage resident registrations, database records, and payment logs easily.</p>
        <a href="/dashboard" class="nav-btn">Enter Admin Dashboard &rarr;</a>
    </div>
</body>
</html>
"""

# 2. SEPARATE DASHBOARD TEMPLATE
DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Hostel Management Portal</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
        h1, h2 { color: #333; }
        .top-bar { display: flex; justify-content: space-between; align-items: center; }
        .back-btn { padding: 8px 16px; background: #6c757d; color: white; text-decoration: none; border-radius: 4px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; background: white; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #007BFF; color: white; }
        tr:hover { background-color: #f1f1f1; }
        .btn { padding: 6px 12px; color: white; background: #dc3545; border: none; cursor: pointer; border-radius: 4px; }
        .form-section { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        input { padding: 8px; margin: 5px 0; width: 200px; display: inline-block; }
    </style>
</head>
<body>

    <div class="top-bar">
        <h1>Hostel Student Dashboard</h1>
        <a href="/" class="back-btn">&larr; Back to Home</a>
    </div>
    
    <div class="form-section">
        <h2>Active Residents</h2>
        <table>
            <tr>
                <th>Name</th><th>Age</th><th>Address</th><th>Room</th><th>Level</th><th>Student ID</th><th>Actions</th>
            </tr>
            {% for row in students %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
                <td>{{ row[3] }}</td>
                <td>{{ row[4] }}</td>
                <td><strong>{{ row[5] }}</strong></td>
                <td>
                    <form action="/delete_student_web" method="POST" style="display:inline;">
                        <input type="hidden" name="student_id" value="{{ row[5] }}">
                        <input type="text" name="reason" placeholder="Reason to remove" required style="width:120px; padding:4px;">
                        <button type="submit" class="btn">Remove</button>
                    </form>
                </td>
            </tr>
            {% endfor %}
        </table>
    </div>

</body>
</html>
"""

# ROUTE 1: Dedicated Home Page Landing URL
@app.route('/')
def home():
    return render_template_string(HOME_HTML)

# ROUTE 2: Dedicated Student List/Dashboard URL
@app.route('/dashboard')
def dashboard():
    students = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            students = [row for row in reader if row]
            
    return render_template_string(DASHBOARD_HTML, students=students)

@app.route('/delete_student_web', methods=['POST'])
def delete_student_web():
    student_id = request.form['student_id']
    reason = request.form['reason']
    delete_student(student_id, reason)
    return redirect(url_for('dashboard')) # Redirects back

if __name__ == '__main__':
    app.run(debug=True, port=5000)