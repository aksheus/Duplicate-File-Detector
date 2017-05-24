import csv
if __name__=="__main__":
    with open('duplicates.csv','w',newline='') as csvfile:
        writer=csv.writer(csvfile, delimiter=',')
        writer.writerow(['FileName','File Size'])
        writer.writerow(['Name','988732'])
        writer.writerow(['Locations'])
        writer.writerow(['C:\\Users\\abkma']) # C:\\Users\\abkma\\ai_project2
        writer.writerow(['C:\\Users\\abkma\\ai_project2'])



