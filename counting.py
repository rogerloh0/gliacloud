urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

def counting(uri):
    record = {}
    for element in uri:
        split_list = element.split('/')
        file_name=split_list[-1]
        print(file_name)
        try:
            record[file_name]+=1
        except KeyError:
            record[file_name] = 1
    for key in record:
        print(key + ": " + str(record[key]))




if __name__ == "__main__":
    counting(urls)