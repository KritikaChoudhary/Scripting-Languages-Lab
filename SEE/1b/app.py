from flask import Flask,sessions,render_template,url_for,request,session

app=Flask(__name__)
app.secret_key='admin'

@app.route("/",methods=['GET','POST'])
def atm():
    try:
        bal=session["bal"]
        count=session["count"]
    except KeyError:
        bal=session["bal"]=800
        count=session["count"]=0
    if request.method=='GET':
        return render_template('index.html',balance=bal,msg="Enter amount to be withdrawn or deposited")
    elif request.method=='POST':
        if request.form['amt']=="":
            return render_template("index.html",balance=bal,msg="Amount has to be entered")
        elif int(request.form['amt'])<0:
            return render_template("index.html",balance=bal,msg="Negative amount not allowed")
        elif count>=5:
            return render_template("index.html",balance=bal,msg="Maximum transactions exceeded")
        if request.form["action"]=="Withdraw":
            if int(request.form["amt"])>=5000:
                return render_template("index.html",balance=bal,msg="Deduction of more than 5000 not allowed")
            elif int(request.form["amt"])>bal:
                return render_template("index.html",balance=bal,msg="Deducing more than the balance")
            else:
                bal-=int(request.form["amt"])
                session["bal"]=bal
                count+=1
                session["count"]=count
                return render_template('index.html',balance=bal,msg=request.form["amt"]+"deducted")
        elif request.form["action"]=="Deposit":
            bal+=int(request.form["amt"])
            session["bal"]=bal
            session["count"]=count
            count+=1
            return render_template('index.html',balance=bal,msg=request.form["amt"]+"deposited")

if __name__=="__main__":
    app.run(debug=True)
