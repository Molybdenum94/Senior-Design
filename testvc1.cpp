int function_a(int x, int y){
return x + y;
}
;
int main(){
int x;
x = 10;
if(x != 10){
x = x << 10;
}
x = x & 1;
printf("x: %d", function_a(x,10));
}