class User():
    def __init__(self, a, b, c, d):
        self.first_name = a
        self.last_name = b
        self.xingbie = c
        self.minzu = d
        self.login_attempts = 0

    def describe_user(self):
        print("用户" + self.first_name + " " + self.last_name +
            "，性别" + self.xingbie + "，民族" + self.minzu +
            "，登录" + str(self.login_attempts))
    
    def greet_user(self):
        print("用户" + self.first_name + " " + self.last_name +
            "，你好！")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0