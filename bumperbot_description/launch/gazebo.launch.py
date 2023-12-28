from launch import LaunchDescription
from launch_ros.actions import Node #importamos la libreria para comenzar un nodo
from launch.actions import DeclareLaunchArgument ,SetEnvironmentVariable,IncludeLaunchDescription#para declarar argumentos del launch file , y para setear el entorno de la simulacion
import os #to indicate a directory
from ament_index_python.packages import get_package_share_directory,get_package_prefix#para que busque la direccion automatica de paquetes
from launch_ros.parameter_descriptions import ParameterValue# para declarar el valor del parameter
from launch.substitutions import Command,LaunchConfiguration#para declarar el comando de transformar el xacro a urdf
from launch.launch_description_sources import PythonLaunchDescriptionSource #para indicar que los archivos que que se quieres anidar son pthon launch files


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
    #definimos el entorno grafico 
    env_var=SetEnvironmentVariable("GAZEBO_MODEL_PATH",os.path.join(get_package_prefix("bumperbot_description"),"share"))
    
    #to nest launch files
    #estos dos gazebo client y server generaran un ambiente de gazebo vacio
    start_gazebo_server=IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(get_package_share_directory("gazebo_ros"),"launch","gzserver.launch.py")
    ))
    start_gazebo_client=IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(get_package_share_directory("gazebo_ros"),"launch","gzclient.launch.py")
    ))

    spawn_robot=Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-entity","bumperbot","-topic","robot_description"],#entity nombre del robot , topic, el topic donde se esta publicando nuestro robot 
        output="screen"

    )



    return LaunchDescription([
        model_arg,
        env_var,
        robot_state_publisher,
        start_gazebo_server,
        start_gazebo_client,
        spawn_robot]
    )