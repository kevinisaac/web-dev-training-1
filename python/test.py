# Datatypes:
# - string
# - integer
# - boolean
# - list

# argument/parameter

def printDetails(friendDetails):
    print(
        'Hello '
        + friendDetails['name']
        + ', you are '
        + str(friendDetails['age'])
        + ' years old'
    )

friends = [
    {
        'name': 'Kevin',
        'age': 30,
        'isMarried': True
    },
    {
        'name': 'Andrid',
        'age': 29,
        'isMarried': True
    },
    {
        'name': 'Aravind',
        'age': 31,
        'isMarried': True
    },
    {
        'name': 'Paul',
        'age': 30,
        'isMarried': True
    }
]

for friend in friends:
    printDetails(friend)



# names = ['Kevin', 'Isaac']
# print(names[1])

# 1 - nameOfFriend = 'Andrid'
#   - ageOfFriend = 30
# def printSomething(nameOfFriend, ageOfFriend, maritalStatusOfFriend):
    # print('Hello ' + nameOfFriend + ', you are ' + str(ageOfFriend) + ' years old.')
    # if maritalStatusOfFriend:
        # print('You are married')
    # else:
        # print('Get a life')


# for friend in friends:
    # printSomething(friend, 30, True)


# print('Hello ' + name + ', you are ' + str(age) + ' years old')
#
#
# if True:
    # print('I execute always')
#
#
# if age > 20:
    # print('You are older than 20')
#
#
# if age > 10:
    # print('You are a teenager')
# else:
    # print('You are not old enough')


