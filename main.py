timeIntervals = [
{
  "name" : "less than 15 min",
  "value": 0
},
{
  "name" : "1 hour",
  "value": 1
},
{
  "name" : "1-2 hours",
  "value": 2
},
{
  "name" : "2-3 hours",
  "value": 3
},
{
  "name" : "3-4 hours",
  "value": 4
},
{
  "name" : "4-5 hours",
  "value": 5
},
{ 
  "name" : "5-6 hours",
  "value": 6
},
{
  "name" : "6-7 hours",
  "value": 7
},
{
  "name" : "7-8 hours",
  "value": 8
},
{
  "name" : "8-9 hours",
  "value": 9
},
{
  "name" : "9-10 hours",
  "value": 10
},
{
  "name" : "10-12 hours",
  "value": 12
},
{
  "name" : "12-24 hours",
  "value": 20
}
]

rate = 100

answer = input("choose your time interval of parking: ")
for timeInterval in timeIntervals:
  if answer == timeInterval['name']:
    print("your parking rate is ", timeInterval['value'] * rate)
