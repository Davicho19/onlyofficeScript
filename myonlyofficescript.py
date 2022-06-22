#!/usr/bin/env python
import os
os.system("clear")
print("se esta instalando posgresql")
os.system("sudo apt-get install postgresql -y")

print("se creara los parametros de su base de datos, cada campo es onlyoffice")
os.systeM("sudo -i -u postgres psql -c "CREATE DATABASE onlyoffice;"")
os.systeM("sudo -i -u postgres psql -c "CREATE USER onlyoffice WITH password 'onlyoffice';"")
os.systeM("sudo -i -u postgres psql -c "GRANT ALL privileges ON DATABASE onlyoffice TO onlyoffice;")

print("se instala rabbitmq-server")
os.systeM("sudo apt-get install rabbitmq-server -y")

print("se esta instalando nginx web-server")
os.systeM("sudo apt-get install nginx -y")
os.systeM("sudo apt-get install nginx-extras -y")

print("se instalan las dependencias de onlyoffice a su servidor")
os.systeM("sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys CB2DE8E5")
os.systeM("sudo echo "deb https://download.onlyoffice.com/repo/debian squeeze main" | sudo tee /etc/apt/sources.list.d/onlyoffice.list")

print("se cargan las actualizaciones")
os.systeM("sudo apt-get update")

print("dependencias de onlyoffice")
os.systeM("sudo apt-get install ttf-mscorefonts-installer -y")
os.systeM("sudo echo "deb http://deb.debian.org/debian $(grep -Po 'VERSION="[0-9]+ \(\K[∧)]+' /etc/os-release) main contrib" | sudo tee -a /etc/apt/sources.list")
os.systeM("sudo apt-get install onlyoffice-documentserver")
os.system("clear")

print("su onlyoffice ha sido creado puedes verificar escribiendo tu direccion ip en tu navegador de preferencia")
print("gracias por elegir este script")

