user_param_fields = [
    {
        "description": "Количество параметров.",
        "is_dim": False,
        "name": "ym:up:params",
        "title": "Параметры",
        "type": "integer",
    },
    {
        "description": "Количество уникальных посетителей.",
        "is_dim": False,
        "name": "ym:up:users",
        "title": "Посетители",
        "type": "integer",
    },
    {
        "description": None,
        "is_dim": True,
        "name": "ym:up:counterID",
        "title": "Счетчик (id)",
        "type": "string",
        "src_key": "id",
    },
    {
        "description": None,
        "is_dim": True,
        "name": "ym:up:counterIDName",
        "title": "Счетчик",
        "type": "string",
    },
    {
        "description": "Первый уровень вложенности параметров посетителя",
        "is_dim": True,
        "name": "ym:up:paramsLevel1",
        "title": "Параметр посетителя, ур. 1",
        "type": "string",
    },
    {
        "description": "Второй уровень вложенности параметров посетителя",
        "is_dim": True,
        "name": "ym:up:paramsLevel2",
        "title": "Параметр посетителя, ур. 2",
        "type": "string",
    },
    {
        "description": "Третий уровень вложенности параметров посетителя",
        "is_dim": True,
        "name": "ym:up:paramsLevel3",
        "title": "Параметр посетителя, ур. 3",
        "type": "string",
    },
    {
        "description": "Четвертый уровень вложенности параметров посетителя",
        "is_dim": True,
        "name": "ym:up:paramsLevel4",
        "title": "Параметр посетителя, ур. 4",
        "type": "string",
    },
    {
        "description": "Пятый уровень вложенности параметров посетителя",
        "is_dim": True,
        "name": "ym:up:paramsLevel5",
        "title": "Параметр посетителя, ур. 5",
        "type": "string",
    },
]