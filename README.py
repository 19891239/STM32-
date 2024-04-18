/*
  *112 CSVS 011024 學習歷程
*/
#include "main.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"
#include <math.h>
static unsigned char V[]={0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xD8,0x80,0x98};
void SystemClock_Config(void);
float sq_val=0.0;
int main(void){
	unsigned short scanPin [3]={GPIO_PIN_0,GPIO_PIN_1,GPIO_PIN_2};
  unsigned short valueInput=0;
	unsigned int count_i[3]={0,0,0};
	unsigned long count_time=0;
	unsigned char pattern,bitSet,bitReset;
	unsigned char stat=0;
	unsigned char stat1=0;
	unsigned char stat2=0;
	unsigned char stat3=0;
	unsigned char valueInput1=0;
	unsigned short valueInput2=0;
	unsigned char valueInput3=0;
	unsigned char valueInput31=0;
	unsigned char valueInput32=0;
	unsigned char valueInput33=0;
	unsigned char valueInput4=0;
	unsigned char valueInput41=0;
	unsigned char valueInput42=0;
	unsigned char valueInput43=0;
	unsigned char valueInput5=0;
	unsigned char valueInput51=0;
	unsigned char valueInput52=0;
	unsigned char valueInput53=0;
	unsigned char valueInput6=0;
	unsigned char valueInput61=0;
	unsigned char valueInput62=0;
	int value_temp=0;
	char i;
	double valueInput63;
	int in_ans;
	double ans;
	int16_t pulseWidth =0;
	int16_t step =0;
  HAL_Init();
  SystemClock_Config();
  MX_GPIO_Init();
  MX_USART2_UART_Init();
  MX_TIM2_Init();
	HAL_TIM_PWM_Start(&htim2,TIM_CHANNEL_1);
	HAL_Delay(450);
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_4|GPIO_PIN_5|GPIO_PIN_10,1);
	HAL_Delay(450);
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_9,1);
	HAL_GPIO_WritePin(GPIOC,GPIO_PIN_4|GPIO_PIN_5,0);
	HAL_Delay(450);
  while (1){
		HAL_GPIO_WritePin(GPIOB,GPIO_PIN_6,1);
		HAL_GPIO_WritePin(GPIOB,GPIO_PIN_7,1);
		HAL_GPIO_WritePin(GPIOB,GPIO_PIN_8,1);
		HAL_GPIO_WritePin(GPIOC,GPIO_PIN_11,1);
		if(pulseWidth==0)step=9000;
		if(pulseWidth==10000)step=-1000;
		pulseWidth=step;
		TIM2->CCR1=pulseWidth ;
		if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_0)==0){	
			if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_1)==0)	{
				if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_2)==0){
					if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
						HAL_GPIO_WritePin(GPIOC,GPIO_PIN_11,0);
						HAL_GPIO_WritePin(GPIOC,GPIO_PIN_1|GPIO_PIN_3|GPIO_PIN_4|GPIO_PIN_5|GPIO_PIN_6|GPIO_PIN_7|GPIO_PIN_8|GPIO_PIN_9,GPIO_PIN_RESET);
					}else if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==0){
						HAL_GPIO_WritePin(GPIOC,GPIO_PIN_11,0);
						HAL_GPIO_WritePin(GPIOC,GPIO_PIN_2|GPIO_PIN_3|GPIO_PIN_4|GPIO_PIN_5|GPIO_PIN_6|GPIO_PIN_7|GPIO_PIN_8|GPIO_PIN_9,GPIO_PIN_RESET);
					}else if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
						HAL_GPIO_WritePin(GPIOC,GPIO_PIN_11,0);
						HAL_GPIO_WritePin(GPIOC,GPIO_PIN_0|GPIO_PIN_3|GPIO_PIN_4|GPIO_PIN_5|GPIO_PIN_6|GPIO_PIN_7|GPIO_PIN_8|GPIO_PIN_9,GPIO_PIN_RESET);
					}else{
						HAL_GPIO_WritePin(GPIOC,GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_2,1);	
					}
				 }
		   }
		 }	
		if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_0)==0){
			if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_1)==0){
				if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_2)==1){
						HAL_GPIO_WritePin(GPIOB,GPIO_PIN_6,0);
						HAL_GPIO_WritePin(GPIOC,scanPin[1],GPIO_PIN_SET);
						pattern=V[8];
						bitSet=pattern;
						bitReset=~pattern;
						HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
						HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
						HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_RESET);
						HAL_Delay(1);
						HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_SET);
						HAL_GPIO_WritePin(GPIOC,scanPin[1],GPIO_PIN_SET);
						pattern=V[8];
						bitSet=pattern;
						bitReset=~pattern;
						HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
						HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
						HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_RESET);
						for(int i=0;i<1000;i++){__NOP();}
						HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_SET);
				}
			}
		}if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_0)==0){
					if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_1)==1){
						if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_2)==0){
							HAL_GPIO_WritePin(GPIOB,GPIO_PIN_6,0);
							HAL_GPIO_WritePin(GPIOB,GPIO_PIN_7,0);
							if(stat==0){
								if(valueInput>99){
									valueInput-=100;
								}
								value_temp=valueInput;
								count_i[1]=value_temp/10;
								value_temp=value_temp-count_i[1]*10;
								count_i[0]=value_temp;
								HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_SET);	
								for(i=0;i<2;i++){
									pattern=V[count_i[i]];
									bitSet=pattern;
									bitReset=~pattern;
									HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
									HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
									HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_RESET);
									HAL_Delay(1);
									HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_SET);
								}
							}else{
								value_temp=in_ans;
								count_i[2]=value_temp/100;
								value_temp=value_temp-count_i[2]*100;
								count_i[1]=value_temp/10;
								value_temp=value_temp-count_i[1]*10;
								count_i[0]=value_temp;
								for(i=0;i<3;i++){if (i==2){
										pattern=V[count_i[i]] & 0b01111111;
									}else{
										pattern=V[count_i[i]];
									}
									bitSet=pattern;
									bitReset=~pattern;
									HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
									HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
									HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_RESET);
									HAL_Delay(1);
									HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_SET);
								}
							}if(stat1==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
									stat1=1;
									count_time=HAL_GetTick();
								}
							}else if(stat1==1){
								if((HAL_GetTick()-count_time)>30){
									stat1=2;
								}
							}else if(stat1==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
									stat1=3;
									stat=0;
									valueInput++;
								}else{
									stat1=1;
									count_time=HAL_GetTick();
								}
							}else if(stat1==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1){
									stat1=4;
								}
							}else if(stat1==4){
								if((HAL_GetTick()-count_time)>30){
									stat1=5;
								}
							}else if(stat1==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1){
									stat1=0;
								}else{
									stat1=4;
									count_time=HAL_GetTick();
								}
							}
							if(stat2==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==0){
									stat2=1;
									count_time=HAL_GetTick();
								}
							}	else if(stat2==1){
								if((HAL_GetTick()-count_time)>30){
									stat2=2;
								}
							}else if(stat2==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==0){
									stat2=3;
									valueInput+=10;
									stat=0;
								}else{
									stat2=1;
									count_time=HAL_GetTick();
								}
							}else if(stat2==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==1){
									stat2=4;
								}
							}else if(stat2==4){
								if((HAL_GetTick()-count_time)>30){
									stat2=5;
								}
							}else if(stat2==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==1){
									stat2=0;
								}else{
									stat2=4;
									count_time=HAL_GetTick();
								}
							}
							if(stat3==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
									stat3=1;
									count_time=HAL_GetTick();
								}
							}	else if(stat3==1){
								if((HAL_GetTick()-count_time)>30){
									stat3=2;
								}
							}else if(stat3==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
									stat3=3;
									stat=1;	
									ans=sqrt(valueInput);
									in_ans=ans*100;
								}else{
									stat3=1;
									count_time=HAL_GetTick();
								}
							}else if(stat3==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
									stat3=4;
								}
							}else if(stat3==4){
								if((HAL_GetTick()-count_time)>30){
									stat3=5;
								}
							}else if(stat3==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
									stat3=0;
								}else{
									stat3=4;
									count_time=HAL_GetTick();
								}
							}
						}else{
							HAL_GPIO_WritePin(GPIOC,GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_2,1);
						}
					}else{
						HAL_GPIO_WritePin(GPIOC,GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_2,1);
					}
				}else{
			HAL_GPIO_WritePin(GPIOC,GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_2,1);
		}
		if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_0)==0){
			if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_1)==1){
				if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_2)==1){
					HAL_GPIO_WritePin(GPIOB,GPIO_PIN_7,0);
					if(stat==0){
						count_i[0]=valueInput1;
						HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_SET);
				  	HAL_GPIO_WritePin(GPIOC,scanPin[1],GPIO_PIN_SET);								
						pattern=V[count_i[0]];
						bitSet=pattern;
						bitReset=~pattern;
						HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
						HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
						HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_RESET);
						HAL_Delay(1);
						HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_SET);
					}else{
							value_temp=valueInput2;
							count_i[2]=value_temp/100;
							value_temp=value_temp-count_i[2]*100;
							count_i[1]=value_temp/10;
							value_temp=value_temp-count_i[1]*10;
						  count_i[0]=value_temp;
							for(i=0;i<3;i++){
								pattern=V[count_i[i]];
								bitSet=pattern;
								bitReset=~pattern;
								HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
								HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
								HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_RESET);
								HAL_Delay(1);
								HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_SET);
							}
						}
						if(stat1==0){
							if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
								stat1=1;
								count_time=HAL_GetTick();
							}
						}	else if(stat1==1){
							if((HAL_GetTick()-count_time)>30){
								stat1=2;
							}
						}else if(stat1==2){
							if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
								stat1=3;
								stat=0;
								valueInput1++;
								if(valueInput1>6){
									valueInput1=1;
								}
							}else{
								stat1=1;
								count_time=HAL_GetTick();
							}
						}else if(stat1==3){
							if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1){
								stat1=4;
							}
						}else if(stat1==4){
							if((HAL_GetTick()-count_time)>30){
								stat1=5;
							}
						}else if(stat1==5){
							if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1){
								stat1=0;
							}else{
								stat1=4;
								count_time=HAL_GetTick();
							}
						}
						if(stat3==0){
							if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
								stat3=1;
								count_time=HAL_GetTick();
							}
						}else if(stat3==1){
							if((HAL_GetTick()-count_time)>30){
								stat3=2;
							}
						}else if(stat3==2){
							if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
								stat3=3;
								stat=1;
                if(valueInput1==1){
									valueInput2=1;
								}else if(valueInput1==2){
									valueInput2=2;
								}else if(valueInput1==3){
									valueInput2=6;
								}else if(valueInput1==4){
									valueInput2=24;
								}else if(valueInput1==5){
									valueInput2=120;
								}else if(valueInput1==6){
									valueInput2=720;
								}
							}else{
							  stat3=1;
							  count_time=HAL_GetTick();
						  }
						}else if(stat3==3){
							if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
								stat3=4;
							}
						}else if(stat3==4){
							if((HAL_GetTick()-count_time)>30){
								stat3=5;
							}
						}else if(stat3==5){
							if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
								stat3=0;
							}else{
								stat3=4;
								count_time=HAL_GetTick();
							}
						}
					}
				}
			}
		if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_0)==1){
			if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_1)==0){
				if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_2)==0){
					HAL_GPIO_WritePin(GPIOB,GPIO_PIN_8,0);
					HAL_GPIO_WritePin(GPIOB,GPIO_PIN_7,0);
						if(stat==0){
								if(valueInput31>9){
									valueInput31=0;
								}
								if(valueInput32>9){
									valueInput32=0;
								}
								HAL_GPIO_WritePin(GPIOC,scanPin[1],GPIO_PIN_SET);	
								pattern=V[valueInput31];
								bitSet=pattern;
								bitReset=~pattern;
								HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
								HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
								HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_RESET);
								HAL_Delay(1);
								HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_SET);
								pattern=V[valueInput32];
								bitSet=pattern;
								bitReset=~pattern;
								HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
								HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
								HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_RESET);
								HAL_Delay(1);
								HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_SET);
							}else{
								value_temp=valueInput33;
								count_i[2]=value_temp/100;
								value_temp=value_temp-count_i[2]*100;
								count_i[1]=value_temp/10;
								value_temp=value_temp-count_i[1]*10;
								count_i[0]=value_temp;
								for(i=0;i<3;i++){
									pattern=V[count_i[i]];
									bitSet=pattern;
									bitReset=~pattern;
									HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
									HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
									HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_RESET);
									HAL_Delay(1);
									HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_SET);
								}
							}
							if(stat1==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
									stat1=1;
									count_time=HAL_GetTick();
								}
							}else if(stat1==1){
								if((HAL_GetTick()-count_time)>30){
									stat1=2;
								}
							}else if(stat1==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
									stat1=3;
									stat=0;
									valueInput31++;
								}else{
									stat1=1;
									count_time=HAL_GetTick();
								}
							}else if(stat1==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1){
									stat1=4;
								}
							}else if(stat1==4){
								if((HAL_GetTick()-count_time)>30){
									stat1=5;
								}
							}else if(stat1==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1){
									stat1=0;
								}else{
									stat1=4;
									count_time=HAL_GetTick();
								}
							}
							if(stat2==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==0){
									stat2=1;
									count_time=HAL_GetTick();
								}
							}	else if(stat2==1){
								if((HAL_GetTick()-count_time)>30){
									stat2=2;
								}
							}else if(stat2==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==0){
									stat2=3;
									valueInput32++;
									stat=0;
								}else{
									stat2=1;
									count_time=HAL_GetTick();
								}
							}else if(stat2==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==1){
									stat2=4;
								}
							}else if(stat2==4){
								if((HAL_GetTick()-count_time)>30){
									stat2=5;
								}
							}else if(stat2==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==1){
									stat2=0;
								}else{
									stat2=4;
									count_time=HAL_GetTick();
								}
							}
							if(stat3==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
									stat3=1;
									count_time=HAL_GetTick();
								}
							}else if(stat3==1){
								if((HAL_GetTick()-count_time)>30){
									stat3=2;
								}
							}else if(stat3==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
									stat3=3;
									stat=1;
									valueInput33=valueInput31+valueInput32;
								}else{
									stat3=1;
									count_time=HAL_GetTick();
								}
							}else if(stat3==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
									stat3=4;
								}
							}else if(stat3==4){
								if((HAL_GetTick()-count_time)>30){
									stat3=5;
								}
							}else if(stat3==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
									stat3=0;
								}else{
									stat3=4;
									count_time=HAL_GetTick();
								}
							}
				}
			}
		}
		if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_0)==1){
			if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_1)==0){
				if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_2)==1){
					HAL_GPIO_WritePin(GPIOB,GPIO_PIN_8,0);
						if(stat==0){
								if(valueInput41>9){
									valueInput41=0;
								}
								if(valueInput42>9){
									valueInput42=0;
								}
								HAL_GPIO_WritePin(GPIOC,scanPin[1],GPIO_PIN_SET);	
								pattern=V[valueInput41];
								bitSet=pattern;
								bitReset=~pattern;
								HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
								HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
								HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_RESET);
								HAL_Delay(1);
								HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_SET);
								pattern=V[valueInput42];
								bitSet=pattern;
								bitReset=~pattern;
								HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
								HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
								HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_RESET);
								HAL_Delay(1);
								HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_SET);
							}else{
								if(valueInput41>=valueInput42){
									valueInput43=valueInput41-valueInput42;
									HAL_GPIO_WritePin(GPIOC,scanPin[1],GPIO_PIN_SET);
								}else{
									valueInput43=valueInput42-valueInput41;
									pattern=0b10111111;
									bitSet=pattern;
									bitReset=~pattern;
									HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
									HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
									HAL_GPIO_WritePin(GPIOC,scanPin[1],GPIO_PIN_RESET);
									HAL_Delay(1);
									HAL_GPIO_WritePin(GPIOC,scanPin[1],GPIO_PIN_SET);
								}
								  count_i[0]=valueInput43;
									HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_SET);
									pattern=V[count_i[0]];
									bitSet=pattern;
									bitReset=~pattern;
									HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
									HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
									HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_RESET);
									HAL_Delay(1);
									HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_SET);
							}
							if(stat1==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
									stat1=1;
									count_time=HAL_GetTick();
								}
							}else if(stat1==1){
								if((HAL_GetTick()-count_time)>30){
									stat1=2;
								}
							}else if(stat1==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
									stat1=3;
									stat=0;
									valueInput41++;
								}else{
									stat1=1;
									count_time=HAL_GetTick();
								}
							}else if(stat1==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1){
									stat1=4;
								}
							}else if(stat1==4){
								if((HAL_GetTick()-count_time)>30){
									stat1=5;
								}
							}else if(stat1==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1){
									stat1=0;
								}else{
									stat1=4;
									count_time=HAL_GetTick();
								}
							}
							if(stat2==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==0){
									stat2=1;
									count_time=HAL_GetTick();
								}
							}else if(stat2==1){
								if((HAL_GetTick()-count_time)>30){
									stat2=2;
								}
							}else if(stat2==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==0){
									stat2=3;
									valueInput42++;
									stat=0;
								}else{
									stat2=1;
									count_time=HAL_GetTick();
								}
							}
							else if(stat2==3)
							{
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==1)
								{
									stat2=4;
								}
							}else if(stat2==4){
								if((HAL_GetTick()-count_time)>30){
									stat2=5;
								}
							}else if(stat2==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==1){
									stat2=0;
								}else{
									stat2=4;
									count_time=HAL_GetTick();
								}
							}
							if(stat3==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
									stat3=1;
									count_time=HAL_GetTick();
								}
							}else if(stat3==1)
							{
								if((HAL_GetTick()-count_time)>30)
								{
									stat3=2;
								}
							}else if(stat3==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
									stat3=3;
									stat=1;
									valueInput43=valueInput31-valueInput42;
								}else{
									stat3=1;
									count_time=HAL_GetTick();
								}
							}else if(stat3==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
									stat3=4;
								}
							}else if(stat3==4){
								if((HAL_GetTick()-count_time)>30){
									stat3=5;
								}
							}else if(stat3==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
									stat3=0;
								}else{
									stat3=4;
									count_time=HAL_GetTick();
								}
							}
				}
			}
		}
		if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_0)==1){
			if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_1)==1){
				if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_2)==0){
					HAL_GPIO_WritePin(GPIOB,GPIO_PIN_6,0);
					HAL_GPIO_WritePin(GPIOB,GPIO_PIN_8,0);
						if(stat==0){
								if(valueInput51>9){
									valueInput51=0;
								}
								if(valueInput52>9){
									valueInput52=0;
								}
								HAL_GPIO_WritePin(GPIOC,scanPin[1],GPIO_PIN_SET);	
								pattern=V[valueInput51];
								bitSet=pattern;
								bitReset=~pattern;
								HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
								HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
								HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_RESET);
								HAL_Delay(1);
								HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_SET);
								pattern=V[valueInput52];
								bitSet=pattern;
								bitReset=~pattern;
								HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
								HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
								HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_RESET);
								HAL_Delay(1);
								HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_SET);
						}else{  
								value_temp=valueInput53;
								count_i[2]=value_temp/100;
								value_temp=value_temp-count_i[2]*100;
								count_i[1]=value_temp/10;
								value_temp=value_temp-count_i[1]*10;
								count_i[0]=value_temp;
								for(i=0;i<3;i++){
									pattern=V[count_i[i]];
									bitSet=pattern;
									bitReset=~pattern;
									HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
									HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
									HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_RESET);
									HAL_Delay(1);
									HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_SET);
								}
							 }
							if(stat1==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
									stat1=1;
									count_time=HAL_GetTick();
								}
							}else if(stat1==1){
								if((HAL_GetTick()-count_time)>30){
									stat1=2;
								}
							}else if(stat1==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
									stat1=3;
									stat=0;
									valueInput51++;
								}else{
									stat1=1;
									count_time=HAL_GetTick();
								}
							}else if(stat1==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1){
									stat1=4;
								}
							}else if(stat1==4){
								if((HAL_GetTick()-count_time)>30){
									stat1=5;
								}
							}else if(stat1==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1){
									stat1=0;
								}
								else{
									stat1=4;
									count_time=HAL_GetTick();
								}
							}
							if(stat2==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==0){
									stat2=1;
									count_time=HAL_GetTick();
								}
							}else if(stat2==1){
								if((HAL_GetTick()-count_time)>30){
									stat2=2;
								}
							}else if(stat2==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==0){
									stat2=3;
									valueInput52++;
									stat=0;
								}else{
									stat2=1;
									count_time=HAL_GetTick();
								}
							}else if(stat2==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==1){
									stat2=4;
								}
							}else if(stat2==4)
							{
								if((HAL_GetTick()-count_time)>30){
									stat2=5;
								}
							}else if(stat2==5)
							{
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==1){
									stat2=0;
								}else{
									stat2=4;
									count_time=HAL_GetTick();
								}
							}
							if(stat3==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
									stat3=1;
									count_time=HAL_GetTick();
								}
							}else if(stat3==1){
								if((HAL_GetTick()-count_time)>30){
									stat3=2;
								}
							}else if(stat3==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0)
								{
									stat3=3;
									stat=1;
									valueInput53=valueInput51*valueInput52;
								}else{
									stat3=1;
									count_time=HAL_GetTick();
								}
							}else if(stat3==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
									stat3=4;
								}
							}else if(stat3==4){
								if((HAL_GetTick()-count_time)>30){
									stat3=5;
								}
							}else if(stat3==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
									stat3=0;
								}else{
									stat3=4;
									count_time=HAL_GetTick();
								}
							}
				}
			}
		}
		if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_0)==1){
			if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_1)==1){
				if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_2)==1){
					HAL_GPIO_WritePin(GPIOB,GPIO_PIN_6,0);
					HAL_GPIO_WritePin(GPIOB,GPIO_PIN_7,0);
					HAL_GPIO_WritePin(GPIOB,GPIO_PIN_8,0);
						if(stat==0){
							if(valueInput61>9){
									valueInput61=0;
								}
								if(valueInput62>9){
									valueInput62=0;
								}
								HAL_GPIO_WritePin(GPIOC,scanPin[1],GPIO_PIN_SET);	
								pattern=V[valueInput61];
								bitSet=pattern;
								bitReset=~pattern;
								HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
								HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
								HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_RESET);
								HAL_Delay(1);
								HAL_GPIO_WritePin(GPIOC,scanPin[2],GPIO_PIN_SET);
								pattern=V[valueInput62];
								bitSet=pattern;
								bitReset=~pattern;
								HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
								HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
								HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_RESET);
								HAL_Delay(1);
								HAL_GPIO_WritePin(GPIOC,scanPin[0],GPIO_PIN_SET);
							}else{
								value_temp=valueInput63;
								count_i[2]=value_temp/100;
								value_temp=value_temp-count_i[2]*100;
								count_i[1]=value_temp/10;
								value_temp=value_temp-count_i[1]*10;
								count_i[0]=value_temp;	
								for(i=0;i<3;i++){
									if(valueInput62==0){
										pattern=0b10111111;
									}else{
										if (i==2){
											pattern=V[count_i[i]] & 0b01111111;
										}else{
											pattern=V[count_i[i]];
										}
									}
									bitSet=pattern;
									bitReset=~pattern;
									HAL_GPIO_WritePin(GPIOC,bitSet<<3,GPIO_PIN_SET);
									HAL_GPIO_WritePin(GPIOC,bitReset<<3,GPIO_PIN_RESET);
									HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_RESET);
									HAL_Delay(1);
									HAL_GPIO_WritePin(GPIOC,scanPin[i],GPIO_PIN_SET);
								}
							}
							if(stat1==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0){
									stat1=1;
									count_time=HAL_GetTick();
								}
							}	
							else if(stat1==1)
							{
								if((HAL_GetTick()-count_time)>30)
								{
									stat1=2;
								}
							}
							else if(stat1==2)
							{
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==0)
								{
									stat1=3;
									stat=0;
									valueInput61++;
								}
								else{
									stat1=1;
									count_time=HAL_GetTick();
								}
							}
							else if(stat1==3)
							{
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1)
								{
									stat1=4;
								}
							}
							else if(stat1==4)
							{
								if((HAL_GetTick()-count_time)>30)
								{
									stat1=5;
								}
							}else if(stat1==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3)==1){
									stat1=0;
								}else{
									stat1=4;
									count_time=HAL_GetTick();
								}
							}
							if(stat2==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==0){
									stat2=1;
									count_time=HAL_GetTick();
								}
							}else if(stat2==1){
								if((HAL_GetTick()-count_time)>30){
									stat2=2;
								}
							}else if(stat2==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==0)
								{
									stat2=3;
									valueInput62++;
									stat=0;
								}
								else{
									stat2=1;
									count_time=HAL_GetTick();
								}
							}else if(stat2==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==1){
									stat2=4;
								}
							}else if(stat2==4){
								if((HAL_GetTick()-count_time)>30){
									stat2=5;
								}
							}else if(stat2==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_4)==1){
									stat2=0;
								}else{
									stat2=4;
									count_time=HAL_GetTick();
								}
							}if(stat3==0){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
									stat3=1;
									count_time=HAL_GetTick();
								}
							}	else if(stat3==1){
								if((HAL_GetTick()-count_time)>30){
									stat3=2;
								}
							}else if(stat3==2){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==0){
									stat3=3;
									stat=1;
									if(valueInput62!=0){
										valueInput63=(float)((float)valueInput61/(float)valueInput62)*100.0;
									}
								}else{
									stat3=1;
									count_time=HAL_GetTick();
								}
							}else if(stat3==3){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
									stat3=4;
								}
							}else if(stat3==4){
								if((HAL_GetTick()-count_time)>30)
								{
									stat3=5;
								}
							}else if(stat3==5){
								if(HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_5)==1){
									stat3=0;
								}else{
									stat3=4;
									count_time=HAL_GetTick();
								}
							}
				}
			}
		}
  }
}
void SystemClock_Config(void){
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
  RCC_PeriphCLKInitTypeDef PeriphClkInit = {0};
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLLMUL_8;
  RCC_OscInitStruct.PLL.PLLDIV = RCC_PLLDIV_2;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK){
    Error_Handler();
  }
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;
  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_1) != HAL_OK){
    Error_Handler();
  }
  PeriphClkInit.PeriphClockSelection = RCC_PERIPHCLK_USART2;
  PeriphClkInit.Usart2ClockSelection = RCC_USART2CLKSOURCE_PCLK1;
  if (HAL_RCCEx_PeriphCLKConfig(&PeriphClkInit) != HAL_OK){
    Error_Handler();
  }
}
void Error_Handler(void){
  __disable_irq();
  while (1){
  }
}
#ifdef  USE_FULL_ASSERT
#endif /* USE_FULL_ASSERT */
