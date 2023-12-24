import rclpy #allow us to use all the functionalities within our python script 
from rclpy.node import Node # se importa la clase node para crear nodos en ros2
from std_msgs.msg import String


class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")#inicializamos la clase base, el constructor de la clase Node
        #damos como argumento el tipo de la interface del mensaje que vamos a utilizar y el nombre del topic y el
        #tamno del queue del mesange que funciona como buffer ,el tiempo en que se recibe el mensaje
        self.pub_=self.create_publisher(String,"chapter",10)
        self.counter_=0#contara el numero de mensajes que vamos a publicar entre los topics
        self.frequency_=1.0# quieree decir que estmos enviando un paquete por segundo
        #to print an informative message in the terminal
        self.get_logger().info("Publishing at %d Hz" % self.frequency_)
        #toma como argumento la frecuencia a la que queremos ejecutar la funcion
        self.timer_=self.create_timer(self.frequency_,self.timerCallback)

    def timerCallback(self):
        """
        la meta es publicar un mensaje entre el topic del mensaje cada vez que este
        funcion es llamada por el timer
        """
        msg=String()#creamos un nuevo mensaje que va a ser publicado por el mensaje
        msg.data="hello ros 2 -counter - %d" % self.counter_
        self.pub_.publish(msg)#publicamos el mensaje 
        self.counter_+=1

def main():
    rclpy.init()#instanciamos la comunicacion con ros 
    simple_publisher=SimplePublisher()
    rclpy.spin(simple_publisher)#mantiene la funcion del publisher abierta corriendo
    #if we terminate the execution of the node by pressing ctrl c en la terminal , 
    simple_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
