from flask import *
from werkzeug.utils import secure_filename
from dressup import *
from dbconnection import *



app=Flask(__name__)
@app.route('/model', methods=['GET', 'POST'])
def model():
        print(request.form)
        file1 = request.form['f']
        file1=file1.replace('\r\n','')
        file2 = request.files['files']
        fname = secure_filename(file2.filename)
        file2.save("static/"+fname)
        res=""
        # try:
        #     res=  head_mrh(fname,file1)
        #     print(res)
        # except:
        #     pass



        return jsonify({'task': "success","imageurl":res})
@app.route('/virtualy')
def virtualy():
    return jsonify()

@app.route("/signup",methods=['get','post'])
def signup():
    try:
        firstname=request.form['fname']
        lastname=request.form['lname']
        phonenumber=request.form['phnumber']
        place=request.form['place']
        post=request.form['post']
        email=request.form['email']
        username=request.form['uname']
        password=request.form['pass']

        q="insert into login values(null,%s,%s,%s)"
        val=(username,password,'user')
        res=iud(q,val)

        q2="insert into user values(null,%s,%s,%s,%s,%s,%s,%s)"
        val2=(firstname,lastname,phonenumber,place,post,email,str(res))
        iud(q2,val2)

        return jsonify({'result':"success"})
    except Exception as e:
        return jsonify({'result': "already exist"})


@app.route("/feedback",methods=['get','post'])
def feedback():
    uid=request.form['uid']
    feedback=request.form['feedback']

    q="insert into feedbacks values(null,%s,%s,curdate())"
    val=(uid,feedback)
    iud(q,val)
    return jsonify({'result': "success"})

@app.route("/complaints",methods=['get','post'])
def complaints():
    uid=request.form['uid']
    complaints=request.form['complaints']

    q="insert into complaints values(null,%s,%s,curdate(),%s)"
    val=(uid,complaints,'pending')
    iud(q,val)

    return jsonify({'result': "success"})

@app.route("/viewcomplaints",methods=['post'])
def viewcomplaints():
    lid=request.form['uid']
    q="select * from complaints where u_id=%s"
    val=(lid)
    res=selectallandroid1(q,val)
    print(res,"=======================")
    return jsonify(res)

@app.route('/login', methods=['get','post'])
def login():
    u_name = request.form['uname']
    password = request.form['password']

    qry = "Select * from login where USERNAME=%s AND PASSWORD=%s and u_type='user'"
    val=(u_name,password)

    result = selectone(qry,val)
    if result is None:
        return jsonify({'result': "invalid"})
    else:
        return jsonify({'result': "success",'lid':result[0]})

@app.route("/viewcloth",methods=['post'])
def viewcloth():
    q="select * from product where not quantity=0"
    res=selectallandroid(q)
    return jsonify(res)

@app.route("/viewnewdesigns",methods=['post'])
def viewnewdesigns():
    q="select *  from design where status='accepted'"
    res=selectallandroid(q)
    return jsonify(res)

@app.route("/viewcolor",methods=['post'])
def viewcolor():
    price=request.form['price']
    res1=price.split('-')
    first=res1[0]
    second=res1[1]
    color=request.form['color']
    q="select * from product where colour=%s and rate between %s and %s and quantity !=0"
    val=(color,first,second)
    res=selectallandroid1(q,val)
    return jsonify(res)

@app.route("/viewprice",methods=['post'])
def viewprice():
    startprice=request.form['startprice']
    endprice=request.form['endprice']
    q="select * from product where price between %s and %s"
    val=(startprice,endprice)
    res = selectallandroid1(q, val)
    return jsonify(res)

#######chat#########

@app.route("/viewchat",methods=['post'])
def viewchat():
    type=request.form['type']
    q="SELECT * FROM `employee` WHERE `TYPE`=%s"
    val=(type)
    res=selectallandroid1(q,val)
    return jsonify(res)

@app.route("/chatinsertion",methods=['post'])
def chatinsertion():
    fromid=request.form['fromid']
    toid=request.form['toid']
    msg=request.form['msg']

    q="insert into inetract values(null,%s,%s,%s,curdate(),%s)"
    val=(fromid,toid,msg,'user')
    iud(q,val)
    return jsonify({'result': "success"})
########

@app.route("/buyitem",methods=['post'])
def buyitem():
    pid=request.form['pid']
    bid=request.form['bid']
    # iid=request.form['iid']
    qty=request.form['qty']
    amount=request.form['amount']
    lid=request.form['lid']
    tot=int(qty)*int(amount)
    q="insert into bookitems values(null,%s,%s,%s,%s,%s)"
    val=(bid,pid,qty,amount,lid)
    iud(q,val)

    q1="update product set quantity=quantity-%s where p_id=%s"
    val2=(qty,pid)
    iud(q1,val2)
    # qry="insert into `book` values(%s,%s,curdate(),%s,'pending')"
    # v=(bid,lid,str(tot))
    # iud(qry,v)
    return jsonify({'result': "success"})

@app.route("/billid",methods=['post'])
def billid():
    q="select b_id from book"
    res=selectone1(q)
    if res is None:
        bill_id=1
        return jsonify({'result': bill_id})
    else:
        # qry="insert into book values(null,%s,%s,%s,%s)"
        q2="select max(b_id)+1 as bill_id1 from book"
        res1=selectone1(q2)
        return jsonify({'result': res1[0]})

@app.route("/bill" , methods=['post'])
def bill():
    uid = request.form['uid']
    bid=request.form['bid']
    q="SELECT SUM(`price`) FROM `bookitems` WHERE b_id=%s"
    v=(str(bid))
    res=selectone(q,v)
    q1="insert into book values(null,%s,curdate(),%s,%s)"
    val=(uid,str(res[0]),'pending')
    res1=iud(q1,val)
    print(res1,"=================")
    return jsonify({'result': "success"})

@app.route('/chat_user',methods=['GET','POST'])
def chat_user():
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='dressup')
    cmd = con.cursor()
    from_id=request.form['from_id']
    to_id=request.form['to_id']
    msg=request.form['msg']
    cmd.execute("INSERT INTO `interact` VALUES(NULL,'"+str(from_id)+"','"+str(to_id)+"','"+msg+"',curdate(),'user')")
    con.commit()
    return 'ok'

@app.route('/Viewchat',methods=['get','Post'])
def Viewchat():
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='dressup')
    cmd = con.cursor()
    uid = request.form['uid']
    print(uid,"=======")
    fid = request.form['fid']
    print(fid,"=====================")
    cmd.execute("SELECT * FROM `interact` WHERE (`FROM_ID`='" + str(uid) + "' AND `TO_ID`='" + str(fid) + "') OR (`FROM_ID`='" + str(fid) + "' AND `TO_ID`='" + str(uid) + "') ORDER BY DATE ASC")
    row_headers = [x[0] for x in cmd.description]
    s = cmd.fetchall()
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
        con.commit()
        print(json_data)
    return jsonify(json_data)





app.run(host='0.0.0.0',port='5000')



