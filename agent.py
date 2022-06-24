import numpy as np


class Agent(object):
    def __init__(self, states, alpha):
        self.state_history = None  # list of states and rewards
        self.alpha = alpha
        self.G = {}
        self.initial_reward(states)

    def initial_reward(self, states):
        for s in states:
            self.G[s] = np.random.uniform(low=-1.0, high=-0.1)

    def choose_action(self):
        pass

    def update_state_history(self):
        pass

    def learn(self):
        target = (
            0  # learn at the end of episode when the agent receives a reward of zero
        )
        for prev, reward in reversed(self.state_history):
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            target += reward
        self.state_history = (
            []
        )  # set agent's memory to zero to make room for the next episode
