#!/usr/bin/env python3

# These tools allows to set quickly a customized 'About this mac' section for a macOS system.

import argparse
import os
import plistlib
import shutil
import subprocess
import sys

# ---------
# Customizable values
MODEL_NAME = 'Hackintosh Pro (30-inch, Early 2019)'
PROCESSOR_NAME = '3,6 GHz Intel Core i9-9900K'
# ---------

RESOURCES = 'resources/atm/'

LOGO_NAME = 'SystemLogo.tiff'
SYSTEM_LOGO = '/Applications/Utilities/System Information.app/Contents/Resources/' + LOGO_NAME

PROFILER_NAME = 'com.apple.SystemProfiler.plist'
SYSTEM_PROFILER = '~/Library/Preferences/' + PROFILER_NAME

CPU_INFO_NAME = 'AppleSystemInfo.strings'
SYSTEM_CPU_INFO = '/System/Library/PrivateFrameworks/AppleSystemInfo.framework/Versions/A/Resources/'


def _need_privileges():
    """ Reruns the script as sudo """
    if os.geteuid() != 0:
        try:
            subprocess.check_call(['sudo', sys.executable] + sys.argv)
            exit(0)
        except subprocess.CalledProcessError:
            exit(1)


def _file_exists(filepath: str):
    """ Argparse validator : check if a file exist """
    if not os.path.isfile(filepath):
        msg = '\'%s\' does not exists' % filepath
        raise argparse.ArgumentTypeError(msg)
    return filepath


def _get_localized_folder(lproj_folder: str):
    """ Returns the localized folder used by the system """

    def expand(s: str):
        return lproj_folder + s + '.lproj/'

    lang = os.popen('defaults read /Library/Preferences/.GlobalPreferences AppleLocale').read().strip()
    matches = {
        'nl': 'Dutch',
        'en': 'English',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'jp': 'Japanese',
        'es': 'Spanish',
    }
    if os.path.exists(f'{lproj_folder}{lang}.lproj'):
        return expand(lang)
    lang = lang[:2]
    if os.path.exists(f'{lproj_folder}{lang}.lproj'):
        return expand(lang)
    elif lang in matches and os.path.exists(f'{lproj_folder}{matches[lang]}.lproj'):
        return expand(matches[lang])
    return None


def set_system_logo(new_logo: str, backup: bool = True):
    """ Replace the original system logo """
    if backup and not os.path.exists(f'{new_logo}.backup'):
        shutil.copyfile(SYSTEM_LOGO, f'{new_logo}.backup')
    shutil.copyfile(new_logo, SYSTEM_LOGO)
    print('System logo updated !')


def set_model_name(new_name: str, backup: bool = True):
    """ Changes the model name """

    if backup and not os.path.exists(f'{RESOURCES}{PROFILER_NAME}.backup'):
        shutil.copyfile(os.path.expanduser(SYSTEM_PROFILER), f'{RESOURCES}{PROFILER_NAME}.backup')

    with open(os.path.expanduser(SYSTEM_PROFILER), 'rb') as file:
        profiler = plistlib.load(file)
        key = next(iter(profiler['CPU Names']))
        profiler['CPU Names'][key] = new_name

    with open(os.path.expanduser(SYSTEM_PROFILER), 'wb') as file:
        plistlib.dump(profiler, file)

    print('Model name updated !')


def set_processor_name(new_name: str, backup: bool = True):
    """ Changes the processor name """
    system_info_path = _get_localized_folder(SYSTEM_CPU_INFO) + f'{CPU_INFO_NAME}'
    if not system_info_path:
        print(f'Could not determine which .lproj folder to use in {SYSTEM_CPU_INFO}.')
        print(f'Please make change your processor name manually')
        return

    if backup and not os.path.exists(f'{RESOURCES}{CPU_INFO_NAME}.backup'):
        shutil.copyfile(system_info_path, f'{RESOURCES}{CPU_INFO_NAME}.backup')

    with open(system_info_path, 'rb') as file:
        system_info = plistlib.load(file)
        system_info['UnknownCPUKind'] = new_name

    with open(system_info_path, 'wb') as file:
        plistlib.dump(system_info, file)

    print('Processor name updated !')


if __name__ == '__main__':

    if 'enabled' in os.popen('csrutil status').read():
        # We check that SIP is properly disabled before doing anything
        print('Please disable SIP before running this script')

    _need_privileges()

    parser = argparse.ArgumentParser(description='Customizes \'About this Mac\' section of a macOS system')
    parser.add_argument('--system-logo', type=_file_exists, default=RESOURCES + LOGO_NAME,
                        help='system logo to use. logo format must be TIFF')
    parser.add_argument('--model-name', type=str, default=MODEL_NAME,
                        help='custom model name')
    parser.add_argument('--processor-name', type=str, default=PROCESSOR_NAME,
                        help='custom processor name')
    args = parser.parse_args()

    set_system_logo(os.path.abspath(args.system_logo))
    set_model_name(args.model_name)
    set_processor_name(args.processor_name)




