.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 11
	putstatic MPClass.a I
	iconst_3
	iconst_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	getstatic MPClass.a I
	invokestatic io/putInt(I)V
	getstatic MPClass.a I
	iconst_1
	iadd
	bipush 15
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "kien"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label9
Label8:
	ldc "no kien"
	invokestatic io/putString(Ljava/lang/String;)V
Label9:
	goto Label5
Label4:
Label5:
	iconst_5
	invokestatic io/putInt(I)V
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
