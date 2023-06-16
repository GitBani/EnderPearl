
import argparse

# main parser
parser = argparse.ArgumentParser()

# sub parsers for different actions
subparsers = parser.add_subparsers(dest='action')

# "to" subparser
to_parser = subparsers.add_parser('to', help='Open a bookmark')
to_parser.add_argument('bookmark', help='Bookmark you would like to open')
to_parser.add_argument('-n', '--new', action='store_true', help='Open the bookmark in a new window')

# "add" subparser
add_link_parser = subparsers.add_parser('add', help='Add a bookmark')
add_link_parser.add_argument('bookmark_name', help='The name of the bookmark (wrap in quotes if it is multiple words)')
add_link_parser.add_argument('bookmark_link', help='The link to add')

# "edit" subparser
edit_parser = subparsers.add_parser('edit', help='edit a bookmark')
edit_parser.add_argument('bookmark', help='Bookmark you would like to edit')

# "remove" subparser
remove_parser = subparsers.add_parser('remove', help='Remove a bookmark')
remove_parser.add_argument('bookmark', help='Bookmark you would like to remove')

# "list" subparser
list_bookmarks_parser = subparsers.add_parser('list', help='List your bookmarks')

# Parse the command-line arguments
args = parser.parse_args()
