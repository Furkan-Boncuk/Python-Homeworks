# key-value ilişkisi

plakalar = {'kocaeli' : 41 , 'istanbul' : 34}
print(plakalar['istanbul'])

plakalar['ankara'] = 6
print(plakalar)

users = {
    'sadikturan' : {
        'age' : 36,
        'email' : 'sadik@gmail.com',
        'phone' : '123456789',
        'adres' : 'kocaeli',
        'roles' : ['admin','user']
    },
    'furkanboncuk' : {
        'age' : 18,
        'email' : 'furkanboncuk@gmail.com',
        'phone' : '123456789',
        'adres' : 'istanbul',
        'roles' : ['user']
    }
}

print(users['sadikturan']['roles'][0])

