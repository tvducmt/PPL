.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static c I
.field static b F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 20
	putstatic MPClass.a I
	iconst_2
	putstatic MPClass.c I
Label2:
	getstatic MPClass.a I
	iconst_1
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	getstatic MPClass.a I
	invokestatic io/putInt(I)V
	getstatic MPClass.a I
	iconst_3
	isub
	putstatic MPClass.a I
Label6:
	getstatic MPClass.c I
	bipush 10
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	getstatic MPClass.c I
	invokestatic io/putInt(I)V
	getstatic MPClass.c I
	iconst_1
	iadd
	putstatic MPClass.c I
	goto Label6
Label7:
	goto Label2
Label3:
Label1:
	return
.limit stack 6
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
