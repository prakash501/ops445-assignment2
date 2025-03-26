#!/usr/bin/env python3

import subprocess
import sys

def percent_to_graph(percent, total_chars):
    """
    Converts a percentage to a bar graph string.
    
    Args:
        percent (float): The percentage value (0-100)
        total_chars (int): Total length of the bar graph
    
    Returns:
        str: Bar graph string composed of '=' and spaces
    
    Example:
        >>> percent_to_graph(50, 10)
        '=====     '
    """
    if not 0 <= percent <= 100:
        raise ValueError("Percent must be between 0 and 100")
    
    # Calculate number of symbols to display
    num_symbols = round((percent / 100) * total_chars)
    num_spaces = total_chars - num_symbols
    
    # Create the graph string
    return '=' * num_symbols + ' ' * num_spaces

def call_du_sub(location):
    """
    Runs 'du -d 1' command on the target directory and returns the output as a list.
    
    Args:
        location (str): Target directory path
    
    Returns:
        list: Each element is a line from the du command output
    
    Example:
        >>> call_du_sub('/usr/local/lib')
        ['164028\t/usr/local/lib/heroku', '11072\t/usr/local/lib/python2.7', ...]
    """
    try:
        # Run the du command
        process = subprocess.Popen(
            ['du', '-d', '1', location],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        output, error = process.communicate()
        
        # Get the valid output even if there were some permission denied errors
        if output:
            return [line.strip() for line in output.split('\n') if line.strip()]
        return []
    except Exception as e:
        print(f"Error running du command: {e}", file=sys.stderr)
        return []
