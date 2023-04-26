import csv

with open('data/movies_metadata.csv', 'r') as f:
    data = list(csv.reader(f,delimiter=","))
    header = data[0]
    print(header)
    title_index = header.index('title')
    year_index = header.index('release_date')
    overview_index = header.index("overview")
    data = data[1:]
    for item in data:
        if len(item) < title_index: continue
        title = item[title_index].replace("'", "''")
        year = item[year_index].replace("'", "''")
        overview = item[overview_index].replace("'", "''")
        print(f"INSERT INTO movies (`title`, `year`, `overview`) VALUES ('{title}', '{year}', '{overview}');")