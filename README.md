# psgen

![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg)

psgen is a powershell payload generator tool for hacking. It can be used to generate, minify, and encode the powershell payload (e.g., reverse-shell, download-file, runas) to copyable text format.



## Installation

### Manual

The latest zip ball can be downloaded [HERE](https://github.com/bongtrop/psgen/archive/master.zip). Or perform the following commands.

```bash
git clone https://github.com/bongtrop/psgen.git
cd psgen
pip install -r requirements.txt
python setup.py install
```
### PIP

Easily install with the following command.

```bash
pip install git+https://github.com/bongtrop/psgen.git
```

## Usage

For getting list of options, please perform:

```bash
psgen -h
```

## Example

For usage example, I generate and exeute hello-world payload:

```
$ psgen -l

Powershell Payloads
===================
╒══════════════════════╤═══════════════╤══════════════════════════════════════════╕
│ Name                 │ Author        │ Description                              │
╞══════════════════════╪═══════════════╪══════════════════════════════════════════╡
│ check-dir-permission │ BHARAT SUNEJA │ Check directory permission               │
├──────────────────────┼───────────────┼──────────────────────────────────────────┤
│ download-file        │ Jusmistic     │ Download file from url                   │
├──────────────────────┼───────────────┼──────────────────────────────────────────┤
│ hello-world          │ Jusmistic     │ Print Hello-World! [COUNT] time(s)       │
├──────────────────────┼───────────────┼──────────────────────────────────────────┤
│ http-eval            │ bongtrop      │ Download and execute ps1 script from URL │
├──────────────────────┼───────────────┼──────────────────────────────────────────┤
│ find-file            │ bongtrop      │ Find files from their filename           │
├──────────────────────┼───────────────┼──────────────────────────────────────────┤
│ runas                │ bongtrop      │ Run a progrom as another user            │
├──────────────────────┼───────────────┼──────────────────────────────────────────┤
│ find-file-content    │ bongtrop      │ Find files from their content            │
├──────────────────────┼───────────────┼──────────────────────────────────────────┤
│ reverse-shell        │ @nikhil_mitt  │ Spawn Reverse shell                      │
╘══════════════════════╧═══════════════╧══════════════════════════════════════════╛

$ psgen hello-world count=5

Payload Detail
==============
Payload Name: hello-world
Payload Author: Jusmistic
Payload Description: Print Hello-World! [COUNT] time(s)
Payload Options: count='5', 

Payload Output
==============
powershell.exe -E RgBvAHIAKAAkAGEAPQAwADsAIAAkAGEAIAAtAGwAdAAgADUAOwAgACQAYQArACsAKQB7AFcAcgBpAHQAZQAtAEgAbwBzAHQAIAAiAEgAZQBsAGwAbwAsACAAVwBvAHIAbABkACEAIgA7AH0A

$ pwsh -E RgBvAHIAKAAkAGEAPQAwADsAIAAkAGEAIAAtAGwAdAAgADUAOwAgACQAYQArACsAKQB7AFcAcgBpAHQAZQAtAEgAbwBzAHQAIAAiAEgAZQBsAGwAbwAsACAAVwBvAHIAbABkACEAIgA7AH0A # Using Linux powershell (pwsh) to test the generated payload.
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
```

## Dev

For developing the powershell payload, the metadata must be set. And Jinja2 syntax can be used in the powershell script as follows:

**File:** payload/hello-world.ps1
```
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
```

## Note

This project creates for helping me to generate the copyable powershell payload and run it on window cmd shell. 