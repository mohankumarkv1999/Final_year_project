import smtplib
import pymysql
import pymysql
def email(id):
    conn = pymysql.connect(host='localhost', database='final_project', user='root', password='7338272260ksv')
    cursor = conn.cursor()
    str = "select email from test where id ='%d'"
    args = (id)
    cursor.execute(str % args)
    row = cursor.fetchone()
    sender='mohankumarkv2016@gmail.com'
    receiver=row[0]
    password='7338272260ksv'
    smtpserver=smtplib.SMTP('smtp.gmail.com',587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(sender,password)
    msg='mohan kumar k v you are sending the email from detect_mask_video file'
    smtpserver.sendmail(sender,receiver,msg)
    print('send')
    smtpserver.close()