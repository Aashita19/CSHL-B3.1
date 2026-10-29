class Summon:
    _total_created = 0
    _active_count = 0
    _total_power = 0.0

    def __init__(self, name="Apprentice", power=100.0, mana_cost=20):
        self._id = f"SUM-{Summon._total_created + 1:03d}"
        self._name = name
        self._active = True

        self._validate_name(name)
        self._validate_power(power)
        self._validate_mana(mana_cost)

        self._power = float(power)
        self._mana_cost = mana_cost

        Summon._total_created += 1
        Summon._active_count += 1
        Summon._total_power += self._power

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")

    @staticmethod
    def _validate_power(power):
        if (isinstance(power, bool)
                or not isinstance(power, (int, float))
                or power <= 0):
            raise ValueError("Power must be greater than 0.")

    @staticmethod
    def _validate_mana(mana_cost):
        if (isinstance(mana_cost, bool)
                or not isinstance(mana_cost, int)
                or mana_cost < 0):
            raise ValueError("Mana cost must be a non-negative integer.")


    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_power(self):
        return self._power

    def get_mana_cost(self):
        return self._mana_cost

    def is_active(self):
        return self._active

    def set_name(self, name):
        self._validate_name(name)
        self._name = name

    def set_power(self, new_power):
        self._validate_power(new_power)

        if self._active:
            Summon._total_power -= self._power
            Summon._total_power += float(new_power)

        self._power = float(new_power)

    def set_mana_cost(self, mana_cost):
        self._validate_mana(mana_cost)
        self._mana_cost = mana_cost

    def upgrade(self, amount):
        if (isinstance(amount, bool)
                or not isinstance(amount, (int, float))
                or amount <= 0):
            raise ValueError("Upgrade amount must be positive.")

        self.set_power(self._power + amount)
        print(f"[SYSTEM] {self._id} upgraded by {amount} power.")

    def deactivate(self):
        if not self._active:
            print(f"[WARN] {self._id} is already inactive. Action skipped.")
            return

        self._active = False
        Summon._active_count -= 1
        Summon._total_power -= self._power

        print(f"[SYSTEM] {self._id} deactivated.")

    def display(self):
        print(
            f"[ID: {self._id} | Name: {self._name} | "
            f"Power: {self._power:.1f} | "
            f"Mana: {self._mana_cost} | Active: {self._active}]"
        )

    @classmethod
    def display_global_stats(cls):
        print(
            f"Total Created: {cls._total_created} | "
            f"Active Count: {cls._active_count} | "
            f"Aggregate Power: {cls._total_power:.1f}"
        )


def main():
    print("=== SUMMON ENGINE TEST SUITE ===")

    # PHASE 1: Multi-instance instantiation
    print("\n--- Phase 1: Instantiation ---")

    summon1 = Summon()

    summon2 = Summon("Fire Dragon", 250, 50)

    summon3 = Summon("Frost Mage", 180, 35)

    summon1.display()
    summon2.display()
    summon3.display()
    Summon.display_global_stats()

    print("\n--- Phase 2: Mutator Bounds Validation ---")

    original_power = summon1.get_power()

    try:
        summon1.set_power(-50)
    except ValueError as error:
        print(f"[ERROR] {error}")

    try:
        summon1.set_name("")
    except ValueError as error:
        print(f"[ERROR] {error}")

    print("Power unchanged:", summon1.get_power() == original_power)
    summon1.display()
    Summon.display_global_stats()

    # PHASE 3: Valid state transformation
    print("\n--- Phase 3: State Transformation ---")

    summon2.upgrade(50)
    summon2.display()
    Summon.display_global_stats()

    # PHASE 4: Lifecycle transformation
    print("\n--- Phase 4: Lifecycle Transformation ---")

    summon3.deactivate()
    summon3.display()
    Summon.display_global_stats()

    print("Historical total remains:", Summon._total_created)

    # PHASE 5: Redundant safeguard
    print("\n--- Phase 5: Redundant Safeguards ---")

    summon3.deactivate()  
    Summon.display_global_stats()

    print("\n=== TEST SUITE COMPLETE ===")


if __name__ == "__main__":
    main()

