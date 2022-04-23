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
        sql = "create table if not exists tbl_users(userid int primary key auto_increment,name varchar(50) ,username varchar(50) unique, password varchar(50))";
        cursor.execute(sql)
        sql = """create table if not exists tbl_passwords(
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
        sql = """
            CREATE TABLE IF NOT EXISTS tbl_notes(
                id int unique auto_increment,
                userid int,
                title varchar(50),
                data varchar(500),
                foreign key (userid) references tbl_users(userid),
                primary key (userid,title)
            );
        """
        cursor.execute(sql)
        cursor.close()

    def login(self,username,password):
        sql = "Select * from tbl_users where username = %s and password = %s"
        values = (username,self.encrypt(password))
        cursor = self.con.cursor()
        cursor.execute(sql,values)
        result = cursor.fetchall()
        # print("len: ",len(result))
        cursor.close()
        if len(result) == 0:
            print("Incorrect Username / Password")
            return None
        else:
            self.loggedInUser = User(result[0][0],result[0][1],result[0][2],result[0][3])
            return self.loggedInUser

    def register(self,name,username,password):
        print("Username:",username)
        print("Password:",password)
        sql = f"Insert into tbl_users(name,username, password) values('{name}','{username}','{self.encrypt(password)}')"
        print(sql)
        try:
            cursor = self.con.cursor()
            cursor.execute(sql)
            self.con.commit()
            rowCount = cursor.rowcount
        except mysql.connector.errors.IntegrityError as err:
            return False

        cursor.close()
        return rowCount != 0

    def saveAccount(self,values):
        try:
            sql = "Insert into tbl_passwords(userid,acc_name,username,password) values(%s,%s,%s,%s)"
            values = tuple([self.loggedInUser.id])+(values[0],values[1],self.encrypt(values[2]))
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
        # print(result)
        accountlist = []
        for x in result:
            accountlist.append(Account(x[0],x[1],x[2],x[3],self.decrypt(x[4])))
        return accountlist

    def updateAccount(self,account):
        sql = f"Update tbl_passwords set username = '{account.username}', password = '{self.encrypt(account.password)}' where userid = {account.owner} and acc_name = '{account.account_name}'"

        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()
        cursor.close()


    def searchAccount(self,searchString):
        sql = f"select * from tbl_passwords where userid = {self.loggedInUser.id} and acc_name like '%{searchString}%' order by id desc "
        print(sql)
        cursor = self.con.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        accountlist = []
        for x in result:
            accountlist.append(Account(x[0],x[1],x[2],x[3],self.decrypt(x[4])))
        return accountlist

    def deleteAccount(self,account):
        sql = f"delete from tbl_passwords where acc_name = '{account.account_name}' and userid = {account.owner}"
        cursor = self.con.cursor()
        cursor.execute(sql)
        result = cursor.rowcount
        cursor.close()
        self.con.commit()
        return bool(result)

    def saveNote(self,values):
        try:
            sql = "Insert into tbl_notes(userid,title,data) values(%s,%s,%s)"
            values = tuple([self.loggedInUser.id])+(values[0],self.encrypt(values[1]))
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

    def getAllNotes(self):
        sql = "select * from tbl_notes where userid = %s order by id desc"
        cursor = self.con.cursor()
        cursor.execute(sql,(self.loggedInUser.id,))
        result = cursor.fetchall()
        cursor.close()
        notelist = []
        for x in result:
            notelist.append(Note(x[0],x[1],x[2],self.decrypt(x[3])))
        return notelist

    def updateNote(self,note):
        sql = f"Update tbl_notes set title = '{note.title}', data = '{self.encrypt(note.data)}' where userid = {note.owner} and title = '{note.title}'"
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()
        print("Updated")
        cursor.close()

    def searchNote(self,searchString):
        sql = f"select * from tbl_notes where userid = {self.loggedInUser.id} and title like '%{searchString}%' order by id desc "
        # print(sql)
        cursor = self.con.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        notelist = []
        for x in result:
            notelist.append(Note(x[0],x[1],x[2],x[3]))
        return notelist

    def deleteNote(self,note):
        sql = f"delete from tbl_notes where title = '{note.title}' and userid = {note.owner}"
        cursor = self.con.cursor()
        cursor.execute(sql)
        result = cursor.rowcount
        cursor.close()
        self.con.commit()
        return bool(result)

    def encrypt(self,data):
        encrypted_data = ""
        for x in range(0, len(data)):
            char = data[x]
            code = ord(char)
            if x % 3 == 0:
                char = chr(code + 3)
            elif x % 2 == 0:
                char = chr(code + 2)
            else:
                char = chr(code + 1)
            encrypted_data += char

        return encrypted_data[::-1]

    def decrypt(self,data):
        data = data[::-1]
        decrypted_data = ""
        for x in range(len(data)):
            char = data[x]
            code = ord(char)
            if x % 3 == 0:
                char = chr(code - 3)
            elif x % 2 == 0:
                char = chr(code - 2)
            else:
                char = chr(code - 1)
            decrypted_data += char
        return decrypted_data

