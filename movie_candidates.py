import json
from random import sample
from pprint import pformat
from time import sleep


def main():
    candidates = read_candidates('./candidates.json')
    print(f'Candidate movies:\n{pformat(candidates)}')
    final_choice = sample(candidates, 1)
    print('And the winner is...\n')
    sleep(2)
    print(f'{final_choice[0]}!!')


def read_candidates(file_path):
    with open(file_path, 'r', encoding='utf-8') as inputfile:
        candidates = json.load(inputfile)
    return candidates


if __name__ == '__main__':
    main()
    input('\nPress Enter to exit.')
