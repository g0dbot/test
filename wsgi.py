import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, get_user_by_username,
                             get_friendship, get_friendship_status, add_friend, delete_friend)

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass', '#')
    create_user('rob', 'robpass', '#')
    print('database intialized')

@app.cli.command("create-user", help="creates a user")
@click.argument("username", default="jer")
@click.argument("password", default="jerpass")
def cli_create_user(username, password):
    newuser = get_user_by_username(username)
    if not newuser:
        newuser = create_user(username, password, '#')
        print(newuser)
    else:
        print(f'{username} already exists')

"""FRIENDSHIP TESTS"""
@app.cli.command("friend-get-friendship", help="if 2 users are confirmed friends")
@click.argument("sender", default="bob")
@click.argument("receiver", default="rob")
def cliFriend_get_friendship(sender, receiver):
    user1 = get_user_by_username(sender)
    user2 = get_user_by_username(receiver)
    friendship = get_friendship(user1.id, user2.id)
    print(friendship)

@app.cli.command("friend-add-friend", help="if 2 users are confirmed friends")
@click.argument("sender", default="bob")
@click.argument("receiver", default="rob")
def cliFriend_add_friend(sender, receiver):
    user1 = get_user_by_username(sender)
    user2 = get_user_by_username(receiver)
    
    request = add_friend(user1.id, user2.id)
    
    print (request)
'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)