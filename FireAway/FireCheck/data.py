"""import xlrd
from .models import user
from django.contrib.auth.models import User,Group
class building_data():

    loc =("/home/singh/Downloads/MOCK_DATA(4).xlsx")

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    data = sheet.cell_value(1, 0)

    print(data)
    for i in range(30,30):
        id = int(sheet.cell_value(i, 0))
        username = sheet.cell_value(i, 1)
        password = sheet.cell_value(i, 2)
        name = sheet.cell_value(i, 3)
        email = sheet.cell_value(i, 4)
        address = sheet.cell_value(i, 5)
        phone_number = int(sheet.cell_value(i,6))
        #print(f"id : {id} \n name : {name} \n username : {username} \n password : {passsword} \n email : {email} \n address : {address} \n phone : {phone_number} ")
        u = user(username=username, name=name, email=email,address=address, phone_number=phone_number)
        user = User.objects.create_user(username=username,email=email,password=password)
        user.last_name = ' '
        group = Group.objects.get(name="operator")
        group.user_set.add(user)
        user.save()
"""##
