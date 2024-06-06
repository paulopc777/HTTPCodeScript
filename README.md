# ScanX
## response status codes SCRIPT HTTP

<img src="img.png" width="100%"/>

This script has a unique function of checking the **status code** returned by a site or route thereof


```mermaid
    graph LR;
        PYTHON-->GET;
        GET-->RESPONSE;
        RESPONSE-->|CODE 200|GET;
```

### Simple to use script

```powershell
[x] - python ScanX.py -h
[x] - python ScanX.py -i InpuFile.txt -o OutputFile
[x] - python ScanX.py -i InpuFile.txt -o OutputFile -sv 403
[x] - python ScanX.py -i InpuFile.txt -v 
[x] - python ScanX.py -i google.com -v 
```

**-i : Input .txt or URL.**

**-o : Opitional OutputFile.**

**-sv : Saves specific response code.**

**-v : Verbose Mode.**

By default the **OutputFile** will be all locations or routes that return *status code 200* saved in a .txt if you want to change the status code **-sv**

Be happy !
