import json


def read_quote_list():
    quotes = []
    with open('quote/quotes.txt', 'r', encoding="utf8") as q:
        quote_list = q.readlines()
        for _, quote in enumerate(quote_list):
            quote = quote.replace('\n', '').split(' * ')
            quote = [quote[0].lstrip('0123456789).- '), quote[1]]
            print(quote)
            quotes.append(quote)
    return quotes


def main():
    quotes = read_quote_list()
    id = int(input("Input starting id: "))
    with open('quote/output.json', 'w', encoding="utf8") as output:
        data = []
        for _, (text, source) in enumerate(quotes):
            print(f"Formatted: {id}) {text} * {source}")
            data.append({
                "text": text,
                "source": source,
                "length": len(text),
                "id": id
            })
            id += 1
        json.dump(data, output, indent=2, ensure_ascii=False)
        print(">>> Finished formatting quotes. Copy and Paste quotes from output.json")


if __name__ == '__main__':
    main()
