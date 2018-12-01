.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	iconst_5
	istore_1
	iconst_1
	ifle Label2
	iconst_1
	iload_1
	bipush 9
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label6
	iload_1
	invokestatic io/putInt(I)V
	goto Label7
Label6:
	iconst_2
	invokestatic io/putInt(I)V
Label7:
Label1:
	return
.limit stack 7
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
