# Scallop

This is a minimal toy shell written in Python.  It was written as a learning exercise.

I wrote a few blog posts about it [here](https://nsreeen.github.io/tags/shell/).

## Features
Features implemented:
- system calls (eg. ls, mkdir, etc.)
- cd
- `&&` command
- pipes

Sample:
```
Scallop>> mkdir hello
Scallop>> cd hello
Scallop/hello>> cd ..
Scallop>> echo hi && echo bye
hi
bye
Scallop>> ls
hello  README.md  scallop.py
Scallop>> ls | wc
      3       3      27
```

## Usage
To run from the root directory:
`python3 scallop.py`

## Resources
The following resources helped me understand shells and write this:
https://github.com/tokenrove/build-your-own-shell
https://github.com/kamalmarhubi/shell-workshop
https://github.com/bminor/bash
https://www.aosabook.org/en/bash.html
https://docs.python.org/3/library/os.html
