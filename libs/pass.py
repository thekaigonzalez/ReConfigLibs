# gpass [wrapper of getpass]

import getpass

def pass_prompt(args):
    return getpass.getpass(args[0])

def pass_username(args):
    return getpass.getuser()

NAME="getpass"
TYPE='full-lib'

rcfg_registers = {
    'getpassword': pass_prompt,
    'getuser': pass_username
}