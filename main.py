#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

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
			self.dominios_txt += '\n' + self.dominio[i]['ip'] + '		' + self.dominio[i]['domain'] + '\n'

		# Salva o host
		with open('/etc/hosts', 'rt') as file:
			hosts_conteudo = file.read()
			with open('/tmp/etc_hosts.tmp', 'wt') as outf:
				outf.write(hosts_conteudo)
				outf.write(self.dominios_txt);
	
		os.system('sudo mv /tmp/etc_hosts.tmp /etc/hosts')
		return 'Host salvo com sucesso.'

	def add(self, domain = '', ip = '127.0.0.1'):

		new_host = {
			'ip': ip,
			'domain': domain
		}

		self.dominio.append(new_host)
		return 'Novo Host adicionado a lista'

	def getDominios(self):
		return self.dominio;


host = Host()

while True:

	print('########### HOSTS ###########')
	print('1) Adicionar um host')
	print('2) Ver oque está na lista')
	print('3) Salvar o que está na lista')
	acao = input('')
	domain = '';

	# Adicionando um host
	if acao == '1':

		print('Informe o domínio')
		domain = input('')
		
		print('Informe o IP')
		ip = input('')

		if ip == '':
			ip = '127.0.0.1'

		res = host.add(domain, ip)
		print(res)

	# Ver oque está na lista
	if acao == '2':
		print(host.getDominios())

	# Salva os hosts que estão na Lista
	if acao == '3':
		res = host.save()
		print(res)