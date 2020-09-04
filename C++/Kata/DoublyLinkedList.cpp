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
    void Append(int n)
    {
        node* tmp = new node;
        tmp->data = n;
        tmp->next = NULL;
        tmp->prev = NULL;

        if (head == NULL) {
            this->head = tmp;
            this->tail = tmp;
        }
        else
        {
            tmp->prev = this->tail;
            this->tail->next = tmp;
            this->tail = tmp;
        }
    }
    void Insert(node* prev, int n) {
        if (prev == NULL) return;
        node* tmp = new node;
        tmp->data = n;
        tmp->next = prev->next;
        prev->next = tmp;
        tmp->prev = prev;
        if (tmp->next != NULL) tmp->next->prev = tmp;
    }
    void InsertAt(int i, int n) {
        node* M = this->GetNode(i);
        this->Insert(M, n);
    }
    int GetValue(int i)
    {
        if (head == NULL) return NULL;
        node* tmp;
        tmp = this->head;
        int j = 0;
        while (j < i) {
            tmp = tmp->next;
            j += 1;
        }
        return tmp->data;
    }
    node* GetNode(int i) {
        if (head == NULL) return NULL;
        node* tmp;
        tmp = this->head;
        int j = 0;
        while (j < i) {
            tmp = tmp->next;
            j += 1;
        }
        return tmp;
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
