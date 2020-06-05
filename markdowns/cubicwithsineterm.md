# Here is a slightly more interesting output
Note that $`u`$ here is the Heaviside step function but it's applied to the (shifted) modulus of a function rather than a variable.  That is, we are interested in roots of $`g(z;k) \equiv f(z)+u(|f(z)|-k-1) k Sin(z)`$. This will yield the same roots as $`f(z)=x^3-x`$ on the real line. This obtains from [Rouché's theorem](https://en.wikipedia.org/wiki/Rouch%C3%A9%27s_theorem) as long as $`|f| < k`$, $`sin(z)`$ being of bounded modulus there.
Elsewhere the value can be seen as depending on the hyperbolic sine of the imaginary part of $`z`$, $`sinh(\Im z)`$.  [Proof of which](https://proofwiki.org/wiki/Modulus_of_Sine_of_Complex_Number).  

@[Is 7 in the basin of attraction of any roots of the function f(z)?]({"stubs": ["sinebrot/plot.py", "sinebrot/basin.py"], "command": "sh -c 'python3 sinebrot/plot.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})
