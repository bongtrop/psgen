##########
Name: "find-file"
Author: "bongtrop"
Description: "Find files from their filename"
Options:
    path: "Seaching path (Ex. c:\\)"
    pattern: "Filename pattern (Ex. *.bak*)"
##########
Get-ChildItem -Path {{ path }} -Include {{ pattern }} -File -Recurse -ErrorAction SilentlyContinue