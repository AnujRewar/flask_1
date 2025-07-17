#IMPORTING
from flask import Flask,render_template,request   #importing a library

#INTERACTION
web=Flask(__name__)
@web.route('/')
@web.route('/register',methods=['GET'])

#MAPPING
def homepage():                #defining a home function 
    return render_template('register.html')

@web.route("/confirmation",methods=["POST","GET"])

def register():
    if request.method=="POST":
        n=request.form.get('name')
        c=request.form.get('city')
        p=request.form.get('phone')
        return render_template('confirm.html',name=n,city=c,phone=p)
    return "Invalid request method"

#MAIN
if __name__=="__main__":     #for entring into main website
    web.run(debug=True)
    