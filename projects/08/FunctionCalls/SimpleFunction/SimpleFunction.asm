@256
D=A
@SP
M=D
@Sys.init
0;JMP
(SimpleFunction.test)
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
@0
D=A
@LCL
D=M+D
@LCL_TMP
A=D
D=M
@SP
A=M
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
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M+D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
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
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
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
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
@SP
M=M+1
@LCL
D=M
@FRAME
M=D
D=M
@5
D=D-A
A=D
D=M
@RET
M=D
@SP
M=M-1
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@FRAME
M=M-1
A=M
D=M
@THAT
M=D
@FRAME
M=M-1
A=M
D=M
@THIS
M=D
@FRAME
M=M-1
A=M
D=M
@ARG
M=D
@FRAME
M=M-1
A=M
D=M
@LCL
M=D
@RET
A=M
0;JMP
(END)
@END
0;JMP