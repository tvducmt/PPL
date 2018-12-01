.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	bipush 49
	istore_1
	iconst_3
	istore_2
	iload_1
	iconst_2
	imul
	bipush 15
	irem
	bipush 15
	iload_2
	iconst_4
	iadd
	idiv
	iadd
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
.limit locals 3
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
