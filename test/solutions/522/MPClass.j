.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static d Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MPClass.d Z
	iconst_3
	putstatic MPClass.b I
	iconst_1
	iconst_0
	getstatic MPClass.d Z
	iand
	iand
	invokestatic io/putBool(Z)V
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
