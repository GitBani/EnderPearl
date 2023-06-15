#!/usr/bin/python3

# Todo:
#   - restore and save data functions (json serialization)
#   - to, add, edit, remove commands

from bookmark_list import BookmarkList
import argparse
import sys

# List of users bookmarks
bk_list = BookmarkList()

# main parser
parser = argparse.ArgumentParser()

# sub parsers for different actions
subparsers = parser.add_subparsers(dest='action')

# "to" subparser
to_parser = subparsers.add_parser('to', help='Open a bookmark')
to_parser.add_argument('bookmark_index', type=int, help='Index of the bookmark you would like to open')
to_parser.add_argument('-p', '--private', action='store_true', help='Open the bookmark in a private tab')

# "add" subparser
add_link_parser = subparsers.add_parser('add', help='Add a bookmark')
add_link_parser.add_argument('bookmark_name', help='The name of the bookmark (wrap in quotes if it is multiple words)')
add_link_parser.add_argument('bookmark_link', help='The link to add')

# "edit" subparser
edit_parser = subparsers.add_parser('edit', help='edit a bookmark')
edit_parser.add_argument('bookmark_index', type=int, help='Index of the bookmark you would like to edit')

# "remove" subparser
remove_parser = subparsers.add_parser('remove', help='Remove a bookmark')
remove_parser.add_argument('bookmark_index', type=int, help='Index of the bookmark you would like to remove')

# "list" subparser
list_bookmarks_parser = subparsers.add_parser('list', help='List your bookmarks')

# Parse the command-line arguments
args = parser.parse_args()

# Check the selected action
if args.action == 'to':
    if args.private:
        # sys call to open browser to specific link in private tab
        pass
    else:
        # sys call to open browser to specific link
        pass
    # deal with potential errors (fail to open browser or link etc)

elif args.action == 'add':
    # prompt for bookmark name and link
    # check link validity
    # create bookmark and add it to the list
    pass

elif args.action == 'edit':
    # give prompts, check input validity and update info
    pass

elif args.action == 'remove':
    # give prompts, check input validity and update info
    pass

elif args.action == 'list':
    bk_list.print_bookmarks()
