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
	iconst_5
	putstatic MPClass.a I
	bipush 6
	putstatic MPClass.b I
	getstatic MPClass.b I
	getstatic MPClass.a I
	iconst_2
	imul
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 3
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
