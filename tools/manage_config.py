#!/usr/bin/env python3
import argparse
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


def _file_exists(filepath):
	if not os.path.isfile(filepath):
		msg = '\'%s\' does not exists' % filepath
		raise argparse.ArgumentTypeError(msg)
	return filepath


def backup_secrets(config_file: str, backup_file: str):
	""" Backup the configuration file secrets """

	backup = SECRETS.copy()
	with open(config_file, 'rb') as cfg, open(backup_file, 'w') as bkp:

		config = plistlib.load(cfg)['PlatformInfo']['Generic']
		for key in SECRETS:
			if config[key] == SECRETS[key]:
				return
			if type(config[key]) is bytes:
				backup[key] = config[key].hex()
			else:
				backup[key] = config[key]

		json.dump(backup, bkp)

		print(f'Secrets from \'{config_file}\' successfully saved to \'{backup_file}\'')


def clean_config(config_file: str, backup_file: str):
	""" Remove secrets from the configuration file to safely publish it on the web """

	if not os.path.exists(backup_file):
		backup_secrets(config_file, backup_file)

	config = None

	with open(CONFIG_FILE, 'rb') as cfg:

		config = plistlib.load(cfg)
		infos = config['PlatformInfo']['Generic']

		for key, default_value in SECRETS.items():
			infos[key] = default_value

	with open(CONFIG_FILE, 'wb') as cfg:
		plistlib.dump(config, cfg)

	print(f'\'{CONFIG_FILE}\' cleaned !')


def restore_config(config_file: str, backup_file: str):
	""" Clean a configuration file to safely publish it on internet """

	config = None

	if not os.path.exists(backup_file):
		print('There\'s no backup file to use. Make sure you have run \'backup\' command before')

	with open(config_file, 'rb') as cfg, open(backup_file, 'rb') as bkp:

		backup = json.load(bkp)
		config = plistlib.load(cfg)
		infos = config['PlatformInfo']['Generic']

		for key in SECRETS:
			if type(infos[key]) is bytes:
				infos[key] = bytes.fromhex(backup[key])
			else:
				infos[key] = backup[key]

	with open(config_file, 'wb') as cfg:
		plistlib.dump(config, cfg)

	print(f'\'{config_file}\' restored !')


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Manage OpenCore configuration secrets')
	parser.add_argument('command', type=str, choices=['backup', 'clean', 'restore'],
						help='command to execute. clean makes also a backup')
	parser.add_argument('-c', '--config', type=_file_exists, default=CONFIG_FILE,
						help='target config file')
	parser.add_argument('-b', '--backup', type=str, default=BACKUP_FILE,
						help='backup file destination. we recommend to put a .json extension')
	args = parser.parse_args()

	if args.command == 'backup':
		backup_secrets(args.config, args.backup)
	elif args.command == 'clean':
		clean_config(args.config, args.backup)
	else:
		restore_config(args.config, args.backup)
