import os
from flask import *
from dressup import *
from dbconnection import *

from werkzeug.utils import secure_filename
from datetime import datetime


app=Flask(__name__)
app.secret_key="2342"
@app.route("/log")
def log():
    return render_template("admin page/LOGIN.html")
@app.route("/")
def start1():
    return render_template("index.html")
@app.route("/inn")
def inn():
    return render_template("admin page/indexadmin.html")
#ADMIN

@app.route("/addseller",methods=['get','post'])
def addseller():
    return render_template("admin page/ADDSELLERS.html")

@app.route('/addseller2', methods=['post'])
def addseller2():
    type = request.form['select']
    print(type)
    f_name = request.form['textfield']
    l_name = request.form['textfield2']
    place = request.form['textfield3']
    post = request.form['textfield4']
    pin = request.form['textfield5']
    e_mail = request.form['textfield6']
    ph_number = request.form['textfield7']
    u_name1=request.form['textfield8']
    password1=request.form['textfield9']
    q="insert into login values (null,%s,%s,%s)"
    vals=(u_name1,password1,type)

    res=iud(q,vals)
    print(res)
    q1="insert into employee values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    vals1=(f_name,l_name,place,post,pin,e_mail,ph_number,str(res),type)
    iud(q1,vals1)

    return ''' <script> alert("Signed in as Admin"); window.location="/adminhome"; </script> '''


@app.route('/login', methods=['post'])
def login():
    u_name = request.form['textfield']
    password = request.form['textfield2']

    qry = "Select * from login where USERNAME=%s AND PASSWORD=%s "
    val=(u_name,password)

    result = selectone(qry,val)

    if result is None:
        return ''' <script> alert("Invalid Login Details"); window.location="/" </script>'''
    elif result[3]=="admin":
        session['lid']=result[0]
        return ''' <script> alert("Signed in as Admin"); window.location="/adminhome"; </script> '''
    elif result[3]=="SELLERS":
        session['lid']=result[0]

        return ''' <script> alert("Signed in as seller"); window.location="/sellerhome"; </script> '''
    elif result[3]=="LOGISTICS":

        session['lid']=result[0]
        return ''' <script> alert("Signed in as logistic"); window.location="/logistichome"; </script> '''
    elif result[3]=="DESIGNERS":

        session['lid']=result[0]
        return ''' <script> alert("Signed in as designer"); window.location="/designerhome"; </script> '''
    else:
        '''<script>alert("invalid option");</script>'''


@app.route("/adminhome")
def adminhome():
    return render_template("admin page/ADMINHOME.html")

@app.route("/itemtransportemployee")
def itemtransportemployee():
    id=request.args.get('id')
    session['bid']=id
    qry="SELECT * FROM `employee` WHERE `TYPE`='LOGISTICS'"
    res=selectall(qry)
    return render_template("admin page/ITEMTRANSPORTEMPLOYEE.html", val=res)

@app.route("/buttonclick", methods=['get','post'])
def buttonclick():
    lid=request.form['select']
    id=session['bid']
    qry="INSERT INTO `assign` VALUES(null,%s,%s)"
    val=(id,lid)
    iud(qry,val)
    return ''' <script>alert("registration successfull"); window.location="/adminhome" </script>'''



@app.route("/quantitytable",methods=['get','post'])
def quantitytable():
    id=request.args.get('id')
    qry="SELECT `product`.`ITEM_NAME`,`bookitems`.* FROM `bookitems` JOIN product ON product.P_ID=`bookitems`.`I_ID` WHERE `bookitems`.`B_ID`='"+str(id)+"'"
    res=selectall(qry)
    return render_template("admin page/QUANTITYTABLE.html", val=res)

@app.route("/viewandreply",methods=['get','post'])
def viewandreply():
    id=request.args.get('id')
    session['cid']=id
    return render_template("admin page/VIEWANDREPLY.html")

@app.route("/viewcomplaintsandreply")
def viewcomplaintsandreply():
    if 'lid' in session:
        qry="SELECT `user`.`F_NAME`,`user`.`L_NAME`,`complaints`.`COMPLAINTS`,`complaints`.`DATE`,`complaints`.`C_ID` FROM `user` JOIN `complaints` ON `user`.`loginid`=`complaints`.`U_ID` WHERE `complaints`.`REPLY`='pending'"
        res=selectall(qry)
        print(res)
        return render_template("admin page/VIEWCOMPLAINTSREPLY.html", val=res)
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''

@app.route("/sendreply",methods=['get','post'])
def sendreply():
    cid=session['cid']
    reply=request.form['textarea']
    qry="UPDATE complaints set reply=%s where C_ID=%s"
    val=(reply,cid)
    iud(qry,val)
    return ''' <script>alert("reply send"); window.location="/viewcomplaintsandreply" </script>'''



@app.route("/viewemployees")
def viewemployees():
    if 'lid' in session:
        q2="select * from employee"
        res2=selectall(q2)
        print(res2)

        return render_template("admin page/VIEWEMPLOYEES.html",val2=res2)
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''


@app.route("/viewfeedback")
def viewfeedback():
    q3="SELECT `feedbacks`.*,`user`.`F_NAME`,`user`.`L_NAME` FROM `user` JOIN `feedbacks` ON `user`.`loginid`=`feedbacks`.`U_ID`"
    res3=selectall(q3)
    print(res3)
    return render_template("admin page/VIEWFEEDBACK.html", val=res3)

@app.route("/viewtransportproduct")
def viewtransportproduct():
    qry="SELECT `user`.`F_NAME`,`user`.`L_NAME`,`book`.`B_ID`,`book`.`DATE`,`book`.`TOTAL_AMOUNTT` FROM `user` JOIN `book` ON `user`.`loginid`=`book`.`U_ID` AND `book`.b_id NOT IN (SELECT `assign`.`b_id` FROM `assign`)"
    res=selectall(qry)
    print(res)
    return render_template("admin page/VIEWTRANSPORTPRODUCT.html", val=res )

@app.route("/viewassignedorders")
def viewassignedorders():
    qry="SELECT `user`.`F_NAME`,`user`.`L_NAME`,`book`.`B_ID`,`book`.`DATE`,`book`.`TOTAL_AMOUNTT`,`employee`.`FIRST_NAME`,`LAST_NAME` FROM `user` JOIN `book` ON `user`.`loginid`=`book`.`U_ID` AND `book`.b_id  JOIN  `assign` ON `assign`.`b_id`=`book`.`B_ID` JOIN `employee`ON `employee`.`L_ID`=`assign`.`logistic_id`"
    res=selectall(qry)

    return render_template("admin page/VIEWASSSIGNEDORDERS1.html",val=res)



#DESIGNER

@app.route("/inn1")
def inn1():
    return render_template("designer page/indexdesigner.html")



@app.route("/chatsellerpage")
def chatsellerpage():
    if 'lid' in session:
        qry = "select * from user"
        res = selectall(qry)
        return render_template("designer page/CHATSELLERPAGE.html", val=res)
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''

@app.route("/designerhome")
def designerhome():
    return render_template("designer page/DESIGNERHOME.html")

@app.route("/employeeeprofile")
def employeeprofile():
    if 'lid' in session:
        loginid=session['lid']
        qry="SELECT * FROM `employee` WHERE `employee`.`L_ID`=%s"
        val=str(loginid)
        res=selectone(qry,val)
        print(res)

        return render_template("designer page/EMPLOYEEPROFILE.html",val=res)
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''

@app.route("/managedeign")
def managedesign():
    if 'lid' in session:
        qry = "SELECT `design`.`DETAILS`,design,design_id FROM `design`"
        res = selectall(qry)
        return render_template("designer page/MANAGEDESIGN.html",val=res)
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''

@app.route("/variousdesigns")
def varuousdesigns():
    if 'lid' in session:
        return render_template("designer page/VARIOUSDESIGNS.html")
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''

@app.route("/updateemployee", methods=['post'])
def updateemployee():
    id=session['lid']
    first_name=request.form["textfield"]
    last_name=request.form["textfield2"]
    place=request.form["textfield3"]
    post=request.form["textfield4"]
    pin=request.form["textfield5"]
    email=request.form["textfield6"]
    ph_number=request.form["textfield7"]
    qry="UPDATE `employee` SET `FIRST_NAME`=%s,`LAST_NAME`=%s,`PLACE`=%s,`POST`=%s,`PIN`=%s,`EMAIL`=%s,`PHONE_NUMBER`=%s WHERE `L_ID`=%s"
    val=(first_name,last_name,place,post,pin,email,ph_number,str(id))
    iud(qry,val)
    return  '''<script>alert("employee profile updated");window.location="/designerhome"</script>'''

@app.route("/uploaddesigns",methods=['post'])
def uploaddesigns():
    details=request.form["textfield"]
    design=request.files["file"]
    file=secure_filename(design.filename)
    fn=datetime.now().strftime("%Y%m%d%H%M%S")+".png"
    design.save("static/design/"+fn)
    desid=session['lid']
    qry="INSERT INTO `design` VALUES(NULL,%s,%s,%s,curdate(),'pending')"
    val=(fn,desid,details)
    iud(qry,val)
    return '''<script>alert("upload successfull");window.location="/designerhome"</script>'''

@app.route("/deletedesigns")
def deletedesigns():
    id=request.args.get('id')
    qry="delete from design where design_id=%s"
    val=id
    iud(qry,val)
    return '''<script>alert("deleted design");window.location="/managedeign" </script>"'''

@app.route("/interaction",methods=['post'])
def interaction():
    type=request.form['select']
    if type=="CUSTOMER":
         qry="select * from user"
         res=selectall(qry)
         return render_template("designer page/CHATSELLERPAGE.html",val=res)
    else:
        qry = "select * from employee where type='sellers'"
        res = selectall(qry)
        return render_template("designer page/CHATSELLERPAGE.html", val=res)
@app.route("/seller1")
def seller1():
    if 'lid' in session:
        qry = "select * from employee where type='sellers'"
        res = selectall(qry)
        return render_template("designer page/CHATSELLERPAGE1.html", val=res)
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''

###############################chat



@app.route('/chat',methods=['GET','POST'])
def chat():
    uid=request.args.get('id')
    session['uidd']=uid
    qry="SELECT `F_NAME` FROM USER WHERE `LOGINID`=%s"
    val=(str(uid))
    s1=selectone(qry,val)
    fid=session['lid']
    session['idd'] = uid
    qry1="select * from interact where (from_id=%s and to_id=%s) or (from_id=%s and to_id=%s) order by date asc"
    val1=(str(uid),str(fid),str(fid),str(uid))
    s=selectall1(qry1,val1)
    return render_template('designer page/chat.html',data=s,fname=s1[0],fr=str(uid))

@app.route('/chat2',methods=['GET','POST'])
def chat2():
    uid = session['uidd']
    qry = "SELECT `F_NAME` FROM USER WHERE `LOGINID`=%s"
    val = (str(uid))
    s1 = selectone(qry, val)
    fid = session['lid']
    session['idd'] = uid
    qry1 = "select * from interact where (from_id=%s and to_id=%s) or (from_id=%s and to_id=%s) order by date asc"
    val1 = (str(uid), str(fid), str(fid), str(uid))
    s = selectall1(qry1, val1)
    return render_template('designer page/chat.html', data=s, fname=s1[0], fr=str(uid))
@app.route('/send',methods=['GET','POST'])
def send():
    btn=request.form['button']
    if (btn=="send"):
        fid=session["lid"]
        print(fid)
        tid=session['idd']
        session['uidd']=tid
        print(tid)
        msg=request.form['textarea']
        qry="insert into interact values(null,%s,%s,%s,curdate(),'designers')"
        val=(str(fid),str(tid),msg)
        iud(qry,val)
        return '''<script>window.location='/chat2'</script>'''
    else:
        return '''<script>window.location='/chat2'</script>'''




@app.route('/seller2',methods=['GET','POST'])
def seller2():
    uid=request.args.get('id')
    session['uidd']=uid
    qry="SELECT `FIRST_NAME` FROM EMPLOYEE WHERE `L_ID`=%s"
    val=(str(uid))
    s1=selectone(qry,val)
    fid=session['lid']
    session['idd'] = uid
    qry1="select * from interact where (from_id=%s and to_id=%s) or (from_id=%s and to_id=%s) order by date asc"
    val1=(str(uid),str(fid),str(fid),str(uid))
    s=selectall1(qry1,val1)
    return render_template('designer page/chatSELLER.html',data=s,fname=s1[0],fr=str(uid))

@app.route('/SELLER3',methods=['GET','POST'])
def SELLER3():
    uid = session['uidd']
    qry="SELECT `FIRST_NAME` FROM EMPLOYEE WHERE `L_ID`=%s"
    val = (str(uid))
    s1 = selectone(qry, val)
    fid = session['lid']
    session['idd'] = uid
    qry1 = "select * from interact where (from_id=%s and to_id=%s) or (from_id=%s and to_id=%s) order by date asc"
    val1 = (str(uid), str(fid), str(fid), str(uid))
    s = selectall1(qry1, val1)
    return render_template('designer page/chatSELLER.html', data=s, fname=s1[0], fr=str(uid))
@app.route('/senddesigner',methods=['GET','POST'])
def senddesigner():
    btn=request.form['button']
    if (btn=="send"):
        fid=session["lid"]
        print(fid)
        tid=session['idd']
        session['uidd']=tid
        print(tid)
        msg=request.form['textarea']
        qry="insert into interact values(null,%s,%s,%s,curdate(),'designers')"
        val=(str(fid),str(tid),msg)
        iud(qry,val)
        return '''<script>window.location='/SELLER3'</script>'''
    else:
        return '''<script>window.location='/SELLER3'</script>'''


#logistsic

@app.route("/inn2")
def inn2():
    return render_template("logistic page/indexlogistics.html")

@app.route("/logistichome")
def logistichome():
    return render_template("logistic page/LOGISTICHOME.html")

@app.route("/logistcprofile")
def logisticprofile():
    if 'lid' in session:
        loginid=session['lid']
        qry="SELECT * FROM `employee` WHERE L_ID=%s and type='LOGISTICS'"
        val=str(loginid)
        res=selectone(qry,val)
        print(res)
        return render_template("logistic page/LOGISTICPROFILE.html", val=res)
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''




@app.route("/logisticbuttonclick",methods=['post'])
def logisticbuttonclick():
    id = session['lid']
    first_name = request.form["textfield"]
    last_name = request.form["textfield2"]
    place = request.form["textfield3"]
    post = request.form["textfield4"]
    pin = request.form["textfield5"]
    email = request.form["textfield6"]
    ph_number = request.form["textfield7"]
    qry="UPDATE `employee` SET `FIRST_NAME`=%s,`LAST_NAME`=%s,`PLACE`=%s,`POST`=%s,`PIN`=%s,`EMAIL`=%s,`PHONE_NUMBER`=%s WHERE `L_ID`=%s AND `TYPE`='LOGISTICS'"
    val=(first_name,last_name,place,post,pin,email,ph_number,str(id))
    iud(qry,val)

    return '''<script>alert("profile updated");window.location="/logistichome"</script>'''




@app.route("/producttransport")
def producttransport():
    qry="SELECT `user`.`U_ID`,`user`.`F_NAME`,`user`.`L_NAME`,`user`.`PLACE`,`book`.`DATE`,`book`.`TOTAL_AMOUNTT` FROM USER JOIN book ON `user`.`loginid`=`book`.`U_ID` JOIN `assign` ON book.`B_ID`=`assign`.`b_id` WHERE `assign`.`logistic_id`=%s"
    val=(str(session['lid']))
    res=selectall1(qry,val)

    return render_template("logistic page/PRODUCTTRANSPORT.html", val=res)

@app.route("/logout")
def logout():
    session.clear()
    return render_template("admin page/LOGIN.html")



#seller

@app.route("/inn3")
def inn3():
    return render_template("seller page/indexseller.html")

@app.route("/addclothbutton")
def addclothbutton():
    if 'lid' in session:
        return render_template("seller page/ADDCLOTHBUTTON.html")
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''

@app.route("/approvedesign")
def approvedesign():
    if 'lid' in session:
        qry="SELECT `employee`.`FIRST_NAME`,`employee`.`LAST_NAME`,`design`.`DESIGN`,`design`.`DATE`,`design`.`DETAILS`,`design`.`DESIGN_ID` FROM `employee` JOIN `design` ON `employee`.`L_ID`=`design`.`STAFF_ID` WHERE `employee`.`TYPE`='DESIGNERS' AND `design`.`STATUS`='pending'"
        res=selectall(qry)
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''


    return render_template("seller page/APPROVEDESIGN.html", val=res)

@app.route("/feedbackseller")
def feedbackseller():
    qry="SELECT `feedbacks`.`U_ID`,`feedbacks`.`FEEDBACK`,`feedbacks`.`DATE`,`user`.`F_NAME`,`user`.`L_NAME` FROM `feedbacks` JOIN `user` ON `feedbacks`.`U_ID`=`user`.`loginid`"
    res=selectall(qry)

    return render_template("seller page/FEEDBACKSELLER.html",val=res)

@app.route("/sellerhome")
def sellerhome():
    return render_template("seller page/SELLERHOME.html")

@app.route("/updatedelete")
def updatedelete():
    return render_template("seller page/UPDATEDELETE.html")

@app.route("/updateimg")
def updateimg():
    return render_template("seller page/UPDATEIMG.html")

@app.route("/user")
def user():
    return render_template("seller page/USERS.html")

@app.route("/viewlogistics")
def viewlogistics():
    qry="SELECT  `E_ID`,`FIRST_NAME`,`LAST_NAME`,`PLACE` FROM `employee` WHERE `TYPE`='LOGISTICS'"
    res=selectall(qry)

    return render_template("seller page/VIEWLOGISTICS.html",val=res)

@app.route("/chatdesignerpage")
def chatdesignerpage():
        return render_template("seller page/CHATDESIGHNERPAGE.html")


@app.route("/addcloth", methods=['post'])
def addcloth():
    itemname=request.form["textfield"]
    price=request.form["textfield2"]
    image=request.files['file']
    img=secure_filename(image.filename)
    path=r"./static/cloths"
    image.save(os.path.join(path,img))
    color=request.form["textfield3"]
    quantity=request.form["textfield4"]
    qry="INSERT INTO `product` VALUES (NULL,%s,%s,%s,%s,%s,CURDATE())"
    val=(itemname,quantity,price,img,color)
    iud(qry,val)
    return '''<script>alert("cloth added successfully");window.location="/addclothbutton"</script>'''

@app.route("/acceptdesign")
def acceptdesign():
    id=request.args.get('id')
    qry="update design set status='accepted' where design_id=%s"
    val=(str(id))
    iud(qry,val)
    return '''<script>alert("design accepted");window.location="/approvedesign"</script>'''

@app.route("/rejectdesign")
def rejectdesign():
    id=request.args.get('id')
    qry="update design set status='rejected' where design_id=%s"
    val=(str(id))
    iud(qry,val)
    return '''<script>alert("design rejected");window.location="/approvedesign"</script>'''


#############
@app.route("/interaction1",methods=['post'])
def interaction1():
    type=request.form['select']
    if type=="CUSTOMER":
         qry="select * from user"
         res=selectall(qry)
         return render_template("seller page/CHATDESIGHNERPAGE.html",val=res)
    else:
        qry = "select * from employee where type='designers'"
        res = selectall(qry)
        return render_template("seller page/CHATDESIGHNERPAGE.html", val=res)


@app.route('/chatseller',methods=['GET','POST'])
def chatseller():
    uid=request.args.get('id')
    session['uidd']=uid
    qry="SELECT `FIRST_NAME` FROM employee WHERE `L_ID`=%s"
    val=(str(uid))
    s1=selectone(qry,val)
    fid=session['lid']
    session['idd'] = uid
    qry1="select * from interact where (from_id=%s and to_id=%s) or (from_id=%s and to_id=%s) order by date asc"
    val1=(str(uid),str(fid),str(fid),str(uid))
    s=selectall1(qry1,val1)
    return render_template('seller page/chat1.html',data=s,fname=s1[0],fr=str(uid))
######

@app.route('/chatseller2',methods=['GET','POST'])
def chatseller2():
    uid = session['uidd']
    qry = "SELECT `FIRST_NAME` FROM employee WHERE `L_ID`=%s"
    val = (str(uid))
    s1 = selectone(qry, val)
    fid = session['lid']
    session['idd'] = uid
    qry1 = "select * from interact where (from_id=%s and to_id=%s) or (from_id=%s and to_id=%s) order by date asc"
    val1 = (str(uid), str(fid), str(fid), str(uid))
    s = selectall1(qry1, val1)
    return render_template('seller page/chat1.html', data=s, fname=s1[0], fr=str(uid))
@app.route('/send1',methods=['GET','POST'])
def send1():
    btn=request.form['button']
    if (btn=="send"):
        fid=session["lid"]
        print(fid)
        tid=session['idd']
        session['uidd']=tid
        print(tid)
        msg=request.form['textarea']
        qry="insert into interact values(null,%s,%s,%s,curdate(),'seller')"
        val=(str(fid),str(tid),msg)
        iud(qry,val)
        return '''<script>window.location='/chatseller2'</script>'''
    else:
        return '''<script>window.location='/chatseller2'</script>'''

@app.route("/chatuser")
def chatuser():
    if 'lid' in session:
        qry = "select * from user"
        res = selectall(qry)
        return render_template("seller page/CHATUSERPAGE.html", val=res)
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''

@app.route("/chatdesigners")
def chatdesigners():
    if 'lid' in session:
        qry = "select * from employee where type='sellers'"
        res = selectall(qry)
        return render_template("seller page/CHATDESIGHNERPAGE.html", val=res)
    else:
        return ''' <script>alert("please login"); window.location="/" </script>'''

@app.route('/chatuser1',methods=['GET','POST'])
def chatuser1():
    uid=request.args.get('id')
    session['uidd']=uid
    qry="SELECT `F_NAME` FROM USER WHERE `LOGINID`=%s"
    val=(str(uid))
    s1=selectone(qry,val)
    fid=session['lid']
    session['idd'] = uid
    qry1="select * from interact where (from_id=%s and to_id=%s) or (from_id=%s and to_id=%s) order by date asc"
    val1=(str(uid),str(fid),str(fid),str(uid))
    s=selectall1(qry1,val1)
    return render_template('seller page/chat1.html',data=s,fname=s1[0],fr=str(uid))
######

@app.route('/chatuser2',methods=['GET','POST'])
def chatuser2():
    uid = session['uidd']
    qry="SELECT `F_NAME` FROM USER WHERE `LOGINID`=%s"
    val = (str(uid))
    s1 = selectone(qry, val)
    fid = session['lid']
    session['idd'] = uid
    qry1 = "select * from interact where (from_id=%s and to_id=%s) or (from_id=%s and to_id=%s) order by date asc"
    val1 = (str(uid), str(fid), str(fid), str(uid))
    s = selectall1(qry1, val1)
    return render_template('seller page/chat1.html', data=s, fname=s1[0], fr=str(uid))
@app.route('/senduser1',methods=['GET','POST'])
def senduser1():
    btn=request.form['button']
    if (btn=="send"):
        fid=session["lid"]
        print(fid)
        tid=session['idd']
        session['uidd']=tid
        print(tid)
        msg=request.form['textarea']
        qry="insert into interact values(null,%s,%s,%s,curdate(),'sellers')"
        val=(str(fid),str(tid),msg)
        iud(qry,val)
        return '''<script>window.location='/chatuser2'</script>'''
    else:
        return '''<script>window.location='/chatuser2'</script>'''






@app.route('/chatsllr',methods=['GET','POST'])
def chatsllr():
    uid=request.args.get('id')
    session['uidd']=uid
    qry="SELECT `FIRST_NAME` FROM EMPLOYEE WHERE `L_ID`=%s"
    val=(str(uid))
    s1=selectone(qry,val)
    fid=session['lid']
    session['idd'] = uid
    qry1="select * from interact where (from_id=%s and to_id=%s) or (from_id=%s and to_id=%s) order by date asc"
    val1=(str(uid),str(fid),str(fid),str(uid))
    s=selectall1(qry1,val1)
    return render_template('seller page/chat2.html',data=s,fname=s1[0],fr=str(uid))
######

@app.route('/chatsllr2',methods=['GET','POST'])
def chatsllr2():
    uid = session['uidd']
    qry = "SELECT `FIRST_NAME` FROM EMPLOYEE WHERE `L_ID`=%s"
    val = (str(uid))
    s1 = selectone(qry, val)
    fid = session['lid']
    session['idd'] = uid
    qry1 = "select * from interact where (from_id=%s and to_id=%s) or (from_id=%s and to_id=%s) order by date asc"
    val1 = (str(uid), str(fid), str(fid), str(uid))
    s = selectall1(qry1, val1)
    return render_template('seller page/chat2.html', data=s, fname=s1[0], fr=str(uid))
@app.route('/sendsllr',methods=['GET','POST'])
def sendsllr():
    btn=request.form['button']
    if (btn=="send"):
        fid=session["lid"]
        print(fid)
        tid=session['idd']
        session['uidd']=tid
        print(tid)
        msg=request.form['textarea']
        qry="insert into interact values(null,%s,%s,%s,curdate(),'sellers')"
        val=(str(fid),str(tid),msg)
        iud(qry,val)
        return '''<script>window.location='/chatsllr2'</script>'''
    else:
        return '''<script>window.location='/chatsllr2'</script>'''

app.run(debug=True)
