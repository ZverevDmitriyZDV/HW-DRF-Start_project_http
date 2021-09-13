from django.shortcuts import render
from django.http import HttpResponse
import re

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view_start(request):
    msg = [key for key in DATA.keys()]
    return HttpResponse(f"На данной странице вы можете просмотреть блюда:{str(msg)}")


def give_dish_view(request, dish):
    new_dict_dish = {}
    qty = request.GET.get("servings", 1)
    dish_ingredients = DATA.get(dish, {})
    for key, value in dish_ingredients.items():
        new_dict_dish.setdefault(key, value*int(qty))

    return render(request, 'calculator/index.html', dict(recipe=new_dict_dish))
