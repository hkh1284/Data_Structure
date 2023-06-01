#AVL Tree 클래스
class AVLTree:
    #생성자
    def __init__(self):
        self.root = None
        
    
    
    #삽입연산
    def insert(self, data):
        self.root = self.InsertNode(self.root, data)
    
    
    #InsertNode - 재귀적으로 삽입연산 구현
    def InsertNode(self, root, data):
        #삽입 위치를 찾았다면 삽입할 노드를 해당 위치에 넣어주기
        if root is None:
            return Node(data)
        #data가 현재 노드의 값보다 작으면 왼쪽 서브트리에서 재귀적으로 탐색
        elif data < root.data:
            root.left = self.InsertNode(root.left, data)
        #data가 현재 노드의 값보다 크면 오른쪽 서브트리에서 재귀적으로 탐색
        else:
            root.right = self.InsertNode(root.right, data)
        
        #노드의 높이 갱신
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        #균형 인수 계산
        balance_factor = self.get_balance(root)
        
        #왼쪽 서브트리가 높이가 큰 경우
        if balance_factor > 1:
            #LL인 경우 - 오른쪽 회전
            if data < root.left.data:
                return self.rotate_right(root)
            #LR인 경우 - 왼쪽 회전 후 오른쪽 회전
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        
        #오른쪽 서브트리가 높이가 큰 경우
        if balance_factor < -1:
            #RR인 경우 - 왼쪽 회전
            if data > root.right.data:
                return self.rotate_left(root)
            #RL인 경우 - 오른쪽 회전 후 왼쪽 회전
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
        return root
    
    
    
    #삭제연산
    def delete(self, data):
        self.root = self.DeleteNode(self.root, data)

    #DeleteNode - 재귀적으로 삭제연산 구현
    def DeleteNode(self, root, data):
        #삭제할 노드가 없다면 None리턴
        if root is None:
            return root
        #삭제할 노드의 값이 현재 노드의 값보다 작으면 왼쪽 서브트리에서 삭제 수행
        elif data < root.data:
            root.left = self.DeleteNode(root.left, data)
        #삭제할 노드의 값이 현재 노드의 값보다 크면 오른쪽 서브트리에서 삭제 수행
        elif data > root.data:
            root.right = self.DeleteNode(root.right, data)
        #삭제할 노드를 찾았다면
        else:
            #삭제할 노드의 왼쪽 자식이 없는 경우
            if root.left is None:
                #삭제할 노드를 None으로 변경하고 해당노드의 오른쪽 자식을 부모노드에 연결
                temp = root.right
                root = None
                return temp
            #삭제할 노드의 오른쪽 자식이 없는 경우
            elif root.right is None:
                #삭제할 노드를 None으로 변경하고 해당노드의 왼쪽 자식을 부모노드에 연결
                temp = root.left
                root = None
                return temp
            
            #오른쪽 서브트리에서 가장 작은 값을 찾아서 현재 노드의 값으로 대체
            temp = self.find_min_node(root.right)
            root.data = temp.data
            #오른쪽 서브트리에서 재귀적으로 삭제연산 수행
            root.right = self.DeleteNode(root.right, temp.data)

        #노드의 높이 갱신
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        #균형 인수 계산
        balance_factor = self.get_balance(root)
        
        #왼쪽 서브트리가 높이가 큰 경우
        if balance_factor > 1:
            #LL인 경우 - 오른쪽 회전
            if self.get_balance(root.left) >= 0:
                return self.rotate_right(root)
            #LR인 경우 - 왼쪽 회전 후 오른쪽 회전
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        #오른쪽 서브트리가 높이가 큰 경우
        if balance_factor < -1:
            #RR인 경우 - 왼쪽 회전
            if self.get_balance(root.right) <= 0:
                return self.rotate_left(root)
            #RL인 경우 - 오른쪽 회전 후 왼쪽 회전
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root
    
    
    
    #탐색연산
    def search(self, data):
        if self.SearchNode(self.root, data) is None:
            print("해당 노드는 AVL트리에 존재하지 않습니다.", end='')
        else:
            print("해당 노드는 AVL트리에 존재합니다.", end='')

    
    #SearchNode - 재귀적으로 탐색연산 구현
    def SearchNode(self, root, data):
        # 노드가 존재하지 않거나 탐색한 값를 찾은 경우
        if root is None or root.data == data:
            return root
        #찾으려는 값보다 data가 더 작으면
        elif data < root.data:
            # 왼쪽 서브트리에서 탐색 수행
            return self.SearchNode(root.left, data)
        #찾으려는 값보다 data가 더 크면
        else:
            #오른쪽 서브트리에서 탐색 수행
            return self.SearchNode(root.right, data)

        
    #find_min_node - 인자를 루트로 하는 서브트리에서 최솟값 노드 찾기
    def find_min_node(self, root):
        min_node = root
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    
    #get_height - 높이 반환
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    
    #get_balance - 왼쪽 서브트리의 높이와 오른쪽 서브트리의 높이 차이 반환
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    
    #rotate_right - 오른쪽 회전
    def rotate_right(self, n):
        #n의 왼쪽 자식노드인 x를 기준으로 회전
        x = n.left
        #x의 오른쪽 자식을 n의 왼쪽 자식으로 지정
        n.left = x.right
        #x의 오른쪽 자식으로 n을 지정
        x.right=n
        
        #높이 갱신
        n.height = max(self.get_height(n.left), self.get_height(n.right))+1
        x.height = max(self.get_height(x.left), self.get_height(x.right))+1
        
        #새로운 부모노드 반환
        return x

    
    #rotate_left - 왼쪽 회전
    def rotate_left(self, n):
        #n의 오른쪽 자식노드인 x를 기준으로 회전
        x = n.right
        #x의 왼쪽 자식을 n의 오른쪽 자식으로 지정
        n.right = x.left
        #x의 왼쪽 자식으로 n을 지정
        x.left=n
        
        #높이 갱신
        n.height = max(self.get_height(n.left), self.get_height(n.right))+1
        x.height = max(self.get_height(x.left), self.get_height(x.right))+1
        
        #새로운 부모노드 반환
        return x

    
    #inorder - 중위순회
    def inorder(self):
        self.inorder_recursive(self.root)
        
    def inorder_recursive(self, node):
        if node:
            self.inorder_recursive(node.left)
            print(node.data, end=" ")
            self.inorder_recursive(node.right)

        
    #preorder - 전위순회
    def preorder(self):
        self.preorder_recursive(self.root)
        
    def preorder_recursive(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.inorder_recursive(node.left)
        self.inorder_recursive(node.right)
