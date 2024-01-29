#!/usr/bin/python3
"""
100-main
"""
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py subreddit_name")
        sys.exit(1)

    # Get subreddit name from command-line arguments
    subreddit_name = sys.argv[1]

    # Call the function and print the result
    subscribers_count = number_of_subscribers(subreddit_name)
    if subscribers_count > 0:
        print(f"The subreddit /r/{subreddit_name} has {subscribers_count} subscribers.")
        print("OK")
    else:
        print(f"The subreddit /r/{subreddit_name} is not valid or doesn't exist.")
        print("OK")