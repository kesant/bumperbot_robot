import rclpy #allow us to use all the functionalities within our python script 
from rclpy.node import Node # se importa la clase node para crear nodos en ros2

class SimplePublisher(Node):
    def __init__(self):
        