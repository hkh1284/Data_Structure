# 세번째 테스트
tree3 = AVLTree()
tree3.insert(36)
tree3.insert(12)
tree3.insert(57)
tree3.insert(7)
tree3.insert(23)
tree3.insert(51)
tree3.insert(73)
tree3.insert(44)
tree3.insert(62)
tree3.insert(87)

print("AVL 트리의 중위 순회 결과:")
tree3.inorder()
print("\nAVL 트리의 전위 순회 결과:")
tree3.preorder()

print("\nAVL 트리에 노드 67 삽입 수행")
tree3.insert(67)

print("노드 67 삽입 후, 중위 순회 결과:")
tree3.inorder()
print("\n노드 67 삽입 후, 전위 순회 결과:")
tree3.preorder()



tree3.delete(57)
print("\n노드 57을 삭제한 후 AVL 트리의 중위 순회 결과:")
tree3.inorder()
print("\n노드 57을 삭제한 후 AVL 트리의 전위 순회 결과:")
tree3.preorder()


print("\n노드 57의 존재 여부:")
tree3.search(57)
print("\n노드 67의 존재 여부:")
tree3.search(67)
