#Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.

#Требования:

#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).

#2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).

#3.Инк Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).апсуляция данных:


class User():
    def __init__(this,usr_id,usr_name,usr_access):
        this._id = usr_id
        this._name =usr_name
        this._level = usr_access

    def set_id(this,usr_id):
        _id =usr_id

    def set_name(this, usr_name):
        _name=usr_name

    def get_id(self):
        return self._id
    def get_name(self):
        return self._name

    def __str__(self):

        return (f"id = {self._id} , имя = {self._name}")




class Admin(User):
    _users = {}

    def __init__(this,usr_id,usr_name,usr_access):
        super().__init__(usr_id,usr_name,usr_access)
        this._admin_access = 'admin'


    def add_usr(Self,User):
        Admin._users[User.get_id()]=User

    def del_users(Self,User):
        if User.get_id() in Admin._users:
            del Admin._users[User.get_id()]

    def info(self):
        print(f"id = {self._id} , имя = {self._name}")

        for k in Admin._users:
            print(f"{Admin._users[k]}"'\n')




user1 = User(1,'Иван','user')
user2 = User(3,'Виктор','user')
user3 = User(5,'Петр','user')
admin1 = Admin(10,'Danil','admin')


admin1.add_usr(user1)
admin1.add_usr(user2)
admin1.add_usr(user3)
admin1.del_users(user1)

admin1.info()