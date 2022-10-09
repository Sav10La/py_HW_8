
import pandas as pd
import csv
import os.path
from random import randint

db_file_name = ''
db = []
global_id = 0  # id for adding entries


def init_data_base(file_name='students.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    with open(db_file_name, 'r', newline='', encoding="utf-8-sig") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if (row[0] != 'ID'):
                db.append(row)
                if (int(row[0]) > global_id):
                    global_id = int(row[0])


def create(name='', last_name='', date_of_birth='', faculty='', grade='', group=''):
    global global_id
    global db
    global db_file_name
    if(name == ''):
        print("No name specified!")
        return
    if(last_name == ''):
        print("No last name specified!")
        return
    if(date_of_birth == ''):
        print("No date of birth specified!")
        return
    if(faculty == ''):
        print("No faculty specified!")
        return
    if(grade == ''):
        print("No grade specified!")
        return
    if(group == ''):
        print("No group specified!")
        return

    for row in db:
        if(row[1] == name.title()
                and row[2] == last_name.title()
                and row[3] == date_of_birth
                and row[4] == faculty.title()
                and row[5] == grade.upper()
                and row[6] == group.upper()):
            print("This entry already exists!")
            return

    global_id += 1
    new_row = [str(global_id), name.title(),
               last_name.title(), date_of_birth, faculty.title(),
               grade.title(), group.upper()]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


def retrieve(id='', name='', last_name='', date_of_birth='', faculty='', grade='', group=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(last_name != '' and row[2] != last_name.title()):
            continue
        if(date_of_birth != '' and row[3] != date_of_birth):
            continue
        if(faculty != '' and row[4] != faculty.title()):
            continue
        if(grade != '' and row[5] != grade.title()):
            continue
        if(group != '' and row[6] != group.upper()):
            continue
        result.append(", ".join(map(str, row)))
        # result.append(row)
        # if(format == 1):
        #     result.append(", ".join(map(str, row)))
        # if(format == 2):
        #     result.append("\n".join(map(str, row)))
    if len(result) == 0:
        return f'Students not found'
    else:
        # return result
        lst = "\n".join(map(str, result))
        return lst



def update(id='', new_name='', new_last_name='', new_date_of_birth='', new_faculty='', new_grade='', new_group=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for update')
        return
    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                if(new_name != ''):
                    row[1] = new_name.title()

                if(new_last_name != ''):
                    row[2] = new_last_name.title()

                if(new_date_of_birth != ''):
                    row[3] = new_date_of_birth

                if(new_faculty != ''):
                    row[4] = new_faculty.title()

                if (new_grade != ''):
                    row[5] = new_grade.upper()

                if (new_group != ''):
                    row[6] = new_group.upper()
            writer.writerow(row)


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for delete')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)


def where_is_student(id=''):
    rows = []
    with open('timetable.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting field names through first row
        fields = next(csvreader)
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        return ', '.join(rows[randint(1, len(rows) - 1)])

# def upload(file_name='data.csv'):
#     user_file_name = file_name
#     # open both files
#     if os.path.exists(user_file_name):
#         with open(user_file_name, 'r') as first, open('base_phone.csv', 'a') as second:
#             # read content from first file
#             for line in first:
#                 # append content to second file
#                 second.write(line)
#             second.seek(0, 2)
