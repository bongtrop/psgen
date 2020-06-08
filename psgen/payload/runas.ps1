##########
Name: "runas"
Author: "bongtrop"
Description: "Run a progrom as another user"
Options:
    username: "Username (Ex. user)"
    password: "Password (Ex. pass)"
    filepath: "Executeable filepath"
##########
$username = '{{ username }}';
$password = '{{ password }}';
$securePassword = ConvertTo-SecureString $password -AsPlainText -Force;
$credential = New-Object System.Management.Automation.PSCredential $username, $securePassword;
Start-Process {{ filepath }} -NoNewWindow -Credential $credential;