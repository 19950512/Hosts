#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

class Host:

	def __init__(self):
		self.dominio = []
		self.dominios_txt = '';
	
	def toString(self, s):  

		# initialize an empty string 
		str1 = ""  

		# traverse in the string   
		for ele in s:  
			str1 += ele   

		# return string   
		return str1 

	def save(self):
		tamanho = len(self.dominio)
		lista_hosts = range(tamanho)

		# Percorre todos os hosts informados,
		# cria-se uma string para salvar
		for i in lista_hosts:
			self.dominios_txt += self.dominio[i]['ip'] + '	' + self.dominio[i]['domain'] + '\n'

		# Salva o host
		with open('/etc/hosts', 'rt') as file:
			hosts_conteudo = file.read()
			with open('/tmp/etc_hosts.tmp', 'wt') as outf:
				outf.write(hosts_conteudo)
				outf.write(self.dominios_txt);

		os.system('sudo mv /tmp/etc_hosts.tmp /etc/hosts')

		# Reset atributos
		self.dominio = []
		self.dominios_txt = ''

		return 'Host salvo com sucesso.'

	# Remove um dominio do .hosts
	def remove(self, domain):

		# Precisamos verificar se no arquivo .hosts já existe esse dominio

		# lista com todos os hosts configurados no .hosts
		hosts = self.getAll()

		# verifica se o dominio existe no arquivo
		res = self.exist(hosts, domain)

		# O domínio existe, então o conteúdo do arquivo deve ser alterado.
		if(res):

			# temp = novo arquivo de hosts, sem o dominio informado
			temp = []
			try:
				for i in range(0, len(hosts)):

					# host[0] = IP
					# host[1] = Domain
					host = hosts[i].split('\t')

					if(host[1].rstrip() != domain):
						temp.append(hosts[i])

			except Exception as e:
				return 'Ops, parece que está fora do padrão o arquivo de hosts, deve conter um ENTER, um TAB, verefique o arquivo e tente novamente.'

			# converte array/list para string
			temp = self.toString(temp)

			# Chegou até aqui, é só salvar.
			
			# OBS: Esse trecho para baixo, precisa criar uma função para isso e reutilizar em outros metodos, não faço isso porque estou sem tempo agora. kk

			# Salva o host
			try:
				with open('/etc/hosts', 'rt') as file:
					with open('/tmp/etc_hosts.tmp', 'wt') as outf:
						outf.write(temp);

				os.system('sudo mv /tmp/etc_hosts.tmp /etc/hosts')
				
				return 'Pronto, dominio removido do arquivo de hosts.'

			except Exception as e:
				return 'Ops, não consegui finalizar a parada. feels bad man. :|'

		return 'Ops, parece que o domínio "' + domain + '" não existe no arquivo .hosts'


	# Adiciona um host a lista dos Hosts
	def add(self, domain = '', ip = '127.0.0.1'):

		# Precisamos verificar se no arquivo .hosts já existe esse dominio

		# lista com todos os hosts configurados no .hosts
		hosts = self.getAll()

		# verifica se o dominio existe no arquivo
		res = self.exist(hosts, domain)

		if(res):
			return 'Ops, parece que o domínio "' + domain + '" já existe.'

		new_host = {
			'ip': ip,
			'domain': domain
		}

		self.dominio.append(new_host)

		return 'Novo Host adicionado a lista'

	# Verifica se na lista de Hosts já existe um dominio específico
	def exist(self, hosts = [], domain = ''):

		for i in range(0, len(hosts)):

			# host[0] = IP
			# host[1] = Domain
			host = hosts[i].split('\t')
			try:
				if(host[1].rstrip() == domain):
					return True
			except Exception as e:
				return False

		return False

	# Retorna uma lista com todos os hosts do arquivo .hosts
	def getAll(self):

		try:
			fp = open('/etc/hosts')
			hosts = fp.readlines()

		finally:
			fp.close()

		return hosts

	def getDominios(self):
		return self.dominio;

sys.modules[__name__] = Host