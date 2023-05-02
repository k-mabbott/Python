

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name}, Email: {self.email}, age: {self.age}, Rewards member? {self.is_rewards_member} Reward points: {self.gold_card_points}")
        return self
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
        else: 
            print("Already a rewards member do not collect 200 points")
            return self
    
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
            return self
        else:
            print(f"Not enough points! Current balance is {self.gold_card_points} You entered {amount}")
            return self


user_kyle = User('Kyle', 'Mabbott', 'fake@email.com', 30)

user_john = User('John', 'Doe', 'faker@email.com', 35)

user_jane = User('Jane', 'Dee', 'fakest@email.com', 32)

# user_kyle.display_info()
user_kyle.enroll().spend_points(50).display_info().enroll().display_info()
# user_kyle.display_info()


user_john.enroll().spend_points(80).display_info()

user_jane.display_info().spend_points(40)
