#!/usr/bin/python3

from argparser import args # Creates parsers, parses arguments and stores them in args
from bookmark_collection import BookmarkCollection
import actions
import data_operations

if __name__ == "__main__":
    # restore data and store it into object (if file is empty, empty dict)
    bookmarks = BookmarkCollection(data_operations.restore_data())
    
    # Check the selected action
    if args.action == 'to':
        actions.to(bookmarks, args.bookmark, args.new)

    elif args.action == 'add':
        actions.add(bookmarks, args.bookmark_name, args.bookmark_link)

    elif args.action == 'edit':
        actions.edit(bookmarks, args.bookmark)

    elif args.action == 'remove':
        actions.remove(bookmarks, args.bookmark)

    elif args.action == 'list':
        actions.list(bookmarks)
    
    else:
        print("No arguments provided. Try enderpearl.py --help")
        exit(0)

    data_operations.save_data(bookmarks)
