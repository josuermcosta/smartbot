from grab_info import SW_colection
import argparse

def speeds(lista):
    aux = helper_function(lista)
    for each in aux:
        print('Name: ' + each[0] + '\nSpeed: ' + str(each[1]))
        print('_____________________________________________')

def race(lista):
    if len(lista) > 1:
        aux = helper_function(lista)
        current_speed = -1
        current_pilot = 'none'
        for each in aux:
            if current_speed < each[1]:
                current_pilot = each[0]
                current_speed = each[1]
            else:
                current_speed = each[1]
        print('Winner: ' + current_pilot)

def helper_function(lista):
    aux = SW_colection.data()
    for each in lista:
        aux.grab_pilot(each)
        aux.grab_ships(each)
    aux.pilot_max_speed()
    return aux.return_pilots()

parser = argparse.ArgumentParser(description='Get the fastest ship from a pilot. Or make a race between them.')

parser.add_argument('pilots', metavar='P', type=str, nargs='+',
                    help='Names from the pilots ')
parser.add_argument('--race', dest='accumulate', action='store_const',
                    const=race, default=speeds,
                    help='Check the fastest pilot with, or just get the speeds of all the pilots you send.')

args = parser.parse_args()
args.accumulate(args.pilots)
