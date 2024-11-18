from faker import Faker


f = Faker(locale='zh_CN')

print(f.ssn())