""" ===| Two Names, One Shirt |=== """

class shirt:

    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True

# create one shirt with two names
red = shirt()
crimson = red

# examine the red/crimson shirt
print(id(red))
print(id(crimson))
print(red.clean)
print(crimson.clean)