#include <stdio.h>
#include <math.h>



int main()



{

   float total;
   char  k;
   float seq;
   
   total = 0;
   seq = 0;
   

   while (scanf("%c", &k) == 1)



        {
          

          if (k == 'C' || k == 'c' || k == 'g' || k == 'G')

              {

                total = total + 1;

              }

           seq++;

        }

          printf("The GC percentage is %f%%\n", (total/seq)*100);



}
