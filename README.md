# Question 1 Time Delta

When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t1 and t2 time .

Constraints

Input contains only valid timestamps
year ≤ 3000
.
Output Format

Print the absolute difference (t1 -t2) in seconds.

Sample Input 0

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sample Output 0

25200
88200

# Question 2 Merge The Tools

Consider the following:

A string,s, of length n where s = c0c1 …cn-1.
An integer,k , where k  is a factor of n .
We can split s into  n/k  substrings where each subtring,tit , consists of a contiguous block k of  characters in s . Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti .
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index < j in ti , then do not include the character in string ui .
Given s and k , print n/k   lines where each line i denotes string ui .

Example
S = ‘AAABCADDE’
K = 3

There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u1 = ‘A’ . The second substring has all distinct characters, so u2 = ‘BCA’ . The third substring has 2 different characters, so u3 = ‘DE’ . Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

string s: the string to analyze
int k: the size of substrings to analyze
Prints

Print each subsequence on a new line. There will be n/k  of them. No return value is expected.

Input Format

The first line contains a single string,s .
The second line contains an integer,k , the length of each substring.

Constraints
1≤ n ≤ 104, where n is the length of s
1 ≤ k ≤ n
It is guaranteed that n is a multiple of k .
Sample Input

STDIN       Function
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output

AB
CA
AD

# Question 3 Regex Substution 
The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.
Learn more about re.sub() .
Transformation of Strings
Code
import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
Output
1 4 9 16 25 36 49 64 81

Replacements in Strings
Code
import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

print re.sub("(<!--.*?-->)", "", html) #remove comment
Output
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">

  <param name="quality" value="high"/>
</object>
Task
You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:
&& → and
|| → or
Both && and || should have a space " " on both sides.
Input Format
The first line contains the integer,N .
The next N  lines each contain a line of the text.
Constraints
0< N < 100
Neither && nor || occur in the start or end of each line.
Output Format
Output the modified text.
Sample Input
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
Sample Output
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.    
