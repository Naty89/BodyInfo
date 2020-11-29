# BodyInfo

This is a code that tells you what your body percentage is using the US Navy Formula or the BMI Formula, it also tells you what category you are in.
It also tells the how many pounds you need to loose to go down a category and it tells you how much you need to lose to get a six pack
Another thing is it tells you how much you need to workout and for how long you need to work out for.
It will also tell you what kind of diet you should and it would show links that lead you to some recipes.

## Installation

You can clone this repository by using this command line

```bash
$ git clone https://github.com/Naty89/BodyInfo
```

Install the requirements
```bash
$ pip3 install -r requirements.txt
```
## Usage

to use this code you can just go to the place your put it and put in this command line to see what to do

```bash
$ python main.py --help
```

and this would be the result:

```bash
Usage: main.py [OPTIONS]

  This is a class that tells you what your body percentage is and what
  category you are in. It also tells the how many pounds you need to loose
  to go down a category and it tells you how much you need to lose to get a
  six pack Another thing is it tells you how much you need to workout and
  for how long you need to work out for It will also tell you what kind of
  diet you should and it would show links that lead you to some recipes

Options:
  -w, --weight INTEGER  the amount of pounds you weigh.
  -h, --height FLOAT    your height in inches
  -g, --gender TEXT     your gender
  -a, --age INTEGER     age
  -n, --neck FLOAT      circumference of your neck in inches
  --waist FLOAT         your waist circumference in inches
  --hip FLOAT           the circumference of your hip in inches, if you are a
                        male then it would be the same as your waist

  -m, --method TEXT     the method that you want to run, here are the method
                        that you can run: US_Navy_Method, BMI_Method,
                        Body_Fat_Category, Pounds_To_Lose

  --help                Show this message and exit.

```

## Example

Here is an example showing how to use this code:

```bash
$ python main.py --weight 152 --height 70.5 --gender 'male' --age 25 --neck 19.5 --waist 37.5 --hip 37.5 --method US_Navy_Method
```

the result would be:

```bash
15.3
```
