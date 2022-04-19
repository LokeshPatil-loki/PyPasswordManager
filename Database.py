import mysql.connector
from Model.Account import *
from Model.Note import *
from Model.User import *
#
class DBPassMan:
    def __init__(self):
        errorCode = 0
        self.TBL_USER = "tbl_users"
        self.TBL_PASSWORDS = "tbl_passwords"
        try:
            con = mysql.connector.connect(host="localhost", user="loki", password="doloris");
            self.con = con
            cursor = con.cursor()
            cursor.execute("use PassMan")
            print("Already Exists")

        except mysql.connector.Error as err:
            errorCode = int(str(err).split(" ")[0])
            print(errorCode)

        if errorCode == 1049:
            cursor.execute("Create database PassMan ");
            cursor.execute("Use PassMan")
            sql = "create table tbl_users(userid int primary key auto_increment, username varchar(50) unique, password varchar(50))";
            cursor.execute(sql)
            sql = """create table tbl_passwords(
            id int unique auto_increment,
            userid int,
            acc_name varchar(50),
            username varchar(50),
            password varchar(50),
            foreign key (userid) references tbl_users(userid),
            primary key (userid,acc_name)
            );
            """
            cursor.execute(sql)
            cursor.close()

    def login(self,username,password):
        sql = "Select * from tbl_users where username = %s and password = %s"
        values = (username,password)
        cursor = self.con.cursor()
        cursor.execute(sql,values)
        result = cursor.fetchall()
        print("len: ",len(result))
        cursor.close()
        if len(result) == 0:
            print("Incorrect Username / Password")
            return None
        else:
            self.loggedInUser = User(result[0][0],result[0][1],result[0][2])
            return self.loggedInUser

    def saveAccount(self,values):
        try:
            sql = "Insert into tbl_passwords(userid,acc_name,username,password) values(%s,%s,%s,%s)"
            values = tuple([self.loggedInUser.id])+values
            cursor = self.con.cursor()
            cursor.execute(sql,values)
            self.con.commit()
            print("Affected",cursor.rowcount)
            cursor.close()
            return True
        except mysql.connector.errors.IntegrityError as err:
            if err.errno == 1062:
                print("Duplicate Entry",err.msg)
        return False

    def getAllAccounts(self):
        sql = "select * from tbl_passwords where userid = %s order by id desc"
        cursor = self.con.cursor()
        cursor.execute(sql,(self.loggedInUser.id,))
        result = cursor.fetchall()
        cursor.close()
        print(result)
        accountlist = []
        for x in result:
            accountlist.append(Account(x[0],x[1],x[2],x[3],x[4]))
        return accountlist

    def updateAccount(self,account):
        sql = f"Update tbl_passwords set username = '{account.username}', password = '{account.password}' where userid = {account.owner} and acc_name = '{account.account_name}'"
        # values = (account.username,account.password,account.owner,account.account_name)
        print(sql)
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()
        cursor.close()
        print(sql)
        print("id",account.id)
        print("Userid",account.owner)
        print("Account Name",account.account_name)
        print("Username",account.username)
        print("Password",account.password)

    def searchAccount(self,searchString):
        sql = f"select * from tbl_passwords where userid = {self.loggedInUser.id} and acc_name like '%{searchString}%' order by id desc "
        print(sql)
        cursor = self.con.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        accountlist = []
        for x in result:
            accountlist.append(Account(x[0],x[1],x[2],x[3],x[4]))
        return accountlist

