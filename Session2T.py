# String Formatting
app_name = "WhatsApp"
contact_number = "+91 99999 11111"

print("Welcome to", app_name)
print("Welcome to %s" %(app_name))

print("Welcome to", app_name, "dear", contact_number)
print("Welcome to {} dear {}".format(app_name, contact_number))

name = "john"
email = "john@example.com"
password = "pass123"

sql = "insert into USER values( '{}', '{}', '{}' )".format(name, email, password)
print(sql)

data = "100"
print("Is it a digit", data.isdigit())

if data.isdigit():
    num = int(data)
    print(num)