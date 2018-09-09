#include <stdio.h>

int  main()
{
  long double fact(long double   x);
  long double mfact(long double   w[], long double   t, long double   v);
  long double ffact(long double   x, long double  k);
  long double Post(long double  p[], long double  n, int  r, long double  x);
  void printlist(long double p[], int r);

  long double p[] = {0,0,8,0};
  long double k = 8;
  long double x = 16;
  long double n = 8;
  int  r = 3;
  long double p1[] = {2,1,0,5};
  long double p2[] = {2,0,2,4};
  long double p3[] = {1,2,1,4};
  long double p4[] = {0,4,0,4};
  long double p5[] = {1,1,3,3};
  long double p6[] = {0,3,2,3};
  long double p7[] = {1,0,5,2};
  long double p8[] = {0,2,4,2};
  long double p9[] = {0,1,6,1};
  long double p10[] = {0,0,8,0};

  long double Z = Post(p1, n, r, x)+Post(p2, n, r, x)+Post(p3, n, r, x)+Post(p4, n, r, x)+Post(p5, n, r, x)+Post(p6, n, r, x)+Post(p7, n, r, x)+Post(p8, n, r, x)+Post(p9, n, r, x)+Post(p10, n, r, x);

  printf("\n");
  printlist(p1, r);
  printf("here is p1 %Lf", Post(p1, n, r, x));
  printf("\n");
  printf("\n");

  printlist(p2, r);
  printf("here is p2 %Lf", Post(p2, n, r, x));
  printf("\n");
  printf("\n");

  printlist(p3, r);
  printf("here is p3 %Lf", Post(p3, n, r, x));
  printf("\n");
  printf("\n");

  printlist(p4, r);
  printf("here is p4 %Lf", Post(p4, n, r, x));
  printf("\n");
  printf("\n");

  printlist(p5, r);
  printf("here is p5 %Lf", Post(p5, n, r, x));
  printf("\n");
  printf("\n");

  printlist(p6, r);
  printf("here is p6 %Lf", Post(p6, n, r, x));
  printf("\n");
  printf("\n");

  printlist(p7, r);
  printf("here is p7 %Lf", Post(p7, n, r, x));
  printf("\n");
  printf("\n");

  printlist(p8, r);
  printf("here is p8 %Lf", Post(p8, n, r, x));
  printf("\n");
  printf("\n");

  printlist(p9, r);
  printf("here is p9 %Lf", Post(p9, n, r, x));
  printf("\n");
  printf("\n");

  printlist(p10, r);
  printf("here is p10 %Lf", Post(p10, n, r, x));
  printf("\n");
  printf("\n");

  printf("\n");
  printf("here is Z %Lf", Z);
  printf("\n");
  printf("\n");

  printf("here is fact test\n");
  printf("%Lf\n", fact(7));
  printf("here is ffact test\n");
  printf("%Lf\n", ffact(40, 16));
  printf("here is mfact test\n");
  printf("%Lf\n", mfact(p, x, r));


  printf("\n");
  printf("The configuration of the most probable congiguration is");
  printf("%Lf", Post(p8, n, r, x)/Z);
  printf("where p1o is", p8);
  printf("\n");

}


long double fact(long double x){
  if (x < 1)
    return 1;
  else{
    long double y=1;
    do {
      y=y*x;
      x = x-1;
    }while (x > 0);
    return y;
  }
}

long double ffact(long double x, long double k){
  if (x < 1)
    return 1;
  else if(k ==0){
    return 1;
  }
  else{
    long double u = x;
    long double y=1;
    do {
      y=y*x;
      x = x-1;
    }while (x > u-k);
    return y;
  }
}

long double mfact(long double m[], long double n, long double l){

  long double z = fact(n);
  int   i = 0;
  while (i < l){
    z = z / (fact(m[i]));
    i=i+1;
  }
  return z;
}

long double  Post(long double p[], long double n, int r, long double x){

  long double w[r+1];
  int d = 0;
  while (d<r+1){
    w[d] = p[d];
    d = d+1;
  }

  long double  b = ffact((n-r)*n, x);
  long double  a = mfact(w, n, r);
  long double m[(int) n];


  int j = 1;
  int i = 0;
  while (i < (r+1)){
    while(w[i] > 0){
      m[j-1]= i;
      j=j+1;
      w[i]=w[i]-1;
    }
    i=i+1;
  }
  long double c = mfact(m, x, n);
  int l= 0;
  while (l<n){
    l=l+1;
  }
  int k = 0;
  while (k<n){
    b = b / ffact(n-r, m[k]);
    k=k+1;
  }
  return (a*c)/b;
}

void printlist(long double p[], int r){
  int i = 0;
  printf("(");
  while (i < r+1){
    printf(" %Lf ", p[i]);
    i =i+1;
  }
    printf(")\n");
}

long double  z(long doublep[], long double n, long double r, long doublex){

}
