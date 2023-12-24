import rclpy #allow us to use all the functionalities within our python script 
from rclpy.node import Node # se importa la clase node para crear nodos en ros2
from rcl_interfaces.msg import SetParametersResult #esta libreria nos sirve para cuando se cambia un parameter , funciona dentro de la funcion call back 

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")#inicializamos la clase base, el constructor de la clase Node, teniendo como parametro el nombre del nodo
        self.declare_parameter("simple_int_parameter",28)#declaramos una nueva configuracion de parametro
        #toma como arguemento un string como el nombre del parametro y un valor por default del parametro
        self.declare_parameter("simple_string_param","Antonio")
        self.add_on_set_parameters_callback(self.paramChangeCallback)#esta funcion se ejecutara cuando cualquiera de los parametros del nodo son cambiados
    def paramChangeCallback(self,params):
        result=SetParametersResult()#declaramos una instancia del setparameterresult