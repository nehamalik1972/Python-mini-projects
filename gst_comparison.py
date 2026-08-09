base_price = {
  "Textbook": 500,
  "Notebook": 50,
  "Labkit": 1200,
  "Stationery set": 300,
  "E_book": 400
}
old_gst = {
  "Textbook": 0,
  "Notebook": 5,
  "Labkit": 18,
  "Stationery set": 12,
  "E_book": 400
  
}
new_gst = {
  "Textbook": 0,
  "Notebook": 5,
  "Labkit": 12,
  "Stationery set": 12, 
  "E_book": 5
}

old_total = 0
new_total = 0
print("GST comparison on study equipment")
   
for item in base_price:
  base = base_price[item]
  old  = old_gst[item]
  new =  new_gst[item]

  old_price = base + (base * old / 100)
  new_price = base + (base * new / 100)
  change = new_price - old_price
  if change < 0:
    print("cheaper")
  elif change > 0:
   print("costlier")
  else:
   print("no change")
  
  print("\n",item)
  print("Base price = ", base)
  print("old_gst = ", old, "% final price = ",old_price)
  print("new_gst = ", new, "% final price = ",new_price)
  
  print("change = ", change,)

  old_total += old_price 
  new_total += new_price
overall = new_total - old_total
print("\n Summery")
print("old_total = ",old_total)
print("new_total = ",new_total)
print("overall result = ",overall)

if overall < 0:
     print("overall result: cheaper for students")
elif overall > 0:
     print("overall result: costlier for students")
else:
     print("overall result:no change")
