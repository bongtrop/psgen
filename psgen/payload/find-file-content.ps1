##########
Name: "find-file-content"
Author: "bongtrop"
Description: "Find files from their content"
Options:
    path: "Seaching path (Ex. c:\\)"
    pattern: "Content pattern (Ex. *https://*)"
##########
Get-ChildItem -Path {{ path }} -Recurse | Select-String -Pattern {{ pattern }}