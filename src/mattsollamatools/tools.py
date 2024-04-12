from nltk.tokenize import sent_tokenize, word_tokenize

def chunker(text, max_words_per_chunk=100, language="english"):
  """
  Splits the input text into overlapping chunks of words up to the max per chunk
  Returns:
    list of chunks which are strings
  """

  sentences = sent_tokenize(text, language=language)
  chunks = []
  current_chunk = []

  for sentence in sentences:
    
      words = word_tokenize(sentence, language=language)

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

from typing import List

def chunk_text_by_sentences(source_text: str, sentences_per_chunk: int, overlap: int, language="english") -> List[str]:
    """
    Splits text by sentences
    """
    if sentences_per_chunk < 2:
        raise ValueError("The number of sentences per chunk must be 2 or more.")
    if overlap < 0 or overlap >= sentences_per_chunk - 1:
        raise ValueError("Overlap must be 0 or more and less than the number of sentences per chunk.")
    
    sentences = sent_tokenize(source_text, language=language)
    if not sentences:
        print("Nothing to chunk")
        return []
    
    chunks = []
    i = 0
    print(len(sentences))
    while i < len(sentences):
        end = min(i + sentences_per_chunk, len(sentences))
        chunk = ' '.join(sentences[i:end])
        
        if overlap > 0 and i > 1:
            overlap_start = max(0, i - overlap)
            overlap_end = i
            overlap_chunk = ' '.join(sentences[overlap_start:overlap_end])
            chunk = overlap_chunk + ' ' + chunk
        
        chunks.append(chunk.strip())
        i += sentences_per_chunk
    
    return chunks