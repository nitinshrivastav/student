#!/usr/bin/env python
# coding: utf-8

# In[8]:


from flask import Flask,render_template,request
import smtplib
app=Flask(__name__)
@app.route("/")
def xyz():
    return render_template("registeration.html")
@app.route("/basicdetails",methods=['GET','POST'])
def hjfhjfhjf():
    if(request.method=='POST'):
        name=request.form['n1']
        email=request.form['e1']
        phone=request.form['p1']
        course=request.form['c1']
        
        
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login('intro.nitin@gmail.com','Nitinstudent@123')
        msg='Hello {0},\nthank you for register in xyz college\nour faculty will call you for the {1}course\nThank you '.format(name,course)
        server.sendmail("intro.nitin@gmail.com",email,msg)
        server.quit()
        
        return render_template("registeration.html")
if __name__=="__main__":
    app.run()

