
from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_proj():
    return render_template('index.html')

@app.route("/<string:page_path>")
def page(page_path):
    return render_template(page_path)

def write_to_file(data):
    with open('database.txt', mode="a") as database:
        email=data["email"],
        subject=data["subject"],
        message=data["message"]
        file=database.write(f'\n{email} {subject} {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email=data["email"],
        subject=data["subject"],
        message=data["message"]
        csv_writer=csv.writer(database2,  delimiter=',')
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data=request.form.to_dict()
        write_to_csv(data)
        print(data)
        return redirect("./thankyou.html")
    else:
        return "something went wrong"

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/work.html")
# def work():
#     return render_template('work.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/components.html")
# def component():
#     return render_template('components.html')