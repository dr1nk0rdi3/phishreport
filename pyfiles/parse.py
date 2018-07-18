from sys import argv
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from textwrap import dedent

def parse_args():

    parser = ArgumentParser(
  	    formatter_class = RawDescriptionHelpFormatter,
    	description = 'Report phishing for www.phishtank.com',
    	epilog = dedent('''\
    Example:

        key defaults:
            default interval:           6 seconds
            default exclude rows:       False
            default verbose:            False

        usage for:
            
            python3 {0} --phish-list file.csv --set-report 50
            python3 {0} --phish-list file.txt --set-report 50 --set-interval 2 --exclude --verbose
        or: 
            Show list of organizations
            python3 {0} --list-org
            
            '''.format(argv[0])))       

    g = parser.add_mutually_exclusive_group()

    g.add_argument(
        '-l',
        '--list-org',
        dest='list_org',
        help='Show list of organizations',
        action='store_true',
        required=False  
        )

    g.add_argument(        
        '-p',
        '--phish-list',
        dest='url_list',
        help='Specify a file with a list of URLs for report',
        action='store',
        metavar='Phish_list',
        required=False 
        )

    parser.add_argument(
        '-r',
        '--set-report',        
        dest='num_report',
        help='Specify the number of reports',
        action='store',
        type=int,
        required=False 
        )

    parser.add_argument(
        '-i',
        '--set-interval',        
        dest='num_interval',
        help='Specify the interval between reports',
        action='store',
        default=6,
        type=int,
        required=False 
        )

    parser.add_argument(
        '-e',
        '--exclude',        
        dest='exclude_lines',
        help='Exclude rows that have been reported',
        action='store_true',
        default=False,
        required=False       
        )

    parser.add_argument(
        '-v',
        '--verbose',        
        dest='verbose',
        help='Show status of reports',
        action='store_true',
        default=False,
        required=False       
        )

    args = parser.parse_args()
    return args, parser
