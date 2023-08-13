
# About

A collection of notes about NCAs useful for the final report/presentation/personal use.

"What is clear is that evolution has learned to exploit the laws of physics and computation to implement the highly robust morphogenetic software that runs on genome-encoded cellular hardware."[1]

- Need to find out the algorithms at the base of morphogenesis
- Multiple subroutines (e.g. "build an eye here") => how many? how complex? how do they interact? what about building "micro" networks and coordinating them? => I smell RL...

"Imagine if we could design systems of the same plasticity and robustness as biological life: structures and machines that could grow and repair themselves."[1]

- The genome bottleneck; intelligence as compression => resolve the genome bottleneck = resolve intelligence? (<https://en.wikipedia.org/wiki/Hutter_Prize>)

- Deep Learning as "the art of stacking together differentiable functions, and optimizing their parameters to perform various tasks"[1]

"Hidden channels don’t have a predefined meaning, and it’s up to the update rule to decide what to use them for."[1]

- NCAs grow and branch out somewhat like the [Mycelium](https://en.wikipedia.org/wiki/Mycelium)! Fractal Geometry of (Artificial) Nature? Interesting thought...

- The MNIST CA case investigates the question: "can CAs use local message passing to achieve global agreement on what digit they compose?"[2], and it gives an affirmative answer! So, why not use just a subset of the "Quick! Draw" classes, and train mininets on single elements of the figure (e.g. if we draw a car, we can have a mininet classify the wheels, one the windows, one the doors, etc...).
This would allow one to study the interesting case in which NCAs need to cooperate! (Check out the sub-routine bullet point above.)

# References

- Growing Neural Cellular Automata, Mordvintsev et al., Distill [1](https://distill.pub/2020/growing-ca)
- Self-classifying MNIST digits, Mordvintsev et al., Distill [2](https://distill.pub/2020/selforg/mnist/)
- The Future of Artificial Intelligence is Self-Organizing and Self-Assembling, S. Risi [3](https://sebastianrisi.com/self_assembling_ai/)
- A New Kind of Science, S. Wolfram [4](https://www.wolframscience.com/nks/)
