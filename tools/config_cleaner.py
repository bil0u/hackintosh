#!/usr/bin/env python3
import os
import plistlib

import click

GENERATE_ME = ">> GENERATE ME <<"
BOARD_SERIAL = ">> PASTE BOARD SERIAL NUMBER HERE <<"


@click.command()
@click.argument('config_file', required=True)
def clean(config_file):
	""" Clean a configuration file to safely publish it on internet """

	if not os.path.exists(config_file):
		print(f'{config_file} does not exists')
		return

	result = plistlib.load(config_file)

	result['SMBIOS']['BoardSerialNumber'] = GENERATE_ME
	result['SMBIOS']['SerialNumber'] = GENERATE_ME
	result['SMBIOS']['SmUUID'] = GENERATE_ME
	result['RtVariables']['MLB'] = BOARD_SERIAL
	result['Boot']['DefaultVolume'] = 'LastBootedVolume'
	result['GUI']['Theme'] = 'embedded'
	result['GUI']['ScreenResolution'] = ''
	result['GUI']['Scan'] = {}
	result['GUI']['Scan']['Entries'] = True
	result['GUI']['Scan']['Legacy'] = True
	result['GUI']['Scan']['Linux'] = False
	del result['GUI']['Custom']

	plistlib.dump(result, config_file)

	print(f'{config_file} cleaned !')

if __name__ == "__main__":
	clean()
