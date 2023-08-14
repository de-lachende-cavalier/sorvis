# A collection of notes about NCAs useful for the final report/presentation/personal use

"What is clear is that evolution has learned to exploit the laws of physics and computation to implement the highly robust morphogenetic software that runs on genome-encoded cellular hardware."[1]

- Need to find out the algorithms at the base of morphogenesis
- Multiple subroutines (e.g. "build an eye here") => how many? how complex? how do they interact? what about building "micro" networks and coordinating them? => I smell RL...

"Imagine if we could design systems of the same plasticity and robustness as biological life: structures and machines that could grow and repair themselves."[1]

- The genome bottleneck; intelligence as compression => solve the genome bottleneck = solve intelligence? (<https://en.wikipedia.org/wiki/Hutter_Prize>)

- Deep Learning as "the art of stacking together differentiable functions, and optimizing their parameters to perform various tasks"[1]

"Hidden channels don’t have a predefined meaning, and it’s up to the update rule to decide what to use them for."[1]

- NCAs grow and branch out somewhat like the [Mycelium](https://en.wikipedia.org/wiki/Mycelium)! Fractal Geometry of (Artificial) Nature? Interesting thought...

- The MNIST CA case investigates the question: "can CAs use local message passing to achieve global agreement on what digit they compose?"[2], and it gives an affirmative answer!
  - So, why not use just a subset of the "Quick! Draw" classes, and train mininets on single elements of the figure (e.g. if we draw a car, we can have a mininet classify the wheels, one the windows, one the doors, etc...). This would allow one to study the interesting case in which NCAs need to cooperate! (i.e. the sub-routine bullet point above)

"Therefore, while they (the cells) do not know where they are, they do know where up, down, left and right are. The biological analogy here is a situation where the remodeling structures exist in the context of a larger body and a set of morphogen gradients or tissue polarity that indicate directional information with respect to the three major body axes."[2]

"The intuition here is that we are placing living cells in a cookie cutter and asking them to identify the global shape of the cookie cutter."[2]

"Keen readers may notice that our model requires each digit to be a single connected component in order for classification to be possible, since any disconnected components will be unable to propagate information between themselves. We made this design decision in order to stay true to our core biological analogy, which involves a group of cells that is trying to identify its global shape."[2]

"Here we aim to build a CA model that not only has regenerative properties, but also has the ability to correct itself when the shape of the overall digit changes."[2]

## References

- Growing Neural Cellular Automata, Mordvintsev et al., Distill [1](https://distill.pub/2020/growing-ca)
- Self-classifying MNIST digits, Mordvintsev et al., Distill [2](https://distill.pub/2020/selforg/mnist/)
- The Future of Artificial Intelligence is Self-Organizing and Self-Assembling, S. Risi [3](https://sebastianrisi.com/self_assembling_ai/)
- A New Kind of Science, S. Wolfram [4](https://www.wolframscience.com/nks/)
