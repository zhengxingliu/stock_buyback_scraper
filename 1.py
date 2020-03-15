import scrapy
import csv

with open('result.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow('item')