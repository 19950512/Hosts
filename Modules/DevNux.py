#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

class DevNux:

	def __init__(self):
		pass

	# Limpa o terminal
	def clear(self):
		os.system('cls' if os.name == 'nt' else 'clear')


sys.modules[__name__] = DevNux