import ex0
import ex1
import ex2


def battle(opponents: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]])\
            -> None:

    print(f"{len(opponents)} opponents involved ..")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            print(" - BATTLE - ")
            
            opponent_1 = opponents[i][0]
            opponent_2 = opponents[j][0]
            strategy_1 = opponents[i][1]
            strategy_2 = opponents[j][1]

            print(f"{opponent_1.describe()}")
            print("   VS   ")
            print(f"{opponent_2.describe()}")
            print("   FIGHT !   ")
            print(f"{opponent_1.strategy_1.act()}")
            print(f"{opponent_2.strategy_2.act()}")


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
    print("*** Tournament ***")
    battle([(creature_1, normal_strategy), (creature_2, defensive_strategy)])
