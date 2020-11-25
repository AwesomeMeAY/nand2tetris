// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program colors the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
// for i in screen..24575:
//	m=-1

// Put your code here.

(LOOP)
@SCREEN
	D=A //get first address
@address
	M=D // save first address
		// D will tell if the key is pressed or not
@KBD
	D=M
@SET_D_NEG
	D;JNE // jump if d is not 0 (Which means screen needs to be black)
@color_status
	M=D // save D's color status (black or white)
(START)
@color_status
	D=M // Change D back to color status
@address
	A=M // set current address to saved address
	M=D // set the pixels to either black or white
	A=A+1
	D=A // Next register to be colored
@address
	M=D // Save the next register address
@KBD
	D=A-D // Subtrack the last register with the next register	
@START
	D;JNE // Continue to color screen if not on last register

// End of start section	
@LOOP
	0;JMP

(SET_D_NEG)
D=-1
@color_status
	M=D
@START
	0;JMP
// end of SET_D_NEG section
