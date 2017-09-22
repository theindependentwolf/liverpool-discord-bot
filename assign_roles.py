###################################################################################################################################################
#
#       File Name       :   csv_mysql.py
#
#       Description     :   exports data from csv file to MySQL
#
#
#       Revision History
#       _______________________________________________________________________________________________________________________________________
#
#       No.     Author              Date                Version             Comments
#       _______________________________________________________________________________________________________________________________________
#
#       1       Aniruth Oblah       Mar 10, 2017        1.0                 Initial Version
#
# 
#################################################################################################################################################
import config
import discord
import asyncio
import praw
from googly_sheets import Gsheet


def verify_user(ctx, username, bot):
    """
    Give the verified role to the user. Allow to assign role only if command issuer has mod or admin status
    """
    #Get server 
    server = ctx.message.server

    if is_author_mod(ctx):
        if user_exists(ctx, username, server):
            result = assign_verified_role(server, username, bot)
            return(result)
        else:
            return ("User doesn't exist")
    else:
        return("You're not a mod or an admin.")


def is_author_mod(ctx):
    """
    Check if author of command has mod/admin status
    """
    author_roles = ctx.message.author.roles

    for role in author_roles:
        if config.MOD_ROLE == role.name or config.ADMIN_ROLE == role.name:
            return True
    return False

def user_exists(ctx, username, server):
    """
    Get member if it exists
    """
    if server.get_member_named(username.strip()):
        return True
    else:
        return False

@asyncio.coroutine
def assign_verified_role(server, username, bot):
    """
    Assign the verified role to the user
    """
    member = server.get_member_named(username.strip())
    role = discord.utils.get(server.roles, name=config.VERIFIED_ROLE)
    if bot.add_roles(member, role):
        bot.add_roles(member, role)
        return(username + " verified!")
    else:
        return("Something went wrong. Please verify manually.")

def get_reddit_user(username, server):
    """
    Checks through comments of a reddit thread and gets the comment owner
    """
    reddit = praw.Reddit(user_agent=config.my_user_agent,
                     client_id=config.my_client_id,
                     client_secret=config.my_client_secret,
                     username=config.my_username,
                     password=config.my_password)
    submission = reddit.submission(id='6t80cl')
    print(submission)
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
#        if server.get_member_named(top_level_comment.body.lower().replace("@","").strip()) == username:
        if top_level_comment.body.lower().replace("@","").strip() == username.lower():
            print("---------------------MATCH FOUND---------------------")
            top_level_comment.reply("Verified.")
            make_googlesheets_entry(username, top_level_comment.author.name)
            return(top_level_comment.author.name)
    print("nothing found")



def make_googlesheets_entry(discord_name, reddit_username):
    """
    Make an entry in Google Sheets
    """
    gs = Gsheet()
    data = gs.get_gsheet()
    start_of_data = len(data)+ 1
    range_of_data = "A" + str(start_of_data) + ":B" + str(start_of_data)
    reddit_name = "https://www.reddit.com/user/" + reddit_username
    worksheet = gs.get_worksheet()
    cell_list = worksheet.range(range_of_data)
    cell_list[0].value = discord_name
    cell_list[1].value = reddit_name
    worksheet.update_cells(cell_list)    
