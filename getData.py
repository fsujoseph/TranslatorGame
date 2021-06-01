import requests


def get_data(page):
    url = 'http://flip1.engr.oregonstate.edu:7043/?query=' + page

    html_data = requests.get(url).text
    html_data = html_data.encode()

    url = "https://cs361-microservice.wl.r.appspot.com/"

    json_data = requests.post(url, data=html_data, headers={"Content-Type": "text/html"}).content
    data = json_data.decode('utf8')

    sentences = []
    bad = ['"', "'", "(", "{", "[", "]", "}", ")", '/', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    start = end = 0
    while end < len(data):
        if data[start] == ".":
            end += 1
            while data[end] not in bad and end < len(data):
                if data[end] == ".":
                    sentences.append(data[start + 2:end + 1])
                    break
                end += 1
        end += 1
        start = end

    final_sentences = []
    final_words = []

    for sentence in sentences:
        if len(sentence) > 30:
            final_sentences.append(sentence)

    for sentence in sentences:
        start = end = 0
        while end < len(sentence):
            if sentence[end] != " " and sentence[end] != ".":
                end += 1
            else:
                final_words.append(sentence[start].upper() + sentence[start+1:end])
                end += 1
                start = end

    return [final_words, final_sentences]


if __name__ == "__main__":
    get_data()