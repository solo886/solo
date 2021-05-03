from faker import Faker


class Utilinfo:
    def __init__(self):
        self.faker = Faker("zh-CN")
    def get_name(self):
        name = self.faker.name()
        return name
    def get_phone_num(self):
        phone_num = self.faker.phone_number()
        return phone_num

# __init__= '__main__'
# aa= Utilinfo()
# print(aa.get_name())
# print(aa.get_phone_num())