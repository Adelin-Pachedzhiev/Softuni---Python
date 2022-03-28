countries_li = input().split(", ")
capitals_li = input().split(", ")

combined_li = zip(countries_li, capitals_li)
for pair in combined_li:
    print(f"{pair[0]} -> {pair[1]}")
