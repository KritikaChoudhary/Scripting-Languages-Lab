from flask import Flask,session,request,render_template

app=Flask(__name__)

app.secret_key='session'

li=['onion','pot','tom']

amt=0

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        msg="The groceries aisle"
        return render_template('index.html',msg=msg)
    elif request.method=='POST':
        if request.form['onion']=="" or request.form['pot']=="" or request.form['tom']=="":
            msg="No field shall be left blank"
            return render_template('index.html',msg=msg)
        elif int(request.form['onion'])<0 or int(request.form['pot'])<0 or int(request.form['tom'])<0:
            msg="Negative quantities not allowed"
            return render_template('index.html',msg=msg)
        else:
            global amt
            for i in li:
                if i not in session:
                    session[i]=int(request.form[i])
                else:
                    session[i]+=int(request.form[i])
                price=[70,40,50]
                index=0
                for i in li:
                    amt+=int(request.form[i])*price[index]
                    index+=1
                msg="Amount:"+str(amt)
                return render_template('index.html',msg=msg)

if __name__=='__main__':
    app.run(debug=True)
