.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MPClass.a I
Label2:
	getstatic MPClass.a I
	iconst_5
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	getstatic MPClass.a I
	iconst_1
	iadd
	putstatic MPClass.a I
	getstatic MPClass.a I
	iconst_3
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
	invokestatic io/putInt(I)V
	goto Label2
Label3:
Label1:
	return
.limit stack 5
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
