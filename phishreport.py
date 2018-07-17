#!/usr/bin/python3

from __future__ import print_function
from sys import argv, version_info, exit

if version_info < (3,0,0): raise SystemExit('Python 3+!')

from requests import Session, ConnectionError
from csv import reader, writer
from huepy import *
from time import sleep, strftime
from pyfiles.orgs import Organization
from pyfiles.account import account
from pyfiles.parse import parse_args
from pyfiles.banner import banner

def login():
    
    url_login = 'https://www.phishtank.com/login.php'
    
    s = Session()

    try:
        response = s.post(url=url_login, params=account())
    except ConnectionError as err:
        print(bad('check your connection'))
        exit(1)
    
    if 'unsuccessful' not in response.text:
        auth_msg = good(bold(green('Authentication sucessfull!')))
    else:
        print(bad(bold(red('Authentication failed!'))))
        exit(1)

    return s, auth_msg
    
def post_phish(file_csv, num_report, interval, verbose):

    url_report = 'https://www.phishtank.com/add_web_phish.php'
    words_fails = ['invalid','attack','received','submitted']
    session, auth_msg = login()
    print(auth_msg) 
    with open(file_csv, newline='', encoding='latin-1') as f_reader:
        fReader = reader(f_reader, delimiter=';')

        for count, f_row in enumerate(fReader):
            if count + 1 <= num_report:
                try:
                    info_phish = {
                            'phish_url':f_row[0],
                            'phish_target':f_row[1],
                            'phish_text':f_row[2],
                            'phish_submit':'Submit'
                            }
                except IndexError:
                    if verbose: print(bad('error: problem with csv file, check line {}'.format(count+1)))
                    pass
                try:
                    response = session.post(url=url_report, params=info_phish)
                except UnboundLocalError:
                    if verbose: print(bad('error: problem with csv file, check line {}'.format(count+1)))
                    continue

                check_report = [True for wds in words_fails if wds in response.text]
                
                if verbose:
                    if check_report:
                        print(bad(red('Report failed - {}'.format(f_row[0]))))
                    else:
                        print(good(blue('{} Report successfull - '.format(strftime('%d %b %Y %H:%M:%S')))),end='')
                        print(green('{}'.format(f_row[0])))
                
                if num_report > 1: sleep(interval)

        print(info(orange('Finished!!')))

def excludes_reported(phish_file, num_report):

    backupList = []
    with open(phish_file, 'r', encoding='latin-1') as f_read:
        fReader = reader(f_read)
        for linR in fReader:
            if fReader.line_num <= num_report: continue
            backupList.append(linR)
    
    with open(phish_file, 'w', encoding='latin-1', newline='') as f_write:
        fWrite = writer(f_write)        
        for linW in backupList: fWrite.writerow(linW)

def main():

    arg, parse = parse_args()

    if len(argv) < 2:
        parse.print_help()
        exit(1)

    if arg.list_org:
        print(Organization())

    elif arg.url_list:
        if not arg.num_report:
            raise SystemExit(bad('erro: please specify the number of reports'))
        else:
            print(banner())
            if not arg.exclude_lines:                
                post_phish(arg.url_list, arg.num_report, arg.num_interval, arg.verbose)
            else:
                post_phish(arg.url_list, arg.num_report, arg.num_interval, arg.verbose)
                excludes_reported(arg.url_list, arg.num_report)

if __name__ == '__main__':
    try: main()
    except KeyboardInterrupt: raise SystemExit('bye ;)')
    except SystemExit: pass
    except FileNotFoundError as err: raise SystemExit(info(err))




