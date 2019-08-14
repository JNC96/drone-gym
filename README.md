[![BuildStatus][build-status]][ci-server]
[![PackageVersion][pypi-version]][pypi-home]
[![PythonVersion][python-version]][python-home]
[![Stable][pypi-status]][pypi-home]
[![Format][pypi-format]][pypi-home]

[build-status]: https://travis-ci.com/Kautenja/gym-super-mario-bros.svg?branch=master
[ci-server]: https://travis-ci.com/Kautenja/gym-super-mario-bros
[pypi-version]: https://badge.fury.io/py/gym-super-mario-bros.svg
[pypi-license]: https://img.shields.io/pypi/l/gym-super-mario-bros.svg
[pypi-status]: https://img.shields.io/pypi/status/gym-super-mario-bros.svg
[pypi-format]: https://img.shields.io/pypi/format/gym-super-mario-bros.svg
[pypi-home]: https://badge.fury.io/py/gym-super-mario-bros
[python-version]: https://img.shields.io/pypi/pyversions/gym-super-mario-bros.svg
[python-home]: https://python.org

![gif](https://media.giphy.com/media/11ASZtb7vdJagM/giphy.gif)

# Drone Gym Environment

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
