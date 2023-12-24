import rclpy
from rclpy.node import Node # se importa la clase node para crear nodos en ros2
from std_msgs.msg import String


class SimpleSubscriber(Node):

    def __init__(self):
        super().__init__("simple_subscriber")#aqui damos como entrada el nombre que le queremos dar al nodo
        #creamos un objeto subscriber e indicamos el tipo de mensaje recibira en el topic y el nombre del topic al que escucha
        self.sub_=self.create_subscription(String,"chapter",self.msgCallback,10)
    
    def msgCallback(self,msg):
        self.get_logger().info(f"i heard from {msg.data}")#to print informative message

def main():
    rclpy.init()
    simple_subscriber=SimpleSubscriber()
    rclpy.spin(simple_subscriber)#para mantener el subscriber activo
    simple_subscriber.destroy_node()#cuando se da ctrl+c se elemimna el nodo
    rclpy.shutdown()#cerramos la interfaz de ros


if __name__=="__main__":
    main()

