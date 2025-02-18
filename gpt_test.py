import jackbox
import time
import random
import asyncio

class JackboxBot:
    def __init__(self, game_id, player_name, bot_id):
        self.game_id = game_id
        self.player_name = player_name
        self.bot_id = bot_id
        self.client = jackbox.Client()

    async def connect(self):
        print(f"Bot {self.bot_id} is trying to connect to the game...")
        # You can use `game_id` to join the specific Jackbox game
        await self.client.connect(self.game_id, self.player_name)
        print(f"Bot {self.bot_id} has joined the game!")

    async def play_game(self):
        print(f"Bot {self.bot_id} is waiting for 30 seconds before leaving...")
        time.sleep(30)
        print(f"Bot {self.bot_id} is disconnecting...")
        await self.client.close()

    def answer_question(self):
        # Simulate answering a question by choosing a random answer
        available_answers = ["A", "B", "C", "D"]  # Example answers
        selected_answer = random.choice(available_answers)
        print(f"Bot {self.bot_id} selects answer: {selected_answer}")
        self.client.submit_answer(selected_answer)

async def start_game_with_bots(game_id, num_bots):
    bots = []
    for i in range(num_bots):
        player_name = f"Bot_{i + 1}"
        bot = JackboxBot(game_id, player_name, i + 1)
        await bot.connect()
        bots.append(bot)
        
    # Start game actions for each bot
    for bot in bots:
        bot.play_game()

def thr(id, i):
    # we need to create a new loop for the thread, and set it as the 'default'
    # loop that will be returned by calls to asyncio.get_event_loop() from this
    # thread.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(start_game_with_bots(id, i))
    loop.run_forever()

if __name__ == "__main__":
    game_id = input("Enter the Jackbox Game ID: ")
    num_bots = int(input("Enter the number of bots to connect: "))
    
    thr(game_id, num_bots)
