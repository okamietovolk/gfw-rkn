import configs

print('1 - сгенерировать конфиг GFW, 2 - сгенерировать конфиг Shadowrocket')
choice = int(input())
print("Добавить в конфиг сайты, блокирующие русские ip? (напрмиер, chat.openai.com) (y/n)")
choice2 = input()

if choice == 1:    
    configs.fckrkn_gfw(choice2)
elif choice == 2:
    configs.fckrkn_shadowrocket(choice2)    
if choice == 3:    
    configs.fcjrkn_adblock(choice2)
