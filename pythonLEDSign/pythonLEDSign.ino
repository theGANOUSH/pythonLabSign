#include <font_5x4.h>
#include <HT1632.h>
#include <images.h>

int i = 0;
int wd;
int arraySize = 0;
char phrase[50]= "Good Morning";
char temp[50];
boolean serialFlag = false;
int largest = 0;

void setup () 
{
  Serial.begin(9600);
  HT1632.begin(11, 13, 12, 10, 9);
  
  wd = HT1632.getTextWidth(phrase, FONT_5X4_WIDTH, FONT_5X4_HEIGHT);
}

void loop () 
{
  int j = 0;
  while(Serial.available())
  {
    if(Serial.available() > 0)
    {
      delay(3);
      serialFlag = true;
      phrase[j] = Serial.read();
      j++;
    }
  }
  
  if(serialFlag)
  {
    //memset(phrase, (char)0, sizeof(phrase));
    //temp.toCharArray(phrase, 50);
    for(j; j< 50; j++)
    {
      phrase[j] = (char)0;
    }
    
    wd = HT1632.getTextWidth(phrase, FONT_5X4_WIDTH, FONT_5X4_HEIGHT);
    
    Serial.println(wd);
  
    j = 0;
    serialFlag = false;
    
    wd = HT1632.getTextWidth(phrase, FONT_5X4_WIDTH, FONT_5X4_HEIGHT);
  
  }
  
  //if( i >= largest)
  //{
    //largest = i;
  //}
  
  //Serial.println(largest);
  
  HT1632.drawTarget(BUFFER_BOARD(1));
  HT1632.clear();
  HT1632.drawText(phrase, 3*OUT_SIZE - i, 2, FONT_5X4, FONT_5X4_WIDTH, FONT_5X4_HEIGHT, FONT_5X4_STEP_GLYPH);
  HT1632.render();
  
  HT1632.drawTarget(BUFFER_BOARD(2));
  HT1632.clear();
  HT1632.drawText(phrase, 2*OUT_SIZE - i, 2, FONT_5X4, FONT_5X4_WIDTH, FONT_5X4_HEIGHT, FONT_5X4_STEP_GLYPH);
  HT1632.render();
  
  HT1632.drawTarget(BUFFER_BOARD(3));
  HT1632.clear();
  HT1632.drawText(phrase, OUT_SIZE - i, 2, FONT_5X4, FONT_5X4_WIDTH, FONT_5X4_HEIGHT, FONT_5X4_STEP_GLYPH);
  HT1632.render();
  

  
  i = (i+1)%(wd + OUT_SIZE * 3);
  
  delay(100);
}
