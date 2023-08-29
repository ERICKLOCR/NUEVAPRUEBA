


# Simulación de AutoMini V2 mediante Gazebo controlado con Joystick

## Instalaciones adicionales

### Configuración e instalación del Joystick

Instalar el controlador del Joystick desde la pagina oficial de [ROS](http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick#Installing)

### Configuración e instalación de AutoMini

Instalar el simulador de AutoMini desde el siguiente tutorial[.pdf](Documentos_de_instalación/Instalación_Simulador_GazeboAUTONOMOUS.pdf).

### Configuración del repositorio local   

Clonar el repositorio de AutoMini_Joystick_ , dirigirse al directorio local donde se clonara el repositorio, en la terminal colocar

```
git clone https://github.com/FilibertoMartinez/AutoMini_Joystick_.git   
```
Para ver si el repositorio local está correctamente inicializado

```
cd  AutoMini_Joystick_/src
rosrun principal joyop.py   
```

Si al ejecutar el programa nos genera el error ( ImportError: No module named ackermann_msgs.msg ) tenemos que ejecutar el siguiente comando 

```
  $ sudo apt-get install ros-melodic-ackermann-msgs
```

##  Simulación AutoMini V2 con Joystick


### -Comandos en Terminal 1  – AutoNomoMini en simulador Gazebo -

 En el directorio AutoNOMOS_simulation 
```
$ cd EK_AutoNOMOS_Sim/
$ source devel/setup.bash
$ cd src/principal/
```

Ejecute el siguiente comando(Para el simulador virtual ):

```
$ roslaunch autonomos_gazebo_simulation curved_road.launch
```

Se debe abrir una nueva ventana de Gazebo con el automóvil y una pista.


### -Comandos en terminal 2 – Joystick node-

“X:0,1,2” colocar el número de puerto:
```
$ rosparam set joy_node/dev "/dev/input/jsX"
$ rosrun joy joy_node                        
```

  Se levanta el nodo joy
 
### -Comandos en terminal 3 – Teleoperación con joystick-


- Dirigirse al  repositorio de AutoMini en simulación  mediante el Joystick :

        $ rosrun principal joyo.py

Finalmente tendremos un entorno virtual en Gazebo y al pulsar un botón en el joystick este ejecutará cierto movimiento correspondiente.






## PRUEB DE IMAG

![SOC top](docs/doxygen/pics/soc_top_v5.png)


## PRUEB DE DOC

SoC documentation in [.pdf](docs/riscv_vhdl_trm.pdf) formats.












