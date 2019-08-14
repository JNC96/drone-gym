# Drone GyM

This repository contains a PIP package which is an OpenAI Gym environment for a drone that learns via RL.

# Installation

  <b> Install OpenAI gym </b>

Then install this package via ``pip install -e .``

Then, make the environment:

	import gym
	import gym_pull
    
    gym_pull.pull('github.com/jnc96/drone-gym')
    env = gym.make('Drone-v0')

<div id="basic_usage"></div>

See https://github.com/matthiasplappert/keras-rl/tree/master/examples for some examples.

# The Environment
