MIST32 Instruction Format
==========

|Addr[Hex]|Addr[Dec]|Type|Instruction|Immediate|Mnemonic|Format1(Operand/Disp)|Format2(Imm)|Operation|Flag|AFE-Format1|AFE-Format2(Imm)|実行権限|トラップ番号|例外発生の条件|備考|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|000|0|integer|add|符号拡張|ADD|O2|I11|Rd = Rd + Rs||||||||
|001|1||sub|符号拡張|SUB|O2|I11|Rd = Rd - Rs||||||||
|002|2||mul output Low 32bit|符号拡張|MULL|O2|I11|Rd = (Rd * Rs) & 0xFFFFFFFF||||||||
|003|3||mul output High 32bit|符号拡張|MULH|O2|I11|Rd = (Rd * Rs) >> 32||||||||
|004|4||unsigned div||UDIV|O2|I11|Rd = Rd / Rs|||||4|0割の時（結果は0）||
|005|5||unsigned mod||UMOD|O2|I11|Rd = Rd % Rs|||||4|0割の時（結果は0）||
|006|6||cmp|符号拡張|CMP|O2|I11|FLAGR = flags(Rd, Rs)|||||||SUBを行ない、結果を破棄しフラグのみ更新|
|007|7||signed div|符号拡張|DIV|O2|I11|Rd = Rd / Rs|||||4|0割の時（結果は0）||
|008|8||signed mod|符号拡張|MOD|O2|I11|Rd = Rd % Rs|||||4|0割の時（結果は0）||
|009|9||Sign Negative||NEG|O2||Rd = neg(Rs)|フラグを発生しない|||||||
|00A|10||unsigned mul output low 32bit||UMULL|O2|I11|||||||||
|00B|11||unsigned mul output high 32bit||UMULH|O2|I11|||||||||
|00D|13||increment(Cary Output)||IC|O2||Rd = cary_output(Rs + 1)||||||||
|00E|14||add cary output|符号拡張|ADDC|O2|I11|Rd = cary_output(Rd + Rs)||||||||
|010|16||Inc||INC|O2||Rd = Rs + 1||||||||
|011|17||Dec||DEC|O2||Rd = Rs - 1||||||||
|013|19||signed Maximum||MAX|O2|I11|Rd = (Rd >= Rs)? Rd : Rs|フラグを発生しない|||||||
|014|20||signed Minimum||MIN|O2|I11|Rd = (Rd <= Rs)? Rd : Rs|フラグを発生しない|||||||
|015|21||unsigned Maximum||UMAX|O2|I11|Rd = (Rd >= Rs)? Rd : Rs|フラグを発生しない|||||||
|016|22||unsigned Minimum||UMIN|O2|I11|Rd = (Rd <= Rs)? Rd : Rs|フラグを発生しない|||||||
|01C|28||Sign Extension8->32||SEXT8|O2||Rd = Sign Extension8->32(Rs)|フラグを発生しない|||||||
|01D|29||Sign Extension16->32||SEXT16|O2||Rd = Sign Extension16->32(Rs)|フラグを発生しない|||||||
|040|64|Shift|logic shift left||SHL|O2|I11|Rd = Rd<<Rs|最後に追い出されたビットをCFに設定、OFは常にゼロクリア||||1|64以上シフトした場合||
|041|65||logic shift right||SHR|O2|I11|Rd = Rd>>Rs|最後に追い出されたビットをCFに設定、OFは常にゼロクリア||||1|64以上シフトした場合||
|045|69||alithmetic shift right||SAR|O2|I11|Rd = Rd>>>Rs|最後に追い出されたビットをCFに設定、OFは常にゼロクリア||||1|64以上シフトした場合||
|048|72||rotate shift left||ROL|O2|I11|Rd = ROL(Rd, Rs)|最後に追い出されたビットをCFに設定(0bit目に入るビットと同じ)、OFは常にゼロクリア||||1|64以上シフトした場合||
|049|73||rotate shift right||ROR|O2|I11|Rd = ROR(Rd, Rs)|最後に追い出されたビットをCFに設定(31bit目に入るビットと同じ)、OFは常にゼロクリア||||1|64以上シフトした場合||
|060|96|Logic|and||AND|O2||Rd = Rd & Rs||||||||
|061|97||or||OR|O2||Rd = Rd | Rs||||||||
|062|98||xor||XOR|O2||Rd = Rd ^ Rs||||||||
|063|99||not||NOT|O2||Rd = ~Rs||||||||
|064|100||nand||NAND|O2||Rd = ~(Rd & Rs)||||||||
|065|101||nor||NOR|O2||Rd = ~(Rd | Rs)||||||||
|066|102||xnor||XNOR|O2||Rd = ~(Rd ^ Rs)||||||||
|067|103||test||TEST|O2||FLAGR = flags(Rd, Rs)||||||||
|06A|106||write 2Byte1/2（下位16ビット）||WL16|I16||Rd = Rd & 0xFFFF0000 | Rs|フラグを発生しない|||||||
|06B|107||write 2Byte2/2（上位16ビット）||WH16|I16||Rd = Rd & 0x0000FFFF | Rs << 16|フラグを発生しない|||||||
|06C|108||clear bit||CLRB||I11|Rd = clb(Rs)|フラグを発生しない|||||||
|06D|109||set bit||SETB||I11|Rd = stb(Rs)|フラグを発生しない|||||||
|06E|110||clear　word||CLR|O1||Rd = 0x00000000|フラグを発生しない|||||||
|06F|111||set word||SET|O1||Rd = 0xFFFFFFFF|フラグを発生しない|||||||
|070|112||ビットリバース命令||REVB|O2||Rd = rvbi(Rs)|フラグを発生しない|||||||
|071|113||バイトリバース命令||REV8|O2||Rd = rvby(Rs)|フラグを発生しない|||||||
|072|114||Get Bit||GETB|O2|I11|Rd = (Rd >> Rs) & 0x00000001|フラグを発生しない|||||||
|073|115||Get Byte||GET8|O2|I11|Rd = (Rd >> Rs*8) & 0x000000FF|フラグを発生しない|||||||
|076|118||Signed Load Immediate(Low)||LIL||I16|Rd = SignExtension(Rs)|フラグを発生しない|||||||
|077|119||Signed Load Immediate(High)||LIH||I16|Rd = Rs<<16|フラグを発生しない|||||||
|07A|122||Unsigned Load Immediate||ULIL||I16|Rd = Rs||||||||
|080|128|Memory Access|load register or immediate||LD8|O2|I11|Rd = mask(MEMORY[Rs], 8)|フラグを発生しない|MA|MA||2|メモリ保護違反の場合||
|081|129|||1bit左シフト|LD16|O2|I11|O2の時 : Rd = mask(MEMORY[Rs], 16) I11の時Rd = mask(MEMORY[Rs>>1], 16)|フラグを発生しない|MA|MA||2|メモリ保護違反の場合||
|082|130|||2bit左シフト|LD32|O2|I11|O2の時 : Rd = mask(MEMORY[Rs], 16) I11の時Rd = mask(MEMORY[Rs>>2], 16)|フラグを発生しない|MA|MA||2|メモリ保護違反の場合||
|083|131||store register or immediate||ST8|O2|I11|MEMORY[Rs] = mask(Rd, 8)|フラグを発生しない||||2|メモリ保護違反の場合||
|084|132|||1bit左シフト|ST16|O2|I11|O2の時 : MEMORY[Rs] = mask(Rd, 16) I11の時 : MEMORY[Rs>>1] = mask(Rd, 16)|フラグを発生しない||||2|メモリ保護違反の場合||
|085|133|||2bit左シフト|ST32|O2|I11|O2の時 : MEMORY[Rs] = mask(Rd, 16) I11の時 : MEMORY[Rs>>2] = mask(Rd, 16)|フラグを発生しない||||2|メモリ保護違反の場合||
|088|136||push|符号拡張|PUSH|O1|CI16|MEMORY[SPR] = Rd|フラグを発生しない||||2|メモリ保護違反の場合||
|089|137||Program Counter Push||PUSHPC|C||MEMORY[SPR] = PC + 8|フラグを発生しない||||2|メモリ保護違反の場合||
|090|144||pop||POP|O1||Rd = MEMORY[SPR]|フラグを発生しない||MA||2|メモリ保護違反の場合||
|09A|154||with signed displacement||LDD8|O2||Rd = mask(MEMORY[Rs+displacement], 8)|フラグを発生しない|MA|||2|メモリ保護違反の場合||
|09B|155||with signed displacement|1bit左シフト|LDD16|O2||Rd = mask(MEMORY[Rs+displacement], 16)|フラグを発生しない|MA|||2|メモリ保護違反の場合||
|09C|156||with signed displacement|2bit左シフト|LDD32|O2||Rd = mask(MEMORY[Rs+displacement], 16)|フラグを発生しない|MA|||2|メモリ保護違反の場合||
|09D|157||with signed displacement||STD8|O2||MEMORY[Rs] = mask(Rd+displacement, 8)|フラグを発生しない||||2|メモリ保護違反の場合||
|09E|158||with signed displacement|1bit左シフト|STD16|O2||MEMORY[Rs] = mask(Rd+displacement, 16)|フラグを発生しない||||2|メモリ保護違反の場合||
|09F|159||with signed displacement|2bit左シフト|STD32|O2||MEMORY[Rs] = mask(Rd+displacement, 16)|フラグを発生しない||||2|メモリ保護違反の場合||
|0A0|160|Branch|(PC relative addressing) register or imm Unsigned!|2bit左シフト|BUR|JO1|JI16|PC = PC + unsigned(Rd)|フラグを発生しない||||2|メモリ保護違反の場合|Word Addressing|
|0A1|161||(PC relative addressing) register or imm Signed!|2bit左シフト|BR|JO1|JI16|PC = PC + signed(Rd)|フラグを発生しない||||2|メモリ保護違反の場合|Word Addressing|
|0A2|162||(direct addressing)register or immediate|2bit左シフト|B|JO1|JI16|PC = unsigned(Rd)|フラグを発生しない||||2|メモリ保護違反の場合|Word Addressing|
|0A3|163||(IRQ Ret)(direct addressing)register or immediate(CC Non Suport )|2bit左シフト|IB|C||PC = unsigned(Rd)|フラグを発生しない||||2|メモリ保護違反の場合|Word Addressing 割り込みルーチンからの復帰に使用(特権操作) CCはALしか対象外。それ以外は未定義|
|0B0|176||(PC relative addressing) register or imm Unsigned!|2bit左シフト|BURN|JO1|JI16|PC = PC + unsigned(Rd)|フラグを発生しない||||2|メモリ保護違反の場合|Word Addressing|
|0B1|177||(PC relative addressing) register or imm Signed!|2bit左シフト|BRN|JO1|JI16|PC = PC + signed(Rd)|フラグを発生しない||||2|メモリ保護違反の場合|Word Addressing|
|0B2|178||(direct addressing)register or immediate|2bit左シフト|BN|JO1|JI16|PC = unsigned(Rd)|フラグを発生しない||||2|メモリ保護違反の場合|Word Addressing|
|0C0|192|System Register Read|Stack Point Register Read||SRSPR|O1||Rd = SPR|フラグを発生しない|||||||
|0C1|193||PDTR Read||SRPDTR|O1||Rd = PDTR|フラグを発生しない|||||||
|0C2|194||CPU ID Read||SRPIDR|O1||Rd = CPUIDR|フラグを発生しない|||||||
|0C3|195||Core ID Read||SRCIDR|O1||Rd = COREIDR|フラグを発生しない|||||||
|0C4|196||Core Mode Read||SRMODER|O1||Rd = mask(SR1)|フラグを発生しない|||||||
|0C5|197||Interrupt Enable Information Read||SRIEIR|O1||Rd = (PSR & 0x00000004) >> 2|フラグを発生しない||||||1で許可|
|0C8|200||TISR Read ||SRTISR|O1||Rd = TISR|フラグを発生しない|||カーネルモードのみ実行可能|3|特権違反||
|0C9|201||KPDTR||SRKPDTR|O1||Rd = KPDTR|フラグを発生しない|||カーネルモードのみ実行可能|3|特権違反||
|0CA|202||MMU Mode Read||SRMMUR|O1||Rd = mask(SR1)|フラグを発生しない||||||0=アドレス変換なし, 1=予約, 2=1段変換, 3=2段変換|
|0CB|203||IOSR Read||SRIOSR|O1||Rd = IOSR|フラグを発生しない|||||||
|0CC|204||Task ID(TID) Read||SRTIDR|O1||Rd = TIDR|フラグを発生しない|||||||
|0CD|205||PPSR Read||SRPPSR|O1|||フラグを発生しない|||||||
|0CE|206||PPCR Read||SRPPCR|O1|||フラグを発生しない|||||||
|0D0|208||PPDTR Read||SRPPDTR|O1|||フラグを発生しない|||||||
|0D1|209||PTIDR Read||SRPTIDR|O1|||フラグを発生しない|||||||
|0D3|211||PSR Read||SRPSR|O1|||フラグを発生しない|||||||
|0D4|212||FRCR -> {FRCHR, FRCLW}||SRFRCR|C|||フラグを発生しない|||||||
|0D5|213||FRCLR Read||SRFRCLR|O1|||フラグを発生しない|||||||
|0D6|214||FRCHR Read||SRFRCHR|O1|||フラグを発生しない|||||||
|0D7|215||PFLAGR Read||SRPFLAGR|O1||Rd = SRPFLAGR|フラグを発生しない|||||||
|0E0|224|System Register Write|Stack Point Register Write||SRSPW|O1||SPR = Rd|フラグを発生しない|||||||
|0E1|225||Page Directory Table Register Write||SRPDTW|O1|||フラグを発生しない|||カーネルモードのみ実行可能||特権違反||
|0E5|229||Interrupt Enable Information Write||SRIEIW|O1|I11|mask(SR1) = (Rs & 0x00000004) >> 2|フラグを発生しない|||ルートモードのみ実行可能|3|特権違反|1で許可|
|0E8|232||TISR Write ||SRTISW|O1||TISPR = Rd|フラグを発生しない|||ルートモードのみ実行可能|3|特権違反||
|0E9|233||KPDTR Write||SRKPDTW|O1||KPDTR = Rd|フラグを発生しない|||ルートモードのみ実行可能|3|特権違反||
|0EA|234||MMU Mode Write||SRMMUW|O1|I11|mask(SR1) = Rs & 0x00000011|フラグを発生しない|||ルートモードのみ実行可能|3|特権違反|0=アドレス変換なし, 1=予約, 2=1段変換, 3=2段変換|
|0ED|237||PPSR Write||SRPPSW|O1|||フラグを発生しない|||||||
|0EE|238||PPCR Write||SRPPCW|O1|||フラグを発生しない|||||||
|0F0|240||PPDTR Write||SRPPDTW|O1|||フラグを発生しない|||||||
|0F1|241||PTIDR Write||SRPTIDW|O1|||フラグを発生しない|||||||
|0F2|242||IDTR Write||SRIDTW|O1|||フラグを発生しない|||||||
|0F3|243||PSR Write||SRPSW|O1|||フラグを発生しない|||||||
|0F4|244||{FRCLR, FRCHR} -> FRCR||SRFRCW|C|||フラグを発生しない|||||||
|0F5|245||FRCLR Write||SRFRCLW|O1|||フラグを発生しない|||||||
|0F6|246||FRCHR Write||SRFRCHW|O1|||フラグを発生しない|||||||
|0FF|255||SPR + Immediate|符号拡張　2bit左シフト|SRSPWADD||CI16|SPR = SPR + signed immediate|フラグを発生しない|||||||
|100|256|Other|No Operation||NOP|C||No Operation|フラグを発生しない|||||||
|101|257||pipline is halt||HALT|C||Halt|フラグを発生しない|||kernelモードのみ実行可能|3|特権違反||
|102|258||move data||MOVE|O2||Rd = Rs|フラグを発生しない|||||||
|103|259||Move Programm Counter + Offset|符号拡張　2bit左シフト|MOVEPC|O2|I11|Rd = Rs(Signed) + PC|フラグを発生しない|||||||
|120|288|OS & Interrupt Support|Software Interrupt ||SWI||I11|Software Interrupt, Interrupt Vector:Mask8bit(Rs)|フラグを発生しない|||||||
|121|289||Test And Set||TAS|O2|I11|tas gr[src0], mem[src1]|フラグを発生しない|||||||
|122|290||IDT Set||IDTS|C||Set IDT|フラグを発生しない|||カーネルモードのみ||特権違反|IDTRの情報をもとにハードウェア割り込みの情報を内部レジスタに退避|
|123|291||Load Linked||LDL|||||||||||
|124|292||Store Conditional||STC|||||||||||
