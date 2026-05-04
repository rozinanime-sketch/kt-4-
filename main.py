class User:
    count = 0
    def __init__(self, fullname, login, password, grade = 0,):
        self._fullname = fullname
        self._login = login
        self._password = password
        self._grade = grade
        if type(self) is User:
            User.count += 1
    def set_fullname(self, fullname):
        self._fullname = fullname
    def set_login(self, login):
        self._login = login
    def set_password(self, password):
        self._password = password
    def get_fullname(self):
        return self._fullname
    def get_login(self):
        return self._login
    def get_password(self):
        return self._password
    def set_grade(self, grade):
        self._grade = grade
    def get_grade(self):
        return self._grade
    def show_info(self):
        print(f'Fullname: {self._fullname}, Login: {self._login}')
    def __lt__(self, other):
        return self._grade < other._grade
    def __eq__(self, other):
        return self._grade == other._grade
    @property
    def name(self):
        return self._fullname
    @name.setter
    def name(self, value):
        self._fullname = value
    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, value):
        print("Нельзя изменить логин")
    @property
    def password(self):
        return "*" * 67
    @password.setter
    def password(self, value):
        self._password = value
    @property
    def grade(self):
        print("Неизвестное свойство grade")
        return None
    @grade.setter
    def grade(self, value):
        print("Неизвестное свойство grade")
class SuperUser(User):
    count = 0
    def __init__(self, fullname, login, password, right, grade = 0):
        super().__init__(fullname, login, password, grade)
        self.right = right
        SuperUser.count += 1
    def get_right(self):
        return self._right

user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)
admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

user1.show_info()
admin.show_info()

users = User.count
admins = SuperUser.count

print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}')

print(user1 < user2)
print(admin > user3)
print(user1 == user3)

user3.name = 'Ringo Star'
user1.password = 'Pa$$w0rd'

print(user3.name)
print(user2.password)
print(user2.login)

user2.login = 'geo'

print(user1.grade)
admin.grade = 10


