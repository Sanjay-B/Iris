By Sanjay-B(Sanjay Bhadra)
Copyright © 2017 Sage Technologies LLC. All rights reserved.

The MIT License (MIT)

Copyright © 2017 Sage Technologies LLC. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, modify, merge, publish and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.


Iris aims to be a simple, but modern language when it comes to graphical interface
functionality and/or design. At the core of any application, you have a codebase. When
working on desktop, that codebase is often written in C++ which is complicated to
understand for new users who are wanting to learn how to code. In partition, Iris
can function as a multi-purpose language. Since Iris is built on top of Python, you
can embed or run python directly in conjunction to running native Iris code. 

The following is the basic syntax/grammar that Iris abides by. 

Object-Types

		Object-types are single valued data structures that allow for the
	creation or manipulation of strings, integers or booleans. Iris supports
	all three.

		- Variables(var)
			- To define a variable: 
				var name = value
			- To call a variable:
				name
			- Rules:
				- Can only handle string values
				- Its implied that a variable will always be a string
				- "var" must be in all lowercase, zero exception

		- Integers(int)
			- To define an integer:
				int name = value
			- To call an integer:
				name

		- Boolean(bool)
			- To define a boolean:
				bool name = true or bool name = false
			- To call an integer:
				name

		You're probably wondering how to change the value of a(n)
	object-type variable. It quite simple...

		- To replace an int, bool or var
			- name = new_value

		- Incorrect
			- <object-type> name = new_value
			- name <object-type> = new_value
			- new_value = <object-type> name
			- new_value = name <object-type>

Commenting/Documentation

		In order to help promote the documentation of code, a keyword
	for commenting was added. It's now possible to comment out code or
	structure sentences explaining your code.
		
		- Ignored(//)
			- To render a comment, a "//" is placed in front of the word or
			code phrase

			- Must have a space after the "//". 
				- Correct: // Comment
				- Wrong: //Comment
			
			- Comments are ignored by Iris



Conditionals
		
		Conditonals were made possible on 11/13 and allowed for the
	comparison of a(n) object-type with a string, integer or boolean. Unfortunately,
	you can't compare a object-type with an object-type(yet?).

	- If Statments(if type-object [operators] do)
		- To create an if-statement:
			
			if <object-type> == [string/int/bool] do
				// code

		- else-declarations after an if-statement is possible
			
			if <object-type> == [string/int/bool] do
				// code
			else
				// code
