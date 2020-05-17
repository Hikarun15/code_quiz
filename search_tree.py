
class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self, root):
		self.root = Node(root)

	def insert(self, key):
		node = self.root
	 	
		while True:#挿入場所が決まるまで繰り返す
			if node.value > key:
				if node.left is None:
					node.left = Node(key)
					return
				node = node.left
			elif node.value < key:
				if node.right is None:
					node.right = Node(key)
					return
				node = node.right

# 探索
	def search(self, key):
		node = self.root
		while True:
			if node.value == key:
				return "yes"
			elif node.value > key:
				node = node.left
			else:
				node = node.right
			if node is None:
				return "no"

	def delete_min(self, node):
		parent = node 
		tmp = node.right#右の部分木
		count = 0
		#右の部分木の最小値を探す
		while tmp.left is not None:#左の子がNone、つまり最小値がtmpに入るまで繰り返す
			parent = tmp
			tmp = tmp.left
			count += 1
		 #右の部分木の内容によって削除方法の場合分け
		if count == 0: #削除対象の右の子が最小値なら
			parent.right = tmp.right
		else:
			parent.left = tmp.right
		return tmp#最小値の節点を返す

# 削除
	def delete(self, key):
		node = self.root

		while True:
			if node is None:
				print(str(key) + "の節点がありません")
				return

			 #削除対象の節点が見つかったときの処理
			if node.value == key:
				if node.left is None and node.right is None:#子を持たない場合
					if flag == "left":#節点が左の子なら
						parent.left = None
					else:#節点が右の子なら
						parent.right = None
					return

				elif node.left is None:#子を1つ持ち、それが右の子である場合
					if flag == "left":
						parent.left = node.right
					else:
						parent.right = node.right
					return
					
				elif node.right is None:#子を1つ持ち、それが左の子である場合
					if flag == "left":
						parent.left = node.left
					else:
						parent.right = node.left
					return
					
				else:
					tmp = self.delete_min(node)
					if flag == "left": #親の調整
						parent.left = tmp
					else:
						parent.right = tmp
					# 削除対象の節点を右の部分の最小値と置き換える
					tmp.left = node.left
					tmp.right = node.right
					return

			# 削除節点の探索と親子の節点の更新
			parent = node
			if node.value > key:
				node = node.left
				flag = "left"
			else:
				node = node.right
				flag = "right"

	# 中間順巡回				
	def inorder(self, node):
		if node is None:
			return
		else:
			self.inorder(node.left)
			print(node.value)
			self.inorder(node.right) 



t = BinarySearchTree(1)
t.insert(3)
t.insert(2)
t.insert(9)
t.insert(8)
t.insert(5)
t.insert(7)
t.insert(10)
t.delete(2)
t.delete(0)
t.delete(9)
t.inorder(t.root)