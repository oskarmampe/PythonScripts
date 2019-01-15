import os
import csv
from data_types import Purchase
'''
For python below 3.4.3 compability 
'''
try:
    import statistics
except:
    import statisticso as statistics

def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)

def print_header():
    print('---------------------------------')
    print(' REAL ESTATE DATA MINING APP')
    print('---------------------------------')

def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')

def load_file(filename):
    with open(filename, 'r') as fin:
        reader = csv.DictReader(fin)
        purchases = []
       # header = fin.readline().strip()
       # reader = csv.reader(fin, delimiter=',')

        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        return purchases
#    with open(filename, 'r', encoding='utf-8') as fin:
#        header = fin.readline().strip()
#        print('found header: ' + header)
#
#        lines = []
#        for line in fin:
#            line_data = line.strip().split(',')
#            lines.append(line_data)
#        print(lines[:5])
#

def query_data(data):
    data.sort(key= lambda p: p.price)

    #if was sorted
    high_purcase = data[-1]
    print('The most expensive house ${:,} with {} beds and {} baths'.format(high_purcase.price, high_purcase.beds,
                        high_purcase.baths))

    low_purchase = data[0]
    print('The least expensive house ${:,} with {} beds and {} baths'.format(low_purchase.price, low_purchase.beds,
                        low_purchase.baths))
   
    prices = [
        p.price
        for p in data
    ]


    avg_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(avg_price)))


    two_bed_homes = (
        p
        for p in data
        if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2
    )

    homes = []

    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    avg_price = statistics.mean((announce(p.price, 'price') for p in homes[:5]))
    avg_baths = statistics.mean((p.baths for p in homes[:5]))
    avg_sqft = statistics.mean((p.sq__ft for p in homes[:5]))

    print('The average 2-bedroom home is ${:,}, baths={} square feet={:,}'.format(int(avg_price), round(avg_baths), round(avg_sqft)))
   
def announce(item, msg):
    print('Pulling item {} for {}'.format(item, msg))
    return item

if __name__ == '__main__':
    main()
