class BookmarkCollection:
    def __init__(self, bk_dict={}) -> None:
        self.__bk_dict = bk_dict
    
    def add_bookmark(self, name: str, link: str) -> None:
        self.__bk_dict[name] = link

    def edit_bookmark(self, bookmark_name: str, new_name: str = "", new_link: str = "") -> None:            
        if new_link:
            self.__bk_dict[bookmark_name] = new_link
        if new_name:
            self.__bk_dict[new_name] = self.__bk_dict.pop(bookmark_name)

    def remove_bookmark(self, bookmark_name: str) -> None:
        self.__bk_dict.pop(bookmark_name)
    
    def print_bookmarks(self) -> None:
        if not self.__bk_dict:
            print("No saved bookmarks!")
            return
        
        for bk_name in self.__bk_dict:
            print(f"{bk_name} - {self.__bk_dict[bk_name]}")

    def length(self) -> int:
        return len(self.__bk_dict)

    def in_collection(self, bk_name: str) -> bool:
        return bk_name in self.__bk_dict

    def get_link(self, bk_name: str) -> str:
        return self.__bk_dict[bk_name]

    def get_dict(self):
        return self.__bk_dict
