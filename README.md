# Jackbox_DoS

### What it is:

Jackbox_DoS is a Denial of Service tool (not purposefully) built for jackbox.tv. As far as I can tell it works for 
any of the games in the Jackbox party pack series. This was started as a project just to add smart bots to jackbox as a
test for myself. And was not meant in any malicious manner. If for some reason you decide to download this and use it I 
am not responsible for any damages or idiotic scenarios you get yourself in. 

### How it works

Jackbox_DoS works by using threading and websockets to rapidly connect and disconnect bots to jackbox.tv. It uses a 
library created by __ShineyDev__ and __Gorialis__ (https://github.com/ShineyDev/jackbox.py). In which websockets are 
used to create client sessions to jackbox.tv and of which I decided to use threading to create multiple clients in order
to flood a Jackbox party pack game. The scripts allow the rapid starting and stopping of the python program in order
to quickly crash the host client. Likely from Jackbox's load balancer, network monitor, or possibly an anti cheat client
taking notice to unusual activity and then decides to close the game as the safest outcome. 

### Why this shouldn't work

This shouldn't work for a few differnt reasons. First off, Jackbox can handle (at least) the connection of a large amount
of players at once. As demonstrated by large streamers getting 1000's of players to join their games in a few seconds. 
What Jackbox can't seem to handle is the connection and disconnection repeatedly. Secondly, the websockets in themselves 
seem like nothing special, they are maintained, data is passed through them, and then they are closed when a session ends. 
Which means that either jackbox.py has unusual responses or data that jackbox.tv isn't expecting, this program isn't passing
correct data, (in which case jackbox.tv's error handling needs to be better), or jackbox.tv has serious issues with how it 
handles the closing of websockets. 

## DISCLAIMER
I already said this before. But I'll say it again. DO NOT USE WITHOUT PERMISSION. And if you do, I am not responsible for
any damage caused. 

# How to use
It's fairly simple to setup 

    python version: 3.8.5 (Not strictly required I believe)
    
    pip install -r requirements.txt

    ## For DoS attack

    ./rapid_start_stop

    then enter the room code

    ## for a single (temporary, last only about 5 seconds) instance

    ./single_connection

Once again. Please don't use this without permission