def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import json
import os
import os.path
import uuid

import click
from profanity_check import predict_prob

import requests
import sys



VERSION = 0.1
MAX_WHISPER_LENGTH = 140
LENGTH_ERROR = 'verbose'
PROFANE_ERROR = 'profane'
APP_DATA_PATH = os.path.join(os.getenv("HOME"), ".whispers", "data.json")
DATABASE_URL = "http://localhost:5000"

def check_first_run():
    return False if os.path.isfile(APP_DATA_PATH) else True

def create_uuid():
    return uuid.uuid4().hex

def set_user_id(uuid):
    dirname = os.path.dirname(APP_DATA_PATH)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(APP_DATA_PATH, 'w') as appdata:
        data = {
            "uuid": uuid
        }
        json.dump(data, appdata)

def get_user_id():
    with open(APP_DATA_PATH, 'r') as appdata:
        data = json.load(appdata)
        return data

def post_user_id(uuid):
    url = DATABASE_URL + "/register_user"
    data = {
        "uuid": uuid
    }
    response = requests.post(url, json=data)
    if response.status_code != 201:
        click.echo("There was an issue registering the user. Please retry at a later time.")
        click.echo("Status Code: " + str(response.status_code))
        sys.exit()

def welcome():
    uuid = create_uuid()
    post_user_id(uuid)
    set_user_id(uuid)
    
    click.echo("Looks like this is your first time running Whispers. Welcome.")
    click.echo()
    click.echo("Whispers is a CLI tool for sending and receiving whispers from The Void.")
    click.echo("Each whisper that floats to you is unique for you. No one else has or will ever see it.")
    click.echo("Simultaneously, each whisper you send will be seen by only one person as it floats to them.")
    click.echo("Whispers get deleted the moment they are viewed, staying only with you.")
    click.echo()

def whispers_today():
    click.echo("152 Whispers today")

def sanitize_input(msg):
    if len(msg) > MAX_WHISPER_LENGTH:
        return LENGTH_ERROR
    elif predict_prob([msg])[0] > 0.6:
        return PROFANE_ERROR
    else:
        return ''

def receive_whisper():
    click.echo("A whisper floats to you:")

def upload_whisper(msg):
    pass

@click.command()
@click.option('-v', '--version', 'version', help='describe current whispers version', is_flag=True)
@click.option('-u', '--user-data', 'user', help='view personal user data', is_flag=True)
@click.option('-m', '--message', 'msg', help='message to whisper from CLI', default='', type=str)
def cli(version, user, msg):
    if version:
        click.echo("whispers v" + str(VERSION))
        return
    if user:
        click.echo("User ID: " + str(get_user_id()))
        return

    if check_first_run():
        welcome()

    whispers_today()
    receive_whisper()

    if msg == '':
        msg = click.prompt("Whisper something to someone", type=str)
    err = sanitize_input(msg)
    while err != '':
        if err == 'profane':
            click.echo("Your whisper seems to be profane. Please be kind, but we will not moderate")
            if click.confirm("Do you still want to post this?"):
                break
        if err == LENGTH_ERROR:
            click.echo("Your whisper seems to be longer than the max (" + str(len(msg)) + " > " + str(MAX_WHISPER_LENGTH) + " chars). Please shorten your whisper.")
        msg = click.prompt("Whisper something to someone", type=str)
        err = sanitize_input(msg)

    click.echo("Your whisper drifts into The Void")
    upload_whisper(msg)
