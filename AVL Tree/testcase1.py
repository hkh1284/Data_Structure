# 첫번째 테스트
tree = AVLTree()
tree.insert(3)
tree.insert(7)
tree.insert(10)
tree.insert(27)
tree.insert(17)
tree.insert(12)
tree.insert(38)
tree.insert(45)
tree.insert(44)
tree.insert(36)

print("AVL 트리의 중위 순회 결과:")
tree.inorder()
print("\nAVL 트리의 전위 순회 결과:")
tree.preorder()

print("\nAVL 트리에 노드 23 삽입 수행")
tree.insert(23)

print("노드 23 삽입 후, 중위 순회 결과:")
tree.inorder()
print("\n노드 23 삽입 후, 전위 순회 결과:")
tree.preorder()



tree.delete(17)
print("\n노드 17을 삭제한 후 AVL 트리의 중위 순회 결과:")
tree.inorder()
print("\n노드 17을 삭제한 후 AVL 트리의 전위 순회 결과:")
tree.preorder()


print("\n노드 36의 존재 여부:")
tree.search(36)
print("\n노드 17의 존재 여부:")
tree.search(17)
