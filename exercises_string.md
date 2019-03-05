<b><Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.</b>

<b>Exercise 2: Given that fruit is a string, what does fruit[:] mean? </b>

<b>Exercise 3: Encapsulate below code in a function named count, and generalize it so that it accepts the string and the letter as arguments.</b>

    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

<b>Exercise 4: There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at:

[https://docs.python.org/library/stdtypes.html#string-methods](https://docs.python.org/library/stdtypes.html#string-methods)

Write an invocation that counts the number of times the letter a occurs in "banana".**</b>

<b>Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.</b>

<b>Exercise 6: Read the documentation of the string methods at [https://docs.python.org/library/stdtypes.html#string-methods](https://docs.python.org/library/stdtypes.html#string-methods) You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.</b>

<b>Exercise 7: In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.</b><br>

<b>NOTE:</b> String letters are case-sensitive.<br>

<b>Input Format</b><br>

The first line of input contains the original string. The next line contains the substring.<br>

<b>Constraints</b><br>
0 < len(string) < 201<br> 
Each character in the string is an ascii character.<br>

<b>Output Format</b><br>
Output the integer number indicating the total number of occurrences of the substring in the original string.<br>

<b>Sample Input</b>

    ABCDCDC
    CDC

<b>Sample Output</b>

    2

<b>Concept</b>

Some string processing examples, such as these, might be useful. <br>
There are a couple of new concepts: <br>
In Python, the length of a string is found by the function len(s), where  is the string. <br>
To traverse through the length of a string, use a for loop:

    for i in range(0, len(s)):
        print (s[i])

A range function is used to loop over some length:

    range (0, 5)

Here, the range loops over 0 to 4. 5 is excluded.


