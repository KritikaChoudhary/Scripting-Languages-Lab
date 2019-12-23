from flask import Flask,render_template,url_for,request,session,redirect

app=Flask(__name__)
app.debug=True

app.secret_key='session'

li=['onion','potato','tomato']

@app.route('/',methods=['GET','POST'])
def shop():
    if request.method=='GET':
        return render_template("shop.html")
    elif request.method=='POST':
        for i in li:
            if i not in session:
                session[i]=int(request.form[i])
            else:
                session[i]+=int(request.form[i])
        return redirect(url_for('cart'))

@app.route('/cart',methods=['GET','POST'])
def cart():

    cart=[]
    index,amount=0,0
    price=[70,40,50]
    for i in li:
        each={}
        each["name"]=i.capitalize()
        each["qty"]=session[i]
        each["price"]=price[index]*session[i]
        amount+=each["price"]
        cart.append(each)
        index+=1
    return render_template('cart.html',cart=cart,amt=amount)

if __name__=='__main__':
    app.run()
