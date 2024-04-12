# Matt's Ollama Tools

I needed some simple tools to make it easier to work with integrating Ollama with the real world. This is a collection of those tools.

## Chunker

Sometimes you need to take a bunch of text in and then spit it out in an array of chunks. This will take in a long text and then split it into chunks of up to a defined number of words. It won't ever get sentence fragments. It will overlap each chunk by one sentence. If you have a text with a bunch of poorly written run-on sentences, this might not work.

### Usage

```python
from mattsollamatools import chunker

textchunks = chunker(text, max_words_per_chunk=110, language='spanish')
```

If you don't include max_words_per_chunk, it will default to 100. If you don't include language, it will default to 'english'.
