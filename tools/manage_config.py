#!/usr/bin/env python3
import os
import json
import plistlib

CONFIG_FILE = 'EFI/OC/config.plist'
BACKUP_FILE = 'tools/secrets.json'

SECRETS = {
	'ROM': b'\x00\x00\x00\x00',
	'MLB': '[REMOVED]',
	'SystemSerialNumber': '[REMOVED]',
	'SystemUUID': '[REMOVED]',
}


def file_required(file):
	""" Stops the script if the file does not exists """
	if not os.path.exists(file):
		print(f'{file} does not exists')
		exit(1)


def backup_secrets():
	""" Backup the configuration file secrets """

	file_required(CONFIG_FILE)

	backup = SECRETS.copy()

	with open(CONFIG_FILE, 'rb') as cfg, open(BACKUP_FILE, 'w') as bkp:

		config = plistlib.load(cfg)['PlatformInfo']['Generic']

		for key in SECRETS:

			if config[key] == SECRETS[key]:
				exit(1)
			if type(config[key]) is bytes:
				backup[key] = config[key].hex()
			else:
				backup[key] = config[key]

		json.dump(backup, bkp)

		print(f'Secrets from \'{CONFIG_FILE}\' successfuly saved to \'{BACKUP_FILE}\'')


def clean_config():
	""" Remove secrets from the configuration file to safely publish it on the web """

	file_required(CONFIG_FILE)

	if not os.path.exists(BACKUP_FILE):
		backup_secrets()

	config = None

	with open(CONFIG_FILE, 'rb') as cfg:

		config = plistlib.load(cfg)
		infos = config['PlatformInfo']['Generic']

		for key, default_value in SECRETS.items():
			infos[key] = default_value

	with open(CONFIG_FILE, 'wb') as cfg:
		plistlib.dump(config, cfg)

	print(f'\'{CONFIG_FILE}\' cleaned !')


def restore_config():
	""" Clean a configuration file to safely publish it on internet """

	file_required(CONFIG_FILE)
	file_required(BACKUP_FILE)

	config = None

	with open(CONFIG_FILE, 'rb') as cfg, open(BACKUP_FILE, 'rb') as bkp:

		backup = json.load(bkp)
		config = plistlib.load(cfg)
		infos = config['PlatformInfo']['Generic']

		for key in SECRETS:
			if type(infos[key]) is bytes:
				infos[key] = bytes.fromhex(backup[key])
			else:
				infos[key] = backup[key]

	with open(CONFIG_FILE, 'wb') as cfg:
		plistlib.dump(config, cfg)

	print(f'\'{CONFIG_FILE}\' restored !')
