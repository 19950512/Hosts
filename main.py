#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.path.abspath('./Modules/'))

import Host, Apache2, DevNux

Host = Host()
Apache2 = Apache2()
DevNux = DevNux()

while True:

	DevNux.clear()
	print('########### VIRTUAL-HOSTS ###########')
	print('\n')
	print('1) Host')
	print('2) Apache2')
	print('3) Hosts & Apache2')
	print('0) Sair')

	acao = input('')

	DevNux.clear()

	if(acao == '1'):

		while True:

			DevNux.clear()
			print('########### VIRTUAL-HOSTS > HOSTS ###########')
			print('\n')
			print('1) Adicionar um novo Host')
			print('2) Ver Carrinho')
			print('3) Salvar tudo')
			print('4) Listar todos do arquivo .hosts')
			print('0) Voltar')
			
			acaoHost = input('')
			domain = '';

			DevNux.clear()
			
			if acaoHost == '1':

				print('Informe o domínio')
				domain = input('')
				
				print('Informe o IP')
				ip = input('')

				if ip == '':
					ip = '127.0.0.1'

				res = Host.add(domain, ip)
				print(res)
				input('Pressione Enter para voltar')

			# Retorna a Lista de Hosts, oque estão na lista para serem salvos
			if acaoHost == '2':

				res = Host.getDominios()

				if(len(res) == 0):
					print('Nenhum host adicionado no carrinho.')
				else:
					print(res)

				input('Pressione Enter para voltar.')

			# Salva os hosts que estão na Lista
			if acaoHost == '3':

				res = Host.save()
				print(res)
				input('Pressione Enter para voltar.')

			# Exibe todos os hosts que estão no .hosts
			if acaoHost == '4':

				res = Host.getAll()

				if(len(res) == 0):
					print('Nenhum host configurado no arquivo ".hosts".')
				else:
					for i in range(0, len(res)):
						print(res[i])

				input('Pressione Enter para voltar.')

			# Se for Voltar ao Menu
			if(acaoHost == '0'):
				break


	# Se for Sair
	if(acao == '0'):
		print('CYA.. :*')
		break

	# # Adicionando um host
	# if acao == '1':

	# 	print('Informe o domínio')
	# 	domain = input('')
		
	# 	print('Informe o IP')
	# 	ip = input('')

	# 	if ip == '':
	# 		ip = '127.0.0.1'

	# 	res = Host.add(domain, ip)
	# 	print(res)

	# # Ver oque está na lista
	# if acao == '2':
	# 	print(Host.getDominios())

	# # Salva os hosts que estão na Lista
	# if acao == '3':
	# 	res = Host.save()
	# 	print(res)