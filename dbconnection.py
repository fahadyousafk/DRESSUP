import pymysql

def iud(qry,val):
    con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='dressup')
    cmd=con.cursor()
    cmd.execute(qry,val)
    id=cmd.lastrowid
    con.commit()
    cmd.close()
    con.close()
    return id

def selectone(qry,val):
    con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='dressup')
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchone()
    con.commit()
    cmd.close()
    con.close()
    return res

def selectone1(qry):
    con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='dressup')
    cmd=con.cursor()
    cmd.execute(qry)
    res=cmd.fetchone()
    con.commit()
    cmd.close()
    con.close()
    return res

def selectall(qry):
    con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='dressup')
    cmd=con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    con.commit()
    cmd.close()
    con.close()
    return res
def selectall1(qry,v):
    con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='dressup')
    cmd=con.cursor()
    cmd.execute(qry,v)
    res=cmd.fetchall()
    con.commit()
    cmd.close()
    con.close()
    return res
def selectallandroid(qry):
    con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='dressup')
    cmd=con.cursor()
    cmd.execute(qry)
    results=cmd.fetchall()
    json_data = []
    row_headers = [x[0] for x in cmd.description]
    for result in results:
        row = []
        for r in result:
            row.append(str(r))
        json_data.append(dict(zip(row_headers, row)))
    con.commit()
    print(json_data)
    return  json_data

def selectallandroid1(qry,v):
    con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='dressup')
    cmd=con.cursor()
    cmd.execute(qry,v)
    results=cmd.fetchall()
    json_data = []
    row_headers = [x[0] for x in cmd.description]
    for result in results:
        row = []
        for r in result:
            row.append(str(r))
        json_data.append(dict(zip(row_headers, row)))
    con.commit()
    print(json_data)
    return json_data