import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

from time import sleep
from math import pi

class Robotutorial(Node):    # this class inherits from the 'Node' class

    def __init__(self):
        super().__init__('robotutorial_node')  # this will be the name of the node

        self.counter = 0
        self.base_linear_velocity = 1.0 # change here for turtlebot

        # publisher that will publish data to the topics for turtlebot to use
        self.velocity_publisher = self.create_publisher(
            Twist,                           # message type
            '/turtle1/cmd_vel',              # name of the topic (change for turtlebot)
            10)
        
        # timer that will call 'self.timer_callback' every second
        # self.create_timer(1, self.timer_callback)

        while True:
            self.timer_callback()


    def timer_callback(self):
        # YOUR CODE HERE START #############################################
        self.move_front()      # move front on 0.3 meters
 
        self.turn_right(90)    # turn right on 90 degrees

        self.move_front()
        self.move_front()

        self.turn_right(90)


        self.move_circle(1, -1, 90)  # make a quater circle in the right(relative to the turtle) position

        self.move_front()


        # YOUR CODE HERE END #############################################



    def move_front(self):
        turtle_velocity = Twist() # instance that will contain turtle's velocity

        turtle_velocity.linear.x = self.base_linear_velocity
        self.velocity_publisher.publish(turtle_velocity) # publish velocity to the topic - to the turtlebot
        # self.get_logger().info(f'move front')
        sleep(1)


    def move_circle(self, radius, direct, angle):
        turtle_velocity = Twist() # instance that will contain turtle's velocity

        angle *= pi/180
        turtle_velocity.linear.x = self.base_linear_velocity

        vel = self.base_linear_velocity/radius
        turtle_velocity.angular.z = vel * direct

        time_m = angle/vel
        counter = 0

        self.get_logger().info(f'time: {time_m}')

        while (counter < time_m):
            self.velocity_publisher.publish(turtle_velocity) # publish velocity to the topic - to the turtlebot
            time_to_sleep = 1 if time_m-counter > 1 else time_m-counter
            sleep(time_to_sleep)
            counter += 1


    
    def turn_right(self, deg):
        turtle_velocity = Twist() # instance that will contain turtle's velocity

        deg *= pi/180

        if (deg > 1.9):
            deg = 1.9

        turtle_velocity.angular.z = -deg
        self.velocity_publisher.publish(turtle_velocity) # publish velocity to the topic - to the turtlebot

        sleep(1)

    def turn_left(self, deg):
        turtle_velocity = Twist() # instance that will contain turtle's velocity

        deg *= pi/180

        if (deg > 1.9):
            deg = 1.9
            
        turtle_velocity.angular.z = deg
        self.velocity_publisher.publish(turtle_velocity) # publish velocity to the topic - to the turtlebot

        sleep(1)

  

def main(args=None):
    rclpy.init(args=args)
    node = Robotutorial()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
