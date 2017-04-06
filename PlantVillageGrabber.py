import urllib, csv, string, os, sys

def urlDownloader(url,path):

    directory = os.path.dirname(path)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    if not os.path.isfile(path):
        print("Downloading " + url + " to " + path)
        u = urllib.urlretrieve(url,path)
    else:
        print ("File exists.")

CSV_LIST = list()
CSV_LIST.append('apple_images.csv')
CSV_LIST.append('banana_images.csv')
CSV_LIST.append('blueberry_images.csv')
CSV_LIST.append('cabbage_red_white_savoy_images.csv')
CSV_LIST.append('cantaloupe_images.csv')
CSV_LIST.append('cassava_manioc_images.csv')
CSV_LIST.append('cherry_including_sour_images.csv')
CSV_LIST.append('corn_maize_images.csv')
CSV_LIST.append('cucumber_images.csv')
CSV_LIST.append('eggplant_images.csv')
CSV_LIST.append('gourd_images.csv')
CSV_LIST.append('grape_images.csv')
CSV_LIST.append('onion_images.csv')
CSV_LIST.append('orange_images.csv')
CSV_LIST.append('peach_images.csv')
CSV_LIST.append('pepper_bell_images.csv')
CSV_LIST.append('potato_images.csv')
CSV_LIST.append('pumpkin_images.csv')
CSV_LIST.append('raspberry_images.csv')
CSV_LIST.append('soybean_images.csv')
CSV_LIST.append('squash_images.csv')
CSV_LIST.append('strawberry_images.csv')
CSV_LIST.append('tomato_images.csv')
CSV_LIST.append('watermelon_images.csv')

newCSV = open('PlantVillageDB.csv','w')
newCSV.truncate()
newCSV.write("Plant Name, Disease, Path\n")

for x in range(len(CSV_LIST)):
    if os.path.isfile(CSV_LIST[x]):
        with open(CSV_LIST[x], 'r') as fintwo:
            for y in range(8):
                print (fintwo.readline())
            reader = csv.reader(fintwo,delimiter=',')
            for row in reader:
                Common_Name = row[0]
                Scient_Name = row[1]
                Disease_Common_Name = row[2]
                Disease_Scient_Name = row[3]
                URL_Address = row[4]
                Description = row[5]
                Metadata = row[6]

                if not Disease_Common_Name:
                    Disease_Common_Name = 'Healthy'

                path = str(Common_Name) + str("/") + str(Disease_Common_Name) + str("/") + URL_Address.split('/')[-1]
                path = path.replace(" ","")
                path = path.split("?")[0]

                newCSV.write(Common_Name + "," + Disease_Common_Name + "," + path + "\n")
                
                urlDownloader(URL_Address,path)
