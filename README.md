[![BuildStatus][build-status]][ci-server]
[![PackageVersion][pypi-version]][pypi-home]
[![PythonVersion][python-version]][python-home]
[![Stable][pypi-status]][pypi-home]
[![Format][pypi-format]][pypi-home]

[build-status]: 
[ci-server]: 
[pypi-version]: 
[pypi-license]: 
[pypi-status]: 
[pypi-format]: 
[pypi-home]: 
[python-version]:
[python-home]: https://python.org

![gif](https://media.giphy.com/media/h5NXof7XfEYHm/giphy.gif)

# Drone Gym Environment

This repository contains a PIP package which is an OpenAI Gym environment for a drone that learns via RL. It also introduces the concept of Interactive Reinforcement Learning with this particular environment.

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

# Dependencies

The entire ecosystem heavily depends on TensorForce (see: https://github.com/tensorforce). OpenAI Gym was also used in the creation of the environment (see: https://gym.openai.com/).

Special thanks to Alexander Kuhnle for his help in developing this.

# The Environment

The environment leverages the framework as defined by OpenAI Gym to create a custom environment. The environment contains a grid of terrain gradient values. The reward of the environment is predicted coverage, which is calculated as a linear function of the actions taken by the agent.

# IRL

Main purpose of this entire system is to investigate how human interaction can affect the traditional reinforcement learning framework. Custom scripts were written to facilitate this, and several TensorForce scripts were modified as well. These can be found in the custom scripts folder, which need to be manually extracted and placed in the TensorForce package directory.

