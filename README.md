# liverpool-discord-bot
Liverpool Discord Bot using Python


pdlb.py is the main file and functions.py contains all the necessary functions that go with it. 


Pre-requisities:
---------------

1. Python3

2. discord.py which you can get using 
    $python3 -m pip install -U discord.py

3. Beautiful Soup.   
    $pip install bs4

4. urllib

5. An app on the discord developer website.

6. Redis NoSQL DB



Instructions:
---------------

1. Set up a new app in the Discord Developer site and get a token. 

2. Add bot to your Discord server by pasting this link in your web browser, with your token information. https://discordapp.com/api/oauth2/authorize?client_id=<your token goes here>&scope=bot&permissions=0, 

2. Make sure you install all the pre-requisies. 

3. Create a config.py file where you store all your credentials, params, and "token".

4. Run pdlb.py file



Features Recently Added:
------------------------

1. Discord verification for /r/LiverpoolFC Discord Server via Reddit --> Checks if new discord user has commented on the verification thread on reddit, adds an entry to google sheets and adds the verified role to the user so they can participate in all channels.
2. Live Scores !score (premier league)
3. Next 5 fixtures for Liverpool
4. Automated the next fixture


To be Done:
--------------

1. Logging
2. Clean the code  
