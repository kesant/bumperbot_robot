import rclpy #allow us to use all the functionalities within our python script 
from rclpy.node import Node # se importa la clase node para crear nodos en ros2
from rcl_interfaces.msg import SetParametersResult #esta libreria nos sirve para cuando se cambia un parameter , funciona dentro de la funcion call back 
from rclpy.parameter import Parameter#para verificar los tipos de datos del parameter

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_parameter")#inicializamos la clase base, el constructor de la clase Node, teniendo como parametro el nombre del nodo
        self.declare_parameter("simple_int_parameter",28)#declaramos una nueva configuracion de parametro
        #toma como arguemento un string como el nombre del parametro y un valor por default del parametro
        self.declare_parameter("simple_string_param","Antonio")
        self.add_on_set_parameters_callback(self.paramChangeCallback)#esta funcion se ejecutara cuando cualquiera de los parametros del nodo son cambiados
    def paramChangeCallback(self,params):
        result=SetParametersResult()#declaramos una instancia del setparameterresult

        for param in params:
            if param.name=="simple_int_parameter" and param.type_==Parameter.Type.INTEGER:
                self.get_logger().info(f"Param simple_int_parameter changed! New value is {param.value}")
                result.successful=True# esto quiere decir que el cambio del valor del parameter ha sido efectuado exiitosamaente de lo contrario se muestra por terminal
            if param.name=="simple_string_param" and param.type_==Parameter.Type.STRING:
                self.get_logger().info(f"Param simple_string_param changed! New value is {param.value}")
                result.successful=True# esto quiere decir que el cambio del valor del parameter ha sido efectuado exiitosamaente de lo contrario se muestra por terminal

        return result


def main():
    rclpy.init()#instanciamos la comunicacion con ros 
    simple_parameter=SimplePublisher()
    rclpy.spin(simple_parameter)#mantiene la funcion del publisher abierta corriendo
    #if we terminate the execution of the node by pressing ctrl c en la terminal , 
    simple_parameter.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()



