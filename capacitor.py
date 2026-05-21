import ex1


def action_for_healing(creature) -> None:
    print(f"{creature.describe()}")
    print(f"{creature.attack()}")
    print(f"{creature.heal()}")


def action_for_transforming(creature) -> None:
    print(f"{creature.describe()}")
    print(f"{creature.attack()}")
    print(f"{creature.transform()}")
    print(f"{creature.attack()}")
    print(f"{creature.revert()}")


if __name__ == "__main__":
    healing_factory = ex1.HealingCreatureFactory()

    print("   TESTING CREATURE WITH HEALING CAPABILITY   ")
    print(" -- base : ")
    sproutling = healing_factory.create_base()
    action_for_healing(sproutling)
    print(" -- evolved : ")
    bloomelle = healing_factory.create_evolved()
    action_for_healing(bloomelle)

    transforming_factory = ex1.TransformCreatureFactory()

    print("\n   TESTING CREATURE WITH TRANSFORMING CAPABILITY   ")
    print(" -- base : ")
    shiftling = transforming_factory.create_base()
    action_for_transforming(shiftling)
    print(" -- evolved : ")
    morphagon = transforming_factory.create_evolved()
    action_for_transforming(morphagon)
