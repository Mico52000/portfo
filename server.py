from flask import Flask,render_template,send_file,request,redirect
import csv



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name=None):
    return render_template(page_name)

def write_to_csv(data):
    with open("database.csv",mode='a',newline="\n") as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_file = csv.writer(database,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email,subject,message])

@app.route("/submit_form",methods=['POST','GET'])
def submit_form():
    if request.method == "POST":
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "did not write to database"
    