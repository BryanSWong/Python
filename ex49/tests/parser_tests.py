from nose.tools import *
from ex49 import parser

def test_peek():
  test = [('noun', 'bear')]
  assert_equal(parser.peek(test), 'noun')
  assert_equal(parser.peek(None), None)

def test_match():
  test = [('noun', 'bear')]
  assert_equal(parser.match(test, 'noun'), ('noun', 'bear'))
  assert_equal(parser.match(test, 'stop'), None)
  assert_equal(parser.match(None, 'noun'), None)

def test_skip():
  test = [('verb', 'punch'), ('noun', 'bear')]
  parser.skip(test, 'verb')
  assert_equal(test, [('noun', 'bear')])
  parser.skip(test, 'noun')
  assert_equal(test, [])

def test_parse_verb():
  test = [('verb', 'punch'), ('stop', 'the'), ('noun', 'bear')]
  assert_equal(parser.parse_verb(test), ('verb', 'punch'))
  test2 = [('noun', 'bear'), ('verb', 'eat'), ('noun', 'honey')]
  assert_raises(parser.ParseError, parser.parse_verb, test)

def test_parse_object():
  test = [('stop', 'the'), ('noun', 'bear')]
  assert_equal(parser.parse_object(test), ('noun', 'bear'))
  test2 = [('stop', 'go'), ('direction', 'up')]
  assert_equal(parser.parse_object(test2), ('direction', 'up'))
  test3 = [('verb', 'punch'), ('stop', 'the'), ('noun', 'bear')]
  assert_raises(parser.ParseError, parser.parse_object, test3)

def test_parse_subject():
  test = [('verb', 'eat'), ('noun', 'bear')]
  assert_equal(parser.parse_subject(test), ('noun', 'player'))
  test2 = [('noun', 'bear'), ('verb', 'eat')]
  assert_equal(parser.parse_subject(test2), ('noun', 'bear'))
  test3 = [('direction', 'up')]
  assert_raises(parser.ParseError, parser.parse_subject, test3)

def test_parse_sentence():
  test = [('noun', 'bear'), ('verb', 'eat'), ('noun', 'honey')]
  result = parser.parse_sentence(test)
  assert_equal(result.subject, ('bear'))
  assert_equal(result.verb, ('eat'))
  assert_equal(result.object, ('honey'))

def test_parse_number():
  test = [('stop', 'the'), ('number', 5), ('noun', 'bear')]
  assert_equal(parser.parse_number(test), ('number', 5))