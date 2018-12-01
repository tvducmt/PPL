.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	putstatic MPClass.a I
	bipush 10
	putstatic MPClass.b I
	getstatic MPClass.a I
	getstatic MPClass.b I
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	getstatic MPClass.b I
	iconst_2
	irem
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	getstatic MPClass.b I
	iconst_2
	imul
	bipush 18
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	ior
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 9
.limit locals 1
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
