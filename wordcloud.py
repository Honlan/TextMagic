#!/usr/bin/env python
# coding:utf8

import sys 
reload(sys)
sys.setdefaultencoding('utf8')

import jieba.analyse

class WordCloud(object):
	"""class for wordcloud generation"""
	def __init__(self, text):
		super(WordCloud, self).__init__()
		self.text = unicode(text)

	def csv(self, n=100):
		content = jieba.analyse.extract_tags(self.text, topK=n, withWeight=True, allowPOS=())
		fw = open('word_freq.txt', 'w')
		for c in content:
			if c[0] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
				continue
			fw.write(c[0] + ';' + str(c[1]) + '\n')
		fw.close()