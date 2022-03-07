#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("app.html")   #use html
@app.route('/info',methods=['POST'])
def abc():
    if(request.method=='POST'):
        u=request.form['a']
        v=request.form['b']
        total=int(u)+int(v)
        return render_template('app.html',total1=total)
if __name__=="__main__":
    app.run()


# In[ ]:




