from launch import LaunchDescription
from launch_ros.actions import Node #importamos la libreria para comenzar un nodo
from launch.actions import DeclareLaunchArgument #para declarar argumentos del launch file 
import os #to indicate a directory
from ament_index_python.packages import get_package_share_directory#para que busque la direccion automatica de paquetes
from launch_ros.parameter_descriptions import ParameterValue# para declarar el valor del parameter
from launch.substitutions import Command,LaunchConfiguration#para declarar el comando de transformar el xacro a urdf

##esta funcion vamos a describir todas la funcionalidades 
def generate_launch_description():
    model_arg=DeclareLaunchArgument(
        name="model",
        #si el usuario no define el path del modelo lanzara el modelo del bumperbot por default
        default_value=os.path.join(get_package_share_directory("bumperbot_description"),"urdf","bumperbot.urdf.xacro"),
        description="Absolute path to urdf file"
    )


    #debemos transformar el xacro a urdf
    robot_description=ParameterValue(Command(["xacro ",LaunchConfiguration("model")]),value_type=str)
    #declaramos el constructor y especificamos el paquete donde esta el nodo que queremos ejecutar 
    #definios el nombre del ejecutable y los parametros
    robot_state_publisher=Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description":robot_description}]#robot_description es un argumento del launch file
    )
    joint_state_publisher_gui=Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    rviz_node=Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",#este sera el nombre del nodo de rviz
        output="screen",#para mostrar los mensajes que impre nodo siendo mostrados  en la terminal 
        arguments=["-d",os.path.join(get_package_share_directory("bumperbot_description"),"rviz","display.rviz")]#-d escoje una configuracion que queremos visualizar
    )   

    
    #retornamos un objeto launchdescription que toma como argumento 
    return LaunchDescription([
        model_arg,
        robot_state_publisher,
        joint_state_publisher_gui,
        rviz_node
    ])