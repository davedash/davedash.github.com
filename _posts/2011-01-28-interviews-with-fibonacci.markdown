---
layout: post
title: "Interviews with Fibonacci"
tags: [mozilla, interviews]
published: True
time: 1:03PM
---
[ch]: http://www.codinghorror.com/blog/2007/02/why-cant-programmers-program.html

I have the privilege of interviewing many of the people who wish to be web
developers at Mozilla.  I unfortunately witness
[programmers not being able to program][ch].  My interviews are 45 minutes
long.  I tend to ask people about their history, experiences and about what
they know.  Then I give them some time to write some code.

### My Question

I use questions relating to the Fibonacci sequence.  E.g.:

* Print `n` digits of the Fibonacci sequence
* Give me a `list` (if the person knows python) of `n` digits of the Fibonacci
  sequence.
* In rare cases, Print the `n`th digit of Fibonacci.

In some cases I dumb it down... a lot:

> Give me `n` digits.  In other words `f(5) = [1 1 1 1 1]`

Here's the sequence:

	1 1 2 3 5 8 13 21 34 ..  k[n-2] k[n-1] k[n]

The **first two numbers are `0` and `1`**.  Each successive number is the
**addition of the two proceeding numbers**.  In other words:

	k[n] = k[n-2] +k[n-1]

I don't care too much about efficiency.  I often don't care if it works, if
they're trying.

### This is a low bar

A good **number of people solve this with no issues**.  They calculate the
sequence and print out the digits, or store them in a `list`.  I run the code,
we optimize it slightly, we move on.

Unfortunately, **I expect *everyone* I interview to easily solve this**.  Quite
honestly, **if they can't solve this they should not have even made it past the
phone screen**.  It's harsh and the only exception is pressure.

### Pressure

Interview pressures is a real thing:

* Interviewees at Mozilla are generally excited by the prospect.
* People want to appear intelligent to their peers.
* They had too much coffee at their hotel.  There's a lot to think about,
  **it's not a natural environment**.

I try to solve this by using a comfortable room with couches.  I also refrain
from yelling at the candidates like a Tiger Mom.  Being nervous, however, is
difficult.

This problem gives a lot of people coders-block.

My advice to anyone doing technical interviews:

> *Practice.*

Have your friends, family, fiance, whomever ask you programming questions.  You
can compile a huge list, and just have them pick one at random.  Make the
process seem natural.

### Excitement

The best **people who solve these problems** are the ones who
**think problems are exciting**.  They enjoy challenge.  They are also find the
interview exciting, they are **entering in with a good attitude**.

It's **not about intelligence**.  Intelligence is rarely a factor.  It's about
effort, and effort is easy to exert if you find something exciting.

If they are excited to ace a simple interview question, I can usually rely on
them to do their jobs, and in many cases turn to them to come up with solutions
to problems I might be running into.

The excited interviewer asks about what the solutions should entail, and the
rules:

* Are we starting at zero or one?
* Do you want a `list`, or a generator?
* Do you want to print this out?

They eagerly churn out code.  They check it with some basic tests.  They let me
know it works with confidence.  Occasionally they stumble and sometimes come
out with the wrong answer, but with some assistance they could usually figure
it out.  I can use their failures as a segue to talk about testing and quality
assurance.

### How do you think?

I don't ask this problem, because I'm dying to know the 12th number of the
fibonacci sequence.  I already know that's 144.  I want to know how people
solve problems.  How do they take a set of requirements and implement them.

Our jobs as software developers are to take requirements or problems, find a
suitable solution and write code to solve it.

This is my approach.  I know the first digit is 1 and the next digit is 1,
therefore I can store those and get the third digit by adding them.  I shift
the variables around in a for loop and I can get this:

	cur = next = 1
	for 1..n:
		print cur
		last = cur
		cur = next
		next += last

That's just pseudo-code.  I'm not a math and/or computer science genius.  I
can, however, take requirements and imagine how I would solve them if I had to
do it by hand, and then transcribe that process.

Likewise if someone tells me, we need to know the average rating that people
gave Firefox in the area of start-up time each day, I can figure out that
problem and then implement it using software.

So now I have to preface my interviews with, "If you read my post about the
Fibonacci sequence, let me know."

