#--- Internet Data ---
#in Python3.3, you need to import urllib.request
import urllib.request

def main():
    # open a connection to a URL using urllib2
    webUrl = urllib.request.urlopen("http://joemarini.com")

    # get the result code and print it
    print("result code: " + str(webUrl.getcode()))

    # read the data from the URL and prints the html code.
    data = webUrl.read().decode("utf-8") # decode the data as UTF-8
    print(data)

if __name__ == "__main__":
    main()