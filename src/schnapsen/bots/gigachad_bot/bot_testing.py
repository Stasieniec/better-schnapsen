import gym
from stable_baselines3 import A2C


class CustomEnv(gym.Env):
	"""Custom Environment that follows gym interface"""

	def __init__(self, arg1, arg2) ->None:
		super(CustomEnv, self).__init__()
		# Define action and observation space
		# They must be gym.spaces objects
		# Example when using discrete actions:

        #5 discrete actions: 5 cards that can be played 
		self.action_space = spaces.Discrete(5)
		# Example for using image as input (channel-first; channel-last also works):
		self.observation_space = spaces.Box(low=0, high=255,
											shape=(N_CHANNELS, HEIGHT, WIDTH), dtype=np.uint8)

	def step(self, action):
		pass
		return observation, reward, done, info
	def reset(self):
		pass
		return observation  # reward, done, info can't be included
	def render(self, mode='human'):
		pass
	def close (self):
		pass

env = gym.make("LunarLander-v2")  # continuous: LunarLanderContinuous-v2
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