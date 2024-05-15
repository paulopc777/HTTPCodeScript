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
```

The **OutputFile** will be all locations or routes that return *status code 200* saved in a .txt

Be happy !
