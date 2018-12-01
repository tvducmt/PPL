.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	putstatic MPClass.a I
	getstatic MPClass.a I
	iconst_5
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
	iconst_0
	iconst_1
	ior
	goto Label5
Label4:
	iconst_1
Label5:
	ifle Label2
	iconst_0
	getstatic MPClass.a I
	bipush 10
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ior
	goto Label3
Label2:
	iconst_1
Label3:
	ifle Label10
	getstatic MPClass.a I
	invokestatic io/putInt(I)V
	goto Label11
Label10:
	iconst_2
	invokestatic io/putInt(I)V
Label11:
Label1:
	return
.limit stack 12
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
