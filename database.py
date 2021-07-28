import pymysql as pm
class Patient:

    def __init__(self,pid=0,pname=None,age=0,gender=None,phone=0,apptime=None,location=None,disease=None,date=None):
        self.pid=pid
        self.pname=pname
        self.age=age
        self.gender=gender
        self.phone=phone
        self.apptime=apptime
        self.location=location
        self.disease=disease
        self.date=date
        
con=pm.connect(host='localhost',user='root',password='',db='hospital')

cursor=con.cursor()

def insert_pat(pat):
    try:
        sqlQuery = f"insert into hosp values ({pat.pid},'{pat.pname}',{pat.age},'{pat.gender}',{pat.phone},'{pat.apptime}','{pat.location}','{pat.disease}','{pat.date}')"
        print(sqlQuery)
        cursor.execute(sqlQuery)
        con.commit()
        return 'Appointment submitted'
    except Exception as e:
        print('Error:- ',e)
        return 'Appointment not submitted'

def show_allpat():
    try:
        patlist = []
        sqlQuery = f"select * from hosp"
        cursor.execute(sqlQuery)

        rows = cursor.fetchall()
        for row in rows:
            pat = Patient(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
            patlist.append(pat)
        else:
            return patlist
        con.commit()
    except Exception as e:
         print('Error:- ',e)

def delete_pat(pid):
    try:
        sqlQuery = f"delete from hosp where pid={pid}"
        cursor.execute(sqlQuery)
        con.commit()
        return 'Employee Deleted Successfully'
    except Exception as e:
        print('Error:- ',e)
        return 'Employee is not Delete'


def get_pat_byid(pid):
    try:
        sqlQuery = f"select *  from hosp where pid={pid}"
        cursor.execute(sqlQuery)
        row = cursor.fetchone()
        pat = Patient(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
        
        con.commit()
        return pat
    except Exception as e:
        print('Error:- ',e)
        return 
def update_pat(pat):
    try:
        sqlQuery = f"update hosp set pname='{pat.pname}', age={pat.age},gender='{pat.gender}',phone='{pat.phone}',apptime='{pat.apptime}',location='{pat.location}',disease='{pat.disease}',date='{pat.date}' where pid={pat.pid}"
        cursor.execute(sqlQuery)
        con.commit()
        return 'Updated Successfully..'
    except Exception as e:
        print('Error:- ',e)
        return 'Not Updated Successfully..'
