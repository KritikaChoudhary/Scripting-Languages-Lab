from flask import Flask,render_template,request
import re
import time

app=Flask(__name__)
app.debug=True

usn='[0-9][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        msg="Welcome to Student page"
        return render_template('index.html',msg=msg)
    elif request.method=='POST':
        if request.form['dob']=="" or request.form["usn"]=="" :
            msg="Empty fields are not allowed"
            return render_template('index.html',msg=msg)
        try:
            time.strptime(request.form['dob'],"%d/%m/%Y")
        except ValueError:
            msg="Enter valid DOB"
            return render_template('index.html',msg=msg)
        if re.match(usn,request.form["usn"])==0:
            msg="Enter valid USN"
            return render_template('index.html',msg=msg)
        if int(request.form["m1"])>100 or int(request.form["m2"])>100 or int(request.form["m3"])>100:
            msg="Marks must be between 0-100"
            return render_template('index.html',msg=msg)
        else:
            msg="Average marks scored:"+str((int(request.form["m1"])+int(request.form["m2"])+int(request.form["m3"]))/3);
            return render_template('index.html',msg=msg)

if __name__=='__main__':
    app.run()
