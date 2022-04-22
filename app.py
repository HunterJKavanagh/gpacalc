from ctypes import sizeof
from logging.config import valid_ident
from flask import Flask, render_template, request
app = Flask(__name__)

letter_grades = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0, '':0}

@app.route('/')
def gpa():
   return render_template('grades.html')

@app.route('/gpa',methods = ['POST', 'GET'])
def grades():
    if request.method == 'POST':
        result = request.form
        values = list(result.values())

        resultf = [("No.", "Grade", "Credits", "Points")]

        i, j = (0,0)
        point_total, credit_total = (0,0)
        while j <  len(values)/2:
            if values[i] != '':
                points = letter_grades[values[i]] * int(values[i+1])
                point_total += points
                credit_total += int(values[i+1])
                resultf.append((j + 1, values[i], values[i+1], points))
            else:
                resultf.append(('#', '', ' ', ' '))
            i += 2
            j += 1
        # end while

        resultf.append(("Total", " ", credit_total, point_total))
        resultf.append(("GPA", " ", " ", point_total/credit_total))

        return render_template("gpa.html",result = resultf)

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)