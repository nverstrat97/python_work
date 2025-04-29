def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    """
    Calculate the guild permissions based on the given bitwise inputs.
    
    Parameters:
    glorfindel (int): Bitwise representation of Glorfindel's permissions.
    galadriel (int): Bitwise representation of Galadriel's permissions.
    elendil (int): Bitwise representation of Elendil's permissions.
    elrond (int): Bitwise representation of Elrond's permissions.
    
    Returns:
    int: Combined bitwise representation of all permissions.
    """
    print("---------------------------------")
    print(f"Inputs: {glorfindel}, {galadriel}, {elendil}, {elrond}")
    return glorfindel | galadriel | elendil | elrond
