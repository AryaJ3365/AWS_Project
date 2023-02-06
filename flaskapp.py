from flask import Flask, render_template, request
 
app = Flask(__name__)  
 
@app.route('/', methods =["GET", "POST"])
def php_database():
    if request.method == "POST":

       first_name = request.form.get("fname")
       last_name = request.form.get("lname")
       email = request.form.get("email")

       return "User Information (First Name, Last Name, Email Address): "+ "(" + first_name + "," + last_name + ","  + email + ")"
    return render_template("index.html")
 
if __name__=='__main__':
   app.run()
