from bookmark_collection import BookmarkCollection
import webbrowser
import validators


url = "https://www.youtube.com/playlist?list=PLuCCEiJQFxV6LrCgajq7R0-jGmKuJiQCd"


def to(bks: BookmarkCollection, bk_name: str, new_window=False) -> None:
    if bks.length() == 0:
        print("No saved bookmarks")
        exit(1)
    
    if not bks.in_collection(bk_name):
        print("Selected bookmark does not exist")
        exit(1)

    webbrowser.open(bks.get_link(bk_name), new=new_window)
    exit(0) # since no changes are made, exit without saving


def add(bks: BookmarkCollection, new_bk_name: str, new_bk_link: str) -> None:
    if not validators.url(new_bk_link):
        print("Invalid url")
        exit(1)

    bks.add_bookmark(new_bk_name, new_bk_link)


def edit(bks: BookmarkCollection, bk_name: str) -> None:
    if bks.length() == 0:
        print("You have no bookmarks to edit")
        exit(1)
    
    if not bks.in_collection(bk_name):
        print("Selected bookmark does not exist")
        exit(1)

    print(f"Selected: {bk_name} - {bks.get_link(bk_name)}\n")

    new_name = input("Enter new name, or just hit enter to cancel: ")
    new_link = input("Enter new url, or just hit enter to cancel: ")

    if not new_name and not new_link:
        print("\nNo changes where made.")
        exit(0) # to avoid redundant save
    
    bks.edit_bookmark(bk_name, new_name, new_link)
    print(f"\nBookmark updated to: {new_name if new_name else bk_name} - {bks.get_link(new_name if new_name else bk_name)}")


def remove(bks: BookmarkCollection, bk_name: str) -> None:
    if bks.length() == 0:
        print("You have no bookmarks to remove")
        exit(1)
    
    if not bks.in_collection(bk_name):
        print("Selected bookmark does not exist")
        exit(1)

    bks.remove_bookmark(bk_name)
    print("Successfully removed bookmark")


def list(bks: BookmarkCollection) -> None:
    print("Your saved bookmarks:")
    bks.print_bookmarks()
    exit(0) # since no changes are made, exit without saving
