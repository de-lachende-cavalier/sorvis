# sorvis

This repo contains the code necessary for an exploration of Mordvintsev et al.'s
[work](https://distill.pub/2020/selforg/) on NCAs.

I mostly focused on the first two articles in the above thread, seeing as they were the two most relevant for computer vision: the notebook provide simplified (and cleaner) code for them.
The bulk of the code (for my use case, and, more generally, for the self-organising effort at Google) can be found in the Google Research [repo](https://github.com/google-research/self-organising-systems).

The organisation is quite intuitive:

- *growing_NCAs.ipynb:* contains the code for growing NCAs into some specified emoji
- *classifying_NCAs.ipynb:* contains the code necessary for object classification on the Quick! Draw dataset
- *classifying_NCAs_mnist.ipynb:* same as above, but for the MNIST dataset
- *notes.md:* contains some miscellaneous interesting notes derived from the articles on Distill

- *mini_experiments:* a mostly inactive directory, meant for some small experiments somewhat related to the main content

## Running the code

To run the code, simply start up a virtual environment (I used venv, but conda would probably work as well) and then install all the requirements, i.e.,

```bash
pip install -r requirements.txt 
```
