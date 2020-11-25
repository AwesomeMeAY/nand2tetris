// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
// for i=R0, i!=i-i, i-- {
// 	if R0 >= 0 {
//		R2 = R1 + R2
//	}
//	else {
//		R2 = R2- R1
// }
// }

// Set R2 to 0
@R2
	M=0

// Check if R0 is negative 
(NEG_CHECK)
@R0
	D=M
@NEG
	D;JLT // If R0 is less than 0 jump to recursive subtractor
(MULT)
@R0
	D=M
	M=M-1 
// Check if the program should finish 
@LOOP
	D;JLE // If R0 is less than or equal to 0, jump to loop
@R1
	D=M
@R2
	M=D+M // Will recursively add to R2 until R0 equals 0
@R0
	D=M 
@MULT
	0;JMP
	
// Multiplication if R0 is negative
(NEG)
@R0
	M=M+1 // Add to R0 until it is 0
@R1
	D=M
@R2
	M=M-D // Subtract "whatever the absolute value of R0 is" times
@R0
	D=M
@NEG
	D;JLT // Jump if R0 is less than 0

// infinite loop after multiplication is finished
(LOOP)
@LOOP
	0;JMP



