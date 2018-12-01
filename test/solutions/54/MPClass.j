.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label2 to Label3
Label2:
	ldc 1.1
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
Label3:
.var 1 is f Z from Label4 to Label5
Label4:
	iconst_1
	istore_1
	iload_1
	invokestatic io/putBool(Z)V
Label5:
Label1:
	return
.limit stack 2
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
