CODE	SEGMENT
			ASSUME CS:CODE,DS:CODE,ES:CODE,SS:CODE
		
PPI_C		EQU		1EH
PPIC		EQU		1CH
PPIB		EQU		1AH
PPIA		EQU		18H
			;
		
			ORG		1000H
			MOV		AL,10000000B	;ALL OUTPUT MODE
			OUT		PPIC_C, AL
			;
			MOV 	AL,11111111B
			OUT		PPIC,AL
			;
			MOV		AL,11111111B
			OUT		PPIB,AL
	L1:		MOV 	AL,11111110B
	L2:		OUT		PPIA,AL			;LED ON
	
			CALL	TIMER
			STC
			ROL		AL,1
			JC		L2
			JMP		L1
			;
			INT		3
			;
	TIMER:	MOV		CX,0FFFFH
	TIMER1:	NOP
			NOP
			NOP
			LOOP	TIMER1
			RET
			;
	
	CODE	ENDS
			END
	