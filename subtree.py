def is_sub_tree(s, t):
	if s is None and t is None:
		return True
	if t is None:
		return True
	if s is None and t is not None:
		return False
	return is_same(s,t) or is_sub_tree(s.left, t) or is_sub_tree(s.right, t)

def is_same(s, t):
	if s is None and t is None:
		return True
	if s is None or t is None:
		return False
	return s.val = t.val and is_same(s.left, t.left) and is_same(s.right, t.right)
