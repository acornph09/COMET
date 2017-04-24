CODE	SEGMENT
		ASSUME CS:CODE,DS:CODE,ES:CODE,SS:CODE
		;
STACK	EQU		0540H
LCDC	EQU		00H		
LCDC_S	EQU		02H
LCDD	EQU		04H
KEY		EQU		01H
SPK		EQU		17H
K_BUF	DB		1
		;
		ORG		1000H
		;

		XOR		AX, AX
		MOV		SS, AX
		MOV		SP, STACK
		;
		;	LCD CLEAR
		CALL	ALLCLR
		CALL	ENTMODE
		CALL	CURSOR1
L1: 	CALL	SCAN
		JMP		L1
ALLCLR:	MOV		AH, 01H
		JMP 	LNXX
		;
ENTMODE:
		MOV 	AH, 00000111B
		JMP		LNXX
		;
CURSOR1:MOV 	AH, 09H
LNXX:	;CALL	BUSY
		MOV		AL, AH
		OUT		LCDC, AL
		RET
		;
BUSY:	IN 		AL, LCDC_S
		AND		AL, 10000000B
		JNZ		BUSY
		RET
		;
SCAN:	IN 		AL, KEY
		TEST	AL, 10000000B
		JNZ		SCAN
		;
		AND		AL, 00011111B
		MOV		BX, 0
		MOV		DS, BX
		CMP		AL, 00001001B
		JG		LETTER
		OR      AL, 00110000B
		JMP		DISP
LETTER:	OR		AL, 01000000B
		AND		AL, 11110111B
		DEC		AL
DISP:	OUT		LCDD, AL
		
		;	KEY CLEAR
		OUT		KEY, AL
		RET
		;
CODE	ENDS
		END