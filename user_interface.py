import control as cl
import logger as lg


print('\nWelcome to the student information system!')


def ls_menu():
    while True:
        print('\nMenu:')
        print('1. Show all students.')
        print('2. Find student by last name.')
        print('3. Find student by name.')
        print('4. Find student by date of birth.')
        print('5. Search by grade.')
        print('6. Search by faculty.')
        print('7. Add new student.')
        print('8. Edit an existing student info.')
        print('9. Delete an entry.')
        print('10. Where is student now?')
        print('11. Close program.\n')
        n = сhecking_the_number(input('Choose menu item: '))

        if n == 1:
            lg.logging.info('The user has selected item number 1')
            print(cl.retrieve())


        elif n == 2:
            lg.logging.info('The user has selected item number 2')
            search = input('Enter last name: ')
            lg.logging.info('User entered: {search}')
            print(cl.retrieve(last_name=search))

        elif n == 3:
            lg.logging.info('The user has selected item number 3')
            search = input('Enter name: ')
            lg.logging.info('User entered: {search}')
            print(cl.retrieve(name=search))

        elif n == 4:
            lg.logging.info('The user has selected item number 4')
            search = input('Enter date of birth: ')
            lg.logging.info('User entered: {search}')
            print(cl.retrieve(date_of_birth=search))

        elif n == 5:
            lg.logging.info('The user has selected item number 5')
            search = input('Enter grade: ')
            lg.logging.info('User entered: {search}')
            print(cl.retrieve(grade=search))

        elif n == 6:
            lg.logging.info('The user has selected item number 6')
            search = input('Enter faculty: ')
            lg.logging.info('User entered: {search}')
            print(cl.retrieve(faculty=search))

        elif n == 7:
            lg.logging.info('The user has selected item number 7')
            name = input('Enter name: ')
            lg.logging.info('User entered: {name}')
            last_name = input('Enter last name: ')
            lg.logging.info('User entered: {last_name}')
            date_of_birth = input('Enter date of birth: ')
            lg.logging.info('User entered: {date_of_birth}')
            faculty = input('Enter faculty: ')
            lg.logging.info('User entered: {faculty}')
            grade = input('Enter grade: ')
            lg.logging.info('User entered: {grade}')
            group = input('Enter group: ')
            lg.logging.info('User entered: {group}')
            cl.create(name, last_name, date_of_birth, faculty, grade, group)

        elif n == 8:
            lg.logging.info('The user has selected item number 8')
            print('1. Find student by last name.')
            print('2. Find student by name.')
            print('3. Find student by date of birth.')
            edit = сhecking_the_number(input('Enter item number: '))

            if edit == 1:
                lg.logging.info('The user has selected item number 8.1')
                search = input('Enter last name: ')
                lg.logging.info('User entered: {search}')
                cl.retrieve(last_name=search)
                user_id = input('Enter entry id: ')
                lg.logging.info('User entered: {user_id}')
                new_name = input('Enter new name: ')
                lg.logging.info('User entered: {new name}')
                new_last_name = input('Enter new last name: ')
                lg.logging.info('User entered: {new last name}')
                new_date_of_birth = input('Enter new date of birth: ')
                lg.logging.info('User entered: {new date of birth}')
                new_faculty = input('Enter new faculty: ')
                lg.logging.info('User entered: {new faculty}')
                new_grade = input('Enter new grade: ')
                lg.logging.info('User entered: {new grade}')
                new_group = input('Enter new group: ')
                lg.logging.info('User entered: {new group}')
                cl.update(id=user_id, new_name=new_name, new_last_name=new_last_name,
                          new_date_of_birth=new_date_of_birth, new_faculty=new_faculty,
                          new_grade=new_grade, new_group=new_group)

            elif edit == 2:
                lg.logging.info('The user has selected item number 8.2')
                search = input('Enter name: ')
                lg.logging.info('User entered: {search}')
                cl.retrieve(name=search)
                user_id = input('Enter entry id: ')
                new_name = input('Enter new name')
                lg.logging.info('User entered: {new name}')
                new_last_name = input('Enter new last name')
                lg.logging.info('User entered: {new last name}')
                new_date_of_birth = input('Enter new date of birth')
                lg.logging.info('User entered: {new date of birth}')
                new_faculty = input('Enter new faculty')
                lg.logging.info('User entered: {new faculty}')
                new_grade = input('Enter new grade')
                lg.logging.info('User entered: {new grade}')
                new_group = input('Enter new group')
                lg.logging.info('User entered: {new group}')
                cl.update(id=user_id, new_name=new_name, new_last_name=new_last_name,
                          new_date_of_birth=new_date_of_birth, new_faculty=new_faculty,
                          new_grade=new_grade, new_group=new_group)

            elif edit == 3:
                lg.logging.info('The user has selected item number 8.3')
                search = input('Enter date of birth: ')
                lg.logging.info('User entered: {search}')
                cl.retrieve(date_of_birth=search)
                user_id = input('Enter entry id: ')
                new_name = input('Enter new name')
                lg.logging.info('User entered: {new name}')
                new_last_name = input('Enter new last name')
                lg.logging.info('User entered: {new last name}')
                new_date_of_birth = input('Enter new date of birth')
                lg.logging.info('User entered: {new date of birth}')
                new_faculty = input('Enter new faculty')
                lg.logging.info('User entered: {new faculty}')
                new_grade = input('Enter new grade')
                lg.logging.info('User entered: {new grade}')
                new_group = input('Enter new group')
                lg.logging.info('User entered: {new group}')
                cl.update(id=user_id, new_name=new_name, new_last_name=new_last_name,
                          new_date_of_birth=new_date_of_birth, new_faculty=new_faculty,
                          new_grade=new_grade, new_group=new_group)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nSuch menu item does not exist.\nEnter the number corresponding to the menu item.')

        elif n == 9:
            lg.logging.info('The user has selected item number 9')
            print('1. Find student by last name.')
            print('2. Find student by name.')
            print('3. Find student by date of birth.')
            deleting = сhecking_the_number(input('Enter item number: '))

            if deleting == 1:
                lg.logging.info('The user has selected item number 9.1')
                search = input('Enter last name: ')
                lg.logging.info('User entered: {search}')
                print(cl.retrieve(last_name=search))
                user_id = input('Enter entry id: ')
                lg.logging.info('User entered: {user_id}')
                cl.delete(id=user_id)

            elif deleting == 2:
                lg.logging.info('The user has selected item number 9.2')
                search = input('Enter name: ')
                lg.logging.info('User entered: {search}')
                print(cl.retrieve(name=search))
                user_id = input('Enter entry id: ')
                lg.logging.info('User entered: {user_id}')
                cl.delete(id=user_id)

            elif deleting == 3:
                lg.logging.info('The user has selected item number 9.3')
                search = input('Enter date of birth: ')
                lg.logging.info('User entered: {search}')
                print(cl.retrieve(date_of_birth=search))
                user_id = input('Enter entry id: ')
                lg.logging.info('User entered: {user_id}')
                cl.delete(id=user_id)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nSuch menu item does not exist.\nEnter the number corresponding to the menu item.')

        elif n == 10:
            lg.logging.info('The user has selected item number 10')
            search1 = input('Enter last name: ')
            lg.logging.info('User entered: {search}')
            print(cl.retrieve(last_name=search1))
            user_id = input('Enter entry id: ')
            lg.logging.info('User entered: {user_id}')
            print(cl.retrieve(id=user_id))
            print('This student is at:\n' + cl.where_is_student(id=user_id))

        elif n == 11:
            lg.logging.info('End')
            print('Bye bye!')
            break

        else:
            lg.logging.info('User entered an invalid menu value: {n}')
            print(
                '\nSuch menu item does not exist.\nEnter the number corresponding to the menu item.')


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        lg.logging.info('User entered an invalid menu value: {arg}')
        print('\nYou did not enter number.')
        arg = input('Enter existing menu item: ')
    return int(arg)
