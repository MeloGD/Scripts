#!/usr/bin/python3

import subprocess
import os
import time
import sys

### Functions ###
# Muestra por pantalla las posibles causas cuando se produce un error relacionado
# con la conexión a Internet.
def printConecctionErrorInfo():
    print(" -   Es posible que la conexión a Internet sea inestable y haya   ")
    print("     causado el error. Revise el estado de la conexión y vuelva a ")
    print("     ejecutar este script.                                        ")

# Instala Docker y asigna los permisos necesarios al usuario que ha lanzado el
# script.
def installDocker():
    try:
        subprocess.run(["sudo apt update"], shell=True)
        command = "sudo apt install apt-transport-https ca-certificates curl "
        command += "software-properties-common -y"
        subprocess.run([command], shell=True)
        command =   "curl -fsSL https://download.docker.com/linux/debian/gpg "
        command += "| sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/"
        command += "docker-ce-archive-keyring.gpg"
        subprocess.run([command], shell=True)
        command =  "printf '%s\n' \"deb https://download.docker.com/linux/debian "
        command += "bullseye stable\" | sudo tee "
        command += "/etc/apt/sources.list.d/docker.list > /dev/null"
        subprocess.run([command], shell=True)
        subprocess.run(["sudo apt update"], shell=True)
        command = "sudo apt-get install docker-ce -y"
        subprocess.run([command], shell=True).check_returncode()
    except subprocess.CalledProcessError: 
        print("\n")
        print("##################################################################")
        print("- SUDO APT INSTALL DOCKER-CE ERROR -                              ")
        print("Posibles causas:                                                  ")
        printConecctionErrorInfo()
        print(" -   Es posible que el sistema haya fallado al añadir la firna    ")
        print("     del nuevo repositorio de Docker.                             ")
        print(" -   Es posible que para instalar docker-ce, el paquete haya      ")
        print("     cambiado de nombre y no puede ser encotrado en los           ")
        print("     repositorios de Docker.                                      ")
        sys.exit()

    user = os.environ.get('USER')
    subprocess.run(["sudo","usermod","-aG","docker",user])

# Reinicia Docker para que entre en efecto el nuevo directorio de almacenamiento de
# imágenes configurado con la función changeDockerDataDirectory().
def reloadDocker():
    try:
        print("Reiniciando docker para cargar /etc/docker/daemon.json            ")
        command = "sudo systemctl restart docker"
        subprocess.run([command], shell=True).check_returncode()
    except subprocess.CalledProcessError:
        print("##################################################################")
        print("\n")
        print("- DOCKER RESTART ERROR -                                          ")
        print("Posibles causas:                                                  ")
        print(" -   Ha fallado el reinicio del servicio de Docker. Haga un:      ")
        print("     sudo systemctl status docker                                 ")
        print("     Para obtener más información del error en el servicio.       ")
        sys.exit()

# Cambia el directorio por defecto de Docker para evitar problemas de almacenamiento.
# Esto es necesario porque puede llegar a ocurrir que el directorio de Docker se llene
# o este ya lleno, imposibilitando el resto de imágenes. Se configura como un directorio oculto 
# dentro del home del usuario que lance el script.
def changeDockerDataDirectory():
    try:
        user = os.environ.get('USER')
        subprocess.run(["mkdir /home/" + user + "/.docker-data"], shell=True)
        file_content1 = "'{\n\t\"data-root\": \"/home/"
        file_content2 = "/.docker_data\"\n}'"
        command_content = file_content1 + user + file_content2
        if os.path.exists("/etc/docker/daemon.json"):
            print("Ya exise un fichero /etc/docker/daemon.json.                 ")
            print("Tiene el siguiente contenido:                                ")
            subprocess.run(["cat /etc/docker/daemon.json"], shell=True)
        else:
            command = "echo " + command_content
            command += " | sudo tee -a /etc/docker/daemon.json"
            subprocess.run([command], shell=True).check_returncode()
            reloadDocker()
    except subprocess.CalledProcessError:
        print("##################################################################")
        print("- daemon.json ERROR -                                     ")
        print("Posibles causas:                                                  ")
        print(" -   Se necesitan permisos de superusuario para escribir en:      ")
        print("     /etc/docker/daemon.json                                      ")
        print("     Es posible que el error sea que haya escrito mal la          ")
        print("     contraseña del superusuario.                                 ")
        sys.exit()

# Llama al Dockerfile que está en el mismo directorio que este script, para crear y 
# configurar la imagen.
def runDockerFile():
    print("Ejecutando Dockerfile")
    try:
        command = "sg docker 'docker build -t subgraph-vega:latest "
        command += "/opt/Scripts/Repositorio_Vega/'" 
        subprocess.run([command], shell=True).check_returncode()
    except subprocess.CalledProcessError: 
        print("\n")
        print("##################################################################")         
        print("- DOCKERFILE ERROR -                                              ")
        print("Posibles causas:                                                  ")
        print(" -   Es posible que la imagen 'Ubuntu 22.04' ya no esté soportada.")
        print(" -   Es posible que la conexión a Internet sea inestable y haya   ")
        print("     causado el error. Revise el estado de la conexión y vuelva a ")
        print("     ejecutar este script.                                        ")
        print("\n")
        print("Se procederá a borrar todos los contenedores parados y las images ")
        print("sin etiquetas genereadas por este proceso fallido.\n              ")
        subprocess.run(["sg docker 'docker container prune -f'"], shell=True)
        subprocess.run(["sg docker 'docker image prune -f'"], shell=True)
        sys.exit()

# Crea un alias en la máquina host, para que al escribir "Docker_Vega-up" en la terminal,
# este llame a la aplicación de Vega dentro del contenedor y cree una ventana gráfica
# en la máquina host.
def createHostAlias():
    command = "echo \"alias Docker_Vega-up='docker container run -d --rm --net host "
    command += "-v /tmp/.X11-unix:/tmp/.X11-unix subgraph-vega:latest &'\" "
    command += ">> ~/.zshrc"
    subprocess.run([command],shell=True)

# Le da la opción al usuario de reiniciar o no, informándole de las consecuencias
def callReboot():
    print("\n")
    print("##################################################################")
    print("\n")
    print("ATENCION: ¿Confirma la operación de reiniciar el sistema?         ")
    print("Escriba \"si\" o \"no\".")
    confirmation = str(input())
    count = 10
    if confirmation == "si": 
        print("El sistema procederá a reiniciarse...                        ")
        while count >= 0: 
            print("Reiniciando en: " + str(count) + " segundos.")
            time.sleep(1)
            count -= 1
        subprocess.run(["sudo reboot"],shell=True)
    elif confirmation == "no":
        print("\n")
        print("Ha seleccionado no reiniciar. Recuerde que no podrá utilizar ")
        print("correctamente ninguna de los alias o herramientas de docker  ")
        print("hasta que reinicie esta máquina.                             ")
    else:
        print("\n")
        print("EL script solo acepta 'si' o 'no'. Queda de su mano reiniciar") 
        print("el sistema para que los alias y los permisos cobren efecto   ") 
   
### Script ###
print("#########################################################################")
print("### Script de instalación y configuración de Docker + Vega(Subgraph) ####")
print("#########################################################################")
print("\n")
print("Este script procederá a instalar Docker en caso de que este no se        ")
print("encuentre en el sistema. Luego creará una imagen para Vega desde un      ")
print("Dockerfile y finalizará configurando la máquina host para que al escribir")
print("'Docker_Vega-up' desde una terminal se ejecute la aplicación en la       ")
print("máquina host.\n")
print("#########################################################################")
print("\n")
print("IMPORTANTE: El USUARIO que se utilizará para configurar Docker será:     ")
current_user = os.environ.get('USER')
print(current_user)
print("\n")
print("IMPORTANTE: A la finalización del script, el sistema le pedirá que       ")
print("confirme una  petición de REINICIO. Esto es necesario para que el usuario")
print("actual entre en el grupo Docker correctamente y así poder ejecutar la    ")
print("imagen de Vega, crear contenedores, etc.                                 ")
print("\n")
print("¿DESEA CONTINUAR CON LA EJECUCIÓN? Escriba \"si\" o \"no\".              ")
confirmation = str(input())
print("\n")
print("#########################################################################")

if confirmation == "si":
    # Comprueba si "Docker.io" está instalado en el sistema.
    command = "sudo apt install docker-ce -y"
    docker_ce_status = subprocess.call([command] , shell=True)
    if docker_ce_status == 0:
        print("Docker ya está instalado. Procediendo a la creación de la imagen.")
        changeDockerDataDirectory()
        runDockerFile()
        createHostAlias()
        callReboot()
    else:
        installDocker()
        changeDockerDataDirectory()
        runDockerFile()
        createHostAlias()
        callReboot()
elif confirmation == "no":
    print("Ha escrito 'no', saliendo del script.                                ")
else:
    print("Ha escrito '" + confirmation + "', saliendo del script.              ")