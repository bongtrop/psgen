##########
Name: hello-world
Author: Jusmistic
Description: Print Hello-World! [COUNT] time(s)
Options:
    count: "Times you want to print Hello world"
##########

For ($i=0; $i -lt {{ count  }}; $i++) {
    Write-Host "Hello, World!";
}