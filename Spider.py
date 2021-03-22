import requests
import ctypes
import time
import re
DelayTime = 5

def Has_Been_Registered(num):
	UPNow = '{}{}'.format(UserPage, num)
	requests.get(UPNow, headers=headers)
	resp=requests.get(UPNow, headers=headers)
	if re.search(Te, resp.text) is not None:
		return False
	else:
		return True

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
UserPage = 'https://www.luogu.com.cn/user/'
UPNow = "https://www.luogu.com.cn/user/500000"

Te=re.compile(".*?出错了",re.S)
now = 499735
tp = 19
while (1):
	if (tp < 0):
		break
	nxt = now + 2 ** tp
	if (Has_Been_Registered(nxt)):
		now = nxt
	tp = tp - 1
	print(now)
if (Has_Been_Registered(now + 1)):
	now = now + 1
print(now)
lst = now
while (1):
	while (Has_Been_Registered(now+1)):
		now = now + 1
	print(now)
	if (now != lst):
		ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True)
	lst = now
	time.sleep(DelayTime)






