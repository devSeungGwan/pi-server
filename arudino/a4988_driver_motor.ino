#define SWITCH 12

#define dir 2
#define steps 3

#define ms1 4
#define ms2 5
#define ms3 6      //핀연결

#include <Stepper.h>  // 스텝모터 라이브러리 불러옴

unsigned int val1, val2, val3;  //입력할 변수값 스텝수, 회전속도 딜레이, 회전방향
unsigned int i;     //for문에 사용할 변수

int stepsNum = 2048;
const int startButton= 7; //누르면 시작 버튼
const int left_button_pin = 12;
const int right_button_pin = 13;

boolean startButton_bool;
Stepper block_motor(stepsNum,8,10,9,11); //IN4 IN2 IN3 IN1

void setup(){
  Serial.begin(9600);

  pinMode(steps, OUTPUT);
  pinMode(dir, OUTPUT);
  
  pinMode(startButton, INPUT_PULLUP);
  pinMode(left_button_pin, INPUT_PULLUP);
  pinMode(right_button_pin, INPUT_PULLUP);
  
  pinMode(ms1, OUTPUT);
  pinMode(ms2, OUTPUT);
  pinMode(ms3, OUTPUT);   //신호보낼 핀 출력설정
  
  digitalWrite(ms1, LOW);
  digitalWrite(ms2, LOW);
  digitalWrite(ms3, LOW);    //분주설정

  block_motor.setSpeed(10);
}

boolean btnRight_bool;
boolean btnLeft_bool;

void loop(){
  btnLeft_bool = digitalRead(left_button_pin); 
  btnRight_bool = digitalRead(right_button_pin); 

  // 왼쪽 이동 버튼을 누른 경우
  if(btnLeft_bool == LOW){
    NEMA_btn_move(0);
  }

  // 오른쪽 이동 버튼을 누른 경우
  if(btnRight_bool == LOW){
    NEMA_btn_move(1);
  }

  startButton_bool = digitalRead(startButton);

  /*
  시작 버튼을 눌려 동작하는 아두이노 코드
  */
  // 시작 버튼을 누른 경우
  if(startButton_bool == LOW){

    // 촬영
    for(int i=0;i<5;i++){
      planeMotor_move();
      NEMA_motor_move(500,0);
    }

    // 원위치 이동
    planeMotor_move();
    NEMA_motor_move(2500,1);
  }
}


//가운데 모터 회전
void planeMotor_move(){ 
  for(int i=0;i<4;i++){
    block_motor.step(stepsNum/4);  // steps, 2048로 두면 정회전 한바퀴
    delay(500);
    Serial.println("Capture");
    delay(1000);
  }
}

// 카메라 회전
void NEMA_motor_move(int distance, int direct){
  digitalWrite(dir, direct);      //회전방향 출력

  for(i=0; i<distance; i++){          //정해진 스텝수만큼 펄스입력
      digitalWrite(steps, HIGH);
      delayMicroseconds(1000);          //딜레이값
      digitalWrite(steps, LOW);
      delayMicroseconds(1000);
    }
    delay(3000);
}

// 버튼을 통한 이동
void NEMA_btn_move(int direct){
   digitalWrite(dir, direct);

   digitalWrite(steps, HIGH);
   delayMicroseconds(1000);          //딜레이값
   digitalWrite(steps, LOW);
   delayMicroseconds(1000);
}


/*if(Serial.available()){   //시리얼 입력이 있을경우
    val1=Serial.parseInt();   //스텝수 입력
    val2=Serial.parseInt();   //회전속도를 결정하는 딜레이값 입력(값이 작을수록 회전속도가 빨라짐)
    val3=Serial.parseInt();   //회전방향을 결정하는 입력
*/