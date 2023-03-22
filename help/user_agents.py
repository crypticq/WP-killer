import random
from pathlib import Path
class UserAgent:

    def __init__(self) -> None:
        pass

    def read_file(self):
        with open(Path(__file__).parent / "agents.txt") as f:
            return f.read().splitlines()
    
    def random(self):
        return random.choice(self.read_file())
    





    
