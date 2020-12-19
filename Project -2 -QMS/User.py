from Features import Features
from Connections import CONNECTIONS


class User(CONNECTIONS):

    def __init__(self):
        super().__init__()

    def create_user(self):
        name = input('Please enter the name: ')
        pwd = input('Please enter the password: ')
        role = input('Please enter the role of the user: ')
        query = "insert into tbl_user(UserName,UserPassword,Role) values('%s','%s','%s')"%(name, pwd, role)
        self.execute_query(query)
        print('User created successfully!!!')

    def login_user(self):
        print('============ ENTER LOGIN DETAILS ============')
        name = input('Please enter the name: ')
        pwd = input('Please enter the password: ')
        data = self.validate_user(name, pwd)
        if data:
            if name.lower() == 'admin':
                self.display_admin_rights()
            else:
                self.display_student_rights(name)
        else:
            print('Invalid User')

    def validate_user(self, name, pwd):
        validate_query = "select * from tbl_User where UserName like '%s' and UserPassword='%s'"%(name, pwd)
        rows = self.fetch_data(validate_query)
        return rows

    def display_admin_rights(self):
        print('============ WELCOME ADMIN ============')
        print('Please choose any one option')
        print('1. Add Questions')
        print('2. View Results')
        selected_option = eval(input())
        feature = Features()

        if selected_option == 1:
            feature.add_questions()
        elif selected_option == 2:
            name = input('enter the name:')
            feature.display_result(name)
        else:
            print('Invalid Input!! Please enter the valid input! ')

    def display_student_rights(self, name):
        print('============ WELCOME %s ============'%name.upper())
        print('Please choose any one option')
        print('1. Start the Quiz')
        print('2. View instructions')
        selected_option = eval(input())
        feature = Features()

        if selected_option == 1:
            feature.start_quiz(name)
        elif selected_option == 2:
            feature.display_instructions()
        else:
            print('InValid Input!! Please enter the valid input! ')