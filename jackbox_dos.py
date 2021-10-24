import jackbox
import asyncio
import threading
import time
import sys

def thr(id, i):
    # we need to create a new loop for the thread, and set it as the 'default'
    # loop that will be returned by calls to asyncio.get_event_loop() from this
    # thread.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(do_stuff(id, i))
    loop.run_forever()

async def do_stuff(id, i):
    print("Bot" + str(i) + " Connecting...")
    client = jackbox.Client()
    await client.connect(id, "Bot"+str(i))
    print("Bot" + str(i) + " Connected")


def main(id):
    num_threads = 100
    threads = [ threading.Thread(target = thr, args=(id, i,)) for i in range(num_threads) ]
    [ t.start() for t in threads ]
    [ t.join() for t in threads ]


if __name__ == "__main__":
    main(sys.argv[1])

