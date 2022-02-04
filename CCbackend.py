#Made by: Harpreet Singh Anand , BITS ID: 2021A7PS2416P


import requests
import json
import csv
import http.client


filename = 'teamstats.csv'
fields = ["id", "Name", "Area", "Available Seasons", "Tier"]
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    
    
connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '6d6457df617848f38cb162998943e5b8' }
connection.request('GET', '/v2/competitions/', None, headers )
response = json.loads(connection.getresponse().read().decode())
tier_num = int(input("Enter the TIER : "))

if tier_num == 1:
    for i in range(0,156):
        tiernum = response["competitions"][i]["plan"]
        if tiernum == "TIER_ONE":
            idNum = response["competitions"][i]["id"]
            name = response["competitions"][i]["name"]
            area = response["competitions"][i]["area"]["name"]
            available_seasons = response["competitions"][i]["numberOfAvailableSeasons"]
            
            rows = [idNum, name, area, available_seasons, tiernum]
            filename = "teamstats.csv"
            with open(filename, 'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                
                csvwriter.writerow(rows)
        else :
            i +=1


if tier_num == 2:
    for i in range(0,156):
        tiernum = response["competitions"][i]["plan"]
        if tiernum == "TIER_TWO":
            idNum = response["competitions"][i]["id"]
            name = response["competitions"][i]["name"]
            area = response["competitions"][i]["area"]["name"]
            available_seasons = response["competitions"][i]["numberOfAvailableSeasons"]
            
            rows = [idNum, name, area, available_seasons, tiernum]
            filename = "teamstats.csv"
            with open(filename, 'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(rows)
        else :
            i +=1
if tier_num == 3:
    for i in range(0,156):
        tiernum = response["competitions"][i]["plan"]
        if tiernum == "TIER_THREE":
            idNum = response["competitions"][i]["id"]
            name = response["competitions"][i]["name"]
            area = response["competitions"][i]["area"]["name"]
            available_seasons = response["competitions"][i]["numberOfAvailableSeasons"]
            
            rows = [idNum, name, area, available_seasons, tiernum]
            filename = "teamstats.csv"
            with open(filename, 'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(rows)
        else :
            i +=1
if tier_num == 4:
    for i in range(0,156):
        tiernum = response["competitions"][i]["plan"]
        if tiernum == "TIER_FOUR":
            idNum = response["competitions"][i]["id"]
            name = response["competitions"][i]["name"]
            area = response["competitions"][i]["area"]["name"]
            available_seasons = response["competitions"][i]["numberOfAvailableSeasons"]
            
            rows = [idNum, name, area, available_seasons, tiernum]
            filename = "teamstats.csv"
            with open(filename, 'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                
                csvwriter.writerow(rows)
        else :
            i +=1



