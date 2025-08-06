from typing import Any, Dict, Iterable, Optional
from collections import Counter
"""Functions to manage a users shopping cart items."""


def add_item(current_cart: Dict[str, int], items_to_add:Iterable[str]) -> Dict[str, int]:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    return dict(Counter(current_cart) + Counter(items_to_add))


def read_notes(notes: Iterable[str]) -> Dict[str, int]:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict(Counter(notes))


def update_recipes(ideas: Dict[str, Dict[str, int]], recipe_updates:Iterable[Any]) -> Dict[str, Dict[str, int]]:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    
    return ideas.update(dict(recipe_updates)) or ideas


def sort_entries(cart: Dict[str, int]):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    return dict(reversed(sorted({key: [cart[key]] + aisle_mapping[key] for key, value in cart.items()}.items())))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    return {key: store_inventory[key] 
    if not fulfillment_cart.get(key, None) 
    else ['Out of Stock'] + store_inventory[key][1:] 
    if store_inventory[key][0] - fulfillment_cart[key][0] == 0 
    else [store_inventory[key].pop(0) - fulfillment_cart[key].pop(0)] + store_inventory[key] 
    for key in store_inventory.keys()}
    
"""
{key: [store_inventory[key].pop(0) - fulfillment_cart[key].pop(0) 
if fulfillment_cart.get(key, None) 
else store_inventory[key].pop(0)] + store_inventory[key] 
if store_inventory[key][0] - fulfillment_cart[key][0] != 0 
else ['Out of Stock'] + store_inventory[key][1:] 
if fulfillment_cart.get(key, None) 
else store_inventory[key] 
for key in store_inventory.keys()}

{key: store_inventory[key] 
if not fulfillment_cart.get(key, None) 
else ['Out of Stock'] + store_inventory[key][1:] 
if store_inventory[key][0] - fulfillment_cart[key][0] != 0 
else [store_inventory[key].pop(0) - fulfillment_cart[key].pop(0)] + store_inventory[key] 
for key in store_inventory.keys()}

"""