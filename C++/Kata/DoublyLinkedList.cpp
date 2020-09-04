//
//
//

struct node
{
    int data;
    node* next;
    node* prev;
};

class DoublyLinkedList {
public:
    DoublyLinkedList()
    {
        this->head = NULL;
        this->tail = NULL;
    }
    void Initialize(node* Node)
    {
        if (this->head == NULL) {
            this->head = Node;
            this->tail = Node;
        }
    }
    node* MakeNode(int n)
    {
        node* Node = new node;
        Node->data = n;
        Node->next = NULL;
        Node->prev = NULL;
        return Node;
    }
    void Append(int n)
    {
        node* Node = this->MakeNode(n);
        this->AppendNode(Node);
    }
    void AppendNode(node* Node)
    {
        if (this->head == NULL) return this->Initialize(Node);

        Node->prev = this->tail;
        this->tail->next = Node;
        this->tail = Node;
    }
    void Push(int n)
    {
        node* Node = this->MakeNode(n);
        this->PushNode(Node);
    }
    void PushNode(node* Node)
    {
        Node->next = this->head;
        Node->prev = NULL;
        this->head->prev = Node;
        this->head = Node;
    }
    void Insert(node* prev, int n) {
        if (prev == NULL) return;
        node* Node = this->MakeNode(n);
        Node->next = prev->next;
        prev->next = Node;
        Node->prev = prev;
        if (Node->next != NULL) Node->next->prev = Node;
    }
    void InsertAt(int i, int n) {
        node* M = this->GetNode(i);
        this->Insert(M, n);
    }
    int GetValue(int i)
    {
        if (this->head == NULL) return NULL;
        node* Node;
        Node = this->head;
        int j = 0;
        while (j < i) {
            Node = Node->next;
            j += 1;
        }
        return Node->data;
    }
    node* GetNode(int i) {
        if (this->head == NULL) return NULL;
        node* Node = this->head;
        int j = 0;
        while (j < i) {
            Node = Node->next;
            j += 1;
        }
        return Node;
    }
    node* Pop() {
        node* Node = this->tail;
        this->tail = Node->prev;
        this->tail->next = NULL;
        Node->prev = NULL;
        return Node;
    }
    void Reverse(void) {
        node* n = this->GetNode(0);
    }
private:
    node* head, * tail;
};

TEST(pch, test_DoublyLinkedList1) {
    DoublyLinkedList DLinkedList;
    DLinkedList.Append(5);

    EXPECT_EQ(5, DLinkedList.GetValue(0));
}
TEST(pch, test_DoublyLinkedList2) {
    DoublyLinkedList DLinkedList;
    DLinkedList.Append(5);
    DLinkedList.Append(10);

    EXPECT_EQ(10, DLinkedList.GetValue(1));
}
TEST(pch, test_DoublyLinkedList3) {
    DoublyLinkedList DLinkedList;
    DLinkedList.Append(5);
    DLinkedList.Append(10);
    DLinkedList.Append(15);
    DLinkedList.InsertAt(1, 12);
    EXPECT_EQ(12, DLinkedList.GetValue(2));
    EXPECT_EQ(15, DLinkedList.GetValue(3));
}
