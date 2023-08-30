


#  Instalación del Turtlebot2 en ROS melodic(Ubuntu 18.04)

## Instalaciones adicionales


```
mkdir -p ~/turtlebot2_ws/src
cd turtlebot2_ws
catkin_make
cd src
curl -sLf https://raw.githubusercontent.com/gaunthan/Turtlebot2-On-Melodic/master/install_all.sh | bash
cd ..
catkin_make

```


#  Instalación del Turtlebot3 en ROS melodic(Ubuntu 18.04)




Creamos nuestro workspace de trabajo 
```
mkdir -p ~/turtlebot3_ws/src
cd turtlebot3_ws
catkin_make
```
Nos ubicamos en la carpeta para clonar el repositorio

```
cd src
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
```


instalar
```
sudo apt install ros-noetic-slam-gmapping
```

roscore

```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```
 






#                 Para abrir el entono virtual de sumulacion del Turtlebot3 en Gazebo


##  Ejecutar Turtlebot en Gazebo

Nos ubicamos en la cartepara de trabajo

```
cd turtlebot3_ws
```

Se puede elejir el model de robot a acargar ene l simulador eentre ellos se tiene model-> burger, waffle, waffle_pi

Ahora para abrir tu espacio de tranajo en el semilador Gaseo podemos tener difeentes entornos entre ellos tenemos

1. Lanza un espacio de trabajo turtlebot uncamente en un plano
 ```
export TURTLEBOT3_MODEL=burger
  roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch     
```
2. Lanza un espacio de trabajo turtlebot uncamente en un plano
```
export TURTLEBOT3_MODEL=burger
 roslaunch turtlebot3_gazebo turtlebot3_world.launch           
```

3. Lanza un espacio de trabajo turtlebot mostrando el interior de una casa

```
 export TURTLEBOT3_MODEL=burger
 roslaunch turtlebot3_gazebo turtlebot3_house.launch         
```

#                 Forma de controlar al Turtlebot3 
##  Se controlara al Turtlebot3 meiante teclado
```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```







###
###
##
##
###
###










Para verificar la instalación que todo este en orden verificamos 

```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```


### Configuración e instalación del Joystick

Instalar el controlador del Joystick desde la pagina oficial de [ROS](http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick#Installing)

### Configuración e instalación de AutoMini

Instalar el simulador de AutoMini desde el siguiente tutorial[.pdf](Documentos_de_instalación/Instalación_Simulador_GazeboAUTONOMOUS.pdf).

### Configuración del repositorio local   

Clonar el repositorio de AutoMini_Vista , dirigirse al directorio local donde se clonara el repositorio, en la terminal colocar

```
git clone https://github.com/FilibertoMartinez/AutoMini_Vista.git   
```
Para ver si el repositorio local está correctamente inicializado
#### -Comandos en Terminal 1

```
roscore  
```
#### -Comandos en Terminal 2
```
cd  AutoMini_Vista
source devel/setup.bash
cd src/Vista
rosrun Vista vista.py   
```
Si al ejecutar el programa nos aparece algo similar a ese texto quiere decir que la configuración se realizó correctamente. . ([INFO] [1693334210.836545]: publishing image  ).



##  Simulación AutoMini V2 con Joystick con Vista en ventana flotante


### -Comandos en Terminal 1  – AutoNomoMini en simulador Gazebo -

 En el directorio AutoNOMOS_simulation, ejecute el siguiente comando(Para el simulador virtual ):

```
 cd EK_AutoNOMOS_Sim/
 source devel/setup.bash
 roslaunch autonomos_gazebo_simulation curved_road.launch
```

Se debe abrir una nueva ventana de Gazebo con el automóvil y una pista.


### -Comandos en terminal 2 – Joystick node-

 /dev/input/jsX “X:0,1,2” colocar el número de puerto:
```
 rosparam set joy_node/dev "/dev/input/js0"
 rosrun joy joy_node                        
```

  Se levanta el nodo joy
 
### -Comandos en terminal 3 – Teleoperación con joystick-


- Dirigirse al  repositorio de AutoMini en simulación  mediante el Joystick el cual se  clonó previamente:

```
  source devel/setup.bash
  cd src/principal/src 
  rosrun principal joyop.py
```

### -Comandos en terminal 4 – Vista -


- Dirigirse al  repositorio de AutoMini en simulación  mediante el Joystick con Vista el cual se  clonó previamente:

```
  source devel/setup.bash
  cd src/Vista/src 
  rosrun Vista vista.py
```

Finalmente tendremos un entorno virtual en Gazebo y al pulsar un botón en el joystick este ejecutará cierto movimiento correspondiente el cual mostrara una vista frontal en una venta independiente para tener una mejor visualización de como se mueve el AutoMini V2 en la pista.






## PRUEB DE IMAG

![SOC top](docs/doxygen/pics/soc_top_v5.png)


## PRUEB DE DOC

SoC documentation in [.pdf](docs/riscv_vhdl_trm.pdf) formats.



## -Comandos en nueva terminal  – Joystick node-

 /dev/input/jsX “X:0,1,2” colocar el número de puerto:
```
 rosparam set joy_node/dev "/dev/input/js0"
 rosrun joy joy_node                        
```

  Se levanta el nodo joy
 
## -Comandos en nueva terminal – Teleoperación con joystick-


- Dirigirse al  repositorio de AutoMini en simulación  mediante el Joystick el cual se  clonó previamente:

```
  source devel/setup.bash
  cd src/principal/src 
  rosrun principal joyop.py
```









