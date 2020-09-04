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
    void append(int n)
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
    int get(int i)
    {
        if (head == NULL) {
            return NULL;
        }
        node* tmp;
        tmp = this->head;
        int j = 0;
        while (j < i) {
            tmp = tmp->next;
            j += 1;
        }
        return tmp->data;
    }
private:
    node* head, * tail;
};

TEST(pch, test_DoublyLinkedList1) {
    DoublyLinkedList DLinkedList;
    DLinkedList.append(5);

    EXPECT_EQ(5, DLinkedList.get(0));
}
TEST(pch, test_DoublyLinkedList2) {
    DoublyLinkedList DLinkedList;
    DLinkedList.append(5);
    DLinkedList.append(10);

    EXPECT_EQ(10, DLinkedList.get(1));
}
