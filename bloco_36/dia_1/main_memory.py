class MainMemory:
    def __init__(self):
        self.clean()

    def load(self, value):
        self.loaded_memory.append(value)

    def get(self, index):
        if type(self.loaded_memory[index] != int):
            return 0

        return self.loaded_memory[index] or 0

    def clean(self):
        self.loaded_memory = []
