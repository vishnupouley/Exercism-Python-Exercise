from collections import Counter
"""
(module) collections
This module implements specialized container datatypes providing alternatives to Python's general purpose built-in containers, dict, list, set, and tuple.

namedtuple factory function for creating tuple subclasses with named fields
deque list-like container with fast appends and pops on either end
ChainMap dict-like class for creating a single view of multiple mappings
Counter dict subclass for counting hashable objects
OrderedDict dict subclass that remembers the order entries were added
defaultdict dict subclass that calls a factory function to supply missing values
UserDict wrapper around dictionary objects for easier dict subclassing
UserList wrapper around list objects for easier list subclassing
UserString wrapper around string objects for easier string subclassing

(class) Counter
Dict subclass for counting hashable items. Sometimes called a bag or multiset. Elements are stored as dictionary keys and their counts are stored as dictionary values.

>>> c = Counter('abcdeabcdabcaba')  # count elements from a string
>>> c.most_common(3)                # three most common elements
[('a', 5), ('b', 4), ('c', 3)]
>>> sorted(c)                       # list all unique elements
['a', 'b', 'c', 'd', 'e']
>>> ''.join(sorted(c.elements()))   # list elements with repetitions
'aaaaabbbbcccdde'
>>> sum(c.values())                 # total of all counts
15
"""

def create_inventory(items: list[str]) -> dict[str, int]:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    return {item: items.count(item) for item in items}


def add_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    # return {item: inventory.get(item, 0) + items.count(item) if inventory.get(item, False) else items.count(item) for item in set(items)}
    return dict(Counter(inventory) + Counter(items))


def decrement_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    return {
        item: (
            inventory.get(item, 0) - items.count(item)
            if inventory.get(item, 0) - items.count(item) > -1
            else 0
        )
        for item in inventory
    }


def remove_item(inventory: dict[str, int], item: str) -> dict[str, int]:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, "")
    return inventory


def list_inventory(inventory: dict[str, int]) -> list[tuple[str, int]]:
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(key, value ) for key, value in inventory.items() if value > 0]