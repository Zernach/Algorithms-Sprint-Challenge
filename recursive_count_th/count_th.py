'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# The instructions say to use recursion, but would recursion be any faster in this situation?
# No, I don't think so.

def count_th(word):
    
    count = 0

    # Cycle through all 2-letter windows within the word provided.
    # Count how many times a window says "th"
    for i in range(0, len(word)-1):
        window = word[i:i+2]
        if window == 'th':
            count += 1

    return count
