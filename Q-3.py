people: int = int(input("How many people are you? "))
if people % 4 == 0:
    print ("there will be ", people // 4, "full room exactly")
else :
    print ("there will be ", people // 4, "full rooms and one room of", people % 4)