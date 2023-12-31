import json
import requests
import base64

print('1 - сгенерировать конфиг GFW, 2 - сгенерировать конфиг Shadowrocket')
choice = int(input())
blocklist = requests.get("https://reestr.rublacklist.net/api/v3/ct-domains/")
blocklist = blocklist.json()

# Генерация конфига GFW

if choice == 1:    
    with open('fckrkn_GFW.txt', 'w') as f:
        f.write('!---------403/451/503/520 & URL Redirects---------')
        f.write('\n')
        f.write('! HomePage: https://github.com/okamietovolk/gfw-rkn')
        f.write('\n')
        for site in blocklist:
            line = "||" + site
            f.write(line)
            f.write('\n')
            print(site)
        f.write('!################Whitelist End##################')
        f.write('\n')
        f.write('!---------------------EOF-----------------------')

#base64

    with open('fckrkn_GFW.txt', 'r') as f:
        content = f.read()

    encoded_content = base64.b64encode(content.encode()).decode()
    with open('fckrkn_GFW.txt', 'w') as f:
        f.write(encoded_content)

# Генерация конфига shadowrocket
elif choice == 2:
        with open('fckrkn_shadowrocket.conf', 'w') as f:
            f.write('[General]\nprivate-ip-answer = true\nalways-real-ip = \nbypass-system = true\nskip-proxy = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, localhost, *.local, captive.apple.com\ntun-excluded-routes = 10.0.0.0/8, 100.64.0.0/10, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.18.0.0/15, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0/4, 255.255.255.255/32\ndns-server = 8.8.8.8, 1.1.1.1/nipv6 = false\n\n[Rule]')
            for site in blocklist:
                line = "DOMAIN-KEYWORD," + site + ",PROXY"
                f.write(line)
                f.write('\n')
                print(site)
            f.write('[Host]\nlocalhost = 127.0.0.1')
       