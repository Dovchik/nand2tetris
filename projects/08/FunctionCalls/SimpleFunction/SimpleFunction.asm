@256
D=A
@SP
M=D
@0
D=A
@LCL
D=M+D
@LCL_TMP
A=D
D=M
@256
M=D
@SP
M=M+1
@1
D=A
@LCL
D=M+D
@LCL_TMP
A=D
D=M
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
M=M+D
@SP
M=M+1
@SP
M=M-1
@256
M=!M
@SP
M=M+1
@0
D=A
@ARG
D=M+D
@ARG_TMP
A=D
D=M
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
M=M+D
@SP
M=M+1
@1
D=A
@ARG
D=M+D
@ARG_TMP
A=D
D=M
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
M=M-D
@SP
M=M+1
(END)
@END
0;JMP