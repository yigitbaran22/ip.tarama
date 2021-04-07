#!/usr/bin/env python
import os
import time
os.system("clear")
guncelleme = raw_input("""   1) Figlet
   2) NMAP
   3) Ike-Scan
   4) Nikto
   5) wafw00f
   6) Hepsi
   7) Hicbiri
Yukarida ki modullerin guncel olmasi programin calismasi icin gereklidir. Yuklemek veya guncellemek icin lutfen seciminizi belirtin: """ )
if(guncelleme == '1'):
	os.system("apt-get install figlet")
elif(guncelleme == '2'):
	os.system("apt-get install nmap")
elif(guncelleme == '3'):
	os.system("apt-get install ike-scan")
elif(guncelleme == '4'):
	os.system("apt-get install nikto")
elif(guncelleme == '5'):
	os.system("apt-get install wafw00f")
elif(guncelleme == '6'):
	os.system("apt-get install figlet")
	os.system("apt-get install nmap")
	os.system("apt-get install ike-scan")
	os.system("apt-get install nikto")
	os.system("apt-get install wafw00f")
elif(guncelleme == '7'):
	pass
else:
	os.system("./Port_Tarama.py")
os.system("clear")
os.system("figlet *Yigit Baran*")
os.system("figlet *INCEDAL*")
while True:
	print("""
	Yigit Baran INCEDAL
	******************************
	
	1)Hizli Tarama
	2)Servis ve Versiyon Bilgileri
	3)Sistem Bilgileri
	4)VPN Kontrol
	5)Zaafiyet Kontrol
	6)Guvenlik Duvari Sorgulama
	7)Cikis
	
	******************************
	
	""")
	islemno = raw_input("Yapmak istediginiz islemi seciniz:")
	if(islemno == '1'):
		hedefip = raw_input("Hedef IP giriniz:")
		os.system("nmap "+ hedefip)
		dewamkee = raw_input("""
		Devam etmek icin bir tusa basiniz...
		""")
		if(dewamkee == ''):
			os.system("clear")
			pass
	elif(islemno == '2'):
		hedefip = raw_input("Hedef IP giriniz:")
		os.system("nmap -sS -sV "+ hedefip)
		dewamkee = raw_input("""
		Devam etmek icin bir tusa basiniz...
		""")
		if(dewamkee == ''):
			os.system("clear")
			pass
	elif(islemno == '3'):
		hedefip = raw_input("Hedef IP giriniz:")
		os.system("nmap -O "+ hedefip)
		dewamkee = raw_input("""
		Devam etmek icin bir tusa basiniz...
		""")
		if(dewamkee == ''):
			os.system("clear")
			pass
	elif(islemno == '4'):
		hedefip = raw_input("Hedef IP giriniz:")
		os.system("ike-scan "+ hedefip)
		dewamkee = raw_input("""
		Devam etmek icin bir tusa basiniz...
		""")
		if(dewamkee == ''):
			os.system("clear")
			pass
	elif(islemno == '5'):
		os.system("clear")
		os.system("figlet NIKTO")
		print("				Yigit Baran INCEDAL")
		hedefip = raw_input("""
Hedef IP giriniz:""")
		try:
			hedefport = raw_input("""Hedef Port giriniz. (Default: 80):""")
			hedefport = int(hedefport)
		except:
			print("""
Gecersiz bir port girdiniz. Port 80 olarak ayarlanmistir.""")
			time.sleep(1)
			hedefport = 80
		if(0 < hedefport < 65537):
			pass
		else:
			hedefport == 80
		hedefport = str(hedefport)
		os.system("nikto -h "+ hedefip +" -port " + hedefport)
		dewamkee = raw_input("""
		Devam etmek icin bir tusa basiniz...
		""")
		if(dewamkee == ''):
			os.system("clear")
			pass
	elif(islemno == '6'):
		hedefweb = raw_input("Hedef web sitesini yaziniz:")
		os.system("wafw00f "+ hedefweb)
		dewamkee = raw_input("""
		Devam etmek icin bir tusa basiniz...
		""")
		if(dewamkee == ''):
			os.system("clear")
			pass
	elif(islemno == '7'):
		os.system("clear")
		print("""Gorusuruz.""")
		time.sleep(1)
		print("1")
		time.sleep(1)
		print("2")
		time.sleep(1)
		os.system("clear")
		break
	else:
		print("""Gecersiz bir islem numarasi girdiniz.""")
		
