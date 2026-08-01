---
title: "Behold Modular Forms, the ‘Fifth Fundamental Operation’ of Math"
source: "https://www.quantamagazine.org/behold-modular-forms-the-fifth-fundamental-operation-of-math-20230921/?fbclid=IwY2xjawTHTLFleHRuA2FlbQIxMABicmlkETFMSkVCa29vZTZ4YlczaWNMc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHks1XLPOoYXApmcE-UHtGuX_34dcUx3y9QtbonX0fWNFbwe9zXybFY7d3oPO_aem_W6_W35bw9rJ0wRJabsfVBg"
author:
  - "[[Jordana Cepelewicz]]"
published: 2023-09-21
created: 2026-07-17
description: "Modular forms are one of the most beautiful and mysterious objects in mathematics. What are they?"
tags:
  - "clippings"
---
![](https://www.quantamagazine.org/wp-content/uploads/2059/12/ModularForms-Courtesy-of-SamuelJinglianLi-Lede-1-scaled.webp)

“There are five fundamental operations in mathematics,” the German mathematician Martin Eichler supposedly said. “Addition, subtraction, multiplication, division and modular forms.”

Part of the joke, of course, is that one of those is not like the others. Modular forms are much more complicated and enigmatic functions, and students don’t typically encounter them until graduate school. But “there are probably fewer areas of math where they don’t have applications than where they do,” said [Don Zagier](https://people.mpim-bonn.mpg.de/zagier/), a mathematician at the Max Planck Institute for Mathematics in Bonn, Germany. Every week, new papers extend their reach into number theory, geometry, combinatorics, topology, cryptography and even string theory.

They are often described as functions that satisfy symmetries so striking and elaborate that they shouldn’t be possible. The properties that come with those symmetries make modular forms immensely powerful. It’s what made them key players in the landmark 1994 proof of Fermat’s Last Theorem. It’s what made them central to [more recent work on sphere packing](https://www.quantamagazine.org/ukrainian-mathematician-maryna-viazovska-wins-fields-medal-20220705/). And it’s what now makes them crucial to the ongoing development of a “mathematical theory of everything” called the [Langlands program](https://www.quantamagazine.org/what-is-the-langlands-program-20220601/).

But what are they?

## Infinite Symmetries

To understand a modular form, it helps to first think about more familiar symmetries.

In general, a shape is said to have symmetry when there is some transformation that leaves it the same.

Merrill Sherman/ *Quanta Magazine*

A function can also exhibit symmetries. Consider the parabola defined by the equation $f(x) = x^2$. It satisfies one symmetry: It can be reflected over the *y* -axis. For instance, . More generally, if you shift any input to , then outputs the same value.

Infinitely many functions satisfy this symmetry. Here are just a few:

Merrill Sherman/ *Quanta Magazine*

The last example is the cosine function from trigonometry. It exhibits reflection symmetry, but it also has other symmetries. If you shift $x$ by integer multiples of , the function always returns the same value — meaning that there are infinitely many transformations that can leave the function unchanged.

Merrill Sherman/ *Quanta Magazine*

This additional symmetry makes functions like cosine incredibly useful. “Much of basic physics begins with understanding the full implications of the trigonometric functions,” said [Ken Ono](https://uva.theopenscholar.com/ken-ono), a mathematician at the University of Virginia.

“Modular forms are something like trigonometric functions, but on steroids,” he added. They satisfy infinitely many “hidden” symmetries.

## The Complex Universe

Functions can only do so much when they’re defined in terms of the real numbers — values that can be expressed as a conventional decimal. As a result, mathematicians often turn to the complex numbers, which can be thought of as pairs of real numbers. Any complex number is described in terms of two values — a “real” component and an “imaginary” one, which is a real number multiplied by the square root of −1 (which mathematicians write as $i$).

Any complex number can therefore be represented as a point in a two-dimensional plane.

Merrill Sherman/ *Quanta Magazine*

It is hard to visualize functions of complex numbers, so mathematicians often turn to color. For example, you can color the complex plane so that it looks like a rainbow wheel. The color of each point corresponds to its angle in polar coordinates. Directly to the right of center, where points have an angle of 0 degrees, you get red. At 90 degrees, or straight up, points are colored bright green. And so on. Finally, contour lines mark changes in size, or magnitude, as on a topographical map.

![](https://www.quantamagazine.org/wp-content/uploads/2059/12/graphic5-one-scaled.jpg)

The complex function f ( z ) = depicted as a rainbow wheel of color. It can be used as a reference to illustrate other functions.

You can now use this as a reference graph to illustrate complex functions. A point’s position on the plane represents the input, and you’ll assign that point a color based on the reference graph. For instance, consider the function $f(z) = z^2$. When , , since . Because is colored bright green on the reference graph, on your new graph you’ll color the point bright green.

![](https://www.quantamagazine.org/wp-content/uploads/2059/12/graphic5-two-scaled.jpg)

This graph of the complex function f (z) = z^2 shows outputs via colors chosen using the reference graph ( z ) =.

The graph of $f(z) = z^2$ runs through the colors twice, because squaring a complex number doubles its angle. It also has more contour lines, because the outputs grow in size more quickly.

More generally, the graph looks the same when you flip any point across the center (or origin).

This is one symmetry of a complex-valued function. Modular forms exhibit a bewildering variety of such symmetries. But it can be tough to make sense of the actual function those colors and contour lines represent.

## The Fundamental Domain

To do so, it helps to try to simplify the way we look at these complicated functions.

Because of the modular form’s symmetries, you can compute the entire function based on just a narrow sliver of inputs, located in a region of the plane called the fundamental domain. This region looks like a strip going up from the horizontal axis with a semicircular hole cut out of its bottom.

If you know how the function behaves there, you’ll know what it does everywhere else.

Here’s how:

<video src="https://www.quantamagazine.org/wp-content/uploads/2023/09/fun-3-1160x578-1.mp4" width="100%" controls=""></video>

Special transformations copy a sliver of the complex plane, called the fundamental domain, to infinitely many other regions. Since a modular form is defined in terms of these transformations, if you know how it behaves in the fundamental domain, you can easily figure out how it behaves everywhere else. Paul Chaikin/ Quanta Magazine

Two kinds of transformations copy the fundamental domain to the right and left, as well as to a series of ever-shrinking semicircles along the horizontal axis. These copies fill the entire upper half of the complex plane.

A modular form relates the copies to each other in a very particular way. That’s where its symmetries enter the picture.

If you can move from a point in one copy to a point in another through the first kind of transformation — by shifting one unit to the left or right — then the modular form assigns the same value to those two points. Just as the values of the cosine function repeat in intervals of $2\pi$, a modular form is periodic in one-unit intervals.

Meanwhile, you can get from a point in one copy to a point in another through the second type of transformation — by reflecting over the boundary of the circle with radius 1 centered at the origin. In this case, the modular form doesn’t necessarily assign those points the same value. However, the values at the two points relate to each other in a regular way that also gives rise to symmetry.

You can combine these transformations in infinitely many ways, which gives you the infinitely many symmetry conditions that the modular form must satisfy.

“That doesn’t necessarily sound very exciting,” said [John Voight](https://math.dartmouth.edu/~jvoight/), a mathematician at Dartmouth College. “I mean, carving up the upper half-plane and putting numbers on various places — who cares?”

“But they’re very elemental,” he added. And there’s a reason why that’s the case.

## Controlled Spaces

In the 1920s and ’30s, the German mathematician Erich Hecke developed a deeper theory around modular forms. Crucially, he realized that they exist in certain spaces — spaces with specific dimensions and other properties. He figured out how to describe these spaces concretely and use them to relate different modular forms to one another.

This realization has driven a lot of 20th- and 21st-century mathematics.

To understand how, first consider an old question: How many ways can you write a given integer as the sum of four squares? There is only one way to write zero, for instance, while there are eight ways to express 1, 24 ways to express 2, and 32 ways to express 3. To study this sequence — 1, 8, 24, 32 and so on — mathematicians encoded it in an infinite sum called a generating function:

$$
1 + 8q + {{24q}^2} + {{32q}^3} + {{24q}^4} + {{48q}^5} + …
$$

There wasn’t necessarily a way to know what the coefficient of, say, $q^{174}$ should be — that was precisely the question they were trying to answer. But by converting the sequence into a generating function, mathematicians could apply tools from calculus and other fields to infer information about it. They might, for instance, be able to come up with a way to approximate the value of any coefficient.

But it turns out that if the generating function is a modular form, you can do much better: You can get your hands on an exact formula for every coefficient.

“If you know it’s a modular form, then you know everything,” said [Jan Bruinier](https://www.mathematik.tu-darmstadt.de/fb/personal/details/jan_hendrik_bruinier.en.jsp) of the Technical University of Darmstadt in Germany.

That’s because the infinitely many symmetries of the modular form aren’t just beautiful to look at — “they’re so constraining,” said [Larry Rolen](https://math.vanderbilt.edu/rolenl/index.html) of Vanderbilt University, that they can be made into “a tool for automatically proving congruences and identities between things.”

Mathematicians and physicists often encode questions of interest in generating functions. They might want to count the number of points on special curves, or the number of states in certain physical systems. “If we are lucky, then it is a modular form,” said [Claudia Alfes-Neumann](https://www.claudia-alfes.de/), a mathematician at Bielefeld University in Germany. That can be very difficult to prove, but if you can, then “the theory of modular forms is so rich that it gives you tons of possibilities to investigate these \[series\] coefficients.”

## Building Blocks

Any modular form is going to look very complicated. Some of the simplest — which are used as building blocks for other modular forms — are called Eisenstein series.

You can think of an Eisenstein series as an infinite sum of functions. To determine each of those functions, use the points on an infinite 2D grid:

Merrill Sherman/ *Quanta Magazine*

When you add the functions associated to just four points in the grid near the origin, you can see how distinct symmetries begin to emerge.

![](https://www.quantamagazine.org/wp-content/uploads/2023/09/7C-01.webp)

The sum of the four simple functions above, shown in the upper half of the complex plane.

If you take the full sum of the grid’s infinitely many functions, you get an Eisenstein series that’s arguably the easiest modular form to write down. The patterns reflect the form’s defining symmetries — repeating endlessly to the left and right, and transforming in more complicated ways closer to the horizontal axis.

![](https://www.quantamagazine.org/wp-content/uploads/2023/09/7C-02.webp)

The full Eisenstein series is the sum of an infinite number of functions.

## The Game Continues

The study of modular forms has led to a flood of mathematical triumphs. For instance, recent work on sphere packing, for which the Ukrainian mathematician Maryna Viazovska [won the Fields Medal last year](https://www.quantamagazine.org/ukrainian-mathematician-maryna-viazovska-wins-fields-medal-20220705/), used modular forms. “When I saw that, I was quite surprised,” Bruinier said. “But it somehow works.”

Modular forms have turned out to be connected to an important algebraic object called the [monster group](https://www.quantamagazine.org/mathematicians-chase-moonshine-string-theory-connections-20150312/). They’ve been used to construct special kinds of networks called [expander graphs](https://www.quantamagazine.org/new-proof-shows-that-expander-graphs-synchronize-20230724/), which show up in computer science, communications theory and other applications. They’ve made it possible to study potential models of particle interactions in string theory and quantum physics.

Perhaps most famously, the 1994 proof of Fermat’s Last Theorem hinged on modular forms. The theorem, widely considered one of the most important problems in number theory, states that there are no three nonzero integers *a*, *b* and *c* that satisfy the equation ${a^n} + {b^n} = {c^n}$ when is an integer greater than 2. The mathematician Andrew Wiles proved it true by assuming the opposite — that a solution to the equation does exist — and then using modular forms to show that such an assumption must lead to a contradiction.

First he used his assumed solution to construct a mathematical object called an elliptic curve. He then showed that you can always associate a unique modular form to such a curve. However, the theory of modular forms dictated that in this case, that modular form couldn’t exist. “It’s too good to be true,” Voight said. Which meant, in turn, that the assumed solution couldn’t exist — thus confirming Fermat’s Last Theorem.

Not only did this resolve a centuries-old problem; it also provided a better understanding of elliptic curves, which can be difficult to study directly (and which play an important role in cryptography and error-correcting codes).

The proof also illuminated a bridge between geometry and number theory. That bridge has since been broadened into the [Langlands program](https://www.quantamagazine.org/what-is-the-langlands-program-20220601/), a greater set of connections between the two fields — and the subject of one of the central research efforts of contemporary mathematics. Modular forms have also been generalized in other areas, where their potential applications are just starting to be recognized.

They continue to turn up all over the place in math and physics, sometimes quite mysteriously. “I look in a paper about black holes,” said [Steve Kudla](http://www.math.toronto.edu/~skudla/) of the University of Toronto, “and I find modular forms that are friends of mine. But I don’t know why they’re there.”

“Somehow,” he added, “modular forms capture some of the most fundamental symmetries of the world.”

***Correction:** September 26, 2023  
*A earlier version of this article implied that the function $f(z)=z^2$ has a reflection symmetry it does not have. It is symmetric if points are rotated 180 **°** around the origin.