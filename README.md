<h1 align="center">phishreport</h1>

### MAINTAINERS

- Vandré Augusto, Twitter: [@dr1nKoRdi3][tw-drink] Github: [@dr1nK0Rdi3][git-drink]
- Ialle Teixeira, Twitter: [@MalwareHunterBR][tw-root] Github: [@ironbits][git-root]

##### OTHER CONTRIBUTORS

- Franklin Timoteo, Github: [@franklintimoteo][git-ftimoteo]

### PREREQUISITES

- [phishtank registered account][phishtank]
- Python 3.x
- pip3
- setuptools
- huepy
- requests

### TESTED ON

- Kali Linux – Rolling Edition

- Linux Mint – 18.3 Sylvia

- Slackware Linux – 14.2

- Debian – 9.4 stretch

### CLONE

```sh
$ git clone https://github.com/dr1nk0rdi3/phishreport
```
### RUNNING
```sh
$ cd phishreport
$ sudo apt install python3-pip
$ sudo pip3 install -r requirements.txt
$ python3 phishreport.py --help
```

### pyfiles account.py

```python

#!/usr/bin/python3
#set login and password

def account():

    user = 'user'
    passwd = 'password'
    return {'username': user, 'password': passwd}
```

### HELP

```sh
usage: phishreport.py [-h] [-l | -p Phish_list] [-r NUM_REPORT]
                      [-i NUM_INTERVAL] [-e] [-v]

Report phishing for www.phishtank.com

optional arguments:
  -h, --help            show this help message and exit
  -l, --list-org        Show list of organizations
  -p Phish_list, --phish-list Phish_list
                        Specify a file with a list of URLs for report
  -r NUM_REPORT, --set-report NUM_REPORT
                        Specify the number of reports
  -i NUM_INTERVAL, --set-interval NUM_INTERVAL
                        Specify the interval between reports
  -e, --exclude         Exclude rows that have been reported
  -v, --verbose         Show status of reports

Example:

    key defaults:
        default interval:           6 seconds
        default exclude rows:       False
        default verbose:            False

    usage for:

        python3 phishreport.py --phish-list file.csv --set-report 50
        python3 phishreport.py --phish-list file.txt --set-report 50 --set-interval 2 --exclude --verbose
    or: 
        Show list of organizations
        python3 phishreport.py --list-or
```

### CSV FILE

phishing            | organization number victim | message contained in email |
| ----------------- | -------------------------- | -------------------------- |
| https://itsfakehere.com | 8:others | click to get discounts |

 **example of the first line:** _https://itsfakehere.com ;8;click to get discounts_

### TELEGRAM

- [UndeadSec][undeadsec]       
- [MalwareverseBR][mlwr]

### SCREENSHOT

![phishreport](https://raw.githubusercontent.com/dr1nk0rdi3/phishreport/master/images/phishreport.png)

[//]: # (REFERENCES)

[tw-drink]: <https://twitter.com/Dr1nkOrdi3>
[git-drink]: <https://github.com/dr1nk0rdi3>
[tw-root]: <https://twitter.com/malwarehunterbr> 
[git-root]: <https://github.com/ironbits>
[git-ftimoteo]: <https://github.com/franklintimoteo>
[phishtank]: <https://www.phishtank.com/register.php>
[undeadsec]: <t.me/UndeadSec>
[mlwr]: <t.me/MalwareverseBR>
