; ModuleID = 'hello.bb'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@str.0 = private unnamed_addr constant [13 x i8] c"Hello World!\00", align 1

declare i32 @puts(i8*)

define i32
