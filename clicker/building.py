class Building:
    def __init__(self, name: str, batch: float = 0, cost: float = 0):
        self.name = name
        self.count = 0
        self.batch = batch
        self.cost = cost
        self.cost_multiplier = 1.15

    def __str__(self):
        return f"<{self.name} count={self.count}, batch={self.batch}>"

    def create(self, n: int = 1):
        self.count += n
        self.cost *= self.cost_multiplier ** n

    def generate_batches(self) -> float:
        return self.count * self.batch
