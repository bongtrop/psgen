##########
Name: Hello-world
Author: Bongtrop
Description: Print Hello-world [COUNT] Time
OPTIONS:
 - COUNT => Print Hello-world COUNT Time
##########

For ($i=0; $i -le {{ count  }}; $i++) {
    Write-Host "Hello, World!";
}
