###persistant URL save
class URLStore: 
    def __init__(self):
        self._url = ""

    #set current url
    def set_url(self, url: str) -> str:
        self._url = url
        return self._url

    #get current url
    def get_url(self) -> str:
        return self._url

store = URLStore()    
