Banner = print("""
 .oOOOo.                                               .oOOOo.  o.OOoOoo       o     
o     o  o         o                                 .O     o   O             O     
O.                            O                      o          o             o     
 `OOoo.                      oOo                     O          ooOO          o     
      `O O  'OoOo. O  .oOo    o   .oOo. `OoOo.       O   .oOOo  O       .oOo. O  o  
       o o   o   O o  `Ooo.   O   OooO'  o           o.      O  o       OooO' OoO   
O.    .O O   O   o O      O   o   O      O            O.    oO  O       O     o  O  
 `oooO'  o'  o   O o' `OoO'   `oO `OoO'  o             `OooO'  ooOooOoO `OoO' O   o 
                                                                                    
                                                                                                                                                 
""")



from telegram.client import Telegram



print("First register Here "+"https://my.telegram.org/apps ")

ask_for_api_id=int(input('Enter the API_ID: '))

ask_for_api_hash=input('Enter the API_HASH: ')

ask_for_user_zip=input('Input zip Code of Your Country: ')

ask_the_number=input('Input Your Phone Number: ')

tg = Telegram(
    api_id=ask_for_api_id,  
    api_hash=ask_for_api_hash,   
    phone=('+' + ask_for_user_zip + ask_the_number),
    database_encryption_key='changeme1234'
)

tg.login()


f = open('contact.txt', 'r') # Change the file  name
cont = []
for line in f.readlines():
    
    #stripped_line = line.strip()

    cont.append(line)

f.close()  


for x in cont:

    
    response = tg.call_method('importContacts', {
        'contacts': [
            {'phone_number': x},
        ]
    })
 


    response.wait()

    user_ids = response.update['user_ids']
    if user_ids[0] == 0:
        
        print('This contact '+ x +'is NOT using Telegram.')
     
    else:
       
        print(f'¡This contact id ({user_ids[0]}) uses Telegram!.' + 'Here, the contact number ' + x)

       
