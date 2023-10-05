# Español  
## Documentación sobre Vega:  
https://subgraph.com/vega/documentation/index.en.html  
https://github.com/subgraph/Vega  

## ¿Qué es Vega?
Vega es una herramienta de código abierto que busca vulnerabiliadades conocidas en  
entornos web. Entre sus principales funciones, se pueden encontrar las siguientes:  
- Escaneo de dominios y URLs utilizando un grafo/árbol que permite definir la  
profundidad de la búsqueda.  
- Permite definir el grado de intensidad en los escanenos/ataques para evitar  
ser bloqueado por los sistemas de seguridad o para no afectar el rendimiento en una  
infraestructura limitada.
- Tiene funciones de escáner en modo proxy, lo que permite identificar vulnerabilidades  
según se navega en un sitio, en tiempo real.  
-  Realiza una serie de ataques en busca de vulnerabilidades comunes. Una vez encontrada  
clasifica su grado de importancia, da una descripción del problema, donde se encontró y  
como se podría llegar a mitigar/solucionar.  
  
### Advertencia
1. Antes de utilizar Vega sobre una web/dominio, asegúrese de tener el permiso para  
hacerlo por parte de la empresa, organización o persona propietaria. De no ser así,  
esto podría llevarlo a una demanda por parte del afectado.   
2. Actualmente no existe una opción para generar un informe o reporte dentro de Vega,  
lo que limita su utilidad.  
3. La herramienta no recibe actualizaciones desde hace bastante tiempo.  

## ¿Qué hace este script?
Este script instala Vega haciendo uso de Docker dado que necesita una serie de dependencias  
que ya no se encuentran en los repositorios de las diversas distribuciones Linux más actualizadas.    
  
Para que la instalación de Vega comience, puede ejecutar el script en este directorio o utilizar  
una ruta absoluta desde cualquier directorio:  
1. Sitúese dentro de '/opt'  
2. Clone este repositorio dentro de '/opt' quedando algo como '/opt/Vega_Docker'
3. 'sudo chown -R dummy:dummy /opt/Vega_Docker', donde "dummy" es el usuario que va a ejecutar  
el script.
4. find Vega_Docker -type f -name "*.sh" -exec chmod u+x {} +
5. find Vega_Docker -type f -name "*.py" -exec chmod u+x {} +


Este script se encagará de instalar y configurar todo lo necesario para que la aplicación de  
Vega esté operativa. El script hace lo siguiente:  
- Comprueba si Docker está en el sistema y lo instala si fuera necesario.  
- Configura al usuario actual con permisos para poder utilizar Docker y sus herramientas.  
- Llama al Dockerfile para crear la imagen.  
- Crea un alias "Docker_Vega_up" en la máquina host para simplificar la  
ejecución del contenedor, abriendo Vega con su interfaz gráfica.  
- Ejecuta un reinicio de la máquina para actualizar los permisos del usuario y el alias.  

# ENGLISH
## About Vega:  
https://subgraph.com/vega/documentation/index.en.html  
https://github.com/subgraph/Vega  

## ¿What is Vega?  
Vega is an Open Source tool which works on Web environments and tries to find any common/uncommon  
vulnerability in a domain or URL. Its main capabilities are:    
- URL and domain scanning using a tree/graph search algorithm which allows to specify the depth level of search.  
- It offers the option of adjunsting the intensity of the scan/attack. It is useful due to the   posibility of avoiding getting blocked/banned by the site as well as adjust the pressure on a  weak infrastructure.
- It can work as an proxy scanner too, which allows to get vulnerabilities from the browser in   real time.  
- Finally, it makes a series of common/uncommon attacks in order to find a vulnerability. Once   found, then proceds to assign them a priority level based on its risk, a description of the   scenario, a suggestion of a possible solution and where it was  
found.

## Disclaimer
1. Before starting a scan on a certain domain/url, ensure that you have the rights granted by   the owner. This can carry to a demmand by the affected if not done properly.  
2. Actually, it doesnt exist the option of exporting the results of the scan in a report format,  text documment, etc.  
3. This tool hasn't been updated in a long time.  

## What this script does
This script installs Vega in a Docker container due to some repositories being missing from the   latest Linux distributions repositories.  

In order to install Vega with this script, I follow this process (as an example):  
1. Locate yourself inside '/opt'  
2. Clone this repository inside '/opt' resulting in something like '/opt/Vega_Docker'
3. 'sudo chown -R dummy:dummy /opt/Vega_Docker', where "dummy" is the user/group that you want   to grant the script permissions.  
4. find Vega_Docker -type f -name "*.sh" -exec chmod u+x {} +
5. find Vega_Docker -type f -name "*.py" -exec chmod u+x {} +

Once the permissions are granted, you can just execute './intall_vega_docker.py' or  '/opt/Vega_Docker/install_vega_docker.py' to start the installation script.  

This script makes and ensures the following steps:  
- Checks if Docker is already installed on the system. If not, proceds its installation and  configuration.  
- Grants Docker permissions to the the current user.
- Executes the Dockerfile in order to create the image.  
- Creates an alias 'Docker_Vega_up' that calls the container from the console as a way of   simplify the execution of the application. This alias opens the Vega GUI without the need of   typing the full Docker command.    
- At the end of the installation the system will try to restart because it is needed for the  correct execution of the alias and Docker itself. This restart  can be  avoided on the first  steps since the scripts already ask if the user wants to run this process at the end.    










