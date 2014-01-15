---
layout: default
title: MIST32 Condition Code
---
MIST32 Condition Code
==========
分岐命令でで使用される分岐条件です。Condition Code(以下CC)は以下のように使用します。


b  _label, #al


CC一覧
====

|Code|Operate|Condition|CC1|CC2|CC3(GCC)|Flag Condition|
|--------|--------|--------|--------|--------|--------|--------|
|0x0|Always|Always|AL|　| |Always|
|0x1|Equal|==|EQ|Z| EQ|ZF|
|0x2|Not Equal|!=|NEQ|NZ|NE|!ZF|
|0x3|Minus|-|　|MI|  |SF|
|0x4|Plus|+|　|PL|  |!SF|
|0x5|Even Number|2%|　|EN|  |PS|
|0x6|Odd Number|!%2|　|ON|  |!PS|
|0x7|Overflow|　|　|OVF|  |OF|
|0x8|Unsigned >=(Cary Set)|>=|UEO|C|GEU|CF|
|0x9|Unsigned <(Not Cary Set)|<|UU|NC|LTU|!CF|
|0xA|Unsigned >|>|UO|　|GTU|CF and !ZF|
|0xB|Unsigned <=|<=|UEU|　|LEU|!CF or ZF|
|0xC|Signed >=|>=|SEO|　|GE|(SF and OF) or (!SF and !OF)|
|0xD|Signed <|<|SU|　|LT|(SF and !OF) or (!SF and OF)|
|0xE|Signed >|>|SO|　|GT|!((SF xor OF) or ZF)|
|0xF|Signed <=|<=|SEU|  |LE|(SF xor OF) or ZF|


