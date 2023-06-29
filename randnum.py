import webbrowser
import random
import os

# +CountryCode(2) - network destination code(3) - home location register(2) - unique code(6-7)

while True :
    os.system("cls")
    print(38*'=')
    print('Indonesian Telephone Number Generator')
    print(38*'=')
    print('\n--- Internet Provider ---')
    print('[1] Telkomsel / By.U')
    print('[2] XL Axiata / AXIS')
    print('[3] Indosat / 3')
    print('[4] Smartfren')
    provider = input('Choose the internet provider : ')

    if provider == '1':
        ndc = [811, 812, 813, 821, 822, 823, 851, 852, 853]
    elif provider == '2':
        ndc = [817, 818, 819, 859, 877, 878, 831, 832, 833, 838]
    elif provider == '3':
        ndc = [814, 815, 816, 855, 856, 857, 858, 895, 896, 897, 898, 899]
    elif provider == '4':
        ndc = [881, 882, 883, 884, 885, 886, 887, 888, 889]
    else:
        print('Option not available :(')
        
    # Random the NDC
    ndc = random.choice(ndc)

    # Random the HLR
    hlr = random.randint(00, 99)

    # Random the Unique Code
    unq1 = random.randint(00, 99)
    unq2 = random.randint(00,99)
    unq3 = random.randint(00,99)

    # Define the phone number as a string
    phone_number = '62' + str(ndc) + str(hlr) + str(unq1) + str(unq2) + str(unq3)

    # Use string formatting to create the URL string
    url = 'https://wa.me/{}'.format(phone_number)

    # Open the URL in the web browser
    webbrowser.open(url)
    again = input("\nAccess again ? (y/n) : ").lower()
    if again == "n":
        break