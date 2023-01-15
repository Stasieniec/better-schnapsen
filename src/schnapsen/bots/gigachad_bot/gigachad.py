import random
from typing import Optional
from schnapsen.game import Bot, PlayerPerspective, Move
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
import gym
from stable_baselines3 import A2C

class GigaChad(Bot):
    # TODO: This class should replace the RandBot class defined in src/schnapsen/cli.py

    def __init__(self) -> None:
        super.__init__()

    def get_move(
        self,
        state: PlayerPerspective,
        leader_move: Optional[Move],
    ) -> Move:

        env = gym.make('LunarLander-v2')  # continuous: LunarLanderContinuous-v2
        env.reset()

        model = A2C('MlpPolicy', env, verbose=1)
        model.learn(total_timesteps=100000)

        episodes = 5

        for ep in range(episodes):
            obs = env.reset()
            done = False
            while not done:
                action, _states = model.predict(obs)
                obs, rewards, done, info = env.step(action)
                env.render()
                print(rewards)
			

        #rand
        moves: list[Move] = state.valid_moves()
        move = self.rng.choice(list(moves))
        num_actions = 4

        return move






    def __repr__(self) -> str:
        return f"RandBot(seed={self.seed})"