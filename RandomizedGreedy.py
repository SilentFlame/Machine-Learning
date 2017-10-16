"""
Randomized-Greedy Algorithm

Randomized-Greedy is one of the variants of Multi-arm bandits algorithm, 
which is a class of decision algorithms aiming to earn highest reward within a 
limitation of steps, which does not suffice for learning. 

Two main factors are considered in this problem:
1) Exploration: learning about reward difference amongst options it could decide
2) Exploitation: utitlize the most potentially rewarded option

The procedure is explained as follows.

- Given a set of actions and T timesteps, players must come up with a strategy 
to  earn the highest reward, or reduce the loss when taking a particular action.

- Let A = {a1, a2, a3, ..., aK} be the set of possible actions to take at each
timestep. p_t is probability to choose each action at timestep t. L_t is 
accumulative loss from timestep 1 up to timestep t.

- Initialize p_t = {1/K, 1/K, ...,1/K}

- For each round t = 1, ..., n
    + Find smallest accumulative loss L_t
    + Find actions having same value with smallest accumative loss
    + Among actions in this set, randomly choose one

Implementatios of Randomized-Greedy clustering algorithm is below.
"""

import random
import numpy

NUMB_ACTIONS = 5
TIME_STEPS = 10
ETA = 10 # it is a non-negative value

def loss_generate(NUMB_ACTIONS, action_index):
    losses = [random.uniform(0, 1) for i in range(NUMB_ACTIONS)]
    return losses
    
def get_loss_action_i(losses, action_index):
    new_loss = [0 for i in range(NUMB_ACTIONS)]
    new_loss[action_index] += losses[action_index]
    return new_loss

def find_min_loss_actions(L_t_min, L_t):
    find_min_index = (L_t == L_t_min)
    return numpy.nonzero(find_min_index)[0]
    
def Randomized_Greedy(losses):
    # initialize probability distribution
    L_t = numpy.array([0. for i in range(NUMB_ACTIONS)])
    print ('Initialization')
    print ('L_t', L_t); print ()
    
    for time_step in range(1, TIME_STEPS+1):
        L_t_min = numpy.min(L_t)
        min_actions = find_min_loss_actions(L_t_min, L_t)
        numb_min_actions = len(min_actions)
        action_i = min_actions[random.randint(0, numb_min_actions-1)]
        loss_t = get_loss_action_i(losses, action_i)
        L_t = L_t + loss_t
        print ('Time step:', time_step); print ('L_t_min', L_t_min)
        print ('Set of min actions', min_actions + 1)
        print ('Chosen action:', action_i + 1); print ('loss_t', loss_t)
        print ('L_t', L_t); print ()
        
    return numpy.sum(L_t)

if __name__ == '__main__':
    random.seed(0) # Keep the program deterministic for testing
    
    losses = loss_generate(NUMB_ACTIONS, loss_generate)
    print ('Loss for each action', losses)
    final_loss = Randomized_Greedy(losses)
    print ('Loss: ', final_loss)
  
