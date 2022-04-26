/*
 * Arduino program to control a model train running a point to point layout with the help of feedback sensors.
 * 
 * Made by Tech Build: https://www.youtube.com/channel/UCNy7DyfhSD9jsQEgNwETp9g?sub_confirmation=1
 * 
 * Feel free to tinker with the code and customize it for your own layout. :)
 */
int s;

int ta = 2;/*Integer variable to store time delay of the train between crossing the 'sensored' track and stopping at point A.*/

int tb = 2;/*Integer variable to store time delay of the train between crossing the 'sensored' track and stopping at point B.*/

int sa = 5;/*Integer variable to store how long will the train stop at station A(in seconds).*/

int sb = 5;/*Integer variable to store how long will the train stop at station B(in seconds).*/

int MidSpeed = 50;/*Integer variable to store the train's initial speed(when leaving or arriving at the station).*/

int MaxSpeed = 90;/*Integer variable to store the train's maximum speed(after leaving the station).*/

#define A 7 
#define B 8 
#define EN 9 

void motor_go(){
 if(s>=1&&s<=255){
  digitalWrite(B,LOW);
  digitalWrite(A,HIGH);
  analogWrite(EN,s);
 }
 if(s<=-1&&s>=-255){
  digitalWrite(A,LOW);
  digitalWrite(B,HIGH);
  analogWrite(EN,-s);
 }
 if(s==0){
  digitalWrite(B,LOW);
  digitalWrite(A,LOW);
  analogWrite(EN,s);
 }
}
void setup() {
  /* put your setup code here, to run once:*/
  
  pinMode(A,OUTPUT);
  pinMode(B,OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
}

void loop() {
      /*
       * The train will start from point A to proceed towards point B.
       */
      for(s=0;s<=10;s++){/*Applying low-voltage across the track rails to make the train's lights turn on(This might not work for all trains!).*/
        motor_go();
        delay(60);
      }

      delay(1000);//Waiting for a second.

      for(s=s;s<=MidSpeed;s++){/*Starting the train from the station at point A.*/
        motor_go();
        delay(250);
      }

      while(digitalRead(A0)!=HIGH);/*The train will keep moving at the set 'MidSpeed' until crossing the 'sensored' track.*/

      for(s=s;s<=MaxSpeed;s++){/*Increasing the speed of the train.*/
        motor_go();
        delay(250);
      }

      while(digitalRead(A1)!=HIGH);/*The train will keep moving at the set 'MaxSpeed' until crossing the next 'sensored' track.*/

      for(s=s;s!=MidSpeed;s--){/*Reducing the speed of the train.*/
        motor_go();
        delay(125);
      }

      delay(tb*1000);/*Wait for set amount of time(in seconds) before stopping the train at the station at point B.*/

      for(s=s;s!=10;s--){/*Bring it to a halt, keeping the lights turned on(This might not work for all trains!).*/
        motor_go();
        delay(250);/*You can increase the value of the number in the parenthesis() to make the locomotive slow down more gradually.*/
      }

      delay(1000);/*Wait for a second.*/

      for(s=s;s!=0;s--){
        motor_go();
        delay(60);
      }

      delay(5000);/*Wait for set amount of time at the station before starting again.*/ 
      /*
       * The train will now start to go back to point A the same way it went from point A to B.
       */
      for(s=s;s!=-10;s--){
        motor_go();
        delay(60);
      }

      delay(1000);

      for(s=s;s!=-MidSpeed;s--){
        motor_go();
        delay(250);
      }

      while(digitalRead(A1)!=HIGH);

      for(s=s;s!=-MaxSpeed;s--){
        motor_go();
        delay(125);
      }

      digitalWrite(25, HIGH);

      while(digitalRead(A0)!=HIGH);

      digitalWrite(25, LOW);

      for(s=s;s<=-MidSpeed;s++){
        motor_go();
        delay(125);
      }

      delay(ta*1000);

      for(s=s;s<=-10;s++){
        motor_go();
        delay(125);/*You can increase the value of the number in the parenthesis() to make the locomotive slow down more gradually.*/
      }

      delay(1000);

      for(s=s;s<=0;s++){
        motor_go();
        delay(60);
      }

      delay(5000);
      
}
