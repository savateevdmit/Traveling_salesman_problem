int val;
int LED = 13;
float x = 254;
float y = 254;
float last_x = 0;
float last_y = 0;
float new_x = 0;
float new_y = 0;
float a = 0;
float last_a = 0;
float new_a = 0;
float distance = 1;

void setup()
{
  pinMode(2, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(6, OUTPUT);
  Serial.begin(9600);

  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);
}

void backward(float distance)
{
  digitalWrite(2, HIGH);
  analogWrite(5, 127.5);
  digitalWrite(4, LOW);
  analogWrite(6, 136.5);
  delay(674.592 * ((distance * 66.67) / 100));

  digitalWrite(2, HIGH);
  analogWrite(5, 127.5);
  digitalWrite(4, LOW);
  analogWrite(6, 127.5);
  delay(674.592 * ((distance * 33.33) / 100));  

  Serial.print("backward ");
  Serial.println(distance);
}

void forward(float distance)
{ 
  digitalWrite(2, HIGH);
  analogWrite(5, 127.5);
  digitalWrite(4, LOW);
  analogWrite(6, 136.5);
  delay(674.592 * ((distance * 66.67) / 100));

  digitalWrite(2, HIGH);
  analogWrite(5, 127.5);
  digitalWrite(4, LOW);
  analogWrite(6, 127.5);
  delay(674.592 * ((distance * 33.33) / 100));  

  Serial.print("forward ");
  Serial.println(distance);
  
}

void left(float new_a)
{
  digitalWrite(2, LOW);
  analogWrite(5, 127.5);
  digitalWrite(4, LOW);
  analogWrite(6, 136.5);

  Serial.print("left ");
  Serial.println(new_a);

  delay(4.9 * new_a);
}

void right(float new_a)
{
  digitalWrite(2, HIGH);
  analogWrite(5, 127.5);
  digitalWrite(4, HIGH);
  analogWrite(6, 136.5);

  Serial.print("right ");
  Serial.println(new_a);

  delay(4.9 * new_a);
}

void stop()
{
  digitalWrite(2, LOW);
  analogWrite(5, 0);
  digitalWrite(4, LOW);
  analogWrite(6, 0);
  delay(2000);
  Serial.println("stop ");
}

void loop()
{
  if (Serial.available())
  {
    val = Serial.read();
    Serial.println(val);
    if (x == 254)
    {
      x = val;
    }

    else if (y == 254)
    {
      y = val;
      new_x = x - last_x;
      new_y = y - last_y;
      // Serial.println(x);
      // Serial.println(last_x);
      // Serial.println(new_x);

      // Serial.println(y);
      // Serial.println(last_y);
      // Serial.println(new_y);

      if (new_x >= 0 && new_y >= 0){  // 1
        // Serial.println(new_x);   
        // Serial.println(new_y);

        // Serial.println(new_x/new_y);
        // Serial.println(atan(new_x/new_y));
        // Serial.println(degrees(atan(new_x/new_y)));
        a = abs(degrees(atan(new_x/new_y)));
        float distance = sqrtf(square(new_x) + square(new_y));
        if (a > last_a){
          new_a = a - last_a;
          right(new_a);
        }

        else if (a == 0 || a != a){
          right(0);
          last_a = 0;
        }

        else {
          Serial.println(last_a);   
          Serial.println(a);
          new_a = last_a - a;
          left(new_a);
        }

        stop();
        forward(distance);
        stop();
        stop();
        // left(a);
      }
      
      else if (new_x >= 0 && new_y <= 0){ // 4
        a = abs(180 - degrees(atan(new_x/new_y)));
        float distance = sqrtf(square(new_x) + square(new_y));    

        if (a > last_a){
          new_a = a - last_a;
          right(new_a);
        }
        
        else if (a == 0){
          right(0);
        }

        else {
          new_a = last_a - a;
          left(new_a);
        }
          
        stop();
        forward(distance);
        stop();
        stop();
        // left(a);
      }

      else if (new_x <= 0 && new_y >= 0){ // 2
        // Serial.println("2");
        a = abs(degrees(atan(new_x/new_y)));
        float distance = sqrtf(square(new_x) + square(new_y));   

        if (a > last_a){
          new_a = a + last_a;
          left(new_a);
        }
        
        else if (a == 0){
          right(0);
        }

        else {
          new_a = last_a + a;
          right(new_a);
        }
          
        stop();
        forward(distance);
        stop();
        stop();
        // right(a);
      }

      else if (new_x <= 0 && new_y <= 0){ // 3
        a = abs(180 - degrees(atan(new_x/new_y)));
        float distance = sqrtf(square(new_x) + square(new_y));    
        
        if (a > last_a){
          new_a = a + last_a;
          left(new_a);
        }
        
        else if (a == 0){
          right(0);
        }

        else {
          new_a = last_a + a;
          right(new_a);
        }

        stop();
        forward(distance);
        stop();
        stop();
        // right(a);
      }

      last_x = x;
      last_y = y;

      if (a != a){
          last_a = 0;
        }
      else {
        last_a = a;
      }

      x = 254;
      y = 254;
    }
  }

  else{
    stop();
  }
}