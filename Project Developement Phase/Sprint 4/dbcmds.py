from connect import execDB, execReturn

# INSERT into user_data(username , email , pass ) values ('Manoj' , 'manoj.selvam312@gmail.com' , 'Abcd123$')
def addUser(username , email , password):
    sql_fd = f"SELECT * FROM user_data WHERE username='{username}'"
    r = execReturn(sql_fd)

    if r != [] :
        return "Username Exists"
        
    sql_st = f"INSERT INTO user_data(username , email , pass ) values ( '{username}' , '{email}' , '{password}' )"
    r = execDB(sql_st)
    return r

def getPassword(username ):
    sql_fd = f"SELECT pass FROM user_data WHERE username='{username}'"
    r = execReturn(sql_fd)
    return r[0]['PASS']
