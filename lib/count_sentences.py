#!/usr/bin/env python3

# import the re module
import re

class MyString:
  
  # initialize the attributes
  def __init__(self, value=''):
    self.value = value
    
  # define value as a property
  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
      
  # compile the getter and setter for value
  value = property(get_value, set_value)
  
  # is_sentence() method
  def is_sentence(self):
    return self.value.endswith('.')
  
  # is_question() method
  def is_question(self):
    return self.value.endswith('?')
  
  # is_exclamation() method
  def is_exclamation(self):
    return self.value.endswith('!')
  
  # count_sentences() method
  def count_sentences(self):
    # define the pattern to split the string
    pattern = r'[.?!]'
    # split the string at the 
    sentences = re.split(pattern, self.value)
    
    # remove trailing white spaces
    sentences = [part.strip() for part in sentences if part.strip()]
    
    # return the count of the sentences
    return len(sentences)