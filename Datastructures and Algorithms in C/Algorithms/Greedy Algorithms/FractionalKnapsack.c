#include <stdio.h>
 
int n = 5; /* The number of objects */
int weight[10] = {8, 5, 2, 4, 2}; 
int profit[10] = {5, 8, 2, 9, 1}; 
int W = 15; /* The maximum weight you can take */
 
void simple_fill() {
    int cur_w;
    float tot_v;
    int i, maxi;
    int used[10];
 
    for (i = 0; i < n; ++i)
        used[i] = 0; /* I have not used the ith object yet */
 
    cur_w = W;
    while (cur_w > 0) { /* while there's still room*/
        /* Find the best object */
        maxi = -1;
        for (i = 0; i < n; ++i)
            if ((used[i] == 0) &&
                ((maxi == -1) || ((float)profit[i]/weight[i] > (float)profit[maxi]/weight[maxi])))
                maxi = i;
 
        used[maxi] = 1; /* mark the maxi-th object as used */
        cur_w -= weight[maxi]; /* with the object in the bag, I can carry less */
        tot_v += profit[maxi];
        if (cur_w >= 0)
            printf("Added object %d (%d$, %dKg) completely in the bag. Space left: %d.\n", maxi + 1, profit[maxi], weight[maxi], cur_w);
        else {
            printf("Added %d%% (%d$, %dKg) of object %d in the bag.\n", (int)((1 + (float)cur_w/weight[maxi]) * 100), profit[maxi], weight[maxi], maxi + 1);
            tot_v -= profit[maxi];
            tot_v += (1 + (float)cur_w/profit[maxi]) * weight[maxi];
        }
    }
 
    printf("Filled the bag with objects worth %.2f$.\n", tot_v);
}
 
int main(int argc, char *argv[]) {
    simple_fill();
 
    return 0;
}