---
layout: default
title: MIST32 Instructions
css: instructions
---
MIST32 Instructions
==========

|Addr\[Hex\]|Addr\[Dec\]|Type\-E|Unit|Instruction|Immediate\[Displacement\]|Mnemonic|Opcode|FMT1\(Operand/Disp\)|FMT2\(Imm\)|Operation|Flag|AFE\-FMT1|AFE\-FMT2\(Imm\)|Auth|Trap|Trap Condition|Note|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|000|0|○|integer|add|sign extension|ADD|0000000000|O2|I11|Rd = Rd \+ Rs| | | | | | | |
|001|1|○| |sub|sign extension|SUB|0000000001|O2|I11|Rd = Rd \- Rs| | | | | | | |
|002|2|○| |mul output low32bit|sign extension|MULL|0000000010|O2|I11|Rd = \(Rd \* Rs\) & 0xFFFFFFFF| | | | | | | |
|003|3|○| |mul output high32bit|sign extension|MULH|0000000011|O2|I11|Rd = \(Rd \* Rs\) >> 32| | | | | | | |
|004|4| | |unsigned div| |UDIV|0000000100|O2|I11|Rd = Rd / Rs| | | | |4|0割の時（結果は0）| |
|005|5| | |unsigned mod| |UMOD|0000000101|O2|I11|Rd = Rd % Rs| | | | |4|0割の時（結果は0）| |
|006|6|○| |cmp|sign extension|CMP|0000000110|O2|I11|FLAGR = flags\_out\(Rd \- Rs\)| | | | | | |SUBを行ない、結果を破棄しフラグのみ更新|
|007|7| | |div|sign extension|DIV|0000000111|O2|I11|Rd = Rd / Rs| | | | |4|0割の時（結果は0）| |
|008|8| | |mod|sign extension|MOD|0000001000|O2|I11|Rd = Rd % Rs| | | | |4|0割の時（結果は0）| |
|009|9| | |sign negative| |NEG|0000001001|O2| |Rd = negative\(Rs\)|not generate flags| | | | | | |
|00A|10|○| |unsigned mul output low32bit| |UMULL|0000001010|O2|I11| | | | | | | | |
|00B|11|○| |unsigned mul output high32bit| |UMULH|0000001011|O2|I11| | | | | | | | |
|00D|13| | |increment output carry| |IC|0000001101|O2| |Rd = cary\_out\(Rs \+ 1\)| | | | | | | |
|00E|14|○| |add output carry|sign extension|ADDC|0000001110|O2|I11|Rd = cary\_out\(Rd \+ Rs\)| | | | | | | |
|010|16|○| |inc| |INC|0000010000|O2| |Rd = Rs \+ 1| | | | | | | |
|011|17|○| |dec| |DEC|0000010001|O2| |Rd = Rs \- 1| | | | | | | |
|013|19| | |maximum| |MAX|0000010011|O2|I11|Rd = \(Rd >= Rs\)? Rd : Rs|not generate flags| | | | | | |
|014|20| | |minimum| |MIN|0000010100|O2|I11|Rd = \(Rd <= Rs\)? Rd : Rs|not generate flags| | | | | | |
|015|21| | |unsigned maximum| |UMAX|0000010101|O2|I11|Rd = \(Rd >= Rs\)? Rd : Rs|not generate flags| | | | | | |
|016|22| | |unsigned minimum| |UMIN|0000010110|O2|I11|Rd = \(Rd <= Rs\)? Rd : Rs|not generate flags| | | | | | |
|01C|28|○| |sign extension 8bit to 32bit| |SEXT8|0000011100|O2| |Rd = sign\_extension8to32\(Rs\)|not generate flags| | | | | | |
|01D|29|○| |sign extension 16bit to 32bit| |SEXT16|0000011101|O2| |Rd = sign\_extension16to32\(Rs\)|not generate flags| | | | | | |
|040|64|○|Shift|logic shift left| |SHL|0001000000|O2|I11|Rd = Rd<<Rs|CF=Rd\[32\], OF=0| | | |1|64以上シフトした場合| |
|041|65|○| |logic shift right| |SHR|0001000001|O2|I11|Rd = Rd>>Rs|CF=Rd\[\-1\], OF=0| | | |1|64以上シフトした場合| |
|045|69|○| |alithmetic shift right| |SAR|0001000101|O2|I11|Rd = Rd>>>Rs|CF=Rd\[\-1\], OF=0| | | |1|64以上シフトした場合| |
|048|72| | |rotate shift left| |ROL|0001001000|O2|I11|Rd = rol\(Rd, Rs\)|not generate flags| | | |1|64以上シフトした場合| |
|049|73| | |rotate shift right| |ROR|0001001001|O2|I11|Rd = ror\(Rd, Rs\)|not generate flags| | | |1|64以上シフトした場合| |
|060|96|○|Logic|and| |AND|0001100000|O2| |Rd = Rd & Rs| | | | | | | |
|061|97|○| |or| |OR|0001100001|O2| |Rd = Rd &\#124; Rs| | | | | | | |
|062|98|○| |xor| |XOR|0001100010|O2| |Rd = Rd ^ Rs| | | | | | | |
|063|99|○| |not| |NOT|0001100011|O2| |Rd = ~Rs| | | | | | | |
|064|100|○| |nand| |NAND|0001100100|O2| |Rd = ~\(Rd & Rs\)| | | | | | | |
|065|101|○| |nor| |NOR|0001100101|O2| |Rd = ~\(Rd &\#124; Rs\)| | | | | | | |
|066|102|○| |xnor| |XNOR|0001100110|O2| |Rd = ~\(Rd ^ Rs\)| | | | | | | |
|067|103|○| |test| |TEST|0001100111|O2| |FLAGR = flags\_out\(Rd & Rs\)| | | | | | | |
|06A|106|○| |write for low 16bit| |WL16|0001101010|I16| |Rd = \(Rd & 0xFFFF0000\) &\#124; \(Rs & 0x0000FFFF\)|not generate flags| | | | | | |
|06B|107|○| |write for high 16bit| |WH16|0001101011|I16| |Rd = \(Rd & 0x0000FFFF\) &\#124; \(\(Rs << 16\) & 0xFFFF0000\)|not generate flags| | | | | | |
|06C|108|○| |clear bit| |CLRB|0001101100| |I11|Rd = clb\(Rs\)|not generate flags| | | | | | |
|06D|109|○| |set bit| |SETB|0001101101| |I11|Rd = stb\(Rs\)|not generate flags| | | | | | |
|06E|110|○| |clear word| |CLR|0001101110|O1| |Rd = 0x00000000|not generate flags| | | | | | |
|06F|111|○| |set word| |SET|0001101111|O1| |Rd = 0xFFFFFFFF|not generate flags| | | | | | |
|070|112| | |bit reverse| |REVB|0001110000|O2| |Rd = rvbi\(Rs\)|not generate flags| | | | | | |
|071|113|○| |byte reverse| |REV8|0001110001|O2| |Rd = rvby\(Rs\)|not generate flags| | | | | | |
|072|114| | |get single bit| |GETB|0001110010|O2|I11|Rd = \(Rd >> Rs\) & 0x00000001|not generate flags| | | | | | |
|073|115|○| |get 1 byte| |GET8|0001110011|O2|I11|Rd = \(Rd >> Rs\*8\) & 0x000000FF|not generate flags| | | | | | |
|076|118|○| |load immediate low 16bit| |LIL|0001110110| |I16|Rd = sign\_extension\(Rs\)|not generate flags| | | | | | |
|077|119|○| |load immediate high 16bit| |LIH|0001110111| |I16|Rd = Rs<<16|not generate flags| | | | | | |
|07A|122|○| |unsigned load immediate 16bit| |ULIL|0001111010| |I16|Rd = Rs| | | | | | | |
|080|128|○|Memory Access|load byte data| |LD8|0010000000|O2|I11|Rd = mask\(MEMORY\[Rs\], 8\)|not generate flags|MA|MA| |2|メモリ保護違反の場合| |
|081|129|○| |load 2byte data|1bit left shift|LD16|0010000001|O2|I11|Rd = mask\(MEMORY\[Rs\], 16\)|not generate flags|MA|MA| |2|メモリ保護違反の場合| |
|082|130|○| |load word data|2bit left shift|LD32|0010000010|O2|I11|Rd = MEMORY\[Rs\]|not generate flags|MA|MA| |2|メモリ保護違反の場合| |
|083|131|○| |store byte data| |ST8|0010000011|O2|I11|MEMORY\[Rs\] = mask\(Rd, 8\)|not generate flags| | | |2|メモリ保護違反の場合| |
|084|132|○| |store 2byte data|1bit left shift|ST16|0010000100|O2|I11|MEMORY\[Rs\] = mask\(Rd, 16\)|not generate flags| | | |2|メモリ保護違反の場合| |
|085|133|○| |store word data|2bit left shift|ST32|0010000101|O2|I11|MEMORY\[Rs\] = Rd|not generate flags| | | |2|メモリ保護違反の場合| |
|088|136|○| |push|sign extension|PUSH|0010001000|O1|CI16|MEMORY\[SPR\] = Rd, SPR = SPR \- 4|not generate flags| | | |2|メモリ保護違反の場合| |
|089|137| | |push program counter| |PUSHPC|0010001001|C| |MEMORY\[SPR\] = PC \+ 8|not generate flags| | | |2|メモリ保護違反の場合| |
|08A|138| | |load byte data \(always use PDTR\)| |LD8U|0010001010|O2|I11|Rd = mask\(MEMORY\[Rs\], 8\)|not generate flags| | |カーネルモードのみ実行可能|2,3|メモリ保護違反、特権違反| |
|08B|139| | |load 2byte data \(always use PDTR\)|1bit left shift|LD16U|0010001011|O2|I11|Rd = mask\(MEMORY\[Rs\], 16\)|not generate flags| | |カーネルモードのみ実行可能|2,3|メモリ保護違反、特権違反| |
|08C|140| | |load word data \(always use PDTR\)|2bit left shift|LD32U|0010001100|O2|I11|Rd = MEMORY\[Rs\]|not generate flags| | |カーネルモードのみ実行可能|2,3|メモリ保護違反、特権違反| |
|08D|141| | |store byte data \(always use PDTR\)| |ST8U|0010001101|O2|I11|MEMORY\[Rs\] = mask\(Rd, 8\)|not generate flags| | |カーネルモードのみ実行可能|2,3|メモリ保護違反、特権違反| |
|08E|142| | |store 2byte data \(always use PDTR\)|1bit left shift|ST16U|0010001110|O2|I11|MEMORY\[Rs\] = mask\(Rd, 16\)|not generate flags| | |カーネルモードのみ実行可能|2,3|メモリ保護違反、特権違反| |
|08F|143| | |store word data \(always use PDTR\)|2bit left shift|ST32U|0010001111|O2|I11|MEMORY\[Rs\] = Rd|not generate flags| | |カーネルモードのみ実行可能|2,3|メモリ保護違反、特権違反| |
|090|144|○| |pop| |POP|0010010000|O1| |Rd = MEMORY\[SPR\], SPR = SPR \+ 4|not generate flags| |MA| |2|メモリ保護違反の場合| |
|09A|154|○| |load byte data with displacement|\[sign extension\]|LDD8|0010011010|O2| |Rd = mask\(MEMORY\[Rs\+displacement\], 8\)|not generate flags|MA| | |2|メモリ保護違反の場合| |
|09B|155|○| |load 2byte data with displacement|1bit left shift\[sign extension・1bit left shift\]|LDD16|0010011011|O2| |Rd = mask\(MEMORY\[Rs\+displacement\], 16\)|not generate flags|MA| | |2|メモリ保護違反の場合| |
|09C|156|○| |load word data with displacement|2bit left shift\[sign extension・2bit left shift\]|LDD32|0010011100|O2| |Rd = MEMORY\[Rs\+displacement\]|not generate flags|MA| | |2|メモリ保護違反の場合| |
|09D|157|○| |store byte data with displacement|\[sign extension\]|STD8|0010011101|O2| |MEMORY\[Rs\+displacement\] = mask\(Rd, 8\)|not generate flags| | | |2|メモリ保護違反の場合| |
|09E|158|○| |store 2byte data with displacement|1bit left shift\[sign extension・1bit left shift\]|STD16|0010011110|O2| |MEMORY\[Rs\+displacement\] = mask\(Rd, 16\)|not generate flags| | | |2|メモリ保護違反の場合| |
|09F|159|○| |store word data with displacement|2bit left shift\[sign extension・2bit left shift\]|STD32|0010011111|O2| |MEMORY\[Rs\+displacement\] = Rd|not generate flags| | | |2|メモリ保護違反の場合| |
|0A0|160|○|Branch|unsigned branch \(PC relative address\)|2bit left shift|BUR|0010100000|JO1|JI16|PC = PC \+ unsigned\(Rd\)|not generate flags| | | |2|メモリ保護違反の場合|Word Addressing|
|0A1|161|○| |branch \(PC relative address\)|sign extension・2bit left shift|BR|0010100001|JO1|JI16|PC = PC \+ signed\(Rd\)|not generate flags| | | |2|メモリ保護違反の場合|Word Addressing|
|0A2|162|○| |branch \(direct address\)|2bit left shift|B|0010100010|JO1|JI16|PC = unsigned\(Rd\)|not generate flags| | | |2|メモリ保護違反の場合|Word Addressing|
|0A3|163|○| |set pcr from ppcr data\(condition code not suport\)| |IB|0010100011|C| |PC = PPCR|not generate flags| | | |2|メモリ保護違反の場合|Word Addressing 割り込みルーチンからの復帰に使用\(特権操作\) CCはALしか対象外。それ以外は未定義|
|0B0|176| | |unsigned branch \(PC relative address\)\. with hint of not branch|2bit left shift|BURN|0010110000|JO1|JI16|PC = PC \+ unsigned\(Rd\)|not generate flags| | | |2|メモリ保護違反の場合|Word Addressing|
|0B1|177| | |branch \(PC relative address\)\. with hint of not branch|sign extension・2bit left shift|BRN|0010110001|JO1|JI16|PC = PC \+ signed\(Rd\)|not generate flags| | | |2|メモリ保護違反の場合|Word Addressing|
|0B2|178| | |branch \(direct address\)\. with hint of not branch|2bit left shift|BN|0010110010|JO1|JI16|PC = unsigned\(Rd\)|not generate flags| | | |2|メモリ保護違反の場合|Word Addressing|
|0C0|192|○|System Register Read|read SPR| |SRSPR|0011000000|O1| |Rd = SPR|not generate flags| | | | | | |
|0C1|193| | |read PDTR| |SRPDTR|0011000001|O1| |Rd = PDTR|not generate flags| | | | | | |
|0C2|194| | |read CPUIDR| |SRPIDR|0011000010|O1| |Rd = CPUIDR|not generate flags| | | | | | |
|0C3|195| | |read COREIDR| |SRCIDR|0011000011|O1| |Rd = COREIDR|not generate flags| | | | | | |
|0C4|196| | |read PSR\_CMOD| |SRMODER|0011000100|O1| |Rd = \(PSR >> 5\) & 0x3|not generate flags| | | | | | |
|0C5|197|○| |read PSR\_IM| |SRIEIR|0011000101|O1| |Rd = \(PSR >> 2\) & 0x1|not generate flags| | | | | |1で許可|
|0C8|200| | |read TISR| |SRTISR|0011001000|O1| |Rd = TISR|not generate flags| | |カーネルモードのみ実行可能|3|特権違反| |
|0C9|201| | |read KPDTR| |SRKPDTR|0011001001|O1| |Rd = KPDTR|not generate flags| | |カーネルモードのみ実行可能|3|特権違反| |
|0CA|202| | |read PSR\_MMUMOD| |SRMMUR|0011001010|O1| |Rd = PSR & 0x3|not generate flags| | | | | |0=アドレス変換なし, 1=予約, 2=1段変換, 3=2段変換|
|0CB|203| | |read IOSR| |SRIOSR|0011001011|O1| |Rd = IOSR|not generate flags| | | | | | |
|0CC|204| | |read TIDR| |SRTIDR|0011001100|O1| |Rd = TIDR|not generate flags| | | | | | |
|0CD|205|○| |read PPSR| |SRPPSR|0011001101|O1| |Rd = PPSR|not generate flags| | | | | | |
|0CE|206|○| |read PPCR| |SRPPCR|0011001110|O1| |Rd = PPCR|not generate flags| | | | | | |
|0D0|208| | |read PPDTR| |SRPPDTR|0011010000|O1| |Rd = PPDTR|not generate flags| | | | | | |
|0D1|209| | |read PTIDR| |SRPTIDR|0011010001|O1| |Rd = PTIDR|not generate flags| | | | | | |
|0D3|211|○| |read PSR| |SRPSR|0011010011|O1| |Rd = PSR|not generate flags| | | | | | |
|0D4|212|○| |read FRCR to \{FRCHR, FRCLR\}| |SRFRCR|0011010100|C| |\{FRCHR, FRCLR\} = FRCR|not generate flags| | | | | | |
|0D5|213|○| |read FRCLR| |SRFRCLR|0011010101|O1| |Rd = FRCLR|not generate flags| | | | | | |
|0D6|214|○| |read FRCHR| |SRFRCHR|0011010110|O1| |Rd = FRCHR|not generate flags| | | | | | |
|0D7|215|○| |read PFLAGR| |SRPFLAGR|0011010111|O1| |Rd = PFLAGR|not generate flags| | | | | | |
|0D8|216|○| |read FI0R| |SRFI0R|0011011000|O1| |Rd = FI0R|not generate flags| | | | | | |
|0D9|217|○| |read FI1R| |SRFI1R|0011011001|O1| |Rd = FI1R|not generate flags| | | | | | |
|0E0|224|○|System Register Write|store SPR| |SRSPW|0011100000|O1| |SPR = Rd|not generate flags| | | | | | |
|0E1|225| | |store PDTR| |SRPDTW|0011100001|O1| |PDTR = Rd|not generate flags| | |カーネルモードのみ実行可能| |特権違反| |
|0E5|229|○| |store PSR\_IM| |SRIEIW|0011100101|O1|I11|PSR = \(PSR & 0xFFFFFFFB\) &\#124; \(\(Rs << 2\) & 0x00000004\)|not generate flags| | |ルートモードのみ実行可能|3|特権違反|1で許可|
|0E8|232| | |store TISR| |SRTISW|0011101000|O1| |TISPR = Rd|not generate flags| | |ルートモードのみ実行可能|3|特権違反| |
|0E9|233| | |store KPDTR| |SRKPDTW|0011101001|O1| |KPDTR = Rd|not generate flags| | |ルートモードのみ実行可能|3|特権違反| |
|0EA|234| | |store PSR\_MMUMOD| |SRMMUW|0011101010|O1|I11|PSR = \(PSR & 0xFFFFFFFC\) &\#124; \(Rs & 0x0000003\)|not generate flags| | |ルートモードのみ実行可能|3|特権違反|0=アドレス変換なし, 1=予約, 2=1段変換, 3=2段変換|
|0ED|237|○| |store PPSR| |SRPPSW|0011101101|O1| |PPSR = Rd|not generate flags| | | | | | |
|0EE|238|○| |store PPCR| |SRPPCW|0011101110|O1| |PPCR = Rd|not generate flags| | | | | | |
|0F0|240| | |store PPDTR| |SRPPDTW|0011110000|O1| |PPDTR = Rd|not generate flags| | | | | | |
|0F1|241| | |store PTIDR| |SRPTIDW|0011110001|O1| |PTIDR = Rd|not generate flags| | | | | | |
|0F2|242|○| |store IDTR| |SRIDTW|0011110010|O1| |IDTR = Rd|not generate flags| | | | | | |
|0F3|243|○| |store PSR| |SRPSW|0011110011|O1| |PSR = Rd|not generate flags| | | | | | |
|0F4|244|○| |store FRCR from \{FRCLR, FRCHR\}| |SRFRCW|0011110100|C| |FRCR = \{FRCLR, FRCHR\}|not generate flags| | | | | | |
|0F5|245|○| |store FRCLR| |SRFRCLW|0011110101|O1| |FRCLR|not generate flags| | | | | | |
|0F6|246|○| |store FRCHR| |SRFRCHW|0011110110|O1| |FRCHR|not generate flags| | | | | | |
|0FF|255|○| |store PSR add immediate|sign extension・2bit left shift|SRSPADD|0011111111| |CI16|SPR = SPR \+ immediate|not generate flags| | | | | | |
|100|256|○|Other|no operation| |NOP|0100000000|C| |no operation|not generate flags| | | | | | |
|101|257| | |pipline halt| |HALT|0100000001|C| |halt|not generate flags| | |kernelモードのみ実行可能|3|特権違反| |
|102|258|○| |move data| |MOVE|0100000010|O2| |Rd = Rs|not generate flags| | | | | | |
|103|259|○| |move PCR add immediate|sign extension・2bit left shift|MOVEPC|0100000011|O2|I11|Rd = Rs \+ PCR|not generate flags| | | | | | |
|120|288| |OS & Interrupt Support|software interrupt | |SWI|0100100000| |I11|Software Interrupt, Interrupt Vector:Mask8bit\(Rs\)|not generate flags| | | | | | |
|121|289| | |test and set| |TAS|0100100001|O2|I11|tas gr\[src0\], mem\[src1\]|not generate flags| | | | | | |
|122|290|○| |set interrupt discriptor table| |IDTS|0100100010|C| |CoreIDT = MEMORY\[IDTR\]|フラグを発生しない| | |カーネルモードのみ| |特権違反|IDTRの情報をもとにハードウェア割り込みの情報を内部レジスタに退避|
|123|291| | |load linked| |LDL|0100100011| | | | | | | | | | |
|124|292| | |store conditional| |STC|0100100100| | | | | | | | | | |
