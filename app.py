from flask import Flask,render_template,request,redirect
from database import Patient,insert_pat,show_allpat,delete_pat,get_pat_byid,update_pat
app=Flask(__name__)




@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/appointment')
def index1():
    plist = show_allpat()
    return render_template('appointment.html',patlist=plist)



@app.route('/savepat',methods=['POST'])
def savepat():
    if request.method=='POST':
        # fetch data from form
        pid = int(request.form['pid'])
        pname = request.form['pname']
        age=int(request.form['age'])
        gender = request.form['gender']
        phone = request.form['phone']
        apptime = request.form['apptime']
        location = request.form['location']
        disease = request.form['disease']
        date = request.form['date']

        

        # create a object of form data
        pat = Patient(pid,pname,age,gender,phone,apptime,location,disease,date)  # here __init__ will called

        # save the Object into database54
        msg = insert_pat(pat)
        plist = show_allpat()
        print(msg)
        return render_template('appointment.html',message=msg,patlist=plist)

@app.route('/showpat')
def showpat():
    plist = show_allpat()
    return render_template('admin.html',patlist=plist)

@app.route('/deletepat/<int:pid>')
def deletepat(pid):
    delete_pat(pid)
    
    return redirect('/appointment') 

@app.route('/editpat/<int:pid>')
def editpat(pid):
    pat = get_pat_byid(pid)
    return render_template('updatepat.html',patient=pat)


@app.route('/updatepat',methods=['POST'])
def updatepat():
    if request.method=='POST':
        # fetch data from form
        pid = int(request.form['pid'])
        pname = request.form['pname']
        age=int(request.form['age'])
        gender = request.form['gender']
        phone = request.form['phone']
        apptime = request.form['apptime']
        location = request.form['location']
        disease = request.form['disease']
        date = request.form['date']

        

        # create a object of form data
        pat = Patient(pid,pname,age,gender,phone,apptime,location,disease,date)  # here __init__ will called


        update_pat(pat)
        return redirect('/appointment') 



if __name__=='__main__':
    app.run(debug=True)