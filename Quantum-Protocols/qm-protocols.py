import re

def qm_protocols(data):
    """
    Function to parse QM_Protocols from the given data.
    """
    # Regular expression pattern to match QM_Protocols
    pattern = r"QM_Protocols\s*:\s*(?P<protocols>[\w\s\-\/]+)"

    # Find matches using the pattern
    matches = re.findall(pattern, data)

    # If no matches found, return an empty list
    if not matches:
        return []

    # Extract the protocols from the matches
    protocols = [match.group("protocols") for match in matches]

    # Return the list of protocols
    return protocols
