
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def db():
    return sqlite3.connect("database.db")

@app.route("/")
def dashboard():
    con = db(); cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM students")
    total = cur.fetchone()[0]
    cur.execute("SELECT roll_number, name FROM students")
    students = cur.fetchall()
    con.close()
    return render_template("dashboard.html", total=total, students=students)

@app.route("/add_student", methods=["GET","POST"])
def add_student():
    if request.method=="POST":
        con=db();cur=con.cursor()
        cur.execute("INSERT INTO students VALUES (?,?)",
                    (request.form["roll"],request.form["name"]))
        con.commit();con.close()
        return redirect("/")
    return render_template("add_student.html")

@app.route("/add_grades", methods=["GET","POST"])
def add_grades():
    if request.method=="POST":
        g=int(request.form["grade"])
        if 0<=g<=100:
            con=db();cur=con.cursor()
            cur.execute("INSERT INTO grades VALUES (?,?,?)",
                        (request.form["roll"],request.form["subject"],g))
            con.commit();con.close()
        return redirect("/")
    return render_template("add_grades.html")

@app.route("/student/<roll>")
def student(roll):
    con=db();cur=con.cursor()
    cur.execute("SELECT name FROM students WHERE roll_number=?", (roll,))
    name=cur.fetchone()[0]
    cur.execute("SELECT subject,grade FROM grades WHERE roll_number=?", (roll,))
    grades=cur.fetchall()
    avg=round(sum(x[1] for x in grades)/len(grades),2) if grades else 0
    con.close()
    return render_template("student.html", name=name, grades=grades, avg=avg)

if __name__=="__main__":
    app.run(debug=True)
