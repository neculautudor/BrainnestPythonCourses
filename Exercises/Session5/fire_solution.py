def authorize(func):
    def inner1(*args):
        if func(args):
            return "Unathorized access"
        else:
            return "Athorized access"
    return inner1

@authorize
def authorization(name):
    answer = False
    if name == "Nickname453":
        answer = True
    return answer

nickname = "Nickname453"


print(authorization(nickname))