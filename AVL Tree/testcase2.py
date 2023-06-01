# 두번째 테스트
tree2 = AVLTree()
tree2.insert(21)
tree2.insert(6)
tree2.insert(26)
tree2.insert(18)
tree2.insert(3)

print("AVL 트리의 중위 순회 결과:")
tree2.inorder()
print("\nAVL 트리의 전위 순회 결과:")
tree2.preorder()

print("\nAVL 트리에 노드 14 삽입 수행")
tree2.insert(14)

print("노드 14 삽입 후, 중위 순회 결과:")
tree2.inorder()
print("\n노드 14 삽입 후, 전위 순회 결과:")
tree2.preorder()



tree2.delete(21)
print("\n노드 21을 삭제한 후 AVL 트리의 중위 순회 결과:")
tree2.inorder()
print("\n노드 21을 삭제한 후 AVL 트리의 전위 순회 결과:")
tree2.preorder()


print("\n노드 21의 존재 여부:")
tree2.search(21)
print("\n노드 26의 존재 여부:")
tree2.search(26)
