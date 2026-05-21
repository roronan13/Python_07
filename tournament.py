import ex0
import ex1
import ex2


def battle(opponents: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]])\
            -> None:

    print(f"{len(opponents)} opponents involved ..")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            print(" - BATTLE - \n")

            opponent_1 = opponents[i][0]
            opponent_2 = opponents[j][0]
            strategy_1 = opponents[i][1]
            strategy_2 = opponents[j][1]

            print(f"{opponent_1.describe()}")
            print("   VS   ")
            print(f"{opponent_2.describe()}")
            print("   FIGHT !   ")

            try:
                strategy_1.act(opponent_1)
            except ex2.StrategyError as err:
                print(f"Battle error, aborting tournament : {err}")
                return

            try:
                strategy_2.act(opponent_2)
            except ex2.StrategyError as err:
                print(f"Battle error, aborting tournament : {err}")
                return


if __name__ == "__main__":
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()
    healing_factory = ex1.HealingCreatureFactory()
    transform_factory = ex1.TransformCreatureFactory()

    normal_strategy = ex2.NormalStrategy()
    aggressive_strategy = ex2.AggressiveStrategy()
    defensive_strategy = ex2.DefensiveStrategy()

    print("   TOURNAMENT 0 (basic)  ")
    creature_1 = flame_factory.create_base()
    creature_2 = healing_factory.create_base()
    print(f"[ ({creature_1.name} + Normal), (Healing + Defensive) ]")
    print("\n   *** Tournament ***   ")
    battle([(creature_1, normal_strategy), (creature_2, defensive_strategy)])

    print("\n\n   TOURNAMENT 1 (error)  ")
    creature_1 = flame_factory.create_base()
    creature_2 = healing_factory.create_base()
    print(f"[ ({creature_1.name} + Aggressive), (Healing + Defensive) ]")
    print("\n   *** Tournament ***   ")
    battle([(creature_1, aggressive_strategy), (creature_2, defensive_strategy)])

    print("\n\n   TOURNAMENT 2 (multiple)  ")
    creature_1 = aqua_factory.create_base()
    creature_2 = healing_factory.create_base()
    creature_3 = transform_factory.create_base()
    print(f"[ ({creature_1.name} + Normal), (Healing + Defensive), (Transform + Aggressive) ]")
    print("\n   *** Tournament ***   ")
    battle([(creature_1, normal_strategy), (creature_2, defensive_strategy), (creature_3, aggressive_strategy)])
