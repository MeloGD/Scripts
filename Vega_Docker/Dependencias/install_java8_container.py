#!/usr/bin/python3

import subprocess

### Functions ###
#def createJavaProfile():
#    subprocess.run(["echo JAVA_HOME=/usr/lib/jvm/jdk1.8.0_202 >> /etc/profile"], shell=True)
#    subprocess.run(["echo PATH=$PATH:$HOME/bin:$JAVA_HOME/bin >> /etc/profile"], shell=True)
#    subprocess.run(["echo export JAVA_HOME >> /etc/profile"], shell=True)                   
#    subprocess.run(["echo export PATH >> /etc/profile"], shell=True)                   

def readUpdateEnvironmentPath():
    java_path = ":/usr/lib/jvm/jdk1.8.0_202/bin:/usr/lib/jvm/jdk1.8.0_202/db/bin:/usr/lib/jvm/jdk1.8.0_202/jre/bin\""
    with open("/etc/environment", "r") as f:
        lines = f.readlines()
    with open("/etc/environment", "w") as f:
        aux = lines[0].strip()
        aux = aux[:-1]
        aux += java_path
        f.write(aux)

### Script ###
#createJavaProfile()
readUpdateEnvironmentPath()
subprocess.run(["update-alternatives --install  \"/usr/bin/java\" \"java\" \"/usr/lib/jvm/jdk1.8.0_202/bin/java\" 0"], shell=True)
subprocess.run(["update-alternatives --install  \"/usr/bin/java\" \"java\" \"/usr/lib/jvm/jdk1.8.0_202/bin/javac\" 0"], shell=True)
subprocess.run(["update-alternatives --set java /usr/lib/jvm/jdk1.8.0_202/bin/javac"], shell=True)
subprocess.run(["update-alternatives --set java /usr/lib/jvm/jdk1.8.0_202/bin/java"], shell=True)
