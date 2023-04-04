VALID_FOODS = [
    "Fish",
    "Egg fried rice",
    "Beetroot soup",
    "Salad",
    "Eggs and bacon",
    "Oatmeal",
    "Steak",
    "Grilled chicken",
    "Beef burger",
    "Chicken salad",
]

VALID_DRINKS = ["Vine", "Beer", "Orange juice", "Cola"]

SPECIAL_MENU = {
    "Vegetarian": {
        "Fish": {
            "weight": "500g",
            "prep.time": "30min",
            "calories": 650,
            "price": 6,
        },
        "Egg fried rice": {
            "weight": "350g",
            "prep.time": "15min",
            "calories": 400,
            "price": 3.5,
        },
    },
    "Vegan": {
        "Beetroot soup": {
            "weight": "300g",
            "prep.time": "10min",
            "calories": 200,
            "price": 2,
        },
        "Salad": {
            "weight": "200g",
            "prep.time": "8min",
            "calories": 100,
            "price": 2.5,
        },
    },
}

BREAKFAST = {
    "Eggs and bacon": {
        "weight": "400g",
        "prep.time": "15min",
        "calories": 450,
        "price": 3,
    },
    "Oatmeal": {
        "weight": "300g",
        "prep.time": "10min",
        "calories": 350,
        "price": 2,
    },
}

LUNCH = {
    "Steak": {
        "weight": "500g",
        "prep.time": "35min",
        "calories": 550,
        "price": 6.5,
    },
    "Grilled chicken": {
        "weight": "500g",
        "prep.time": "30min",
        "calories": 480,
        "price": 6,
    },
}

DINNER = {
    "Beef burger": {
        "weight": "400g",
        "prep.time": "25min",
        "calories": 400,
        "price": 4.5,
    },
    "Chicken salad": {
        "weight": "350g",
        "prep.time": "20min",
        "calories": 350,
        "price": 5.5,
    },
}

DRINKS = {
    "Alcohol": {
        "Vine": {
            "weight": "300ml",
            "prep.time": "3min",
            "calories": 15,
            "price": 4,
        },
        "Beer": {
            "weight": "300ml",
            "prep.time": "3min",
            "calories": 50,
            "price": 3,
        },
    },
    "Alcohol free": {
        "Orange juice": {
            "weight": "330ml",
            "prep.time": "3min",
            "calories": 80,
            "price": 2,
        },
        "Cola": {
            "weight": "330ml",
            "prep.time": "3min",
            "calories": 100,
            "price": 2,
        },
    },
}

SINGLE_TABLES = {
    1: "free",
    2: "free",
    3: "free",
    4: "free",
}

DOUBLE_TABLES = {
    1: "free",
    2: "free",
    3: "free",
}
FAMILY_TABLES = {
    1: "free",
    2: "free",
}
