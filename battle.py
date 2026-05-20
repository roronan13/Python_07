import ex0


def create_creature(factory: ex0.CreatureFactory) -> None:
    print("\nTESTING FACTORY")

    try:
        creature_1 = factory.create_base()
    except Exception as e:
        print(f"{e}")
        return
    try:
        creature_2 = factory.create_evolved()
    except Exception as e:
        print(f"{e}")
        return

    print(f"{creature_1.describe()}")
    print(f"{creature_1.attack()}")
    print(f"{creature_2.describe()}")
    print(f"{creature_2.attack()}")


def base_battle(aqua_factory: ex0.AquaFactory, flame_factory: ex0.FlameFactory) -> None:
    print("\nTESTING BATTLE")

    creature_1 = aqua_factory.create_base()
    creature_2 = flame_factory.create_base()

    print(f"{creature_1.describe()}")
    print("   VS   ")
    print(f"{creature_2.describe()}")
    print("   FIGHT !   ")
    print(f"{creature_1.attack()}")
    print(f"{creature_2.attack()}")


if __name__ == "__main__":
    flame_factory: ex0.FlameFactory = ex0.FlameFactory()
    aqua_factory: ex0.AquaFactory = ex0.AquaFactory()

    create_creature(flame_factory)
    create_creature(aqua_factory)

    base_battle(aqua_factory, flame_factory)
