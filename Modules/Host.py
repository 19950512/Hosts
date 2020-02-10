#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

class Host:

	def __init__(self):
		self.dominio = []
		self.dominios_txt = '';

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

			if(host[1].rstrip() == domain):
				return True

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