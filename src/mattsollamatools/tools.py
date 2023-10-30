from nltk.tokenize import sent_tokenize, word_tokenize

def chunker(text, max_words_per_chunk=100):
  """
  Splits the input text into overlapping chunks of words up to the max per chunk

  Returns:
    list of chunks which are strings
  """

  sentences = sent_tokenize(text)
  chunks = []
  current_chunk = []

  for sentence in sentences:
      words = word_tokenize(sentence)

      if len(current_chunk) + len(words) <= max_words_per_chunk:
          current_chunk.extend(words)
      else:
          chunks.append(' '.join(current_chunk))
          current_chunk = words

  # Add the last chunk if it's not empty
  if current_chunk:
      chunks.append(' '.join(current_chunk))

  overlapping_chunks = []
  for i in range(len(chunks)):
      chunk_start = max(0, i - 1)
      chunk_end = i + 1
      overlapping_chunk = ' '.join(chunks[chunk_start:chunk_end])
      overlapping_chunks.append(overlapping_chunk)

  return overlapping_chunks