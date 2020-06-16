from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/save',methods = ['POST'])
def save():
    result = request.form
    import csv
    fields = [result['hal_id'], result['keyp1'], result['keyp2'], result['keyp3'], result['keyp4'], result['keyp5']]
    with open(r'data/web.csv', 'a') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(fields)
    unique = True
    if result['email'] != '':
        with open(r'data/contact.csv', 'r') as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                if row[0] == result['email']:
                    unique = False
        with open(r'data/contact.csv', 'a') as f:
            mail = [result['email']]
            writer = csv.writer(f, delimiter=";")
            if unique == True:
                writer.writerow(mail)
    return render_template("save.html")

app.run(debug=True)