from collections import defaultdict

def count_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return str(len(words))


def character_frequency(text:str) -> int:
    """
    Counts the frequency of each character in a given text.
    
    Args:
        text (str): The text to count character frequency in.
        
    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    frequency = defaultdict(int)
    for char in text:
        ch = char.lower()
        frequency[ch] += 1
    return frequency

def order_map(frequency_map):
    """
    Orders the frequency map by frequency in descending order.
    
    Args:
        frequency_map (dict): The frequency map to order.
        
    Returns:
        dict: The ordered frequency map.
    """
    output = []
    for key, val in frequency_map.items():
        output.append({"char":key, "num":val})
    output.sort(key=lambda x: x["num"], reverse=True)
    return output