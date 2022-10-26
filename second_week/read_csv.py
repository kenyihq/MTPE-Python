import csv



class Titanic:
    

    def __init__(self):
        pass

    def read_data(self):

        df = './dataset/titanic.csv'

        with open(df,'r') as csvfile:
            titanic = csv.reader(csvfile)

            return titanic

    def avg_age_titanic(self):

        # with open(df, 'r') as csvfile:
        #     # read csv
        #     titanic = csv.reader(csvfile)

            # # save age and average age
            # age_list = [int(i[5]) for i in titanic if i[5].isnumeric()]
            # # age_list.pop(0)
            # age_avg = round(sum(age_list)/len(age_list), 2)


        # save age and average age
        df_titanic = self.read_data()
        

        age_list = [int(i[5]) for i in df_titanic if i[5].isnumeric()]
        # age_list.pop(0)
        age_avg = round(sum(age_list)/len(age_list), 2)

        return age_avg


    def cuantity_genre(self, genre):
        
        with open(df, 'r') as csvfile:
            # read csv
            titanic = csv.reader(csvfile)

            total = [person[4] for person in titanic if person[4] == genre]
            total = len(total)

        return total

titanic = Titanic()

print(titanic.read_data())

print(titanic.avg_age_titanic())
# print(titanic.cuantity_genre('male'))
# print(titanic.cuantity_genre('female'))