from bookmark import Bookmark

class BookmarkList:
    __bk_dict = {}
    
    def add_bookmark(self, name: str, link: str) -> None:
        new_bookmark = Bookmark(name, link)
        self.__bk_dict[len(self.__bk_dict) + 1] = new_bookmark

    def edit_bookmark(self, bookmark_num: int, new_name: str = "", new_link: str = "") -> None:
        bk_to_edit = self.__bk_dict[bookmark_num]

        if new_name:
            bk_to_edit.set_name(new_name)
            
        if new_link:
            bk_to_edit.set_link(new_link)

    def remove_bookmark(self, bookmark_num: int) -> None:
        self.__bk_dict.pop(bookmark_num)

    def get_bookmark(self, bookmark_num: int) -> Bookmark:
        return self.__bk_dict[bookmark_num]
    
    def print_bookmarks(self) -> None:
        if not self.__bk_dict:
            print("No saved bookmarks!")
            return
        
        for i in range(1, len(list(self.__bk_dict)) + 1):
            bk = self.__bk_dict[i]
            print(f"{(i)} {bk.get_name()} - {bk.get_link()}")
