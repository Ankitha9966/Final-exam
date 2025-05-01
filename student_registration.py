def generate_ID():
    return "123456"
def generate_username():
    return "Ankitha"
def generate_income():
    return "RD012345"
def verify_income(income):
    return income==generate_income()
def verify_name(name):
    return name==generate_username()
def verify_ID(id):
    return id==generate_ID()

    return sms_otp==generate_otp()
def registration(studentname,studentid,studentincome):
    if not verify_name(studentname):
        return "invalid student name"
    if not verify_ID(studentid):
        return "invalid student id"
    if not verify_income(studentincome):
        return "wrong student income number"
    return "Registration successful"