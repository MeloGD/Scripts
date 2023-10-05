# Dockerfile para Vega-Subgraph en Ubuntu 18.04
FROM 		ubuntu:18.04
# Instalación de paquetes necesarios
RUN   		apt-get update && apt-get install -y \ 
			libwebkitgtk-1.0-0 \
			default-jre	
# Traspaso de ficheros necesarios, tanto Vega como Java 8
COPY		./Dependencias/vega.tar.gz  /tmp
COPY		./Dependencias/jdk-8u202-linux-x64.tar.gz \
			./Dependencias/install_java8_container.py /usr/lib/jvm/
# Descompresión de Java 8 y ejecución del script de configuración
WORKDIR 	/usr/lib/jvm
RUN			tar -xf jdk-8u202-linux-x64.tar.gz
RUN			./install_java8_container.py
# Descompresión de Vega y eliminación de ficheros no necesarios 
RUN			tar -xf /tmp/vega.tar.gz -C /opt/
RUN			rm -rf /tmp/vega.tar.gz \
			/usr/lib/jvm/jdk-8u202-linux-x64.tar.gz \
			/urs/lib/jvm/install_java8_container.py
# Creación del usuario y asignación de permisos para poder ejecutar Vega
# ¡ATENCIÓN! Cambiar /home/user por la ruta que se desee utilizar
RUN			groupadd -r dummy && useradd -ms /bin/bash dummy -g dummy
RUN			chown -R dummy:dummy /opt/vega
# ¡ATENCIÓN! Cambiar /home/user por la ruta que se desee utilizar
WORKDIR		/home/dummy
# Variable de entorno DISPLAY que permite lanzar la GUI de Vega a la máquina 
# host
ENV			DISPLAY ":0"
# Usuario por defecto con el que funcionará el contenedor
USER		dummy
# Exportación de la aplicación de Vega para facilitar la ejecución desde 
# el terminal en la máquina host
RUN		echo "export PATH=$PATH:/opt/vega/" >> .bashrc
ENTRYPOINT	["/opt/vega/Vega"]
