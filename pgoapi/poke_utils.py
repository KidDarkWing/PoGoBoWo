import os


def pokemon_iv_percentage(pokemon):
    return ((pokemon.get('individual_attack', 0) + pokemon.get('individual_stamina', 0) + pokemon.get(
        'individual_defense', 0) + 0.0) / 45.0) * 100.0


def get_pokemon_num(res):
    inventory_delta = res['responses']['GET_INVENTORY'].get('inventory_delta', {})
    inventory_items = inventory_delta.get('inventory_items', [])
    inventory_items_dict_list = map(lambda x: x.get('inventory_item_data', {}), inventory_items)
    inventory_items_pokemon_list = filter(lambda x: 'pokemon_data' in x and 'is_egg' not in x['pokemon_data'], inventory_items_dict_list)
    return len(inventory_items_pokemon_list)


def get_inventory_data(res, poke_names):
    inventory_delta = res['responses']['GET_INVENTORY'].get('inventory_delta', {})
    inventory_items = inventory_delta.get('inventory_items', [])
    inventory_items_dict_list = map(lambda x: x.get('inventory_item_data', {}), inventory_items)
    inventory_items_pokemon_list = filter(lambda x: 'pokemon_data' in x and 'is_egg' not in x['pokemon_data'],
                                          inventory_items_dict_list)
    inventory_items_pokemon_list_sorted = sorted(inventory_items_pokemon_list, key=lambda x: poke_names[str(x['pokemon_data']['pokemon_id'])].encode('ascii', 'ignore'))

    inventory_items_pokemon_list_sorted = sorted(
        inventory_items_pokemon_list,
        key=lambda pokemon: pokemon['pokemon_data']['cp']
    )
    return (os.linesep.join(map(lambda x: "{0}, CP {1}, IV {2:.2f}".format(
        poke_names[str(x['pokemon_data']['pokemon_id'])].encode('ascii', 'ignore'),
        x['pokemon_data']['cp'],
        pokemon_iv_percentage(x['pokemon_data'])), inventory_items_pokemon_list_sorted)))


def get_incubators_stat(res):
    inventory_delta = res['responses']['GET_INVENTORY'].get('inventory_delta', {})
    inventory_items = inventory_delta.get('inventory_items', [])
    inventory_items_incubators = map(lambda x: x.get('inventory_item_data', {}), inventory_items)
    inventory_items_dict_list = map(lambda x: x.get('egg_incubators', {}), inventory_items_incubators)
    inventory_items_incubator_list = filter(lambda x: 'egg_incubator' in x and 'target_km_walked' in x, inventory_items_dict_list)
    if inventory_items_incubator_list:
        return (os.linesep.join(map(lambda x: "Incubator {0:.2f} km, walked {1:.2f} km".format(
            x['egg_incubator']['target_km_walked'],
            x['egg_incubator']['start_km_walked']), inventory_items_incubator_list)))
    else:
        return 'No incubators'
