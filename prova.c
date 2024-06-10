#include <stdio.h>
#include <math.h>

int main ()
{
    float D, a, b, c, d;
    
    printf("Digita il valore del lato D e premi INVIO\n");
    scanf("\n%f)", &D);

    a=D*D; //area quadrato
    d=D/2; //raggio cerchio
    b=3.14*(d*d); // area cerchio
    c=(1.732/4)*a; //area del triangolo equilatero

    printf("L'area del quadrato di lato D è: %f\n", a);
    printf("L'area del cerchio di diametro D è: %f\n", b);
    printf("L'area del trinagolo equilatero di lato D è: %f\n", c);

    return 0;
}