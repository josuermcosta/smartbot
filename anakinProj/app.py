from anakinProj.grab_info import SW_colection
import argparse

parser = argparse.ArgumentParser(description='Get the fastest ship from a pilot.')

parser.add_argument('pilots', metavar='P', type=str, nargs='+',
                    help='Names from the pilots')
                    
parser.add_argument('--get', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))