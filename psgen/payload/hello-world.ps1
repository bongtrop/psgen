##########
Name: Hello-world
Author: Bongtrop
Description: Print Hello-world [COUNT] Time
Options:
    count: "Times you want to print Hello world"
##########

For ($i=0; $i -le {{ count  }}; $i++) {
    Write-Host "Hello, World!";
}
