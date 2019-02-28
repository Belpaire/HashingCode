class Picture:
	# True for horizontal orientation, false otherwise
	# id = unique number
	#nbtags should be equal to length tags
	#tags is a list of tags
	def __init__(self,id,ishorizontal,nbtags,tags):
		self.id = id
		self.ishorizontal = ishorizontal
		self.nbtags = nbtags
		self.tags = tags

	def __str__(self):
		return "pic id:%s %s %s" % (self.id, "H" if self.ishorizontal else "V", self.tags)

	def merge(self, other):
		assert not self.ishorizontal and not other.ishorizontal
		id = "%s %s" % (self.id, other.id)
		tags = self.tags
		tags.extend(x for x in other.tags if x not in tags)
		tags = tags
		nbtags = len(tags)
		ishorizontal = True

		return Picture(id, ishorizontal, nbtags, tags)

