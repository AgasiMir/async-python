from time import sleep
import asyncio


# Максимальное время для каста заклинания
max_cast_time = 3  # Секунды

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]


spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
}


async def cast_spell(student, spell, cast_time):

    await asyncio.sleep(cast_time)
    if cast_time <= max_cast_time:
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")
    else:
        print(
            f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield."
        )


async def main():
    tasks = [
        asyncio.wait_for(
            asyncio.shield(cast_spell(student, spell, cast_time)), timeout=max_cast_time
        )
        for student in students
        for spell, cast_time in spells.items()
    ]

    try:
        await asyncio.gather(*tasks)
    except asyncio.TimeoutError:
        m = max(spells, key=lambda x: spells[x])
        await asyncio.sleep(spells[m] + 0.5)


asyncio.run(main())
