.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a F
.field static c I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 7.5
	putstatic MPClass.a F
	iconst_1
	putstatic MPClass.c I
	getstatic MPClass.a F
	getstatic MPClass.c I
	iconst_2
	imul
	invokestatic MPClass/foo(FI)F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static foo(FI)F
.var 0 is x F from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	fload_0
	iload_1
	i2f
	fdiv
	goto Label1
Label1:
	freturn
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
