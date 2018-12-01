.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static c I
.field static b I
.field static e F
.field static d Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	putstatic MPClass.b I
	iconst_2
	putstatic MPClass.c I
.var 1 is a Z from Label2 to Label3
Label2:
	getstatic MPClass.c I
	iconst_3
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_1
	iload_1
	iconst_1
	ior
	ifle Label6
Label8:
	getstatic MPClass.b I
	bipush 15
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
	getstatic MPClass.b I
	invokestatic io/putInt(I)V
	getstatic MPClass.b I
	iconst_3
	iadd
	putstatic MPClass.b I
	goto Label8
Label9:
	goto Label7
Label6:
Label7:
Label3:
Label1:
	return
.limit stack 7
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
