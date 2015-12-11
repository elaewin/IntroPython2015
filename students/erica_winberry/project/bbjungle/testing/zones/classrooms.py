# coding=utf-8
"""
Rooms inside Parsely High

'Tale' mud driver, mudlib and interactive fiction framework
Copyright by Irmen de Jong (irmen@razorvine.net)
"""

from tale.shop import ShopBehavior, Shopkeeper
from tale.base import Item, Location, Exit, clone, Door
from tale.npc import NPC
from tale.pubsub import Listener
from tale import mud_context
from npcs.teachers import Librarian


def init(driver):
    # called when zone is first loaded
    pass

english = Location("English Class", 
    '''
    You step into the classroom and your teacher, Mr. Bushel, clears his throat.
    "You're late, as usual. I sincerely hope you remembered your homework." He holds out his hand expectantly.
    ''')

library = Location("Library", 
    """
    You're in the library, where you usually spend your after-school time in detention.
    """)

hallway_door = Door(["hallway", "hallway door", "south", "s", "out"], "hallways.north_hallway", short_description="An open door to the south leads back into the hallway.", 
    locked=False,
    opened=True)

library.add_exits([hallway_door])

english.add_exits([Exit(["w", "west"], "hallways.north_hallway", "The hallway to the west offers the possibility of escape.")])

cubby = Item("cubby", "study cubby")
cubby.add_extradesc({"cubby", "study cubby"}, "Your typical wooden study cubby. Generations of students in detention have scratched various messages into the aging wood. ")
cubby.add_extradesc({"scratches", "messages"}, "The cubby's wooden desk has a series of numbers freshly scratched into it: 16-32-64.")

book = Item("book", "dog-eared book")
book.add_extradesc({"book"}, "The book's title is Cryptography for Dummies. You remember skimming it during detention yesterday but that was a long time ago.")

librarian = Librarian("School Librarian", "f", race="human", title="Ms. Smith, the School Librarian", description="Ms. Smith, the school librarian.")
librarian.add_extradesc({"librarian", "school librarian"}, "Female, elderly, hair in a bun. Could she be more stereotypical?")

library.init_inventory([cubby, book, librarian])
