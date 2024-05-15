
from colorama import Fore # type: ignore
import requests  # type: ignore
import sys

    
def PrintLogo():
    linha1 = f"{Fore.GREEN} ███████ ███████ ████████{Fore.RED} ██    █  █      █"
    linha2 = f"{Fore.GREEN} ██      ██      ██    ██{Fore.RED} █ █   █  █      █"
    linha3 = f"{Fore.GREEN} ███████ ██      ██    ██{Fore.RED} █  █  █   █ ██ █ "
    linha4 = f"{Fore.GREEN}      ██ ██      ████████{Fore.RED} █   █ █  █ █  █ █"
    linha5 = f"{Fore.GREEN} ███████ ███████ ██    ██{Fore.RED} █    ██  █      █"
    linha6 = f"{Fore.CYAN} ╚═══════════════════════{Fore.CYAN}═══════╝           "
    print(linha1)
    print(linha2)
    print(linha3)
    print(linha4)
    print(linha5)       
    print(linha6)   
    print(f"\n")        
         
def Text_Format(Domian:str):
    FormaDomain = ""
    
    if Domian.find("https://www.") == -1 and Domian.find("www.") == -1 and Domian.find("https://") == -1:
        # FormaDomain = "https://www." + Domian
        FormaDomain = "https://" + Domian
        # print(FormaDomain + "1")
        return FormaDomain
    
    elif Domian.find("https://") == -1 and Domian.find("www.") >= 0 :
        FormaDomain = "https://" + Domian
        
        # print(FormaDomain + "2")
        return FormaDomain
    elif Domian.find("https://") >= 0 and Domian.find("www.") == -1  :
        FormaDomain = Domian.replace("https://", "https://www.")
        # print(Domian + "3")
        return FormaDomain
    else:
        # print(Domian + "4")
        return Domian

def Get_Sattus_Code(Dominio:str):

    try:
        getCode = requests.get(Dominio,timeout=5)
        Statuscode = getCode.status_code
        
        if Statuscode == 200:
            print(f"{Fore.GREEN} [+] {Fore.WHITE} - {Dominio} - HTTP OPEN - {Fore.GREEN}{Statuscode}")
            return Statuscode
        else:
            print(f"{Fore.RED} [-] {Fore.WHITE} - {Dominio} - HTTP CLOSE - {Fore.RED}{Statuscode} ")
            return Statuscode
    except requests.exceptions.ConnectionError or requests.exceptions.ReadTimeout as e:
        print(f"{Fore.RED} [-] {Fore.WHITE} - {Dominio} - {Fore.YELLOW}ERROR")
        
def Create_Output(Array:list,name:str):
     with open(name, 'w') as arquivo:
           for Objeto in Array:
               arquivo.write(f"{Objeto}\n")
    
def Start(ArquivoEntrada:str,ArquivoSaida:str):
    meu_array_200 = []
    
    try:
        with open(ArquivoEntrada , 'r') as arquivo: 
            for linha in arquivo:
                Site = Text_Format(linha.strip())
                if Site == "":
                    print(f"{Fore.YELLOW}start.py -h")
                    print(f"{Fore.YELLOW}Input.txt:")
                    print(f"{Fore.YELLOW}Website.com.br")
                    print(f"{Fore.YELLOW}www.Site.com.br")
                    print(f"{Fore.YELLOW}http://www.Site.com.br")
                    print(f"{Fore.WHITE}")
                    return
                else:
                    if Get_Sattus_Code(Site) == 200:
                        meu_array_200.append(Site)
                        return
                                    
        OutputFile = ArquivoSaida + ".txt"            
        Create_Output(meu_array_200,OutputFile)
    except FileNotFoundError:
        print(f"{Fore.YELLOW}start.py -h")
        print(f"{Fore.YELLOW}Input File not Fund")
    
def Prompt():
    print(f"{Fore.YELLOW}\n")
    PrintLogo()
    # print(f"{Fore.YELLOW}Uso: python start.py -o arquivo.txt")
    
    if len(sys.argv) <= 1:
        print(f"{Fore.YELLOW}start.py -h")
        print(f"{Fore.YELLOW}Uso: python start.py -i arquivoInput.txt -o arquivoOutput -sv403")
        print(f"{Fore.WHITE}")
        sys.exit(1)
    
    arg_1 = sys.argv[1]
    if len(sys.argv) >= 4:
        arg_2 = sys.argv[3]

        if arg_1 == "-i" and arg_2 == "-o" and  len(sys.argv) >= 4:
            nome_arquivo_entrada = sys.argv[2]
            nome_arquivo_saida = sys.argv[4]
            Start(nome_arquivo_entrada,nome_arquivo_saida)
        else:
            print("Argumento inválido ou nome do arquivo não fornecido corretamente.")
    elif arg_1 == "-h":
        print(f"{Fore.RED}TIPOS DE USO")
        print(f"{Fore.GREEN}Uso: python start.py -i arquivoInput.txt -o arquivoOutput \n")
        
        print(f"{Fore.GREEN}Uso: python start.py -i arquivoInput.txt -o arquivoOutput -sv403")
        print(f"{Fore.CYAN}Salva Codes = 403")
    else:
        print("Argumento inválido ou nome do arquivo não fornecido.")
    
    print(f"{Fore.WHITE}")
    print("\n")

Prompt()

