.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static c I

.method public static abc()I
.var 0 is b I from Label0 to Label1
Label0:
Label2:
	iconst_1
	ifle Label3
	iconst_1
	goto Label1
	goto Label2
Label3:
	iconst_2
	goto Label1
Label1:
	ireturn
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is d I from Label0 to Label1
Label0:
	iconst_5
	istore_1
	bipush 6
	istore_2
	invokestatic MPClass/abc()I
Label1:
	return
.limit stack 1
.limit locals 4
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
