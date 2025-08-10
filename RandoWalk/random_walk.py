from random import choice

class RandoWalk:
    """A class to generate random walks"""
    def __init__(self,num_points=5000):
        """initializing attribute of a walk"""
        self.num_points = num_points
        #all walks starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all the point in the walk"""
        # Keep taking steps until the the walk reaches a desired length
        while len(self.x_values)<self.num_points:
            #deciding which direction to go and  which direction
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_steps = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_steps = y_direction * y_distance

            #Reject moves that go nowhere:
            if x_steps == 0 and y_steps == 0:
                continue

            #calculate the new postion
            x = self.x_values[-1] + x_steps
            y = self.y_values[-1] + y_steps
            
            self.x_values.append(x)
            self.y_values.append(y)