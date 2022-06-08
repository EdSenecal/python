# For this assignment you will create the user class and add a couple methods!

# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:

# first_name
# last_name
# email
# age
# Also include default attributes:

# is_rewards_member - default value of False
# gold_card_points = 0
# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.


class User:
    def __init__(self, firstName, lastName, email, age):
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name )
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
    
    def enroll(self):
        if self.is_rewards_member == False:
            self.gold_card_points = self.gold_card_points + 200
            print("It's dangerous to go alone, take these points")
            self.is_rewards_member= True
        else:
            print("User is already a member.")
            return False
    
    def spend_points(self, amount):
        if self.gold_card_points - amount >= 0:
            self.gold_card_points = self.gold_card_points - amount
            print("spent")
        else:
            print ("Get more points noob")
    

Rick_user = User("Rick","Astley","rickroll@gmail.com",56)

Rick_user.display_info()
Rick_user.enroll()
Rick_user.enroll()
print(Rick_user.is_rewards_member)
Rick_user.spend_points(199)
Rick_user.spend_points(199)

