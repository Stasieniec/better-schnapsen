import gym
import random
from gym import spaces
from schnapsen.game import (Bot, Move, PlayerPerspective,
                            SchnapsenGamePlayEngine, Trump_Exchange)

from schnapsen.bots.rdeep import RandBot
from schnapsen.bots.gigachad_bot.gigachad import GigaChad
from schnapsen.bots.gigachad_bot.training_agent import GigaChad



class SchnapsenEnv(gym.Env):
	def __init__(self) -> None:
		super(SchnapsenEnv, self).__init__()

		#SCHNAPSEN ENGINE:
		self.engine = SchnapsenGamePlayEngine
		self.bot = Dummy()
		#ENVIRONMENTAL SHIT:
		self.action_space = spaces.Discrete(5)
		# Example for using image as input (channel-first; channel-last also works):
		self.observation_space = spaces.Box(low=0, high=255,
											shape=(N_CHANNELS, HEIGHT, WIDTH), dtype=np.uint8)


	def step(self, action):
		observations = self.bot.observations
		move = observations[action]
		self.bot.
		return observations, self.reward, self.done



	def reset(self, opponent: Bot):
		self.engine = SchnapsenGamePlayEngine
		self.bot = Dummy
		self.engine.play_game(opponent, self.bot)



	def render(self, mode='human'):
		pass


	def close (self):
		pass


class Dummy(Bot):

	def __init__(self) -> None:
		self.rng = random.Random()
		self.step_was_made = False
		self.curr_move: Move = None


		self.observations = []
		
	def get_move(self, state: PlayerPerspective, leader_move: Optional[Move]) -> Move:
		self.observations = [state.valid_moves]
		while not self.step_was_made:
			Wait = True
		return self.curr_move
		


	def __repr__(self) -> str:
		return f"RandBot(seed={self.seed})"




model.learn(SchnapsenEnv)