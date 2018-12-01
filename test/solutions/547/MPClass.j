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
Label4:
	getstatic MPClass.a I
	bipush 10
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	getstatic MPClass.a I
	bipush 9
	if_icmpne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	goto Label3
	goto Label10
Label9:
Label10:
	getstatic MPClass.a I
	invokestatic io/putInt(I)V
	getstatic MPClass.a I
	putstatic MPClass.c I
Label11:
	getstatic MPClass.c I
	iconst_1
	if_icmple Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label12
	getstatic MPClass.c I
	iconst_1
	isub
	putstatic MPClass.c I
	getstatic MPClass.c I
	iconst_3
	if_icmpne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
	goto Label11
	goto Label18
Label17:
Label18:
	getstatic MPClass.c I
	invokestatic io/putInt(I)V
	goto Label11
Label12:
Label2:
	getstatic MPClass.a I
	iconst_1
	iadd
	putstatic MPClass.a I
	goto Label4
Label3:
Label1:
	return
.limit stack 10
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
