"""
This is a class that tells you what your body percentage is
and what category you are in.
It also tells the how many pounds you need to loose to go down a category
and it tells you how much you need to lose to get a six pack
Another thing is it tells you how much you need to workout and for how long you need
to work out for
It will also tell you what kind of diet you should and it would show links that lead you
to some recipes

"""

from math import log10
import pandas as pd
import click


class BodyInfo:
    """
    waist, neck, and hip should be in inches
    height in inches
    weight should be in pounds
    gender should be written in male or female

    """

    def __init__(self, weight, height, gender, age, neck, waist, hip):
        self.weight = weight
        self.height = height
        self.gender = gender
        self.age = age
        self.neck = neck
        self.waist = waist
        self.hip = hip

    """
    This method calculates 
    your body fat percentage
    using the U.S Navy method
    """

    def US_NAVY_METHOD(self):
        if self.gender.lower() == 'male':
            return round(86.010 * log10(self.waist - self.neck) - 70.041 * log10(self.height) + 36.76, 1)
        return round(163.205 * log10(self.waist + self.hip - self.neck) - 97.684 * log10(self.height) - 78.387, 1)

    """
    This method calculates your
    body fat percentage using
    the BMI(Body Mass Index) method
    """

    def BMI_METHOD(self):
        BMI = (self.weight / self.height ** 2) * 703
        if self.gender.lower() == 'male':
            return round(1.20 * BMI + 0.23 * self.age - 16.2, 1)
        return round(1.20 * BMI + 0.23 * self.age - 5.4, 1)

    """
    This shows you the body fat 
    categories, and which one your in
    """

    def BODY_FAT_CATEGORY(self):
        """
        This part of the code figures out the body fat
        percantage using the navy method
        """
        BFP = round(self.US_NAVY_METHOD(), 1)
        #         if self.gender.lower() == 'male':
        #             BFP = round(86.010 * log10(self.waist - self.neck) - 70.041 * log10(self.height) + 36.76)
        #         else:
        #             BFP = round(163.205 * log10(self.waist + self.hip - self.neck) - 97.684 * (log10(self.height)) - 78.387)
        """
        This makes a dictionary of the category
        and the body percentage associated with it.
        """
        df = pd.read_csv('BFP_Catergories.csv')
        print(df)
        female = {}
        male = {}
        for i in range(len(df.Description)):
            female[df.Description[i]] = df.Women[i].replace('%', '').replace('+', '').split('-')
        for i in range(len(df.Description)):
            male[df.Description[i]] = df.Men[i].replace('%', '').replace('+', '').split('-')

        """
        This tells what category you are in 
        """
        if self.gender.lower() == 'male':
            for key, value in male.items():
                if BFP > int(value[0]) and BFP < int(value[-1]):
                    return ('You are in the {} category'.format(key))
        if self.gender.lower() == 'female':
            for key, value in female.items():
                if BFP > int(value[0]) and BFP < int(value[-1]):
                    return ('You are in the {} category'.format(key))

    """
    This method calculates the amount of 
    pounds you need to lose to go down a category.

    I am going to be using three function inside
    this method so that it is more organized
    the three functions will be one that finds what category
    your in, another one that will find what category is down and BFP
    to be in that category, the third one calculates the how
    pounds you need to lose.
    """

    def POUNDS_TO_LOSE(self):

        """
        This function tells you what category your
        are in
        """
        def category_in():

            # This part of the code calls out the US_Navy_Method method
            # to get the BFP
            BFP = round(self.US_NAVY_METHOD(), 1)
            df = pd.read_csv('BFP_Catergories.csv')
            # This makes a dictionary of the category
            # and the body percentage associated with it.

            BFP = round(self.US_NAVY_METHOD(), 1)
            df = pd.read_csv('BFP_Catergories.csv')
            female = {}
            male = {}
            for i in range(len(df.Description)):
                female[df.Description[i]] = df.Women[i].replace('%', '').replace('+', '').split('-')
            for i in range(len(df.Description)):
                male[df.Description[i]] = df.Men[i].replace('%', '').replace('+', '').split('-')

            """
            This tells what category you are in
            """
            if self.gender.lower() == 'male':
                for key, value in male.items():
                    if BFP > int(value[0]) and BFP < int(value[-1]):
                        return (key)
            else:
                for key, value in female.items():
                    if BFP > int(value[0]) and BFP < int(value[-1]):
                        return (key)

        # return(category_in())

        def category_below():
            #"""
            #This makes a dictionary of the category
            #and the body percentage associated with it.
            #"""
            df = pd.read_csv('BFP_Catergories.csv')
            female = {}
            male = {}
            c_in = category_in()
            for i in range(len(df.Description)):
                female[df.Description[i]] = df.Women[i].replace('%', '').replace('+', '').split('-')
            for i in range(len(df.Description)):
                male[df.Description[i]] = df.Men[i].replace('%', '').replace('+', '').split('-')
            y = list(female.keys())
            x = list(male.keys())
            if self.gender == 'male':
                for i in range(len(x)):
                    if x[i] == c_in:
                        return(int(male[x[i - 1]][-1]))
            else:
                for i in range(len(y)):
                    if y[i] == c_in:
                        return(int(female[y[i - 1]][-1]))


        def pounds_to_lose():
            BFP = round(self.US_NAVY_METHOD(), 1)
            goal_bfp = category_below()
            if self.gender.lower() == 'male':
                if BFP <= 5:
                    return("You shouldn't be losing any more weight.")
                else:
                    return("You need to lose {} pounds to go down a category".format(round(self.weight - self.weight * (1 - (BFP / 100)) / (1 - (goal_bfp / 100)), 1)))
            else:
                if BFP <= 13:
                    return("You shouldn't be losing any more weight.")
                else:
                    return ("You need to lose {} pounds to go down a category".format(round(self.weight - self.weight * (1 - (BFP / 100)) / (1 - (goal_bfp / 100)), 1)))

        return(pounds_to_lose())

    def SIX_PACK(self):

        goal_bfp = 10
        BFP = round(self.US_NAVY_METHOD(), 1)
        if self.gender.lower() == 'male':
            if BFP <= 5:
                return("You shouldn't be losing any more weight.")
            else:
                return("You need to lose {} pounds to get a six pack".format(round(self.weight - self.weight * (1 - (BFP / 100)) / (1 - (goal_bfp / 100)), 1)))
        else:
            if BFP <= 13:
                return("You shouldn't be losing any more weight.")
            else:
                return("You need to lose {} pounds to get a six pack".format(round(self.weight - self.weight * (1 - (BFP / 100)) / (1 - (goal_bfp / 100)), 1)))





@click.command()
@click.option('--weight', '-w', default=146, help='the amount of pounds you weigh.')
@click.option('--height', '-h', default=64.5, help='your height in inches')
@click.option('--gender', '-g', default='male', help='your gender')
@click.option('--age', '-a', default=15, help='age')
@click.option('--neck', '-n', default=14.5, help='circumference of your neck in inches')
@click.option('--waist', default=33.5, help='your waist circumference in inches')
@click.option('--hip', default=33.5,
              help='the circumference of your hip in inches, if you are a male then it would be the same as your waist')
@click.option('--method', '-m', default='us_navy_method',
              help='the method that you want to run, here are the method that you can run:'
                   '\n US_Navy_Method, BMI_Method, Body_Fat_Category, Pounds_To_Lose, Six_Pack')
def runBodyInfo(weight, height, gender, age, neck, waist, hip, method):
    """
    This is a class that tells you what your body percentage is
    and what category you are in.
    It also tells the how many pounds you need to loose to go down a category
    and it tells you how much you need to lose to get a six pack
    Another thing is it tells you how much you need to workout and for how long you need
    to work out for
    It will also tell you what kind of diet you should and it would show links that lead you
    to some recipes
    """
    x = BodyInfo(weight, height, gender, age, neck, waist, hip)

    if method.lower() == 'us_navy_method':
        print(x.US_NAVY_METHOD())

    elif method.lower() == 'bmi_method':
        print(x.BMI_METHOD())

    elif method.lower() == 'body_fat_category':
        print(x.BODY_FAT_CATEGORY())

    elif method.lower() == 'pounds_to_lose':
        print(x.POUNDS_TO_LOSE())

    elif method.lower() == 'six_pack':
        print(x.SIX_PACK())

if __name__ == '__main__':
    runBodyInfo()
