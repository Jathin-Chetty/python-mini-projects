## what is this project?
We will generate a random number and ask the user to guess the random number and specify if they guessed above or below the random number till they guess the right number.

##  Building process
we start by importing the random library
```python
import random
```
Then we initiate a variable to hold the maximum value for the user to guess.
```python
top_of_range = input("Type the higest range: ")
```

Then we need to verify weather that the input is a number and greater than 0 or not
 ```python
 if top_of_range.isdigit():
 	top_of_range = int(top_of_range)
 else:
 	print("please type a number that is greater than zero")
 	quit()
 ```
Next we use the random library to store a random number in a variable called random_number. Also a variable to count number of gusses
```python
random_number = random.randint(0,top_of_range)
gusses = 0
```
Then we initiate a while loop that will increase the guess count.
Take input from the use and validate it to be a positive number.
use the comparison operators to check if the number is greater or less than the number.
End the loop if the number is equal to the number 
```python
while True:
	gusses += 1
	user_guess = input("Make a guess: ")
	if user_guess.isdigit():
		user_guess = int(user_guess)
	else:
		print("please typa a number next time")
		continue
	if user_guess == random_number:
		print("you got it!")
		break
	elif user_guess > random_number :
		print("You were above hit number!")
	else:
		print("you were below the number!")
```
Then finally print the output of number of guesses the user took
```python
print("you got it in" , gusses ," guesses")
```
## code points learnt
in the code we start with using the random library.
**randrange()** in random library will only consider the number below the lower bound
> randrange()
>```python
> random.randrange(1 ,10)
> # note: 10 is the upper bround in this function. Therefore it wont select 10 when choosing numbers. For it to consider number 10 you need to provide it with the number 11. 
> # the lower bound 1 will be considered.
> #therefore it will choose from 1 -9.
>
>random.randrange(11)
>#for the random integer to start choosing from 0 to 10
>```
>

When using the rangint() function it will consider the lower bound
> [!info] randrange()
>```python
> random.randint(1 ,10)
> # the lower bound 1 to the upper bound 10 will be considered.
> # therefore it will choose from 1 -10.
>```

Using continue key word
> [!info] continue
>```python
> if user_guess.isdigit():
>user_guess = int(user_guess)
>else:
>print("please typa a number next time")
>continue
># the loop will again to the top if the continue word is hit 
>```
 
 printing using coma instead of str()
 >printing without using str()
>```python
> print("you got it in" , gusses ," guesses")
>#converting gusses to string implicitly be seperating it with comma
>```

