# import requests as req
from os import path, system


if path.exists("./requirements.txt"):
    with open("./requirements.txt") as file:
        libs = [i.split("==")[0] for i in file.readlines()]
    
    for lib in libs:
        print(lib)
        try:
            __import__(lib)
        except ModuleNotFoundError:
            system("pip install "+lib)


from pystyle import Col, Center, System
from Plugins.api_list import handler
from colorama import Fore
from Plugins.functions import Functions

r, g = Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX

if __name__ == "__main__":
    logo = f'''{g}

{r}SmsBomber by X-rg Community™®
{r}discord : https://discord.gg/TD6YZkbNkZ
    '''




    while True:
        System.Clear()
        print(Center.XCenter(logo))

        try:
            proxy_state = Fore.GREEN + "Enabled" if Functions.proxy_state() else Fore.RED + "Disabled"
            choices = {
                "1": "call",
                "2": "sms"      
            }
            print(f"{Col.red}[XRG-TEAM]{Col.gray} Proxies are {proxy_state}")
            print(f"{Col.red}[XRG-TEAM]{Fore.CYAN} Choices: ")

            for ch in choices:
                print(f"   {Fore.CYAN}{ch}- {Fore.GREEN}{choices[ch].capitalize()} Bomber ")
            
            print()
            choice = Functions.get_input(f"{Fore.CYAN}[XRG]{Col.gray} Enter Your Choice: {Col.green}", lambda x: x in [str(i) for i in choices])
            number = Functions.get_input(f"{Fore.CYAN}[XRG]{Col.gray} Enter the phone number {Fore.CYAN}[9xxxxxxxxx]{Col.gray}: {Col.green}", checker=lambda x: x != "" and x.isnumeric() and x.startswith("9") and len(x) == 10)
            count = Functions.get_input(f"{Fore.CYAN}[XRG]{Col.gray} Enter spam count: {Col.green}", lambda x: x.isnumeric() and int(x) >= 0)

            Functions.start(choices[choice], number, int(count))


        except KeyboardInterrupt:
            print("\n" + Fore.BLUE, "Exiting...")
            exit()
