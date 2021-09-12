#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@ruks3
# Coded by ruks
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# Instagram : https://instagram.com/_v_go?utm_medium=copy_link
# github : https://github.com/muntazir-halim
# ---------------------
import requests,time,random
from user_agent import generate_user_agent

ruks_ = '\033[1;36m'	
ruks__ = '\033[1;36m'
jruks = '\033[1;33m'
_ruks  = '\033[1;31m'
BGreen='\033[1;32m'
BRed ='\033[1;31m'
Number = 0
class start:
		
	def __init__(self,us,tok,id,count):
		self.tok=tok
		self.id=id		
		self.us=us
		self.count=count
		self.tim=time.asctime()
		self.http = requests.Session()
		
	def send_uesr(self):
		req = self.http.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=⌯  ʜɪ ѕɪʀ  ⌯\n. — — — — —  — — — — — . \n⌯ ᴜѕᴇʀɴᴀᴍᴇ : @{self.us}\n⌯ {self.tim} \n. — — — — —  — — — — —\n• Tele : @DIBIBl . @RUKS3 .')
				
	def check(self):		
		if self.count >10: print("="*30),print("Please write a number less than 10"),exit()
		self.res=self.http.get(f"https://story.snapchat.com/@{self.us}",headers={'Host': 'story.snapchat.com',
'cache-control': 'max-age=0',
'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"','save-data': 'on',
'upgrade-insecure-requests': '1',
'user-agent': generate_user_agent(),
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document'}).status_code
				
		if self.res == 200:
			print(jruks+'['+BRed+f'{Number}'+jruks+'] Unavailable'+BRed+f'-[{self.us}]')
		elif self.res == 404:
			print(jruks+'['+BGreen+f'{Number}'+jruks+'] Available'+BGreen+f' [{self.us}]')
			self.send_uesr()
		else:
			print(jruks+'['+BGreen+f'{Number}'+jruks+'] erorr '+BGreen+f' [False]') 
		
		
     #=========#

tok = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' TOKEN BOT ! -> ; '+BGreen)
id = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' ID ! -> ; '+BGreen)
try:
	count = int(input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' Character count ! -> ; '+BRed))
except:
	print("="*30)
	print("Please put numbers only")
	exit(0)
	
print("="*60)
if __name__ == '__main__':
	while True:
		Number +=1
		us_ruks = str("".join(random.choice( 'poiuytrewqasdfghjklmnbvcxz1234567890_')for i in range(count)))	
		start(us_ruks,tok,id,count).check()
