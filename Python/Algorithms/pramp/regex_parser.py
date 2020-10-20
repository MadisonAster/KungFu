import unittest

def parse_terms(pattern):
  #parse terms
  terms = []
  for i, a in enumerate(pattern):
    if a == "*":
      b = terms.pop()
      terms.append(b+a)
    elif a == ".":
      terms.append(a)
    else:
      terms.append(a)
  return terms

def match_terms(terms, text):
  #match terms
  c = 0
  for term in terms:
    if "*" in term:
      pterm = term[0]
      while c < len(text) and match_terms(pterm, text[c]):
        c += 1
    elif term == ".":
      c += 1
    else:
      if term != text[c]:
        return False
      else:
        c += 1
  return c

def is_match(text, pattern):
  terms = parse_terms(pattern)
  c = match_terms(terms, text)
  
  #check remainder
  if c == len(text):
    return True
  else:
    return False

class test_is_match(unittest.TestCase):
  def test_1(self):
    self.assertEqual(True, is_match("", ""))
  
  def test_2(self):
    self.assertEqual(False, is_match("aa", "a"))
  
  def test_3(self):
    self.assertEqual(True, is_match("bb", "bb"))
    
  def test_4(self):
    self.assertEqual(True, is_match("", "a*"))
    
  def test_5(self):
    self.assertEqual(False, is_match("abbdbb", "ab*d"))
  
  def test_6(self):
    self.assertEqual(True, is_match("aba", "a.a"))
  
  def test_7(self):
    self.assertEqual(True, is_match("acd", "ab*c."))
  
  def test_8(self):
    self.assertEqual(True, is_match("abaa", "a.*a*"))
  
if __name__ == '__main__':
  unittest.main()