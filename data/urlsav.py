cur_url = ""

###persistant URL save

#set current url
def set_url(url):
    global cur_url
    cur_url = url
    return cur_url

#get current url scheme
def get_url():
    return cur_url
