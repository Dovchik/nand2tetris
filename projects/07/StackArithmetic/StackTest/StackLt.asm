@256
D=A
@SP
M=D
@892
D=A
@256
M=D
@SP
M=M+1
@891
D=A
@257
M=D
@SP
M=M+1
@SP
M=M-1
@257
D=M
@SP
M=M-1
@256
D=M-D
@BOOL.TRUE.0
D;JLT
@BOOL.FALSE.0
0;JMP
(BOOL.TRUE.0)
@256
M=-1
@NEXT.0
0;JMP
(BOOL.FALSE.0)
@256
M=0
@NEXT.0
0;JMP
(NEXT.0)
@SP
M=M+1
(END)
@END
0;JMP