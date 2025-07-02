from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Dummy data
students = [
    {'id': 1, 'roll_no': '003', 'name': 'PRAGATHISH RAJ T'},
    {'id': 2, 'roll_no': '004', 'name': 'PRADEESH P'},
    {'id': 3, 'roll_no': '005', 'name': 'DANANJAN J'},
    {'id': 4, 'roll_no': '007', 'name': 'DHANYA S'},
    {'id': 5, 'roll_no': '008', 'name': 'SHUNMUGAPRIYAN A'},
    {'id': 6, 'roll_no': '009', 'name': 'VISHAL V'},
    {'id': 7, 'roll_no': '010', 'name': 'MEENA KAVIN B'},
    {'id': 8, 'roll_no': '011', 'name': 'SANTHI K'},
    {'id': 9, 'roll_no': '014', 'name': 'NAVEEN KUMAR K M'},
    {'id': 10, 'roll_no': '017', 'name': 'SHIVA SHREE R'},
    {'id': 11, 'roll_no': '019', 'name': 'DENISHA ANTONY RAMYAA A'},
    {'id': 12, 'roll_no': '024', 'name': 'KRISHNAKUMAR N'},
    {'id': 13, 'roll_no': '025', 'name': 'RAMASAMY D'},
    {'id': 14, 'roll_no': '027', 'name': 'MANI BHARATHI S'},
    {'id': 15, 'roll_no': '028', 'name': 'SONIYA S'},
    {'id': 16, 'roll_no': '032', 'name': 'NANDHINI K'},
    {'id': 17, 'roll_no': '033', 'name': 'RAJA SRI VARSHA R'},
    {'id': 18, 'roll_no': '035', 'name': 'RAMYA R'},
    {'id': 19, 'roll_no': '036', 'name': 'DIVYABHARATHI T'},
    {'id': 20, 'roll_no': '039', 'name': 'PRAJIT B'},
    {'id': 21, 'roll_no': '040', 'name': 'VIJAY KUMAR G'},
    {'id': 22, 'roll_no': '041', 'name': 'ANNAMALAI K'},
    {'id': 23, 'roll_no': '042', 'name': 'FAZIL IQBAL T'},
    {'id': 24, 'roll_no': '048', 'name': 'AKILANDESWARI A'},
    {'id': 25, 'roll_no': '053', 'name': 'ANUSUYA DEVI R'},
    {'id': 26, 'roll_no': '054', 'name': 'KEERTHIGA N'},
    {'id': 27, 'roll_no': '056', 'name': 'GEETHADEVI S'},
    {'id': 28, 'roll_no': '060', 'name': 'ARUNA S'},
    {'id': 29, 'roll_no': '061', 'name': 'VISHWAA T'},
    {'id': 30, 'roll_no': '062', 'name': 'ROHAN A'},
    {'id': 31, 'roll_no': '065', 'name': 'PANDI S'}, 
    {'id': 32, 'roll_no': '069', 'name': 'SRIDHAR S'},
    {'id': 33, 'roll_no': '070', 'name': 'VIGNESHWARAN P'},
    {'id': 34, 'roll_no': '072', 'name': 'SHUNMUGAPRIYA E'},
    {'id': 35, 'roll_no': '074', 'name': 'JEGATHEESH A'},
    {'id': 36, 'roll_no': '075', 'name': 'ALAGU ISHWARYA K'},
    {'id': 37, 'roll_no': '076', 'name': 'SUBHASRI A'},
    {'id': 38, 'roll_no': '079', 'name': 'SRINIDHI V'},
    {'id': 39, 'roll_no': '080', 'name': 'SATHISHKUMAR K'},
    {'id': 40, 'roll_no': '087', 'name': 'IRZANA BARVEEN S'},
    {'id': 41, 'roll_no': '089', 'name': 'DHARUN R'},
    {'id': 42, 'roll_no': '090', 'name': 'NIRUBA D'},
    {'id': 43, 'roll_no': '091', 'name': 'NEHA SHREE M'},
    {'id': 44, 'roll_no': '092', 'name': 'DHARANI R'},
    {'id': 45, 'roll_no': '093', 'name': 'MADHUMITHA S'},
    {'id': 46, 'roll_no': '095', 'name': 'SWETHA B'},
    {'id': 47, 'roll_no': '097', 'name': 'ZAKIYA HASEENA M'},
    {'id': 48, 'roll_no': '098', 'name': 'SRI PRIYADHARSHAN T'},
    {'id': 49, 'roll_no': '099', 'name': 'GUNA NANDHINI S'},
    {'id': 50, 'roll_no': '100', 'name': 'ARCHANA M'},
    {'id': 51, 'roll_no': '105', 'name': 'LOKESH KUMAR S'},
    {'id': 52, 'roll_no': '109', 'name': 'NAVEENA S'},
    {'id': 53, 'roll_no': '110', 'name': 'SACHIN A'},
    {'id': 54, 'roll_no': '111', 'name': 'SIVAGURU M'},
    {'id': 55, 'roll_no': '112', 'name': 'VRIJIN STEFFI A'},
    {'id': 56, 'roll_no': '113', 'name': 'PRAGADHEESHWARAN M'},
    {'id': 57, 'roll_no': '116', 'name': 'MANOJ KUMAR S'},
    {'id': 58, 'roll_no': '119', 'name': 'KARTHICK BABU'},
    {'id': 59, 'roll_no': '120', 'name': 'OMMUNEES S'},
    {'id': 60, 'roll_no': '121', 'name': 'THASLIMA BEGAM'}
]



# In-memory attendance records by date
attendance_records = {}  # key = date, value = list of attendance data

@app.route('/mark_attendance', methods=['GET'])
def mark_attendance():
    return render_template('mark_attendance.html', students=students)

@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    date = request.form.get('date')
    submitted_data = []

    for student in students:
        status = request.form.get(f'status_{student["id"]}')
        submitted_data.append({
            'name': student['name'],
            'roll_no': student['roll_no'],
            'status': status
        })

    # Store attendance by date
    attendance_records[date] = submitted_data

    return redirect(url_for('view_attendance_summary', date=date))

@app.route('/attendance_summary/<date>')
def view_attendance_summary(date):
    records = attendance_records.get(date)
    if not records:
        return f"No attendance record found for {date}", 404
    return render_template('attendance_summary.html', date=date, records=records)

@app.route('/attendance_history')
def attendance_history():
    dates = sorted(attendance_records.keys(), reverse=True)  # newest first
    return render_template('attendance_history.html', dates=dates)

if __name__ == '__main__':
    app.run(debug=True)
