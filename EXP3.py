"""
EXP3 (EXPONENTIAL weights for EXPLORATION and EXPLOITATION (Exp-Exp-Exp))

Exp3 is one of the variants of Multi-arm bandits algorithm, which is a class 
of decision algorithms aiming to earn highest reward within a limitation of
steps, which does not suffice for learning. 

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
    + Draw an action ai from probability distribution p_t
    + Update the loss of action i. loss = (0, ..., loss_i/p_t[i], ..., 0)
    + Update cumulative loss L_t. L_t = L_{t-1} + loss
    + Update probability for next time step with lambda_t = exp(-eta * L_t),
    p_t = lambda_t/|lambda_t|

Implementatios of K-mean clustering algorithm is below.
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

def chose_action(p_t):
    random_val = random.uniform(0., 1.)
    index = 0
    accumulative_prob = 0.
    for prob in p_t:
        accumulative_prob += prob
        if (random_val - accumulative_prob < 0):
            return index
        index += 1
    return index

def EXP3(losses):
    # initialize probability distribution
    p_t = numpy.array([float(1/NUMB_ACTIONS) for i in range(NUMB_ACTIONS)])
    L_t = numpy.array([0. for i in range(NUMB_ACTIONS)])
    print ('Initialization')
    print ('p_t', p_t ); print ('L_t', L_t)
    
    for time_step in range(1, TIME_STEPS+1):
        action_i = chose_action(p_t)
        loss_t = get_loss_action_i(losses, action_i)
        L_t = L_t + loss_t
        lambda_t = numpy.exp(-ETA * L_t)
        p_t = lambda_t/numpy.sum(lambda_t) 
        print ('Time step:', time_step)
        print ('Chosen action:', action_i + 1); print ('loss_t', loss_t)
        print ('L_t', L_t); print ('lambda_t', lambda_t)
        print ('p_t', p_t); print ()
        
    return numpy.sum(L_t)

if __name__ == '__main__':
    random.seed(0) # Keep the program deterministic for testing
    
    losses = loss_generate(NUMB_ACTIONS, loss_generate)
    print ('Loss for each action', losses)
    final_loss = EXP3(losses)
    print ('Loss: ', final_loss)
  
