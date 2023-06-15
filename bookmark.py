class Bookmark:
    def __init__(self, name: str, link: str) -> None:
        self.__name = name
        self.__link = link
    
    def get_name(self) -> str:
        return self.__name
    
    def get_link(self) -> str:
        return self.__link
    
    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def set_link(self, new_link: str) -> None:
        self.__name = new_link
