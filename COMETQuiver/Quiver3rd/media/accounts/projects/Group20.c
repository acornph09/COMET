/*Candelaria, Aaron ; Canonizado, Ian ; Fadul, Jedrek - S12 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int NullChecker(char *dna);
extern int TerminatorChecker(char *dna);
extern int TruncateString(char *dna);
extern int LengthChecker(char *dna);
extern int ValidityChecker(char *dna);
extern int ACount(char *dna);
extern int CCount(char *dna);
extern int GCount(char *dna);
extern int TCount(char *dna);
extern char* Complement(char *dna);
extern char* Reverse(char *dna);
extern int PalindromeTest(char *dna, char *reversed);
extern int PopCount (char *dna);
extern void FibonacciSequence(int* fib, int month);

int NullCheck(char *DNA){
	int flag = 0;
	flag = NullChecker(DNA);
	
	if(flag == 1){
		printf("Error: Null Input!\n");
		return 1;
	}
	return 0;
		
}	

int TerminatorCheck(char *DNA){
	int flag = 0;
	flag = TerminatorChecker(DNA);
	
	if(flag==1){
		printf("Error: Terminator not found in DNA String!\n");
		return 1;
	}
	return 0;
}

void Truncate(char *DNA){
	int index = TruncateString(DNA);
	DNA[index] = '\0';
}

int LengthCheck(char *DNA){
	int flag = 0;
	flag = LengthChecker(DNA);
	
	if(flag==1){
		printf("Error: DNA string exceeds Maximum Length!\n");
		return 1;
	}
	return 0;
}

int ValidityCheck(char *DNA){
	int flag = 0;
	flag = ValidityChecker(DNA);
	
	if(flag==1){
		printf("Error: Invalid Input!\n");
		return 1;
	}
	return 0;
}

void ReverseComplement(char *DNA){
	strcpy(DNA,Complement(DNA));
	strcpy(DNA,Reverse(DNA));
	
}

void Palindrome(char *DNA){
	char *original;
	size_t length = strlen(DNA);
	original = malloc(sizeof(char)*length);
	int flag = -1;
	strcpy(original, DNA);
	strcpy(DNA,Complement(DNA));
	strcpy(DNA,Reverse(DNA));
	flag = PalindromeTest(original, DNA);
	if(flag==0){
		printf("Reverse Palindrome: Yes\n");
	}
	else{
		printf("Reverse Palindrome: No\n");
	}
}

void Pop(char *DNA){
	printf("Pop Count: %d\n", PopCount(DNA));
}

void Fibonacci(int month){
	int fibsequence[month];
	size_t i;
	for(i = 0 ; i<month ; i++){
		fibsequence[i]=0;
	}
	FibonacciSequence(fibsequence, month);
	printf("Fibonacci Sequence is : ");
	for(i = 0;i<month;i++){
		if(i!=month-1){
		printf("%d, ", fibsequence[i]);
		}
		else{
			printf("%d", fibsequence[i]);
		}
	}
	printf("\n");
}

char* DNAInput(FILE* fp, size_t size){

    char *dnastring;
    int last;
    size_t dnalength = 0;
    dnastring = realloc(NULL, sizeof(char)*size);
    
    if(!dnastring)
		return dnastring;
		
    while(EOF!=(last=fgetc(fp)) && last != '\n'){
        dnastring[dnalength++]=last;
        if(dnalength==size){
            dnastring = realloc(dnastring, sizeof(char)*(size+=16));
            if(!dnastring)
				return dnastring;
    
	    }
	}
	dnastring[dnalength++]='\0';
    return realloc(dnastring, sizeof(char)*dnalength);
}


int UserChoice()
{
     int choice;
     printf("\n\t\t\t\tMain Menu\n");
     printf("\t\t1.Perform DNA Frequency Count\n");
     printf("\t\t2.Perform DNA Reverse Complement\n");
     printf("\t\t3.Perform Reverse Palindrome Test\n");
     printf("\t\t4.Perform DNA Pop Count\n");
     printf("\t\t5.Perform Genetic Fibonacci Sequence\n");
     printf("\t\t6.Exit\n");
     printf("\t\tEnter your choice: ");
     
	 
	 scanf("%d", &choice);
     fflush(stdin);
     return choice;
}

/*Main Menu*/
int MainMenu(int option){
	
	char *DNAstring;
	int errors = 0;
	int month = 0;
	
	
	switch(option){
		case 1:
    			printf("Task to be performed: DNA Frequency Count\n");
    			printf("Enter DNA String : "); 
				DNAstring = DNAInput(stdin, 10);
  				errors=NullCheck(DNAstring);
  				if(errors != 0){
  					break;
				  } 
				
				errors=TerminatorCheck(DNAstring);
				if(errors != 0){
  					break;
				}
				
				Truncate(DNAstring);
				errors=LengthCheck(DNAstring);
				if(errors != 0){
  					break;
				}
				errors=ValidityCheck(DNAstring);
				if(errors != 0){
  					break;
				}
               printf("\nFrequency of A: %d", ACount(DNAstring));
               printf("\nFrequency of C: %d", CCount(DNAstring));
               printf("\nFrequency of G: %d", GCount(DNAstring));
               printf("\nFrequency of T: %d\n", TCount(DNAstring));
				break;
				
    		case 2:
    			printf("Task to be performed: DNA Reverse Complement\n");
    			printf("Enter DNA String : ");
  				DNAstring = DNAInput(stdin, 10);
  				errors=NullCheck(DNAstring);
  				if(errors != 0){
  					break;
				  } 
				
				errors=TerminatorCheck(DNAstring);
				if(errors != 0){
  					break;
				}
				
				Truncate(DNAstring);
				errors=LengthCheck(DNAstring);
				if(errors != 0){
  					break;
				}
				errors=ValidityCheck(DNAstring);
				if(errors != 0){
  					break;
				}
				
				ReverseComplement(DNAstring); 
				printf("Reverse Complemented DNA String : %s\n", DNAstring);
				break;
    			
    		case 3:
    			printf("Task to be performed: DNA Reverse Palindrome Test\n");
    			printf("Enter DNA String : ");
  				DNAstring = DNAInput(stdin, 10);
  				errors=NullCheck(DNAstring);
  				if(errors != 0){
  					break;
				  } 
				
				errors=TerminatorCheck(DNAstring);
				if(errors != 0){
  					break;
				}
				
				Truncate(DNAstring);
				errors=LengthCheck(DNAstring);
				if(errors != 0){
  					break;
				}
				
				errors=ValidityCheck(DNAstring);
				if(errors != 0){
  					break;
				}
				Palindrome(DNAstring);
				break;
    		
    		case 4:
    			printf("Task to be performed: DNA Pop Count\n");
    			printf("Enter DNA String : ");
  				DNAstring = DNAInput(stdin, 10);
  				errors=NullCheck(DNAstring);
  				if(errors != 0){
  					break;
				  } 
				
				errors=TerminatorCheck(DNAstring);
				if(errors != 0){
  					break;
				}
				
				Truncate(DNAstring);
				errors=LengthCheck(DNAstring);
				if(errors != 0){
  					break;
				}
				errors=ValidityCheck(DNAstring);
				if(errors != 0){
  					break;
				}
				Pop(DNAstring);
				break;
    			
    		case 5:
    			printf("Task to be performed: Genetic Fibonacci Computation\n");
    			printf("Enter month: ");
  				scanf("%d", &month);
  				
  				Fibonacci(month);
  				
    			break;
    		case 6:
    			printf("Program End!");
    			break;
		
		
	}
	
	free(DNAstring);
	printf("Press Any Key to Continue: ");
	getchar();
    return UserChoice();
}


int main(void){
	
	int option = 0;
	
	option = UserChoice();
	
	do{
		option=MainMenu(option);
		fflush(stdin);
	}while(option!=6);
	
}

