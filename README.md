# Minimal Password Generator
<b>pwgen.py</b> is a simple password generation tool that will create you a permutated list of passwords based on given input and flags.

## pwgen.py usage:
```
usage: pwgen.py [-h] [-l LENGTH] [-s] [-w WORD] [-o OUTPUT]

Minimal password generator.

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Client requirement for minimum password length.
  -s, --seasons         Enable the seasons passwords.
  -w WORD, --word WORD  Give a word to permutate like the company name.
  -o OUTPUT, --output OUTPUT
                        File to write to!
```
   Basic usage of script:
   
    python3 pwgen.py -l 8 -w contoso -s -o passwords.txt
    

   Advanced usage of pwgen.py:
   
    $ python3 pwgen.py -l 8 -w contoso -s -o passwords.txt
    [+] Wrote 1258 passwords to passwords.txt
    
   Example output of passwords.txt:
   
    Contoso2020
    contoso22!!
    springtime2018#
    Contoso15#
    spring13@
    spring22$
    Contoso21
    winter20$
    summertime2019!!
    spring21!
