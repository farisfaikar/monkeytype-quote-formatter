import json


def read_quote_list():
    quotes = []
    with open('cpp/cpp-quotes.cpp', 'r') as q:
        quote = q.read()
        quote_list = quote.replace('    ', '\\t').split('// code\n')
        quote_list_2 = []
        for _, q in enumerate(quote_list):
            q = q.split('// source\n')
            q[0] = q[0].replace('\n', '\\n').rstrip('\\n')
            q[1] = q[1].replace('\n', '').lstrip('/ ')
            q = [q[0], q[1]]
            print(q)
            quote_list_2.append(q)
    return quote_list_2


def main():
    quotes = read_quote_list()
    id = int(input("Input starting id: "))
    with open('cpp/cpp-output.json', 'w') as output:
        data = []
        for _, (text, source) in enumerate(quotes):
            print(f"Formatted: {id}) {text} ~ {source}")
            data.append({
                "text": text,
                "source": source,
                "length": len(text),
                "id": id
            })
            id += 1
        json.dump(data, output, indent=2)
        print(">>> Finished formatting quotes. Copy and Paste quotes from cpp-output.json")


if __name__ == '__main__':
    main()
    