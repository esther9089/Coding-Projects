#include "a1.h"

FILE *fopen(const char *Menu_FNAME, const char* r);
//int scanf(const char* format);
/**
    Add your functions to this file.
    Make sure to review a1.h.
    Do NOT include a main() function in this file
    when you submit.
*/

/**
    Constructing needed structs (initializing)
*/
Restaurant* initialize_restaurant(char* name){
    //return pointer to a Restaurant

   
    //allocating memory for n numbers of struct Restaurant
    Restaurant* p = (Restaurant*)malloc(sizeof(Restaurant));
    Queue *new = (Queue*)malloc(sizeof(Queue));

   
   
    p->name = (char*)malloc(sizeof(char)*(strlen(name)+1));
    strcpy(p->name, name);

    p->menu = load_menu(MENU_FNAME);
    p->num_completed_orders = 0;
    p->num_pending_orders = 0;

    //p->pending_orders->head = NULL;
    //p->pending_orders->tail = NULL;

    //initialize pending_orders to empty Queue
    new->head = NULL;
    new->tail = NULL;
    p->pending_orders = new;

    return p;
   
   
}

Menu *load_menu(char *fname)
{
    // return a pointer to a Menu initialized with the contents of the file <fname>

    // Menu* new_menu = (Menu *)malloc(sizeof(Menu));
    //  FINDING NUM_ITEMS

    // FINDING NUM_ITEMS
    FILE *fptr2;
    fptr2 = fopen(fname, "r"); // opening and reading the file
    char line2[100];
    char *token2;
    int num_items = 0;

    while (fgets(line2, sizeof(line2), fptr2))  
    {
        char *a = strchr(line2, '$'); // to find accurat num_items
        token2 = strtok(line2, MENU_DELIM);
        if (a != NULL)
        {
            num_items++;
            while (token2 != NULL)
            {
                token2 = strtok(NULL, MENU_DELIM);
            }
        }
    }

    // making the arrays
    char **array_codes = (char **)malloc(sizeof(char *) * num_items);
    for (int i = 0; num_items > i; i++)
    {
        *(array_codes + i) = (char *)malloc(sizeof(char) * (ITEM_CODE_LENGTH));
    }

    char **array_names = (char **)malloc(sizeof(char *) * num_items);
    for (int i = 0; num_items > i; i++)
    {
        *(array_names + i) = (char *)malloc(sizeof(char) * (MAX_ITEM_NAME_LENGTH));
    }

    //double array_price[num_items];
    double *array_price = (double *)malloc(sizeof(double)*(num_items));
    // FINDING EACH ARRAY
    FILE *fptr;
    fptr = fopen(fname, "r"); // opening and reading the file

    char line[100];
    char *token;
    int counter = 0;
    int bruh = 0;
    char *end;

    while (fgets(line, sizeof(line), fptr))
    {
        char *a = strchr(line, '$'); // to find accurate num_items
        token = strtok(line, MENU_DELIM);
        if (a != NULL)
        {
            if (token != NULL)
            {
                //to clear the whitespace:
                //char temp_array[sizeof(*token)];
                //strncpy(temp_array, token, (ITEM_CODE_LENGTH));
                char *empty = token;
           
                    while (*empty == ' ' || *empty =='\t' || *empty == '\r'){
                        empty++;
                    }
                           
                *(array_codes + counter) = strncpy(array_codes[counter], empty, (ITEM_CODE_LENGTH));
                token = strtok(NULL, MENU_DELIM);
            }

            if (token != NULL)
            {
                *(array_names + counter) = strncpy(array_names[counter], token, (MAX_ITEM_NAME_LENGTH));
                
                token = strtok(NULL, "$");
            }

            if (token != NULL)
            {
                int i = 1;
               
                double temp_price = atof(token);
                array_price[counter] = temp_price;

                token = strtok(NULL, MENU_DELIM);
            }
            counter++;
        }
    }

    //double *pointer = array_price;
    fclose(fptr);
    fclose(fptr2);

    Menu *new_menu = (Menu *)malloc(sizeof(Menu));

    new_menu->num_items = num_items;
    new_menu->item_codes = array_codes;
    new_menu->item_names = array_names;
    new_menu->item_cost_per_unit = array_price;

    return(new_menu);
}

Order* build_order(char* items, char* quantities){
    //return a pointer to Order

    Order *point = (Order *)malloc(sizeof(Order));
    int num = (strlen(items))/2 ;
    int count1 = 0;
    int count2 = 0;
 
    //for item_codes
    char** array_codes = (char **)malloc(sizeof(char*)*num);
    for (int i =0; i<num; i++){
        //array_codes[i] = (char*)malloc(sizeof(char)*(ITEM_CODE_LENGTH));
        *(array_codes + i) = (char*)calloc((ITEM_CODE_LENGTH), sizeof(char));
        *(array_codes+i) = strncpy(array_codes[i], items + i*2, (ITEM_CODE_LENGTH-1));
    }
 
    //for quantities
    int* quant = (int *)malloc(sizeof(double)*num);
    char *pointer;
    double val;

    char quant_array[(num*ITEM_CODE_LENGTH)+1];
    strcpy(quant_array, quantities);
    pointer = strtok(quant_array, MENU_DELIM);  
    val = atoi(pointer);
    quant[0] = val;
    for (int i = 1; num>i; i++){
      pointer = strtok(NULL, MENU_DELIM);
      val = atoi(pointer);
      quant[i] = val;
    }
   
    point->num_items = num;
    point->item_codes = array_codes;
    point->item_quantities = quant;
   
    return (point);
   

}


void enqueue_order(Order* order, Restaurant* restaurant){
    //modify the Queue referenced by <restaurant>'s pending_orders field
    //update the <restaurant>'s num_pending_orders field

    //--------------NEW---------------
    struct QueueNode *new_order = malloc(sizeof(QueueNode));
    new_order -> order = order;
    new_order -> next = NULL;
   
    //Order *order = order;
    //struct QueueNode *next = NULL;                        // step 2 make next of new node point to null

    // if there is a tail, connect tail to new node
    if (restaurant->pending_orders->tail == NULL){
        restaurant->pending_orders->head = new_order;
    }
    if (restaurant->pending_orders->tail != NULL){
        restaurant->pending_orders->tail->next = new_order; // since both are pointers
    }
    restaurant->pending_orders->tail = new_order;

   
    // to update pending orders:
    restaurant->num_pending_orders = (restaurant->num_pending_orders) + 1;
   
}

Order* dequeue_order(Restaurant* restaurant){

    // step 1 make temp pointer to first node
    struct QueueNode *temp = restaurant->pending_orders->head;
    // saving order info
 
    //print_order(restaurant -> pending_orders -> head -> order);
    Order *order_info = temp->order;
    // step 2: make head point to second node
  
    restaurant->pending_orders->head = restaurant -> pending_orders -> head->next; //(?) also pretty sure this sets both head and tail to null in the case that queue is emptied -> check tho
   
    if (temp->next == NULL){
        restaurant->pending_orders->tail = NULL;
    } //MIGHT NEED THIS

    // step 3: free(temp)
    free(temp);

    // updating pending orders and completed orders
    restaurant->num_pending_orders --;
    restaurant->num_completed_orders ++;

    return (order_info);
   

}

double get_item_cost(char* item_code, Menu* menu){

    //return the floating point cost of the item <item_code> given by <menu>
    //int size = menu->num_items;
    int menu_items = menu->num_items; // get number of items avaliable in menu
    double price;

        // getting price of item
        for (int j = 0; j < menu_items; j++)
        {

            if (strcmp(item_code, (menu->item_codes)[j]) == 0)
            {

                price = (menu->item_cost_per_unit)[j];
            }
        }

    return price;
}
   

//------------------------------
double get_order_subtotal(Order* order, Menu* menu){
    //return the floating point cost of all items in the order <order>
    //with their respective quantities, with item costs given by <menu>

    double sub_total = 0;
    //int arr_size = sizeof(order->item_quantities)/sizeof((order->item_quantities)[0]); //find size of array
    int size = order->num_items;
    int menu_items = menu->num_items; //get number of items avaliable in menu
    double price;

    for (int i = 0; i<size; i++){

        //getting price of item
        for(int j = 0; j<menu_items; j++){

           
            if (strcmp((order->item_codes)[i], (menu->item_codes)[j]) == 0){
               
                price = (menu->item_cost_per_unit)[j];

            }
           
        }

        sub_total += ((order->item_quantities)[i])*price; //calculate subtotal

    }

    return sub_total;


}

double get_order_total(Order* order, Menu* menu){
    //return the floating point costs of all items in the order <order> with item costs given by <menu>

    double sub_tot = get_order_subtotal(order, menu);
    double tot;
    double tax = (double)TAX_RATE/100 + 1;
    tot = sub_tot*(tax);
    return tot;

}

int get_num_completed_orders(Restaurant* restaurant){
    //return the number of completed/pending orders indicated by complete_orders

    return (restaurant->num_completed_orders);

}

int get_num_pending_orders(Restaurant* restaurant){
    //return the number of completed/pending orders indicated by pending_orders

    return (restaurant->num_pending_orders);
}

void clear_order(Order** order){
    //clear all memory associated with <*order>

    int num_items = (*order)->num_items;

    for (int i = 0; i <num_items; i++){
        free((*order)->item_codes[i]);
    }
    free((*order)->item_codes);
    free((*order)->item_quantities);
   
    free(*order);
    *order = NULL;
   
}

void clear_menu(Menu** menu){
    //clear all memory associated with <*menu>

   
    for(int i = 0; i<((*menu)->num_items); i++){
        free((*menu)->item_codes[i]);
        free((*menu)->item_names[i]);
    }

    free((*menu)->item_codes);
    free((*menu)->item_names);
    free((*menu)->item_cost_per_unit);

   
    free(*menu);
    *menu = NULL;



}

void close_restaurant(Restaurant** restaurant){
    //clear all memory associated with <*restaurant>

    //call dequeue to free length of pending orders

    int num = (*restaurant)->num_pending_orders;

    clear_menu(&((*restaurant)->menu));
    while ((*restaurant)->pending_orders->head != NULL)
    {
        QueueNode *del = (*restaurant)->pending_orders->head;
        Order *order = del->order;
        (*restaurant)->pending_orders->head = (*restaurant)->pending_orders->head->next;
        clear_order(&order);
        free(del);
    }

    free((*restaurant)->name);
    free((*restaurant)->pending_orders);

    free((*restaurant));
    *restaurant = NULL;
}

void print_menu(Menu* menu){
    fprintf(stdout, "--- Menu ---\n");
    for (int i = 0; i < menu->num_items; i++){
        fprintf(stdout, "(%s) %s: %.2f\n",
            menu->item_codes[i],
            menu->item_names[i],
            menu->item_cost_per_unit[i]
        );
    }
}


void print_order(Order* order){
    for (int i = 0; i < order->num_items; i++){
        fprintf(
            stdout,
            "%d x (%s)\n",
            order->item_quantities[i],
            order->item_codes[i]
        );
    }
}


void print_receipt(Order* order, Menu* menu){
    for (int i = 0; i < order->num_items; i++){
        double item_cost = get_item_cost(order->item_codes[i], menu);
        fprintf(
            stdout,
            "%d x (%s)\n @$%.2f ea \t %.2f\n",
            order->item_quantities[i],
            order->item_codes[i],
            item_cost,
            item_cost * order->item_quantities[i]
        );
    }
    double order_subtotal = get_order_subtotal(order, menu);
    double order_total = get_order_total(order, menu);
   
    fprintf(stdout, "Subtotal: \t %.2f\n", order_subtotal);
    fprintf(stdout, "               -------\n");
    fprintf(stdout, "Tax %d%%: \t$%.2f\n", TAX_RATE, order_total);
    fprintf(stdout, "              ========\n");
}
