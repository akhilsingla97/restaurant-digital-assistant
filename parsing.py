from __future__ import unicode_literals, print_function

import plac
import spacy


@plac.annotations(
    model=("Model to load", "positional", None, str))
def main(model='en_core_web_sm'):
    nlp = spacy.load(model)
    print("Loaded model '%s'" % model)

    doc = nlp("displaCy uses CSS and JavaScript to show you how computers "
               "understand language")

    # The easiest way is to find the head of the subtree you want, and then use
    # the `.subtree`, `.children`, `.lefts` and `.rights` iterators. `.subtree`
    # is the one that does what you're asking for most directly:
    for word in doc:
        if word.dep_ in ('xcomp', 'ccomp'):
            print(''.join(w.text_with_ws for w in word.subtree))

    # It'd probably be better for `word.subtree` to return a `Span` object
    # instead of a generator over the tokens. If you want the `Span` you can
    # get it via the `.right_edge` and `.left_edge` properties. The `Span`
    # object is nice because you can easily get a vector, merge it, etc.
    for word in doc:
        if word.dep_ in ('xcomp', 'ccomp'):
            #print(word, end = " ") 
            subtree_span = doc[word.left_edge.i : word.right_edge.i + 1]
            print(subtree_span.root.text, '|', subtree_span.text)

    # You might also want to select a head, and then select a start and end
    # position by walking along its children. You could then take the
    # `.left_edge` and `.right_edge` of those tokens, and use it to calculate
    # a span.

if __name__ == '__main__':
    plac.call(main)
