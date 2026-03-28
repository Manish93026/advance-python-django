from django.db import connection


class UserService:

    def nextPk(self):
        pk = 0
        with connection.cursor() as cursor:
            sql = "select max(id) from hello_user"
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        return pk + 1

    def add(self, data):
        f = data['firstName']
        l = data['lastName']
        e = data['email']
        p = data['password']
        d = data['dob']
        a = data['address']

        sql = "insert into hello_user values((%s), (%s), (%s), (%s), (%s), (%s), (%s))"
        data = [UserService.nextPk(self), f, l, e, p, d, a]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def update(self, data):
        f = data['firstName']
        l = data['lastName']
        e = data['email']
        p = data['password']
        d = data['dob']
        a = data['address']
        i = data['id']

        sql = "update hello_user set firstName = (%s), lastName = (%s), email = (%s), password = (%s), dob = (%s), address = (%s) where id = (%s)"
        data = [f, l, e, p, d, a, i]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def delete(self, id):
        sql = "delete from hello_user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def auth(self, email, password):
        sql = "select * from hello_user where email = (%s) and password = (%s)"
        data = [loginId, password]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "email", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def get(self, id):
        sql = "select * from hello_user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "email", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def findByLogin(self,email):
        sql = "select * from hello_user where email = (%s)"
        data = [email]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "email", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def search(self, params):
        fname = params.get("firstName", "")
        pageNo = params.get("pageNo", 0)
        pageSize = params.get("pageSize", 0)
        sql = "select * from hello_user where 1=1"
        if fname != "":
            sql += " and firstName like '" + fname + "%%' "
        if (pageSize > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit %s, %s"
        print('sql => ', sql)
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo, pageSize])
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "email", "password", "dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res