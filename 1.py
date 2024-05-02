import threading, time, datetime, requests, random, json, tls_client,string
from colorama      import *
from pystyle       import *
from libs.utils import *
from bs4 import BeautifulSoup as bs

#region Logger
class log:
    lock = threading.Lock()

    def success(text):
        time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
        with log.lock:
            print(Colors.gray + time_now + " " + Colorate.Horizontal(Colors.green_to_cyan, "SUCCESS", 1) + Colors.gray + " > " + Colors.light_gray + text + Colors.reset)

    def error(text):
        time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
        with log.lock:
            print(Colors.gray + time_now + " " + Colorate.Horizontal(Colors.red_to_purple, "ERROR", 1) + Colors.gray + " > " + Colors.light_gray + text + Colors.reset)

    # def captcha(cap_token, time_n):
    #     time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
    #     with log.lock:
    #         print(Colors.gray + time_now + " " + Colorate.Horizontal(Colors.blue_to_cyan, "CAPTCHA", 1) + Colors.gray + " > " + Colors.light_gray + f"[{Colors.light_gray}{cap_token[:16]}...{Colors.gray}] [{Colors.light_gray}{str(time_n)}{Colors.gray}]" + Colors.reset)

    def captcha(cap_token):
        time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
        with log.lock:
            print(Colors.gray + time_now + " " + Colorate.Horizontal(Colors.blue_to_cyan, "CAPTCHA", 1) + Colors.gray + " > " + Colors.light_gray + f"[{Colors.light_gray}{cap_token[:16]}...{Colors.gray}]" + Colors.reset)


    def humanized(data):
        time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
        with log.lock:
            print(Colors.gray + time_now + " " + Colorate.Horizontal(Colors.purple_to_blue, "HUMANIZED", 1) + Colors.gray + " > (" + Colors.light_gray + data + Colors.gray + ")" + Colors.reset)

    def unlocked(token):
        time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
        with log.lock:
            print(Colors.gray + time_now + " " + Colorate.Horizontal(Colors.green_to_cyan, "UNLOCKED", 1) + Colors.gray + " > " + Colors.light_gray + token[:30] + "..." + Colors.reset)

    def locked(token):
        time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
        with log.lock:
            print(Colors.gray + time_now + " " + Colorate.Horizontal(Colors.red_to_purple, "LOCKED", 1) + Colors.gray + " > " + Colors.light_gray + token[:30] + "..." + Colors.reset)

    # def onlined(token):
    #     time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
    #     with log.lock:
    #         print(Colors.gray + time_now + " " + Colorate.Horizontal(Colors.blue_to_wTestte, "ONLINED", 1) + Colors.gray + " > " + Colors.light_gray + token[:30] + "..." + Colors.reset)

    def verified(token, email):
        time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
        with log.lock:
            print(Colors.gray + time_now + " " + Colorate.Horizontal(Colors.yellow_to_red, "VERIFIED", 1) + Colors.gray + " > " + Colors.light_gray + f"[{Colors.light_gray}{token[:30]}...{Colors.gray}] [{Colors.light_gray}{email}{Colors.gray}]" + Colors.reset)
print("======LOGGING TEST======")
log.success("Test")
log.captcha("Test")
log.error("Test")
log.humanized("Test")
log.locked("Test")
log.unlocked("Test")
log.verified("Test", "test@mail7.io")
print("======LOGGING TEST======")
#endregion

def login(proxy, mail,pw):
    try:
        req=requests.Session()
        req.proxies.update({'http': proxy, 'https':proxy})

        req.headers.update({
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en_US','cache-control': 'max-age=0',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'})
        res=req.get("https://m.facebook.com").text
        inspect=bs(res,'html.parser')
        lsd_key=inspect.find('input',{'name':'lsd'})['value']
        jazoest_key=inspect.find('input',{'name':'jazoest'})['value']
        m_ts_key=inspect.find('input',{'name':'m_ts'})['value']
        li_key=inspect.find('input',{'name':'li'})['value']
        try_number_key=inspect.find('input',{'name':'try_number'})['value']
        unrecognized_tries_key=inspect.find('input',{'name':'unrecognized_tries'})['value']
        bi_xrwh_key=inspect.find('input',{'name':'bi_xrwh'})['value']
        data={
        'lsd':lsd_key,'jazoest':jazoest_key,
        'm_ts':m_ts_key,'li':li_key,
        'try_number':try_number_key,
        'unrecognized_tries':unrecognized_tries_key,
        'bi_xrwh':bi_xrwh_key,'email':mail,
        'pass':pw,'login':"submit"}
        response_body2=req.post("https://m.facebook.com/login.php",data=data,allow_redirects=True,timeout=300)
        open("resopnse.html",'wb').write(response_body2.content)
        cookie=str(req.cookies.get_dict())
        if 'checkpoint' in cookie:return {'working':False,'checkpoint': True}
        elif 'c_user' in cookie:
            return {'working':True,'checkpoint': False}
            
        else:
            return {'working':False,'checkpoint': None}
    except requests.exceptions.ConnectionError:return {"working":None}

# br = mechanize.Browser()
# def workingCheck(id, pwd):
#         try:
#             sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
#             data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
#             x=hashlib.new("md5")
#             x.update(sig.encode())
#             a=x.hexdigest()
#             data.update({'sig':a})
#             urlc = "https://api.facebook.com/restserver.php"
#             r=requests.get(urlc,params=data)
#             z=json.loads(r.text)
#             print(z)
#             # unikers = open("login.txt", 'w')
#             # unikers.write(z['access_token'])
            
#             # unikers.close()
#             # if('save-device' in url):
#             #     return {"checkpoint":False, "verified": True, "consented": True}
#             # elif "confirmemail" in url:
#             #     return {"checkpoint":False, "verified": False, "consented": False}
#             # elif "consent_framework" in url:
#             #     return {"checkpoint":False, "verified": True, "consented": False}
#             # else:
#             #     print(url)
#         except requests.exceptions.ConnectionError:
#             return "networkerror"
from bs4 import BeautifulSoup
import random
import string

def main(proxy, mail, pw):
    p = profile()
    g = getHeader('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    s = tls_client.Session(client_identifier="opera_91", random_tls_extension_order=True)
    # print(s.get("https://httpbin.org/ip",proxy=proxy).text)
    lsd=""
    s.get("https://mbasic.facebook.com",headers=g.getHeaderbyActivity('get'),proxy=proxy )
    while(True):
        try:
            details = s.get("https://mbasic.facebook.com/reg", headers=g.getHeaderbyActivity('get'),proxy=proxy)
            soup = BeautifulSoup(details.text, "html.parser")
            lsd = soup.find("input", attrs={"name": "lsd"})['value']
            break
        except:
            return
            pass

    reg_instance = soup.find("input", attrs={"name": "reg_instance"})['value']
    reg_impression_id = soup.find("input", attrs={"name": "reg_impression_id"})['value']

    lsd = details.text.split('name="lsd" value="')[1].split('"')[0]
    jazoest = details.text.split('name="jazoest" value="')[1].split('"')[0]
    print("Fetched ->")
    print("    jazoest  > " + jazoest)
    print("    lsd      > " + lsd)
    print("    instance > " + reg_instance)
    print("    reg_impr > " + reg_impression_id)
    print()

    reg = s.post('https://mbasic.facebook.com/reg/submit/', cookies=s.cookies, headers=g.getHeaderbyActivity("reg"), proxy=proxy,
        data={
            'lsd': lsd,
            'jazoest': jazoest,
            'ccp': '2',
            'reg_instance': reg_instance,
            'submission_request': 'true',
            'helper': '',
            'reg_impression_id': reg_impression_id,
            'ns': '0',
            'zero_header_af_client': '',
            'app_id': '',
            'logger_id': '',
            'field_names[]': [
                'firstname',
                'reg_email__',
                'sex',
                'birthday_wrapper',
                'reg_passwd__',
            ],
            'lastname': p['first'],
            'firstname': p['last'],
            'reg_email__': mail,
            'sex': str(p['sex']),
            'custom_gender': '',
            'did_use_age': 'false',
            'birthday_year': random.randint(1905, 2010),
            'birthday_month': random.randint(1, 12),
            'birthday_day': random.randint(1, 28),
            'age_step_input': '',
            'reg_passwd__': pw,
            'korean_tos_is_present': 'true',
            'checkbox_privacy_policy': 'on',
            'checkbox_tos': 'on',
            'checkbox_location_policy': 'on',
            'submit': 'Sign up',
        })
    
    if reg.status_code == 200:
        print(reg.text)
        print(f"{mail} {pw} | Proxy mail issue. Phone locked")
    elif reg.status_code == 302:
        print(reg.text)
        print("Respones -> 302")
        stat = login(proxy=proxy, mail=mail, pw=pw)
        print(stat)

def random_char(char_num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))
with open('proxies.txt', 'r') as file:
    proxies = file.readlines()

main("http://"+random.choice(proxies).replace("\n",""),f"{random_char(7)}@web.de", random_char(10)+"!")
