#노드 클래스
class Node:
    def __init__(self, data):
        #노드 객체의 값
        self.data = data
        #현재 노드의 왼쪽 자식노드
        self.left = None
        #현재 노드의 오른쪽 자식노드
        self.right = None
        #현재 노드의 높이
        self.height = 1
