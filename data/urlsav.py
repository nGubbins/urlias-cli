cur_url = ""

###persistant URL save

def set_url(url):
    global cur_url
    cur_url = url
    return cur_url

def get_url():
    return(cur_url)