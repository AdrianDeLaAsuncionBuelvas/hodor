#!/usr/bin/python3

"""
Level 0
"""
import requests


def cheat_vote_Level_0(times):
    """
    cheat_vote_Level_0 - program that votes 1024 times for your id
    times - number of times voted
    """
    succes = 0
    failures = 0

    my_data = {'id': '1550', 'holdthedoor': 'submit'}
    url = "http://158.69.76.135/level0.php"
    s = requests.Session()

    for i in range(times):
        rq = requests.post(url, my_data)
        if (rq.status_code == 200):
            print("vote {:d}".format(succes))
            succes += 1
        else:
            print('Failure!')
            failures += 1

    print('=============================')
    print("\nYou Id 1550")
    print('=============================')
    print('SUCCESS!! [{:d}]'.format(succes))
    print('=============================')
    print('FAILURES [{:d}]'.format(failures))
    print('=============================')
    print('Headers')
    print(rq.headers)

if __name__ == '__main__':
    times = 1024
    cheat_vote_Level_0(times)
