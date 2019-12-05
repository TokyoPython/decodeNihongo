"""
There are various encodings of Japanese-language web pages.  Sometimes its easier to try all possibilities when you wish to read page text.
It requires python libraries "urlib" and "html"
This code accepts an URL, tries open the specified page, and then tries to extract text by decoding it.
To decode, it employs several nested try-except blocks, cascading from more to less prominent encodings
The code assumes the page is HTML-like.  Result text it "unescape"d to convert some punctuation marks. 
Note:  If page is XML-like you will not want to unescape the page.
"""
def retrieveURL(URL):
    import urllib.request
    import urllib.parse
    response = None
    reqfull = urllib.request.Request(URL)  #create Post request
    try:
        response = urllib.request.urlopen(reqfull)
    except urllib.request.HTTPError as err:
        if err.code == 404:
            print("URL not found 404 " + str(URL))
        else:
            print("URL not found " + str(err.code)+" "+ str(URL))
    return response

def get_decodedNihongo_PageText(URL):  #various encodings of Japanese-language web pages
    import html  #To unescape webpage content
    # Transmit request, and read first page of results
    response = retrieveURL(URL)
    if response != None:
        responseHTML = response.read()
        try:
            text = responseHTML.decode('utf-8')  #standard (utf-8 encoding)
        except:
            try:
                text = responseHTML.decode('shiftjis')  #most likely alternate Japanese encoding
            except:
                text = responseHTML.decode('shift_jisx0213') #be prepared for other Japanese encodings
        text = html.unescape(text)  #get rid of "&quot:", "&lt;", "&gt;",etc.
    return text
