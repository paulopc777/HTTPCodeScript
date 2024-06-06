
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
            print(f"{Fore.YELLOW} [-] {Fore.WHITE} - {Dominio} - HTTP BLOCK - {Fore.YELLOW}{Statuscode}")
            return Statuscode
    except requests.exceptions.ConnectionError or requests.exceptions.ReadTimeout as e:
            print(f"{Fore.RED} [x] {Fore.WHITE} - {Dominio} - NOT HTTP - {Fore.RED}CLOSE")
        
def Create_Output(Array:list,name:str):
     with open(name, 'w') as arquivo:
           for Objeto in Array:
               arquivo.write(f"{Objeto}\n")
    
def SaveAndArquivo(ArquivoEntrada:str,ArquivoSaida:str,statusCode:int):
    
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
                else:
                    if Get_Sattus_Code(Site) == statusCode:
                        meu_array_200.append(Site)
                        
        if ArquivoSaida:            
            OutputFile = ArquivoSaida + ".txt"            
            Create_Output(meu_array_200,OutputFile)
        else:
            return meu_array_200
        
    except FileNotFoundError:
        print(f"{Fore.YELLOW}start.py -h")
        print(f"{Fore.YELLOW}Input File not Fund")

def Onechar(Input:str,ArquivoSaida:str,statusCode:int):
  
    meu_array_200 = []
    
    try:  
        Site = Input
        
        if Site == "":
            print(f"{Fore.YELLOW}start.py -h")
            print(f"{Fore.YELLOW}Input.txt:")
            print(f"{Fore.YELLOW}Website.com.br")
            print(f"{Fore.YELLOW}www.Site.com.br")
            print(f"{Fore.YELLOW}http://www.Site.com.br")
            print(f"{Fore.WHITE}")
        else:
            if Get_Sattus_Code(Site) == statusCode:
                meu_array_200.append(Site)
            
            if ArquivoSaida:            
                OutputFile = ArquivoSaida + ".txt"            
                Create_Output(meu_array_200,OutputFile)
            else:
                return meu_array_200
        
    except FileNotFoundError:
        print(f"{Fore.YELLOW}start.py -h")
        print(f"{Fore.YELLOW}Input File not Fund")

def Prompt():
    # Print Logos
    print(f"{Fore.YELLOW}\n")
    PrintLogo()
    
    if len(sys.argv) <= 1:
        print(f"{Fore.YELLOW}start.py -h")
        print(f"{Fore.YELLOW}Uso: python start.py -i arquivoInput.txt -o arquivoOutput -sv403")
        print(f"{Fore.WHITE}")
        sys.exit(1)
    
    #Numero de argumentos passados contando -i -o etc...
    #Pedindo o Minimo que e -i = Input & -sv 
    
    pedidominimo = 1
    
    if len(sys.argv) >= pedidominimo:
        
        # argumentos
        Input=False
        Output=False
        Verbose=False
        Save=200
        
        # Passando por todos os argumentos passados
        for i in range(len(sys.argv)):
            data = i + 1
            if sys.argv[i] == "-i":
                Input = sys.argv[data]
            if sys.argv[i] == "-o":
                Output = sys.argv[data]
            if sys.argv[i] == "-v":
                Verbose = True
            if sys.argv[i] == "-sv":
                Save=int(sys.argv[data])
                
                
        if ".txt" in Input:
            # Casso tenha passado um arquivo 
            SaveAndArquivo(Input,Output,Save)
        else:
            SiteFormat = Text_Format(Input)
            Onechar(SiteFormat,Output,Save)
            # Casso não tenh apassado
                
    print(f"{Fore.WHITE}")
    print("\n")

Prompt()

