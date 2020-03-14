#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

class Apache2:

	def __init__(self):
		self.dominio = []

	def save(self):

		# Percorre todos os virtuais-hosts informados,
		for i in range(0, len(self.dominio)):

			with open('/tmp/' + self.dominio[i]['domain'] + '_temp.tmp', 'wt') as outf:
				outf.write(self.dominio[i]['text']);

			os.system('sudo mv /tmp/' + self.dominio[i]['domain'] + '_temp.tmp /etc/apache2/sites-enabled/' + self.dominio[i]['domain'] + '.conf')

		# Reset atributos
		self.dominio = []

		os.system('sudo service apache2 restart')

		return 'Virtuais-Hosts salvo com sucesso.'

	# Remove um dominio
	def remove(self, domain):

		check = self.exist(domain)

		# Se o dominio informado existe, então remove ele
		if(check):
			try:
				os.system('sudo rm -rfv /etc/apache2/sites-enabled/' + domain + '.conf')
				return 'Feito, host-virtual removido com sucesso.'
			except Exception as e:
				return 'Ops, não consegui remover esse host-virtual, sei lá oque houve...'

		return 'Bro, eu não achei nenhum host-virtual com esse dominio.'


	# Adiciona um novo host-virtual
	def add(self, domain = '', diretorio = ''):

		# Precisa verificar se já existe um virtual-host com o esse domínio

		# lista com todos os vistuais-Hosts configurados no apache2
		virtualHost = self.getAll()

		# verifica se o dominio existe no arquivo
		res = self.exist(domain)

		if(res):
			return 'Ops, parece que o domínio "' + domain + '" já está configurado no Virtual Host do Apache2'

		mascara = "# HTTP \n";
		mascara += "<VirtualHost *:80>\n"
		mascara += "\tServerName " + domain +"\n"
		mascara +=	"\tServerAdmin webmaster@localhost\n"
		mascara +=	"\tDocumentRoot " + diretorio  + "\n"
		mascara +=	"\t\t<Directory " + diretorio  + "/>\n"
		mascara +=	"\t\t\tOptions Indexes FollowSymLinks MultiViews\n"
		mascara +=	"\t\t\tAllowOverride All\n"
		mascara +=	"\t\t\tOrder allow,deny\n"
		mascara +=	"\t\t\tallow from all\n"
		mascara +=	"\t\t\tRequire all granted\n"
		mascara +=	"\t\t</Directory>\n"
		mascara +=	"\tRewriteEngine on\n"
		mascara += "\n"
		mascara +=	"\tRewriteCond %{SERVER_NAME} =" + domain + "\n";
		mascara +=	"\tRewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]\n";
		mascara += "</VirtualHost>\n"

		mascara += "# HTTPS \n";
		mascara += "<VirtualHost *:443>\n"
		mascara += "\tServerName " + domain +"\n"
		mascara +=	"\tServerAdmin webmaster@localhost\n"
		mascara +=	"\tDocumentRoot " + diretorio  + "\n"
		mascara +=	"\t<Directory " + diretorio  + "/>\n"
		mascara +=	"\t\tOptions Indexes FollowSymLinks MultiViews\n"
		mascara +=	"\t\tAllowOverride All\n"
		mascara +=	"\t\tOrder allow,deny\n"
		mascara +=	"\t\tallow from all\n"
		mascara +=	"\t\tRequire all granted\n"
		mascara +=	"\t</Directory>\n"
		mascara +=	"\n"
		mascara += "\tSSLCertificateFile /etc/letsencrypt/live/" + domain + "fullchain.pem\n"
		mascara += "\tSSLCertificateFile /etc/letsencrypt/live/" + domain + "privkey.pem\n"
		mascara += "\tInclude /etc/letsencrypt/options-ssl-apache.conf\n"
		mascara += "</VirtualHost>\n"

		hostVirtual = {
			'domain': domain,
			'text': mascara
		}

		self.dominio.append(hostVirtual)

		return 'Novo Virtual-Host adicionado a lista'

	# Verifica se existe esse domínio no Apache2
	def exist(self, domain = ''):

		if os.path.isfile('/etc/apache2/sites-enabled/' + domain + '.conf'):
			return True
		else:
			return False

	# Retorna uma lista com todos os hosts do arquivo .hosts
	def getAll(self):
		hosts = os.listdir('/etc/apache2/sites-enabled/')
		return hosts

	def getHosts(self):
		return self.dominio;

sys.modules[__name__] = Apache2