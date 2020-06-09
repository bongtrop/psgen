##########
Name: example
Author: Jusmistic
Description: Print a word [COUNT] time(s)
Options:
    word: "The word that you want to print"
    count: "Times you want to print the word"
##########

For ($i=0; $i -lt {{ count }}; $i++) {
    Write-Host "{{ word }}";
}