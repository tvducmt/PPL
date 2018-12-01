.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static c I
.field static b F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	putstatic MPClass.a I
Label2:
	getstatic MPClass.a I
	bipush 10
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	getstatic MPClass.a I
	invokestatic io/putInt(I)V
	getstatic MPClass.a I
	iconst_1
	iadd
	putstatic MPClass.a I
	getstatic MPClass.a I
	bipush 8
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	goto Label2
	goto Label9
Label8:
Label9:
	getstatic MPClass.a I
	putstatic MPClass.c I
Label10:
	getstatic MPClass.c I
	iconst_0
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	getstatic MPClass.c I
	iconst_1
	isub
	putstatic MPClass.c I
	getstatic MPClass.c I
	iconst_3
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	goto Label10
	goto Label17
Label16:
Label17:
	getstatic MPClass.c I
	invokestatic io/putInt(I)V
	goto Label10
Label11:
	goto Label2
Label3:
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
