#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.path.abspath('./Modules/'))

import Host, Apache2, DevNux

Host 	= Host()
Apache2 = Apache2()
DevNux 	= DevNux()

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
			print('5) Excluir um Host')
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

			if acaoHost == '5':

				print('Informe o domínio')
				domain = input('')
				
				res = Host.remove(domain)
				print(res)
				input('Pressione Enter para voltar')

			# Se for Voltar ao Menu
			if(acaoHost == '0'):
				break


	if(acao == '2'):
		
		while True:

			DevNux.clear()
			
			print('########### VIRTUAL-HOSTS > APACHE2 ###########')
			print('\n')
			print('1) Adicionar um novo Host-Virtual')
			print('2) Ver Carrinho')
			print('3) Salvar tudo')
			print('4) Listar todos do arquivo .hosts')
			print('5) Excluír um Host-Virtual')
			print('0) Voltar')
			
			acaoApache = input('')
			domain = '';

			DevNux.clear()
			
			if acaoApache == '1':
				
				print('Informe o domínio')
				domain = input('')
				
				print('Informe o diretório do projeto')
				diretorio = input('')

				print('Tem sub-dominio?')
				print('1) SIM')
				print('2) NÃO')

				acaosub = input('')

				# Reset variaveis
				subdomain = ''
				subdiretorio = ''

				if acaosub == '1':
					print('Informe o sub-domínio')
					subdomain = input('')
					
					print('Informe o diretório do sub-dominio')
					subdiretorio = input('')

				res = Apache2.add(domain, diretorio)
				print(res)
				input('Pressione Enter para voltar')


			# Retorna a Lista de Virtual-Hosts, oque estão na lista para serem salvos
			if acaoApache == '2':

				res = Apache2.getHosts()

				if(len(res) == 0):
					print('Nenhum virtual-host adicionado no carrinho.')
				else:
					print(res)

				input('Pressione Enter para voltar.')

			# Salva os Virtuais-hosts que estão na Lista
			if acaoApache == '3':

				res = Apache2.save()
				print(res)
				input('Pressione Enter para voltar.')

			# Exibe todos os hosts que estão no .hosts
			if acaoApache == '4':

				res = Apache2.getAll()

				if(len(res) == 0):
					print('Nenhum virtual-host configurado no diretório do apache2.')
				else:
					for i in range(0, len(res)):
						print(res[i])

				input('Pressione Enter para voltar.')

			# Exclui um host-virtual pelo dominio
			if acaoApache == '5':

				print('Informe o domínio')
				domain = input('')

				res = Apache2.remove(domain)
				print(res)
				input('Pressione Enter para voltar.')
			

			# Se for Voltar ao Menu
			if(acaoApache == '0'):
				break


	if(acao == '3'):
		
		while True:

			DevNux.clear()
			
			print('########### VIRTUAL-HOSTS > HOST && APACHE2 ###########')
			print('\n')
			print('1) Adicionar um novo Site')
			print('2) Ver Carrinho')
			print('3) Salvar tudo')
			print('4) Listar todos os projetos')
			print('0) Voltar')
			
			acaoApacheHost = input('')
			domain = '';

			DevNux.clear()
			
			if acaoApacheHost == '1':
				
				print('Informe o domínio')
				domain = input('')
				
				print('Informe o diretório do projeto')
				diretorio = input('')

				# Host-Virtual
				res = Apache2.add(domain, diretorio)
				print(res)
				input('Pressione Enter para voltar')

				# Host
				ip = '127.0.0.1'
				res = Host.add(domain, ip)
				print(res)
				input('Pressione Enter para voltar')


			# Retorna a Lista de Virtual-Hosts, oque estão na lista para serem salvos
			if acaoApacheHost == '2':

				# Apache2
				res = Apache2.getHosts()

				if(len(res) == 0):
					print('Nenhum virtual-host adicionado no carrinho.')
				else:
					print(res)

				input('Pressione Enter para voltar.')

				# Hosts
				res = Host.getDominios()

				if(len(res) == 0):
					print('Nenhum host adicionado no carrinho.')
				else:
					print(res)

				input('Pressione Enter para voltar.')


			# Salva os Virtuais-hosts que estão na Lista
			if acaoApacheHost == '3':

				# Apache2
				res = Apache2.save()
				print(res)
				input('Pressione Enter para voltar.')

				# Hosts
				res = Host.save()
				print(res)
				input('Pressione Enter para voltar.')

			# Exibe todos os hosts que estão no .hosts
			if acaoApacheHost == '4':

				# Apache2
				res = Apache2.getAll()

				if(len(res) == 0):
					print('Nenhum virtual-host configurado no diretório do apache2.')
				else:
					for i in range(0, len(res)):
						print(res[i])

				input('Pressione Enter para voltar.')
			

				# Host
				res = Host.getAll()

				if(len(res) == 0):
					print('Nenhum host configurado no arquivo ".hosts".')
				else:
					for i in range(0, len(res)):
						print(res[i])

				input('Pressione Enter para voltar.')


			# Se for Voltar ao Menu
			if(acaoApacheHost == '0'):
				break

	# Se for Sair
	if(acao == '0'):
		print('CYA.. :*')
		break