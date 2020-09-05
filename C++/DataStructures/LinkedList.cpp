//
//
//
struct node
{
    int data;
    node* next;
};

class LinkedList {
public:
    LinkedList()
    {
        this->head = NULL;
        this->tail = NULL;
    }
    void append(int n)
    {
        node* tmp = new node;
        tmp->data = n;
        tmp->next = NULL;

        if (head == NULL) {
            this->head = tmp;
            this->tail = tmp;
        }
        else 
        {
            this->tail->next = tmp;
            this->tail = tmp;
        }
    }
    int get(int i)
    {
        if (head == NULL) {
            return NULL;
        }
        node *tmp;
        tmp = this->head;
        int j = 0;
        while (j < i) {
            tmp = tmp->next;
            j += 1;
        }
        return tmp->data;
    }
private:
    node *head, *tail;
};

TEST(pch, test_LinkedList1) {
    LinkedList LinkedList1;
    LinkedList1.append(5);

    EXPECT_EQ(5, LinkedList1.get(0));
}
TEST(pch, test_LinkedList2) {
    LinkedList LinkedList1;
    LinkedList1.append(5);
    LinkedList1.append(10);

    EXPECT_EQ(10, LinkedList1.get(1));
}
