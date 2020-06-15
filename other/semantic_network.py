"""
this file implements a semantic network to solve the Rey-Snoke-Kylo version of the prisoner's dilema

"""
__author__ = 'Cameron Redovian'

def generator(current_state):
    print('\nGenerator')
    print('---------')
    print('Current State:', current_state)
    Quesh = current_state[0]
    Ship = current_state[1]
    potential_states = []
    Q1, Q2, Q3, Q4 = list(Quesh), list(Quesh), list(Quesh), list(Quesh)
    S1, S2, S3, S4 = list(Ship), list(Ship), list(Ship), list(Ship)
    if 'Shuttle' in Quesh:
        Q1.remove('Shuttle'); S1.append('Shuttle')
        potential_states.append([Q1, S1])
        if 'Rey' in Quesh:
            Q2.remove('Shuttle'); Q2.remove('Rey')
            S2.append('Shuttle'); S2.append('Rey')
            potential_states.append([Q2, S2])
        if 'Snoke' in Quesh:
            Q3.remove('Shuttle'); Q3.remove('Snoke')
            S3.append('Shuttle'); S3.append('Snoke')
            potential_states.append([Q3, S3])
        if 'Kylo Ren' in Quesh:
            Q4.remove('Shuttle'); Q4.remove('Kylo Ren')
            S4.append('Shuttle'); S4.append('Kylo Ren')
            potential_states.append([Q4, S4])
    elif 'Shuttle' in Ship:
        Q1.append('Shuttle'); S1.remove('Shuttle')
        potential_states.append([Q1, S1])
        if 'Rey' in Ship:
            S2.remove('Shuttle'); S2.remove('Rey')
            Q2.append('Shuttle'); Q2.append('Rey')
            potential_states.append([Q2, S2])
        if 'Snoke' in Ship:
            S3.remove('Shuttle'); S3.remove('Snoke')
            Q3.append('Shuttle'); Q3.append('Snoke')
            potential_states.append([Q3, S3])
        if 'Kylo Ren' in Ship:
            S4.remove('Shuttle'); S4.remove('Kylo Ren')
            Q4.append('Shuttle'); Q4.append('Kylo Ren')
            potential_states.append([Q4, S4])
    print('Potential States', potential_states)
    return potential_states

def tester(potential_states):
    global visited_states
    invalid_states = [['Rey', 'Snoke'], ['Snoke', 'Rey'], ['Rey', 'Kylo Ren'], ['Kylo Ren', 'Rey']]
    valid_states = []
    print('\nTester')
    print('------')
    for state in potential_states:
        print('Quesh:', state[0])
        print('Ship:', state[1])
        if state not in visited_states:
            if state[0] not in invalid_states:
                if state[1] not in invalid_states:
                    valid_states.append(state)
                    print('--> Valid State')
                else:
                    print('--> Invalid: Illegal State')
            else:
                print('--> Invalid: Illegal State')
        else:
            print('--> Invalid: Duplicate State')
    print('Valid States', valid_states)
    return valid_states

init_Quesh = ['Kylo Ren', 'Snoke', 'Rey', 'Shuttle']; init_Ship = []
init_state = [init_Quesh, init_Ship]
goal_Quesh = []; goal_Ship = ['Kylo Ren', 'Snoke', 'Rey', 'Shuttle']
goal_state = [goal_Quesh, goal_Ship]
visited_states = []; open_states = []
open_states.append(init_state)
found = False
while open_states:
    current_state = open_states.pop()
    visited_states.append(current_state)
    if current_state == goal_state:
        print('\n**************************************')
        print('**************************************')
        print('Shuttle quarantine transfer completed!')
        print('**************************************')
        print('**************************************')
        found = True
    potential_states = generator(current_state)
    valid_states = tester(potential_states)
    [open_states.append(state) for state in valid_states]
if not found:
    print('There is no possible solution to this problem!')
print('Scroll up to view all explored nodes!')
