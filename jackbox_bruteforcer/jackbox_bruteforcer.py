import jackbox
import asyncio
import threading
import time
import sys

live_games = []
test_games = open("jackbox_codes.txt")
game_codes = test_games.readlines()

def thr(i):
    # we need to create a new loop for the thread, and set it as the 'default'
    # loop that will be returned by calls to asyncio.get_event_loop() from this
    # thread.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(do_stuff(i, i))
    loop.run_forever()

async def do_stuff(id, i):
    client = jackbox.Client()
    try:
        await client.connect(game_codes[id], "Bot"+str(i))
        print("Bot" + str(i) + " Connected")
        live_games.append(game_codes[id])
    except Exception as e:
        print("Room "+game_codes[id]+" not available")

    client.close()
    do_stuff(game_codes[id + 100], i)


def main():
    num_threads = 100
    threads = [ threading.Thread(target = thr, args=(i,)) for i in range(num_threads) ]
    [ t.start() for t in threads ]
    [ t.join() for t in threads ]


if __name__ == "__main__":
    main()
