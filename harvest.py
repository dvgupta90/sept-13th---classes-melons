############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name 

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code





def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskmelon = MelonType("musk",int(1998),"green","seedless","bestseller","muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType("cas", int(2003), "orange", "has seeds", "not bestseller", "casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", int(1996),"green","has seeds", "not a bestseller","crenshaw")
    crenshaw.add_pairing("proscuitto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", int(2013), "yellow", "has seeds", "bestseller", "yellow_watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for a_melon_type in melon_types:
        print(a_melon_type.name, "pairs with ")
        for pairing in a_melon_type.pairings:
            print(pairing)

print_pairing_info(make_melon_types())





def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_code_lookup_dict = {}
    for a_melon_type in melon_types:
        key = a_melon_type.code
        value = a_melon_type
        melon_code_lookup_dict[key] = value
    print(melon_code_lookup_dict)
    return (melon_code_lookup_dict)

make_melon_type_lookup(make_melon_types())


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""


    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, MelonType_code , shape_rating, color_rating, harvest_field, harvest_person, 
                 name):

        
       
        self.MelonType_code = MelonType_code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvest_person = harvest_person
        self.name = name 

    def is_sellable(self,shape_rating,color_rating,harvest_field):

        if self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field != 3:
            return True

        False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    all_melon_types_numbers = []

    MelonType_code = make_melon_type_lookup(make_melon_types())

    melon_1 = Melon(MelonType_code['yw'],8, 7, 2, "sheila","melon_1")
    all_melon_types_numbers.append(melon_1)

    return  all_melon_types_numbers    





def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 

    for melon_type_number in melons:
        print("harvested by", melon_type_number.harvest_person , "from Field", melon_type_number.harvest_field)

get_sellability_report(make_melons(make_melon_types))        





