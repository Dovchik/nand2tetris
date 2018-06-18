// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/02/ALU.tst

load Zero16.hdl,
output-file Zero16.out,
compare-to Zero16.cmp,
output-list in%B1.16.1 zx%B3.1.3 out%B1.16.1;

set in %B0000000000000100,  // x = 4

// Compute 4
set zx 1,
eval,
output;