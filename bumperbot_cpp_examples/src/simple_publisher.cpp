#include <rclcpp/rclcpp.hpp>//nos permitira usar todas las funcionalidades de ros 2 entre nuestro script

class simplePublisher: public rclcpp :: Node
{
public://constructor de la clase
    simplePublisher(): Node("simple_publisher")
    {

    };
};

