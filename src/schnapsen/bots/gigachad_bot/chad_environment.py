import gym
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
		self.egine = SchnapsenGamePlayEngine
		#ENVIRONMENTAL SHIT:
		self.action_space = spaces.Discrete(5)
		# Example for using image as input (channel-first; channel-last also works):
		self.observation_space = spaces.Box(low=0, high=255,
											shape=(N_CHANNELS, HEIGHT, WIDTH), dtype=np.uint8)


	def step(self):
		self.engine.
		pass

	def reset(self, opponent: Bot):
		self.engine = SchnapsenGamePlayEngine
		self.engine.play_game(opponent, TrainingBot)
		game = self.engine.play_game()
		self.engine.

	def render(self, mode='human'):
		pass
	def close (self):
		pass


class TrainingBot(Bot):
	def __init__(self, seed: int) -> None:
		self.rng = random.Random(self.seed)
		
	def get_move(self, state: PlayerPerspective, leader_move: Optional[Move]) -> Move:
		moves = state.valid_moves()
		move = self.rng.choice(list(moves))
		return move

	def __repr__(self) -> str:
		return f"RandBot(seed={self.seed})"