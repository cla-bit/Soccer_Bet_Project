import os
from random import shuffle, choice
import pandas as pd
import time
import datetime

od1 = f'Over {1.5}'
od2 = f'Over {2.5}'
od3 = "FTD [Full Time Draw]"
od4 = "BTTS [Both Teams To Score]"
odd_item = [od1, od2, od3, od4]

team1 = 'norwich vs ajax'
team2 = 'arsenal vs inter milan'
team3 = 'chelsea vs manchester city'
team4 = 'porto fc vs manchester united'
team5 = 'bayern munich vs juventus'
team6 = 'liverpool vs southampton'
matches = [team1, team2, team3, team4, team5, team6]

od_resp = ['yes', 'no']
shuffle(od_resp)

team1_odds = [(f'Over {1.5}', f'{choice(od_resp)}'), (f'Over {2.5}', f'{choice(od_resp)}'),
              ('FTD [Full Time Draw]', f'{choice(od_resp)}'), ('BTTS [Both Teams To Score]', f'{choice(od_resp)}')]
team2_odds = [(f'Over {1.5}', f'{choice(od_resp)}'), (f'Over {2.5}', f'{choice(od_resp)}'),
              ('FTD [Full Time Draw]', f'{choice(od_resp)}'), ('BTTS [Both Teams To Score]', f'{choice(od_resp)}')]
team3_odds = [(f'Over {1.5}', f'{choice(od_resp)}'), (f'Over {2.5}', f'{choice(od_resp)}'),
              ('FTD [Full Time Draw]', f'{choice(od_resp)}'), ('BTTS [Both Teams To Score]', f'{choice(od_resp)}')]
team4_odds = [(f'Over {1.5}', f'{choice(od_resp)}'), (f'Over {2.5}', f'{choice(od_resp)}'),
              ('FTD [Full Time Draw]', f'{choice(od_resp)}'), ('BTTS [Both Teams To Score]', f'{choice(od_resp)}')]
team5_odds = [(f'Over {1.5}', f'{choice(od_resp)}'), (f'Over {2.5}', f'{choice(od_resp)}'),
              ('FTD [Full Time Draw]', f'{choice(od_resp)}'), ('BTTS [Both Teams To Score]', f'{choice(od_resp)}')]
team6_odds = [(f'Over {1.5}', f'{choice(od_resp)}'), (f'Over {2.5}', f'{choice(od_resp)}'),
              ('FTD [Full Time Draw]', f'{choice(od_resp)}'), ('BTTS [Both Teams To Score]', f'{choice(od_resp)}')]
team_odds = [team1_odds, team2_odds, team3_odds, team4_odds, team5_odds, team6_odds]

q1m = []
q2m = []
q3m = []
q1 = []
q2 = []
q3 = []
user_name = {}
user_cash = {}
comp_choice_make = []
user_choice_make = []
user_balance = []
odd_select = []
odsel_ = []
ab = []
bc = []
cd = []
u_sel = []
match_l = []


def usb(qb):
    while not qb.isdigit() or int(qb) not in range(1, 7):
        qb = input('enter team again: ')
    else:
        qb = int(qb)
        return qb


def display(val):  # function to ensure accurate user input
    while val != '2':
        if val == '1':
            break
        else:
            val = input('>> ')
    return val


def u_name(q_name):  # checkmates the username
    while not q_name.isalpha():
        q_name = input('enter username again: ')
    return q_name


def cash(w):  # checkmates the cash to deposit
    while not w.isdigit() or int(w) < 200:
        w = input('enter number greater than 200: ')
    else:
        w = int(w)
        return w


def username_cash():
    u_nam = input('enter username: ')
    u_nam = u_nam.title()
    user_name.update({'Username': u_name(u_nam)})
    u_cash = input('enter cash deposit: ')
    user_cash.update({'Cash': cash(u_cash)})


def choice_sel(q_a_b):  # checkmates the user to put A or B
    q_a_b = q_a_b.upper()
    while not q_a_b.isalpha() or q_a_b.upper() != 'A' and q_a_b.upper() != 'B':
        q_a_b = input('>> ')
        q_a_b = q_a_b.upper()
    else:
        return q_a_b


def u_bal():  # checkmates the user amount between 10 and less than user cash
    bal = input('Amount: ')
    while not bal.isdigit() or int(bal) < 10 or int(bal) > user_cash.get('Cash'):
        bal = input('Enter Amount: ')
    else:
        bal = int(bal)
        user_balance.append(bal)
        h = user_cash.get('Cash') - bal
        user_cash['Cash'] = h
        print(f'\nUser ID: {user_name.get("Username").title()}\nCash: ${user_cash.get("Cash")}')


def odd_resp(qod):
    while not qod.isalpha() or qod.lower() != 'yes' and qod.lower() != 'no':
        qod = input('>> ')
        qod = qod.lower()
    else:
        if qod.lower() == 'yes':
            print('Selected Choice: "yes"')
            odsel_.append(qod)
            print()
            u_bal()
        else:
            print('Selected Choice: "no"')
            odsel_.append(qod)
            print()
            u_bal()


def odd_chk(qck):
    while not qck.isdigit() or int(qck) not in range(1, 5):
        qck = input('again: ')
    else:
        v = int(qck)
        if v == 1:
            print(f'Selected Odd: Over {od1}')
            odd_select.append(od1)
            print('\nChoose your bet [yes] or [no]')
            resp = input('>> ')
            resp = resp.lower()
            odd_resp(resp)
        elif v == 2:
            print(f'Selected Odd: {od2}')
            odd_select.append(od2)
            print('\nChoose your bet [yes] or [no]')
            resp = input('>> ')
            resp = resp.lower()
            odd_resp(resp)
        elif v == 3:
            print(f'Selected Odd: {od3}')
            odd_select.append(od3)
            print('\nChoose your bet [yes] or [no]')
            resp = input('>> ')
            resp = resp.lower()
            odd_resp(resp)
        else:
            print(f'Selected Odd: {od4}')
            odd_select.append(od4)
            print('\nChoose your bet [yes] or [no]')
            resp = input('>> ')
            resp = resp.lower()
            odd_resp(resp)


class LiveResult:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def live_table(self):
        ltable = pd.DataFrame(
            {
                'Matches': self.m,
                'Match Odd Set': self.n
            }
        )
        ltable.index = ltable.index + 1
        # print(ltable)

        if os.path.exists("soccer.csv"):
            os.remove("soccer.csv")
            ltable.to_csv("soccer.csv")
        else:
            ltable.to_csv('soccer.csv')

    def show_match(self):
        match_shw = pd.DataFrame(
            {
                'Match Fixtures': self.m
            }
        )
        match_shw.index = match_shw.index + 1
        print(match_shw)

    def name_cash(self):
        self.__str__()
        print(f"\nUser ID: {user_name.get('Username'.title())}\nCash: ${user_cash.get('Cash')}"
              f"\nTime: {time.strftime('%H:%M:S')}\nDate: {datetime.date.today()}")
        print('***********************************************')
        print(f'\n{user_name.get("Username".title())}, here are the available matches:\n')
        time.sleep(1)


class MatchOdd:
    def __init__(self, m, f):
        self.m = m
        self.f = f

    def mat_op(self):
        for i in self.m:
            q1m.append(i)

    def mat_tm(self):
        for j in self.f:
            q2m.append(j)


class CompOwn:
    def __init__(self, a):
        self.a = a
        self.a = q1m
        self.x = comp_choice_make
        self.y = odd_select
        self.z = odsel_

    def comp_choice(self):
        comp = 0
        while comp < 4:
            shuffle(self.a)
            comp_chosen = self.a.pop()
            comp_choice_make.append(comp_chosen)
            comp += 1

    def user_ticket_comp_table(self):  # dataframe of user ticket
        for i in self.x:
            q1.append(i)
        for i in self.y:
            q2.append(i)
        for i in self.z:
            q3.append(i)

        utic = pd.DataFrame(
            {
                'Match Selected': q1,
                'Odd Selected': q2,
                'Bet': q3
            }
        )
        utic.index = utic.index + 1
        print(utic)


class UserOwn:
    def __init__(self, a):
        self.a = a
        self.n = match_l
        self.c = odd_select
        self.m = odsel_

    def user_own(self):
        i = 4
        print(f'{user_name.get("Username")} select 4 matches of your choice from (1 - 6)')
        while i > 0:
            w = input('\nTeam Select: ')
            zx = usb(w)
            if zx in u_sel:
                print('Team selected already')
                i += 1
            else:
                for mk in range(len(self.a)):
                    if zx == mk + 1:
                        print(f'You have selected: {self.a[mk]}')
                        u_sel.append(zx)
                        match_l.append(self.a[mk])

            i -= 1

    def user_ticket_table(self):  # dataframe of user ticket
        for i in self.n:
            q1.append(i)
        for i in self.c:
            q2.append(i)
        for i in self.m:
            q3.append(i)

        utick = pd.DataFrame(
            {
                'Match Selected': q1,
                'Odd Selected': q2,
                'Bet': q3
            }
        )
        utick.index = utick.index + 1
        print(utick)


class WinLost(MatchOdd):
    def __init__(self, m, f):
        super().__init__(m, f)
        self.t = comp_choice_make
        self.y = odd_select
        self.u = odsel_
        self.z = match_l

    def comp_win_lost(self):
        bal_count = 0
        w = list(zip(self.y, self.u))
        print(f'\nGame Bet won {user_name.get("Username")}:')
        for i in range(len(self.t)):
            for j in range(len(self.m)):
                if self.t[i] in self.m[j] and w[i] in self.f[j]:
                    print(f'\n{i + 1}. {self.t[i]}')
                    print(f'{w[i]}---------------> WIN')
                    bal_count += 1
        if bal_count == 4:
            print('\nYou won all games. Ticket won\nYou have been awarded 20% bonus on cash')
            print('*' * 20)
            cvb = user_cash.get('Cash') + (sum(user_balance) * 20)
            user_cash.update({'Cash': cvb})
            print(f'\nUser ID: {user_name.get("Username")}\nCash: ${user_cash.get("Cash")}')
            print('\nThanks for playing LEGEND BET')
        else:
            print('\nYou did not win all games. Ticket Lost')
            print('*' * 20)
            print(f'\nThanks for playing LEGEND BET {user_name.get("Username")}')

    def user_win_lost(self):
        bal_count = 0
        w = list(zip(self.y, self.u))
        print(f'\nGame Bet won {user_name.get("Username")}:')
        for i in range(len(self.z)):
            for j in range(len(self.m)):
                if self.z[i] in self.m[j] and w[i] in self.f[j]:
                    print(f'\n{i + 1}. {self.z[i]}')
                    print(f'{w[i]}-----------------> WIN')
                    bal_count += 1
        if bal_count == 4:
            print('\nYou won all games. Ticket won\nYou have been awarded 20% bonus onn cash')
            print('*' * 20)
            cvb = user_cash.get('Cash') + (sum(user_balance) * 20)
            user_cash.update({'Cash': cvb})
            print(f'\nUser ID: {user_name.get("Username")}\nCash: {user_cash.get("Cash")}')
            print('\nThanks for playing LEGEND BET')
        else:
            print('You did not win all games. Ticket Lost')
            print('*' * 20)
            print(f'\nThanks for playing LEGEND BET {user_name.get("Username")}')


l_match = MatchOdd(matches, team_odds)
l_match.mat_op()
l_match.mat_tm()
live_table = LiveResult(q1m, q2m)
live_table.live_table()  # live result table

cm = CompOwn(q1m)
wl = WinLost(matches, team_odds)
uc = UserOwn(matches)


a_start = True
while a_start:
    print('----Welcome to LEGEND BET-----')
    print('\n1 to continue\n2 to quit')
    n_start = input('> ')
    d = display(n_start)  # checks the user input to continue or not
    if n_start == '2':
        print('------Logging Out from LEGEND BET.-------')
        time.sleep(1)
        print('Logged Out Successful')
        break
    else:
        username_cash()
        live_table.name_cash()
        live_table.show_match()
        print(f'\nPick your choice {user_name.get("Username")}\n"A" = System\'s Choice\n"B" = User\'s Choice')
        q = input('> ')
        d = choice_sel(q)
        if d.upper() == 'A':
            cm.comp_choice()
            for m1 in range(len(comp_choice_make)):
                if user_cash.get('Cash') < 199:
                    print('\nYour wallet balance is too low to place other bets')
                    break
                else:
                    print(f'\nSelected Match picked for you {user_name.get("Username")}')
                    print(f'\n {m1 + 1}. {comp_choice_make[m1]}')
                    print('\nPick a number from 1 - 4 to select an odd')
                    for jk in range(len(odd_item)):
                        print(jk + 1, odd_item[jk])
                    print('\nPick from 1 - 4')
                    b = input('> ')
                    odd_chk(b)
            print()
            if len(odd_select) == 4:
                cm.user_ticket_comp_table()
                wl.comp_win_lost()
            a_start = False

        else:
            print('B')
            uc.user_own()
            for mi in range(len(match_l)):
                if user_cash.get('Cash') < 199:
                    print('\nYour wallet balance is too low to place other bet')
                    break
                else:
                    print('\nMatch and Their Odds')
                    print(f'{mi + 1}. {match_l[mi]}')
                    for gh in range(len(odd_item)):
                        print(gh + 1, odd_item[gh])
                    print('\nPick from 1 - 4')
                    x = input('> ')
                    odd_chk(x)

            print()
            if len(odd_select) == 4:
                uc.user_ticket_table()
                wl.user_win_lost()
            a_start = False
