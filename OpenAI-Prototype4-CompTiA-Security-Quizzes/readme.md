## How to use

**Warning**: Still buggy. But should work IF you follow the instructions. Don't use if you are not into experimenting with code. The JS is inside the html, so each html quiz should not be loading from any external source.

1. git clone this folder
2. make a 10 item multiple choice quiz with 4 choices each and save it in a text file.
    It should look like this:

>   1. This is quiz question 1<br>
>   A) This is quiz answer 1<br>
>   B) This is quiz answer 2<br>
>   C) This is quiz answer 3<br>
>   D) This is quiz answer 4<br>
>
>   2. This is quiz question 2<br>
>   A) This is quiz answer 1<br>
>   B) This is quiz answer 2<br>
>   C) This is quiz answer 3<br>
>   D) This is quiz answer 4<br>
>
>   (Ideal number is 10)
3. Run Quizzinator.py (I ran this in pyCharm)
    - It will prompt you for the name of the text file (the file above)
    - It will prompt you for the file name for the output, can be html.
4. Copy the contents. Starts with '''<form>''', ends with '</form>'
5. Open template.html, find '<form>' and should end with '</form>'. Paste above it.

### Notes, bugs and other disclaimers

- Make sure each question ends with a '</div>'
- **Important:** For Question 10, instead of:
> '<button type="button" class="next-btn">Next</button>'

replace with:

> '<button type="submit" class="submit-btn">Next</button>'

#### Finally, scroll down a bit

- Input the correct answers in the <script section>
- Replace the <head> and <title> fields.

SAVE!

