.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c F
.field static d F
.field static e Z
.field static f Z
.field static g Ljava/lang/String;
.field static h Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MPClass.c F
	invokestatic MPClass/foo(F)F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo(F)F
.var 0 is a F from Label0 to Label1
.var 1 is x Z from Label0 to Label1
.var 2 is y Z from Label0 to Label1
Label0:
	ldc 2.5
	fstore_0
	fload_0
	goto Label1
Label1:
	freturn
.limit stack 1
.limit locals 3
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
