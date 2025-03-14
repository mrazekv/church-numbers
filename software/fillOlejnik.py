# nacteni rejstriku z https://www.zaltar.cz/rejstrik.html
alld = """
OL1 – Do domu Hospodinova s radostí půjdeme. – Žalm 122
OL2 – Zaradoval jsem se, když mi řekli: „Do domu Hospodinova půjdeme!“ – Žalm 122
OL3 – Bože, obnov nás, rozjasni svou tvář, a budeme spaseni. – Žalm 80
OL4 – K tobě pozvedám svou duši, Hospodine. – Žalm 25
OL5 – Pane, Bože můj, k tobě pozvedám svou duši. – Žalm 25
OL6 – Do domu Hospodinova s radostí půjdeme. – Žalm 122
OL7 – V jeho dnech rozkvete spravedlnost a hojnost pokoje na věky. – Žalm 72
OL8 – Smím přebývat v Hospodinově domě, na dlouhé, předlouhé časy. – Žalm 23
OL9 – Děkujte Hospodinu, neboť je dobrý, jeho milosrdenství trvá na věky. – Žalm 118
OL10 – Hospodin je mé světlo a má spása. – Žalm 27
OL11 – Pán je mé světlo a má spása. – Žalm 27
OL12 – Chvalte Hospodina, který uzdravuje ty, jimž puká srdce. – Žalm 147
OL13 – Pane, ukaž nám své milosrdenství! – Žalm 85
OL14 – Pane, ukaž nám své milosrdenství a uděl nám svou spásu. – Žalm 85
OL15 – Ukaž nám, Hospodine, své milosrdenství a dej nám svou spásu! – Žalm 85
OL16 – Velkou věc s námi učinil Hospodin, naplnila nás radost. – Žalm 126
OL17 – Vypravujte mezi všemi národy o Hospodinových divech. – Žalm 96
OL18 – Veleb, duše má, Hospodina. – Žalm 104
OL19 – Budu tě oslavovat na věky, můj Bože, králi. – Žalm 145
OL20 – Blaze tomu, kdo svou naději vložil do Hospodina. – Žalm 1
OL21 – Pane, přijď, a zachraň nás! – Žalm 146
OL22 – Duch můj plesá v Bohu mém! – Lk 1
OL23 – Plesejte a jásejte, neboť nad vámi vládne Svatý Izraele. – Iz 12
OL24 – Ukaž mi své cesty, Hospodine. – Žalm 25
OL25 – Hle, ubožák zavolal, a Hospodin slyšel. – Žalm 34
OL26 – Chci tě oslavovat, Hospodine, neboť jsi mě vysvobodil. – Žalm 30
OL27 – Ať tě, Bože, velebí národy, ať tě velebí, kdekterý národ! – Žalm 67
OL28 – Ať vejde Hospodin, on je král slávy! – Žalm 24
OL29 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL30 – V jeho dnech rozkvete spravedlnost a hojnost pokoje na věky. – Žalm 72
OL31 – V jeho dnech rozkvete spravedlnost a hojnost pokoje na věky. – Žalm 72
OL32 – Ústa má budou vyprávět o tvé spravedlnosti. – Žalm 71
OL33 – Radujte se, spravedliví, v Hospodinu. – Žalm 33
OL34 – Mé srdce jásá v Bohu, mém spasiteli. – 1. Sam 2
OL35 – Na věky budu zpívat o tvém milosrdenství, Hospodine. – Žalm 89
OL36 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL37 – Dnes se nám narodil Spasitel, Kristus Pán. – Žalm 96
OL38 – Světlo dnes zazáří nad námi, neboť se nám narodil Pán. – Žalm 97
OL39 – Všechny končiny země viděly spásu od našeho Boha. – Žalm 98
OL40 – Uzřely všechny končiny země spásu našeho Boha. – Žalm 98
OL41 – Blaze každému, kdo se bojí Hospodina, kdo kráčí po jeho cestách. – Žalm 128
OL42 – Blaze každému, kdo se bojí Hospodina. – Žalm 128
OL43 – Hospodin sám je náš Bůh, pamatuje věčně na svoji smlouvu. – Žalm 105
OL44 – Hospodin pamatuje věčně na svoji smlouvu. – Žalm 105
OL45 – Blaze těm, kdo přebývají v tvém domě, Bože. – Žalm 84
OL46 – Šťastní jsou, Pane, kdo přebývají ve tvém svatém chrámě. – Žalm 84
OL47 – Vypravujte mezi všemi národy o Hospodinových divech. – Žalm 96
OL48 – Vypravujte mezi všemi národy o Hospodinových divech. – Žalm 96
OL49 – Vypravujte mezi všemi národy o Hospodinových divech. – Žalm 96
OL50 – Hospodine, Pane náš, jak podivuhodné je tvé jméno po celé zemi! – Žalm 8
OL51 – Bože, buď milostiv a žehnej nám! – Žalm 67
OL52 – Slovo se stalo tělem a přebývalo mezi námi. – Žalm 147
OL53 – Uzřely všechny končiny země spásu našeho Boha. – Žalm 98
OL54 – Uzřely všechny končiny země spásu našeho Boha. – Žalm 98
OL55 – Uzřely všechny končiny země spásu našeho Boha. – Žalm 98
OL56 – Pojďte se poklonit Pánu! – Žalm 100
OL57 – Jeruzaléme, oslavuj Hospodina! – Žalm 147
OL58 – Hospodin miluje svůj národ. – Žalm 149
OL59 – Budou se ti, Hospodine, klanět všechny národy. – Žalm 72
OL60 – Dám ti v majetek národy. – Žalm 2
OL61 – Budou se ti, Hospodine, klanět všechny národy. – Žalm 72
OL62 – Budou se ti, Hospodine, klanět všechny národy. – Žalm 72
OL63 – Budou se ti, Hospodine, klanět všechny národy. – Žalm 72
OL64 – Pán dá požehnání a pokoj svému lidu. – Žalm 29
OL65 – Budete vážit vodu s radostí z pramenů spásy. – Iz 12
OL66 – Veleb, duše má, Hospodina. – Žalm 104
OL67 – Smiluj se, Pane, neboť jsme zhřešili. – Žalm 51
OL68 – Stvoř mi čisté srdce Bože! – Žalm 51
OL69 – Tys, Pane, dobrý a shovívavý. – Žalm 86
OL70 – Všechno tvé jednání, Hospodine, je láska a věrnost pro ty, kdo plní tvou smlouvu. – Žalm 25
OL71 – Buď se mnou, Pane, v mé tísni. – Žalm 91
OL72 – Tvá slova, Pane, jsou duch a jsou život. – Žalm 19
OL73 – Pán mě vysvobodil ze všech mých obav. – Žalm 34
OL74 – Stvoř mi čisté srdce Bože! – Žalm 51
OL75 – Když jsem volal, Hospodine, vyslyšels mě. – Žalm 138
OL76 – U Hospodina je slitování, hojné u něho je vykoupení. – Žalm 130
OL77 – Blaze těm, kdo kráčejí v zákoně Hospodinově. – Žalm 119
OL78 – Ať spočine na nás, Hospodine, tvé milosrdenství, jak doufáme v tebe. – Žalm 33
OL79 – Budu kráčet před Hospodinem v zemi živých. – Žalm 116
OL80 – Hospodin je mé světlo a má spása. – Žalm 27
OL81 – Nejednej s námi podle našich hříchů, Hospodine! – Žalm 79(78)
OL82 – Kdo žije správně, tomu ukážu Boží spásu. – Žalm 50
OL83 – Zachraň mě svou slitovností, Hospodine. – Žalm 31
OL84 – Pamatujte na divy, které učinil Hospodin. – Žalm 105
OL85 – Hospodin je milosrdný a milostivý. – Žalm 103
OL86 – Kéž byste dnes uposlechli jeho hlasu: „Nezatvrzujte svá srdce!“ – Žalm 95
OL87 – Zaslechnete-li dnes jeho hlas, nezatvrzujte svá srdce! – Žalm 95
OL88 – Pane, ty máš slova věčného života. – Žalm 19
OL89 – Hospodin je milosrdný a milostivý. – Žalm 103
OL90 – Má duše žízní po tobě, Pane, Bože můj! – Žalm 42
OL91 – Rozpomeň se, Hospodine, na své slitování. – Žalm 25
OL92 – Jeruzaléme, oslavuj Hospodina! – Žalm 147
OL93 – Plesejte Bohu, který nám pomáhá. – Žalm 81
OL94 – Smiluj se, Pane, neboť jsme zhřešili. – Žalm 51
OL95 – Hospodin je můj pastýř, nic nepostrádám. – Žalm 23
OL96 – Pán je můj pastýř, nic mi neschází. – Žalm 23
OL97 – Vyslyš nás, Pane, a vysvoboď nás. – Žalm 137
OL98 – Okuste a vizte, jak je Hospodin dobrý. – Žalm 34
OL99 – Proudy bystřin jsou k radosti Božímu městu, přesvatému stánku Nejvyššího. – Žalm 46
OL100 – Blízký je Hospodin všem, kdo ho vzývají. – Žalm 145
OL101 – Pamatuj na nás, Hospodine, pro náklonnost k svému lidu. – Žalm 106
OL102 – Hle, ubožák zavolal, a Hospodin slyšel. – Žalm 34
OL103 – Hospodine, můj Bože, k tobě se utíkám. – Žalm 7
OL104 – Stvoř mi čisté srdce, Bože! – Žalm 51
OL105 – Stvoř mi čisté srdce Bože! – Žalm 51
OL106 – Hospodine, slyš mou modlitbu a volání mé ať k tobě pronikne! – Žalm 102
OL107 – chvályhodný a svrchovaně velebený navěky. – Dan 3
OL108 – Hospodin pamatuje věčně na svoji smlouvu. – Žalm 105
OL109 – Miluji tě, Hospodine, má sílo! – Žalm 18
OL110 – Hospodin bude nad námi bdít, jako pastýř nad svým stádem. – Jer 31
OL111 – Bože můj, Bože můj, proč jsi mne opustil? – Žalm 22
OL112 – Hospodin je mé světlo a má spása. – Žalm 27
OL113 – Ústa má budou vyprávět o tvé spravedlnosti. – Žalm 71
OL114 – Vyslyš mě, Hospodine, ve své veliké lásce! – Žalm 69
OL115 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL116 – Kalich požehnání je společenstvím Krve Kristovy. – Žalm 116
OL117 – Otče, do tvých rukou poroučím ducha svého. – Žalm 31
OL118 – Sešli svého ducha, Pane, a obnov tvářnost země. – Žalm 104
OL119 – Země je plná Hospodinovy milosti. – Žalm 33
OL120 – Ochraň mě, Bože, neboť se k tobě utíkám. – Žalm 16
OL121 – Hospodinu chci zpívat, neboť je velmi vznešený. – Ex 15
OL122 – Jako laň prahne po vodních bystřinách, tak prahne má duše po tobě, Bože! – Žalm 42
OL123 – Stvoř mi čisté srdce, Bože! – Žalm 51
OL124 – Toto je den, který připravil Pán, jásejme a radujme se z něho! – Žalm 118
OL125 – Ochraň mě, Bože, neboť se k tobě utíkám. – Žalm 16
OL126 – Země je plná Hospodinovy milosti. – Žalm 33
OL127 – Ze srdce ať se radují, kdo hledají Hospodina. – Žalm 105
OL128 – Hospodine, Pane náš, jak podivuhodné je tvé jméno po celé zemi! – Žalm 8
OL129 – Kámen, který stavitelé zavrhli, stal se kvádrem nárožním. – Žalm 118
OL130 – Děkujte Hospodinu, neboť je dobrý, jeho milosrdenství trvá na věky. – Žalm 118
OL131 – Děkujte Hospodinu, neboť je dobrý, jeho milosrdenství trvá na věky. – Žalm 118
OL132 – Děkujte Hospodinu, neboť je dobrý, jeho milosrdenství trvá na věky. – Žalm 118
OL133 – Děkujte Hospodinu, neboť je dobrý, jeho milosrdenství trvá na věky. – Žalm 118
OL134 – Blaze všem, kdo se uchylují k Hospodinu. – Žalm 2
OL135 – Hospodin kraluje, oděl se velebností. – Žalm 93
OL136 – Hle, ubožák zavolal, a Hospodin slyšel. – Žalm 34
OL137 – Hle, ubožák zavolal, a Hospodin slyšel. – Žalm 34
OL138 – Ať spočine na nás, Hospodine, tvé milosrdenství, jak doufáme v tebe. – Žalm 33
OL139 – Ukaž mi, Pane, cestu k životu. – Žalm 16
OL140 – Hospodine, ukaž nám svou jasnou tvář! – Žalm 4
OL141 – Blaze těm, kdo kráčejí v zákoně Hospodinově. – Žalm 119
OL142 – Do tvých rukou, Pane, svěřuji ducha svého. – Žalm 31
OL143 – Jásejte Bohu, všechny země! – Žalm 66
OL144 – Jásejte Bohu, všechny země! – Žalm 66
OL145 – Jděte do celého světa a hlásejte evangelium. – Žalm 117
OL146 – Vezmu kalich spásy a budu vzývat jméno Hospodinovo. – Žalm 116
OL147 – Kámen, který stavitelé zavrhli, stal se kvádrem nárožním. – Žalm 118
OL148 – Jsme jeho lid a stádce, které on pase. – Žalm 100
OL149 – Chvalte Hospodina, všechny národy! – Žalm 87
OL150 – Ať tě, Bože, velebí národy, ať tě velebí, kdekterý národ! – Žalm 67
OL151 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL152 – Ty jsi můj syn, já dnes jsem tě zplodil. – Žalm 2
OL153 – Budu tě chválit, Hospodine, ve velkém shromáždění. – Žalm 22
OL154 – Budu tě oslavovat na věky, můj Bože, králi. – Žalm 145
OL155 – Nikoliv nám, Hospodine, ale svému jménu zjednej slávu. – Žalm 115
OL156 – Ať tvoji zbožní, Hospodine, vypravují o slávě tvé vznešené říše. – Žalm 145
OL157 – Do domu Hospodinova s radostí půjdeme. – Žalm 122
OL158 – Vypravujte mezi všemi národy o Hospodinových divech. – Žalm 96
OL159 – Budu tě chválit mezi národy, Pane! – Žalm 57
OL160 – Pojďte se poklonit Pánu! – Žalm 100
OL161 – Jásejte Bohu, všechny země! – Žalm 66
OL162 – Jásejte Bohu, všechny země! – Žalm 66
OL163 – Jásejte Bohu, všechny země! Aleluja. – Žalm 66
OL164 – Hospodin zjevil svou spásu před zraky pohanů. – Žalm 98
OL165 – Jinoši a panny, chvalte Hospodinovo jméno! – Žalm 148
OL166 – Bůh se vznáší za jásotu, Hospodin vystupuje za hlaholu polnice. – Žalm 47
OL167 – Bůh se vznáší za jásotu, Hospodin vystupuje za hlaholu polnice. – Žalm 47
OL168 – Bůh se vznáší za jásotu, Hospodin vystupuje za hlaholu polnice. – Žalm 47
OL169 – Věřím, že uvidím blaho od Hospodina v zemi živých! – Žalm 27
OL170 – Hospodin si zřídil na nebi trůn. – Žalm 103
OL171 – Hospodin kraluje, je povznesen nad celou zemí. – Žalm 97
OL172 – Bože, ve své dobrotě ses postaral o chudáka. – Žalm 68
OL173 – Bože, ve své dobrotě ses postaral o chudáka. – Žalm 68
OL174 – Bože, ve své dobrotě ses postaral o chudáka. – Žalm 68
OL175 – Zbožní uzří tvou tvář, Hospodine. – Žalm 11
OL176 – Blaze lidu, který si Hospodin vyvolil za svůj majetek. – Žalm 33
OL177 – Oslavujte Hospodina, neboť na věky trvá jeho milosrdenství. – Žalm 107
OL178 – Sešli svého ducha, Hospodine, a obnovíš tvář země. – Žalm 104
OL179 – Sešli svého ducha, Pane, a obnov tvářnost země. – Žalm 104
OL180 – Sešli svého ducha, Hospodine, a obnovíš tvář země. – Žalm 104
OL181 – Sešli svého ducha, Pane, a obnov tvářnost země. – Žalm 104
OL182 – Chvalte Hospodina, všechny národy! – Žalm 87
OL183 – Hle, přicházím, Pane, splnit tvou vůli. – Žalm 40
OL184 – Ty jsi kněz na věky podle Melchizedechova řádu! – Žalm 110
OL185 – Hospodin je můj pastýř, nic nepostrádám. – Žalm 23
OL186 – Blaze lidu, který si Hospodin vyvolil za svůj majetek. – Žalm 33
OL187 – Vezmu kalich spásy a budu vzývat jméno Hospodinovo. – Žalm 116
OL188 – Ty jsi kněz na věky podle Melchizedechova řádu! – Žalm 110
OL189 – Hospodinova láska od věků pro ty, kdo se ho bojí. – Žalm 103
OL190 – Hle, přicházím, Pane, splnit tvou vůli. – Žalm 40
OL191 – Vypravujte mezi všemi národy o Hospodinových divech. – Žalm 96
OL192 – Blahoslavení chudí v duchu, neboť jejich je království nebeské. – Žalm 146
OL193 – Spravedlivý září v temnotách jako světlo. – Žalm 112
OL194 – Budu ti hrát, Hospodine, před anděly. – Žalm 138
OL195 – Blaze těm, kdo kráčejí v zákoně Hospodinově. – Žalm 119
OL196 – Tys mé útočiště, zahrneš mě radostí ze záchrany. – Žalm 32
OL197 – Hospodin je milosrdný a milostivý. – Žalm 103
OL198 – Pán je milosrdný a milostivý. – Žalm 103
OL199 – Uzdrav mě, Pane, zhřešil jsem proti tobě. – Žalm 41
OL200 – V Bohu jen odpočívej, duše má. – Žalm 62
OL201 – Dobré je chválit Hospodina. – Žalm 92
OL202 – Buď mi, Hospodine, ochrannou skálou! – Žalm 31
OL203 – Plesejte Bohu, který nám pomáhá. – Žalm 81
OL204 – Kdo žije správně, tomu ukážu Boží spásu. – Žalm 50
OL205 – Odpusť, Pane, co jsem zavinil hříchem. – Žalm 32
OL206 – Vyslyš mě, Hospodine, ve své veliké lásce! – Žalm 69
OL207 – Oslavujte Hospodina, neboť na věky trvá jeho milosrdenství. – Žalm 107
OL208 – Má duše žízní po tobě, Pane, Bože můj! – Žalm 63
OL209 – Má duše po tobě žízní, Hospodine, Bože můj! – Žalm 63
OL210 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL211 – Ty jsi, Hospodine, mým dědičným podílem. – Žalm 16
OL212 – Budu velebit tvé jméno, můj Bože, králi. – Žalm 145
OL213 – Bože, můj králi, na věky chci dobrořečit tvému jménu. – Žalm 145
OL214 – Naše oči hledí na Hospodina, dokud se nad námi nesmiluje. – Žalm 123
OL215 – Semeno padlo na dobrou půdu a přineslo užitek. – Žalm 65
OL216 – Hledejte, ubožáci, Hospodina a pookřejte v srdci. – Žalm 69
OL217 – Hospodinovy předpisy jsou správné, působí radost srdci. – Žalm 19
OL218 – Tys, Pane, dobrý a shovívavý. – Žalm 86
OL219 – Hospodine, kdo smí prodlévat ve tvém stánku? – Žalm 15
OL220 – Jak miluji tvůj zákon, Hospodine. – Žalm 119
OL221 – Otvíráš svou ruku a sytíš nás, Hospodine. – Žalm 145
OL222 – Když jsem volal, Hospodine, vyslyšels mě. – Žalm 138
OL223 – Otvíráš svou ruku a sytíš nás, Hospodine. – Žalm 145
OL224 – Nebeský pokrm dal jim Hospodin. – Žalm 78
OL225 – Pane, tys nám býval útočištěm od pokolení do pokolení. – Žalm 90
OL226 – Okuste a vizte, jak je Hospodin dobrý. – Žalm 34
OL227 – Okuste a vizte, jak dobrý je Pán. – Žalm 34
OL228 – Blaze lidu, který si Hospodin vyvolil za svůj majetek. – Žalm 33
OL229 – Okuste a vizte, jak je Hospodin dobrý. – Žalm 34
OL230 – Hospodine, na pomoc mi pospěš! – Žalm 40
OL231 – Hospodine, tvá dobrota trvá na věky, dílo svých rukou neopouštěj! – Žalm 138
OL232 – Okuste a vizte, jak je Hospodin dobrý. – Žalm 34
OL233 – Bože, ve své dobrotě ses postaral o chudáka. – Žalm 68
OL234 – Duše má, chval Hospodina! – Žalm 146
OL235 – Budu kráčet před Hospodinem v zemi živých. – Žalm 116
OL236 – Vstanu a půjdu k svému Otci. – Žalm 51
OL237 – Blízký je Hospodin všem, kdo ho vzývají. – Žalm 145
OL238 – Pán mě udržuje naživu. – Žalm 54
OL239 – Chvalte Hospodina, který povyšuje chudého. – Žalm 113
OL240 – Hospodinovy předpisy jsou správné, působí radost srdci. – Žalm 19
OL241 – Dům Izraelův je vinicí Páně. – Žalm 80
OL242 – Ať nám Hospodin žehná po všechny dny našeho života. – Žalm 128
OL243 – Nasyť nás, Pane, svou slitovností, abychom se radovali. – Žalm 90
OL244 – Vzdejte Hospodinu moc a slávu! – Žalm 96
OL245 – Pomoc nám přijde od Hospodina, který učinil nebe i zemi. – Žalm 121
OL246 – Miluji tě, Hospodine, má sílo! – Žalm 18
OL247 – Miluji tě, Hospodine, má sílo! – Žalm 18
OL248 – Hle, ubožák zavolal, a Hospodin slyšel. – Žalm 34
OL249 – Opatruj, Pane, mou duši ve svém pokoji! – Žalm 131
OL250 – Ochraň, Pane, duši mou v pokoji u tebe. – Žalm 131
OL251 – Má duše po tobě žízní, Hospodine, Bože můj! – Žalm 63
OL252 – Až procitnu, Hospodine, nasytím se pohledem na tebe. – Žalm 17
OL253 – Přišel Hospodin, aby spravoval národy podle práva. – Žalm 98
OL254 – Do domu Hospodinova s radostí půjdeme. – Žalm 122
OL255 – Blahoslavená jsi, Panno Maria, žes nosila Syna věčného Otce. – Lk 1
OL256 – Vypravujte mezi všemi národy o Hospodinových divech. – Žalm 96
OL257 – Hospodin zástupů, on je král slávy! – Žalm 24
OL258 – Ty jsi čest našeho lidu. – Jdt 13
OL259 – Jeho potomstvo potrvá na věky. – Žalm 89
OL260 – Hle, přicházím, Pane, splnit tvou vůli. – Žalm 40
OL261 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL262 – Pane, dej zdar práci našich rukou! – Žalm 90
OL263 – Všude na zemi pronikl jejich hlas. – Žalm 19
OL264 – Pán ho posadil vedle knížat svého lidu. – Žalm 113
OL265 – Vyslyš mě, Bože, ve své veliké lásce! – Žalm 69
OL266 – Hospodin zjevil svou spásu před zraky pohanů. – Žalm 98
OL267 – Od klína mé matky byls mým ochráncem. – Žalm 71
OL268 – Chválím tě, že jsem vznikl tak podivuhodně. – Žalm 139
OL269 – Pán mě vysvobodil ze všech mých obav. – Žalm 34
OL270 – Má zalíbení v Hospodinově zákoně. – Žalm 1
OL271 – Ustavičně chci velebit Hospodina. – Žalm 34
OL272 – Kdo sejí v slzách žnout budou s jásotem. – Žalm 126
OL273 – Pán Bůh mu dá trůn jeho otce Davida. – Žalm 132
OL274 – Hospodin kraluje, je povznesen nad celou zemí. – Žalm 97
OL275 – Blaze muži, který se slitovává a půjčuje. – Žalm 112
OL276 – Vstaň, Hospodine, vejdi na místo svého odpočinku, ty i tvá vznešená archa! – Žalm 132
OL277 – Po své pravici máš královnu ozdobenou ofirským zlatem. – Žalm 45
OL278 – Ať tvoji zbožní, Hospodine, vypravují o slávě tvé vznešené říše. – Žalm 145
OL279 – Radostí zajásám v Pánu. – Žalm 13
OL280 – Nezapomínejte na Boží skutky! – Žalm 78
OL281 – Zachraň mě svou slitovností, Hospodine. – Žalm 31
OL282 – Blaze těm, kdo kráčejí v zákoně Hospodinově. – Žalm 119
OL283 – Ty, Hospodine, vládneš nade vším. – 1. Kron 29
OL284 – Budu ti hrát, Hospodine, před anděly. – Žalm 138
OL285 – Svým andělům vydal o tobě příkaz, aby tě střežili na všech tvých cestách. – Žalm 91
OL286 – To je pokolení těch, kdo hledají tvář tvou, Hospodine. – Žalm 24
OL286a – To je pokolení těch, kdo hledají tvář tvou, Hospodine. – Žalm 24
OL287 – Zpívejte Hospodinu píseň novou, protože učinil podivuhodné věci. – Žalm 98
OL288 – Do tvých rukou, Pane, svěřuji ducha svého. – Žalm 31
OL289 – Radujte se, spravedliví, v Hospodinu. – Žalm 97
OL290 – Naše duše vyvázla jako pták z ptáčníkovy léčky. – Žalm 124
OL291 – Jak milý je tvůj příbytek, Hospodine zástupů! – Žalm 84
OL292 – Ty, Hospodine, vládneš nade vším. – 1. Kron 29
OL293 – Hle, stánek Boží mezi lidmi! – Žalm 84
OL294 – Kéž byste dnes uposlechli jeho hlasu: „Nezatvrzujte svá srdce!“ – Žalm 95
OL295 – Do domu Hospodinova s radostí půjdeme. – Žalm 122
OL296 – Radostně půjdeme do domu Pánova. – Žalm 122
OL297 – Buď veleben Hospodin nyní i na věky! – Žalm 113
OL298 – Po své pravici máš královnu ozdobenou ofirským zlatem. – Žalm 45
OL299 – Ty jsi, Hospodine, mým dědičným podílem. – Žalm 16
OL300 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL301 – Ústa spravedlivého mluví moudře. – Žalm 37
OL302 – Hospodinovy výroky jsou pravdivé, všechny jsou spravedlivé. – Žalm 19
OL303 – Nauč mě, Hospodine, svým příkazům! – Žalm 119
OL304 – Tvá slova, Pane, jsou duch a jsou život. – Žalm 19
OL305 – Ženich je tu, jděte naproti Kristu Pánu! – Žalm 45
OL306 – Hle, ženich přichází, jděte naproti Kristu Pánu! – Žalm 45
OL307 – Spravedlivý bude, Pane, přebývat na tvé svaté hoře. – Žalm 15
OL308 – Blaze muži, který se bojí Hospodina. – Žalm 112
OL309 – Veleb, duše má, Hospodina. – Žalm 103
OL310 – Ustavičně chci velebit Hospodina. – Žalm 34
OL311 – Chci dobrořečit Pánu v každé chvíli. – Žalm 34
OL312 – Okuste a vizte, jak je Hospodin dobrý. – Žalm 34
OL313 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL314 – Jásejte Bohu, všechny země! – Žalm 66
OL315 – Stvoř mi čisté srdce, Bože! – Žalm 51
OL316 – Hospodin je mé světlo a má spása. – Žalm 27
OL317 – Sešli svého ducha, Hospodine, a obnovíš tvář země. – Žalm 104
OL318 – Budu velebit tvé jméno, můj Bože, králi. – Žalm 145
OL319 – Budu tě chválit, Hospodine, ve velkém shromáždění. – Žalm 22
OL320 – Vypravujte mezi všemi národy o Hospodinových divech. – Žalm 96
OL321 – Blaze těm, kdo přebývají v tvém domě, Bože. – Žalm 84
OL322 – Kalich požehnání je společenstvím Krve Kristovy. – Žalm 116
OL323 – Vy jste mými přáteli, budeteli činiti to, co vám přikazuji. – Žalm 100
OL324 – Země je plná Hospodinovy milosti. – Žalm 33
OL325 – Jinoši a panny, chvalte Hospodinovo jméno! – Žalm 148
OL326 – Blízký je Hospodin všem, kdo ho vzývají. – Žalm 145
OL327 – Hospodin je milosrdný a milostivý. – Žalm 103
OL328 – Hospodinova láska od věků pro ty, kdo se ho bojí. – Žalm 103
OL329 – Dobré je chválit Hospodina. – Žalm 92
OL330 – Okuste a vizte, jak je Hospodin dobrý. – Žalm 34
OL331 – Hle, přicházím, Pane, splnit tvou vůli. – Žalm 40
OL332 – Jak milý je tvůj příbytek, Hospodine zástupů! – Žalm 84
OL333 – Jsme jeho lid a stádce, které on pase. – Žalm 100
OL334 – Blaze lidu, který si Hospodin vyvolil za svůj majetek. – Žalm 33
OL335 – Hospodin je mé světlo a má spása. – Žalm 27
OL336 – Děkujte Hospodinu, neboť je dobrý, jeho milosrdenství trvá na věky. – Žalm 118
OL337 – Hospodin je milosrdný a milostivý. – Žalm 103
OL338 – Věřím, že uvidím blaho od Hospodina v zemi živých! – Žalm 27
OL339 – Budu kráčet před Hospodinem v zemi živých. – Žalm 116
OL340 – Smím si vykračovat před Pánem v zemi živých. – Žalm 116
OL341 – K tobě pozvedám svou duši, Hospodine. – Žalm 25
OL342 – Má duše žízní po tobě, Pane, Bože můj! – Žalm 42
OL343 – Hospodine, slyš mou modlitbu a volání mé ať k tobě pronikne! – Žalm 143
OL344 – K tobě pozvedám svou duši, Hospodine. – Žalm 25
OL345 – Drahocenná je v Hospodinových očích smrt jeho zbožných. – Žalm 116
OL346 – Aleluja, aleluja, aleluja. – Žalm 118
OL401 – Hospodin kraluje, je povznesen nad celou zemí. – Žalm 97
OL402 – Hospodine, Pane náš, jak podivuhodné je tvé jméno po celé zemi! – Žalm 8
OL403 – Hospodin pamatuje věčně na svoji smlouvu. – Žalm 105
OL404 – Kéž byste dnes uposlechli jeho hlasu: „Nezatvrzujte svá srdce!“ – Žalm 95
OL405 – Nezapomínejte na Boží skutky! – Žalm 78
OL406 – Tvá slova, Pane, jsou duch a jsou život. – Žalm 19
OL407 – Ty jsi kněz na věky podle Melchizedechova řádu! – Žalm 110
OL408 – Hospodin pamatuje věčně na svoji smlouvu. – Žalm 111
OL409 – Hle, přicházím, Pane, splnit tvou vůli. – Žalm 40
OL410 – Pane, ukaž nám své milosrdenství! – Žalm 85
OL411 – Bůh se vznáší za jásotu, Hospodin vystupuje za hlaholu polnice. – Žalm 47
OL412 – Zpívejte Hospodinu píseň novou, protože učinil podivuhodné věci. – Žalm 98
OL413 – Hle, přicházím, Pane, splnit tvou vůli. – Žalm 40
OL414 – To je pokolení těch, kdo hledají tvář tvou, Hospodine. – Žalm 24
OL414a – To je pokolení těch, kdo hledají tvář tvou, Hospodine. – Žalm 24
OL415 – Ústa spravedlivého mluví moudře. – Žalm 37
OL416 – Pochválen buď Hospodin, Bůh Izraele, neboť navštívil svůj lid. – Lk 1
OL417 – Vzmužte se a buďte srdnatí, všichni, kdo spoléháte na Hospodina. – Žalm 31
OL418 – Budu tě chválit, Hospodine, ve velkém shromáždění. – Žalm 22
OL419 – Hospodinova láska od věků pro ty, kdo se ho bojí. – Žalm 103
OL420 – Vzpomínáme, Bože, na tvé milosrdenství ve tvém chrámě. – Žalm 48
OL421 – Hospodin je mé světlo a má spása. – Žalm 27
OL422 – Hospodin je můj pastýř, nic nepostrádám. – Žalm 23
OL423 – Sešli svého ducha, Pane, a obnov tvářnost země. – Žalm 104
OL424 – Hospodine, Pane náš, jak podivuhodné je tvé jméno po celé zemi! – Žalm 8
OL425 – Veleb, duše má, Hospodina. – Žalm 104
OL426 – Blaze každému, kdo se bojí Hospodina. – Žalm 128
OL427 – Tys mé útočiště, zahrneš mě radostí ze záchrany. – Žalm 32
OL428 – Pane, tys nám býval útočištěm od pokolení do pokolení. – Žalm 90
OL429 – Kdo žije správně, tomu ukážu Boží spásu. – Žalm 50
OL430 – Pán dá požehnání a pokoj svému lidu. – Žalm 29
OL431 – Vezmu kalich spásy a budu vzývat jméno Hospodinovo. – Žalm 116
OL432 – Hospodin popatřil z nebe na zem. – Žalm 102
OL433 – Blaze lidu, který si Hospodin vyvolil za svůj majetek. – Žalm 33
OL434 – Budu velebit tvé jméno, můj Bože, králi. – Žalm 145
OL435 – Hospodin kraluje, oděl se velebností. – Žalm 93
OL436 – Ústa spravedlivého mluví moudře. – Žalm 37
OL437 – Jak miluji tvůj zákon, Hospodine. – Žalm 119
OL438 – Blaze tomu, kdo svou naději vložil do Hospodina. – Žalm 1
OL439 – Voď mě po cestě svých předpisů, Hospodine. – Žalm 119
OL440 – Hospodinova láska od věků pro ty, kdo se ho bojí. – Žalm 103
OL441 – Kdo žije správně, tomu ukážu Boží spásu. – Žalm 50
OL442 – Ukaž nám, Pane, světlo svého slitování. – Žalm 98
OL443 – Země je plná Hospodinovy milosti. – Žalm 33
OL444 – Hospodin miluje svůj národ. – Žalm 149
OL445 – Hospodinovy předpisy jsou správné, působí radost srdci. – Žalm 19
OL446 – Blaze muži, který se bojí Hospodina. – Žalm 112
OL447 – Blaze muži, který se bojí Hospodina. – Žalm 112
OL448 – K tobě pozvedám svou duši, Hospodine. – Žalm 25
OL449 – Duše má, chval Hospodina! – Žalm 146
OL450 – Veliký jsi, Hospodine, na věky. – Tob 13 (zkráceno)
OL451 – Okuste a vizte, jak je Hospodin dobrý. – Žalm 34
OL452 – Jasnou tvář ukaž svému služebníku, Hospodine! – Žalm 119
OL453 – Svatý jsi, Hospodine, náš Bože! – Žalm 99
OL454 – Pane, ukaž nám své milosrdenství! – Žalm 85
OL455 – Budu kráčet před Hospodinem v zemi živých. – Žalm 116
OL456 – Hospodin je milosrdný a milostivý. – Žalm 103
OL457 – Hospodin zjevil svou spásu před zraky pohanů. – Žalm 98
OL458 – Duše má, chval Hospodina! – Žalm 146
OL459 – Blaze muži, který se bojí Hospodina. – Žalm 112
OL460 – Skutky tvých rukou, Pane, jsou věrné a spravedlivé. – Žalm 111
OL461 – Okuste a vizte, jak je Hospodin dobrý. – Žalm 34
OL462 – Okuste a vizte, jak je Hospodin dobrý. – Žalm 34
OL463 – Blaze lidu, který si Hospodin vyvolil za svůj majetek. – Žalm 33
OL464 – Hospodine, kdo smí prodlévat ve tvém stánku? – Žalm 15
OL465 – Oslavujte Hospodina, neboť na věky trvá jeho milosrdenství. – Žalm 106
OL466 – Pán pamatoval na své milosrdenství. – Lk 1
OL467 – Hospodin je milosrdný a milostivý. – Žalm 103
OL468 – Tvou dobrotu, Pane, mám na zřeteli. – Žalm 26
OL469 – Hle, ubožák zavolal, a Hospodin slyšel. – Žalm 34
OL470 – Budu kráčet před Hospodinem v zemi živých. – Žalm 116
OL471 – Chvalte Hospodina, protože je dobrý. – Žalm 135
OL472 – Buď se mnou, Pane, v mé tísni. – Žalm 91
OL473 – Až procitnu, Hospodine, nasytím se pohledem na tebe. – Žalm 17
OL474 – Ať spočine na nás, Hospodine, tvé milosrdenství, jak doufáme v tebe. – Žalm 33
OL475 – Pamatujte na divy, které učinil Hospodin. – Žalm 105
OL476 – Ze srdce ať se radují, kdo hledají Hospodina. – Žalm 105
OL477 – Naše duše vyvázla jako pták z ptáčníkovy léčky. – Žalm 124
OL478 – Hledejte, ubožáci, Hospodina a pookřejte v srdci. – Žalm 69
OL479 – Hospodin je milosrdný a milostivý. – Žalm 103
OL480 – Hospodin pamatuje věčně na svoji smlouvu. – Žalm 105
OL481 – Vezmu kalich spásy a budu vzývat jméno Hospodinovo. – Žalm 116
OL482 – jeho milosrdenství trvá na věky. – Žalm 136
OL483 – Hospodinu chci zpívat, neboť je velmi vznešený. – Ex 15
OL484 – Hospodinu chci zpívat, neboť je velmi vznešený. – Ex 15
OL485 – Nebeský pokrm dal jim Hospodin. – Žalm 78
OL486 – chvályhodný a svrchovaně velebený navěky. – Dan 3
OL487 – Pane, ty máš slova věčného života. – Žalm 19
OL488 – Kdo žije správně, tomu ukážu Boží spásu. – Žalm 50
OL489 – Oslavujte Hospodina, neboť na věky trvá jeho milosrdenství. – Žalm 106
OL490 – Hospodin je milosrdný a milostivý. – Žalm 103
OL491 – Svatý jsi, Hospodine, náš Bože! – Žalm 99
OL492 – Jak milý je tvůj příbytek, Hospodine zástupů! – Žalm 84
OL493 – Plesejte Bohu, který nám pomáhá. – Žalm 81
OL494 – Ať tě, Bože, velebí národy, ať tě velebí, kdekterý národ! – Žalm 67
OL495 – Plesejte Bohu, který nám pomáhá. – Žalm 82
OL496 – Smiluj se, Pane, neboť jsme zhřešili. – Žalm 51
OL497 – Pamatuj na nás, Hospodine, pro náklonnost k svému lidu. – Žalm 106
OL498 – Kéž byste dnes uposlechli jeho hlasu: „Nezatvrzujte svá srdce!“ – Žalm 95
OL499 – Vzpomínám na Hospodinovy činy. – Žalm 77
OL500 – Miluji tě, Hospodine, má sílo! – Žalm 18
OL501 – Jeruzaléme, oslavuj Hospodina! – Žalm 147
OL502 – Hospodinovým podílem je jeho lid. – Dt 32
OL503 – Jásejte Bohu, všechny země! – Žalm 66
OL504 – Nezapomínejte na Boží skutky! – Žalm 114
OL505 – jeho milosrdenství trvá na věky. – Žalm 136
OL506 – Ty jsi, Hospodine, mým dědičným podílem. – Žalm 16
OL507 – Pamatuj na nás, Hospodine, pro náklonnost k svému lidu. – Žalm 106
OL508 – Hospodine, z tvé síly se raduje král. – Žalm 21
OL509 – Hle, přicházím, Pane, splnit tvou vůli. – Žalm 40
OL510 – Duše má, chval Hospodina! – Žalm 146
OL511 – Hospodine, ty mě zkoumáš a znáš. – Žalm 139
OL512 – Hospodine, ty mě zkoumáš a znáš. – Žalm 139
OL513 – Nasyť nás, Pane, svou slitovností, abychom se radovali. – Žalm 90
OL514 – Radujte se, spravedliví, v Hospodinu. – Žalm 97
OL515 – Přišel Hospodin, aby spravoval národy podle práva. – Žalm 98
OL516 – Hospodin přichází řídit zemi. – Žalm 96
OL517 – Věřím, že uvidím blaho od Hospodina v zemi živých! – Žalm 27
OL518 – Stále spoléhám na Boží slitovnost. – Žalm 52
OL519 – Hospodin zjevil svou spásu před zraky pohanů. – Žalm 98
OL520 – Jsme jeho lid a stádce, které on pase. – Žalm 100
OL521 – Pán mě udržuje naživu. – Žalm 54
OL522 – V Bohu jen odpočívej, duše má. – Žalm 62
OL523 – Budu tě oslavovat na věky, můj Bože, králi. – Žalm 145
OL524 – Budu tě oslavovat na věky, můj Bože, králi. – Žalm 145
OL525 – Všechno, co dýchá, ať chválí Hospodina! – Žalm 150
OL526 – Buď veleben Hospodin nyní i na věky! – Žalm 113
OL527 – Požehnán buď Hospodin, že vyslyšel mou úpěnlivou prosbu! – Žalm 28
OL528 – Chci kráčet v nevinnosti srdce. – Žalm 101
OL529 – Veliká jsou Hospodinova díla. – Žalm 111
OL530 – Veliká jsou Hospodinova díla. – Žalm 111
OL531 – Blahoslavení chudí v duchu, neboť jejich je království nebeské. – Žalm 49
OL532 – Velkou věc s námi učinil Hospodin, naplnila nás radost. – Žalm 126
OL533 – Do domu Hospodinova s radostí půjdeme. – Žalm 122
OL534 – Veliký jsi, Hospodine, na věky. – Tob 13
OL535 – Doufej v Boha, vždyť zase ho budu chválit, svého spasitele a svého Boha! – Žalm 43
OL536 – Hospodin bude nad námi bdít, jako pastýř nad svým stádem. – Jer 31
OL537 – Hospodin znovu zbuduje Sión, objeví se ve své slávě. – Žalm 102
OL538 – Hospodin je s námi. – Žalm 87
OL539 – Vyslyš nás, Pane, a vysvoboď nás. – Žalm 137
OL540 – Pro slávu svého jména vysvoboď nás, Pane! – Žalm 79
OL541 – Vyslyš mě, Hospodine, ve své veliké lásce! – Žalm 69
OL542 – Ze záhuby vysvobodíš můj život, Hospodine! – Jon 2
OL543 – U Hospodina je slitování, hojné u něho je vykoupení. – Žalm 130
OL544 – Tys, Pane, dobrý a shovívavý. – Žalm 86
OL545 – Hospodin bude soudit svět podle práva. – Žalm 9
OL546 – Radujte se, spravedliví, v Hospodinu. – Žalm 97
OL547 – Všude na zemi pronikl jejich hlas. – Žalm 19
OL548 – V Bohu jen odpočívej, duše má. – Žalm 62
OL549 – U Hospodina je slitování, hojné u něho je vykoupení. – Žalm 130
OL550 – Tys mé útočiště, zahrneš mě radostí ze záchrany. – Žalm 32
OL551 – Hospodin pamatuje věčně na svoji smlouvu. – Žalm 105
OL552 – Nauč mě, Hospodine, svým příkazům! – Žalm 119
OL553 – Náš Bůh je Bohem spásy. – Žalm 68
OL554 – Důvěřuji v tvé slitování, Hospodine! – Žalm 13
OL555 – Zachraň mě, Hospodine, podle svého slitování! – Žalm 109
OL556 – Nezavrhne Hospodin svůj národ. – Žalm 94
OL557 – Vyslyš mě, Hospodine, ve své veliké lásce! – Žalm 69
OL558 – Opatruj, Pane, mou duši ve svém pokoji! – Žalm 131
OL559 – Blaze muži, který se slitovává a půjčuje. – Žalm 112
OL560 – Hospodine, ty mě zkoumáš a znáš. – Žalm 139
OL561 – Ustavičně chci velebit Hospodina. – Žalm 34
OL562 – Povstaň, Bože, suď zemi! – Žalm 82
OL563 – Nauč mě, Hospodine, svým příkazům! – Žalm 119
OL564 – Pamatujte na divy, které učinil Hospodin. – Žalm 105
OL565 – Zachovej mi život, Pane, a budu dbát na tvá přikázání. – Žalm 119
OL566 – Povstaň, Hospodine, zachraň mě! – Žalm 3
OL567 – Až procitnu, Hospodine, nasytím se pohledem na tebe. – Žalm 17
OL568 – Ty, Hospodine, vládneš nade vším. – 1. Kron 29
OL569 – Rozjásám se nad tvou pomocí, Hospodine! – Žalm 9
OL570 – chvalte a oslavujte ho na věky. – Dan 3
OL571 – chvalte a oslavujte ho na věky. – Dan 3
OL572 – chvalte a oslavujte ho na věky. – Dan 3
OL573 – chvalte a oslavujte ho na věky. – Dan 3
OL574 – chvalte a oslavujte ho na věky. – Dan 3
OL575 – Vezmu kalich spásy a budu vzývat jméno Hospodinovo. – Žalm 116
OL576 – Mé srdce jásá v Bohu, mém spasiteli. – 1 Sam 2
OL577 – Hle, přicházím, Pane, splnit tvou vůli. – Žalm 40
OL578 – Vysvoboď nás, Pane, pro svou lásku! – Žalm 44
OL579 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL580 – Kdo žije správně, tomu ukážu Boží spásu. – Žalm 50
OL581 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL582 – Veleben buď Hospodin, má Skála! – Žalm 144
OL583 – V Boha důvěřuji, nebudu se bát. – Žalm 56
OL584 – Smiluj se nade mnou, Bože, smiluj se! – Žalm 57
OL585 – Bože, obnov nás, rozjasni svou tvář, a budeme spaseni. – Žalm 80
OL586 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL587 – Hospodin zástupů, on je král slávy! – Žalm 24
OL588 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL589 – Pán Bůh mu dá trůn jeho otce Davida. – Žalm 132
OL590 – Smiluj se, Pane, neboť jsme zhřešili. – Žalm 51
OL591 – Stvoř mi čisté srdce, Bože! – Žalm 51
OL592 – Tys, Pane, dobrý a shovívavý. – Žalm 86
OL593 – Odpusť, Pane, co jsem zavinil hříchem. – Žalm 32
OL594 – Miluji tě, Hospodine, má sílo! – Žalm 18
OL595 – Nauč mě, Hospodine, svým příkazům! – Žalm 119
OL596 – Vstaň, Hospodine, vejdi na místo svého odpočinku, ty i tvá vznešená archa! – Žalm 132
OL597 – Jak milý je tvůj příbytek, Hospodine zástupů! – Žalm 84
OL598 – Ústa spravedlivého mluví moudře. – Žalm 37
OL599 – Pamatuj na nás, Hospodine, pro náklonnost k svému lidu. – Žalm 106
OL600 – Plesejte Bohu, který nám pomáhá. – Žalm 81
OL601 – Pamatuj na nás, Hospodine, pro náklonnost k svému lidu. – Žalm 106
OL602 – Ať se mi dostane tvého slitování, Hospodine, abych byl živ. – Žalm 119
OL603 – Šťastný člověk, jehož vychováváš, Hospodine. – Žalm 94
OL604 – Spravedlivý bude, Pane, přebývat na tvé svaté hoře. – Žalm 15
OL605 – Hle, ubožák zavolal, a Hospodin slyšel. – Žalm 34
OL606 – Ty nás, Hospodine, ochráníš. – Žalm 12
OL607 – Hospodinovy předpisy jsou správné, působí radost srdci. – Žalm 19
OL608 – Svou starost hoď na Hospodina, a on tě zachová. – Žalm 55
OL609 – Blahoslavení chudí v duchu, neboť jejich je království nebeské. – Žalm 49
OL610 – Blahoslavení chudí v duchu, neboť jejich je království nebeské. – Žalm 49
OL611 – Má modlitba, Pane, ať je před tebou jako kadidlo. – Žalm 141
OL612 – Hospodin pamatuje věčně na svoji smlouvu. – Žalm 111
OL613 – Hospodin přichází řídit zemi. – Žalm 96
OL614 – Má duše po tobě žízní, Hospodine, Bože můj! – Žalm 63
OL615 – Buď se mnou, Pane, v mé tísni. – Žalm 91
OL616 – Pane, tys nám býval útočištěm od pokolení do pokolení. – Žalm 90
OL617 – Naše oči hledí na Hospodina, dokud se nad námi nesmiluje. – Žalm 123
OL618 – Ukaž mi své cesty, Hospodine. – Žalm 25
OL619 – Jak miluji tvůj zákon, Hospodine. – Žalm 119
OL620 – Ústa má budou vyprávět o tvé spravedlnosti. – Žalm 71
OL621 – Pomoc nám přijde od Hospodina, který učinil nebe i zemi. – Žalm 121
OL622 – Hospodine, ukaž nám svou jasnou tvář! – Žalm 4
OL623 – Ochraň mě, Bože, neboť se k tobě utíkám. – Žalm 16
OL624 – Semeno padlo na dobrou půdu a přineslo užitek. – Žalm 65
OL625 – Hospodin je mé světlo a má spása. – Žalm 27
OL626 – Ty jsi, Hospodine, mým dědičným podílem. – Žalm 16
OL627 – Hospodine, všimni si mého volání! – Žalm 5
OL628 – Smiluj se, Pane, neboť jsme zhřešili. – Žalm 51
OL629 – Vzmužte se a buďte srdnatí, všichni, kdo spoléháte na Hospodina. – Žalm 31
OL630 – Radujte se, spravedliví, v Hospodinu. – Žalm 97
OL631 – Pán Bůh mu dá trůn jeho otce Davida. – Žalm 132
OL632 – Na věky chci zpívat o Hospodinových milostech. – Žalm 89
OL633 – Pomoz, Bože, svou pravicí a vyslyš nás! – Žalm 60
OL634 – Bůh dává věčné trvání svému městu. – Žalm 48
OL635 – Nauč mě, Hospodine, svým příkazům! – Žalm 119
OL636 – Nezapomínej na chudáky, Hospodine! – Žalm 74
OL637 – Kdo žije správně, tomu ukážu Boží spásu. – Žalm 50
OL638 – Veď mě ve své spravedlnosti, Hospodine! – Žalm 5
OL639 – Kdo žije správně, tomu ukážu Boží spásu. – Žalm 50
OL640 – Hospodinovy výroky jsou pravdivé, všechny jsou spravedlivé. – Žalm 19
OL641 – Jak miluji tvůj zákon, Hospodine. – Žalm 119
OL642 – Budu velebit tvé jméno, můj Bože, králi. – Žalm 145
OL643 – Izraelův dům doufá v Hospodina. – Žalm 115
OL644 – Hledejte vždy Hospodinovu tvář! – Žalm 105
OL645 – Bože, obnov nás, rozjasni svou tvář, a budeme spaseni. – Žalm 80
OL646 – Smiluj se, Pane, neboť jsme zhřešili. – Žalm 51
OL647 – Bůh dává věčné trvání svému městu. – Žalm 48
OL648 – Nezavrhne Hospodin svůj národ. – Žalm 94
OL649 – Hospodin popatřil z nebe na zem. – Žalm 102
OL650 – Ty, Hospodine, jsi zachránil mou duši, aby nezhynula. – Iz 38
OL651 – Nezapomínej na chudáky, Hospodine! – Žalm 10
OL652 – Kdo žije správně, tomu ukážu Boží spásu. – Žalm 50
OL653 – Pane, ukaž nám své milosrdenství! – Žalm 85
OL654 – Ústa má budou vyprávět o tvé spravedlnosti. – Žalm 71
OL655 – U tebe je, Bože, pramen života. – Žalm 36
OL656 – Opustil jsi Boha, který tě zplodil. – Dt 32
OL657 – Pro slávu svého jména vysvoboď nás, Pane! – Žalm 79
OL658 – Bůh je mé útočiště, když je mi úzko. – Žalm 59
OL659 – Duše má, chval Hospodina! – Žalm 146
OL660 – Vyslyš mě, Hospodine, ve své veliké lásce! – Žalm 69
OL661 – Vyslyš mě, Hospodine, ve své veliké lásce! – Žalm 69
OL662 – Nauč mě, Hospodine, svým příkazům! – Žalm 119
OL663 – Stvoř mi čisté srdce, Bože! – Žalm 51
OL664 – Já usmrcuji a já oživuji. – Dt 32
OL665 – Neopouštíš, Hospodine, ty, kteří tě hledají. – Žalm 9
OL666 – Jinoši a panny, chvalte Hospodinovo jméno! – Žalm 148
OL667 – Jak miluji tvůj zákon, Hospodine. – Žalm 119
OL668 – Nad nebesa je sláva Hospodinova. – Žalm 113
OL669 – Nezapomínejte na Boží skutky! – Žalm 78
OL670 – Plesejte a jásejte, neboť nad vámi vládne Svatý Izraele. – Iz 12
OL671 – Já usmrcuji a já oživuji. – Dt 32
OL672 – Oslavujte Hospodina, neboť na věky trvá jeho milosrdenství. – Žalm 107
OL673 – Vypravujte mezi všemi národy o Hospodinových divech. – Žalm 96
OL674 – Blaze každému, kdo se bojí Hospodina. – Žalm 128
OL675 – Budu velebit tvé jméno, můj Bože, králi. – Žalm 145
OL676 – Země je plná Hospodinovy milosti. – Žalm 33
OL677 – Blaze lidu, který si Hospodin vyvolil za svůj majetek. – Žalm 33
OL678 – Jak miluji tvůj zákon, Hospodine. – Žalm 119
OL679 – Budu tě oslavovat na věky, můj Bože, králi. – Žalm 145
OL680 – Blaze lidu, který si Hospodin vyvolil za svůj majetek. – Žalm 33
OL681 – Ať vejde Hospodin, on je král slávy! – Žalm 24
OL682 – Ústa spravedlivého mluví moudře. – Žalm 37
OL683 – Blízký je Hospodin všem, kdo ho vzývají. – Žalm 145
OL684 – Veď mě ve své spravedlnosti, Hospodine! – Žalm 5
OL685 – Hle, ženich přichází, jděte naproti Kristu Pánu! – Žalm 45
OL686 – Chválím tě, že jsem vznikl tak podivuhodně. – Žalm 139
OL687 – Jak milý je tvůj příbytek, Hospodine zástupů! – Žalm 84
OL688 – Vezmu kalich spásy a budu vzývat jméno Hospodinovo. – Žalm 116
OL689 – Blaze lidu, který si Hospodin vyvolil za svůj majetek. – Žalm 33
OL690 – Děkujte Hospodinu, neboť je dobrý, jeho milosrdenství trvá na věky. – Žalm 118
OL691 – Až procitnu, Hospodine, nasytím se pohledem na tebe. – Žalm 17
OL692 – Budu kráčet před Hospodinem v zemi živých. – Žalm 56
OL693 – Voď mě po cestě svých předpisů, Hospodine. – Žalm 119
OL694 – Svítilnou mým nohám je tvé slovo. – Žalm 119
OL695 – Pane, tys nám býval útočištěm od pokolení do pokolení. – Žalm 90
OL696 – Veleben buď Hospodin, má Skála! – Žalm 144
OL697 – Popřej mi sluchu, slyš mé slovo! – Žalm 17
OL698 – Kéž pronikne k tobě má modlitba, Hospodine! – Žalm 88
OL699 – Kéž pronikne k tobě má modlitba, Hospodine! – Žalm 88
OL700 – Věřím, že uvidím blaho od Hospodina v zemi živých! – Žalm 27
OL701 – Chválím tě, že jsem vznikl tak podivuhodně. – Žalm 139
OL702 – Jasnou tvář ukaž svému služebníku, Hospodine! – Žalm 119
OL703 – Hospodin pamatuje věčně na svoji smlouvu. – Žalm 111
OL704 – Chválím tě, že jsem vznikl tak podivuhodně. – Žalm 139
OL705 – Jděte do celého světa a hlásejte evangelium. – Žalm 117
OL706 – Hospodin pamatuje věčně na svoji smlouvu. – Žalm 111
OL707 – Hospodin pamatuje věčně na svoji smlouvu. – Žalm 105
OL708 – Ať se mi dostane tvého slitování, Hospodine, abych byl živ. – Žalm 119
OL709 – Hospodin zjevil svou spásu před zraky pohanů. – Žalm 98
OL710 – Blaze lidu, který si Hospodin vyvolil za svůj majetek. – Žalm 33
OL711 – Hospodine, Pane náš, jak podivuhodné je tvé jméno po celé zemi! – Žalm 8
OL712 – Budete vážit vodu s radostí z pramenů spásy. – Iz 12
OL713 – Země je plná Hospodinovy milosti. – Žalm 33
OL714 – Do domu Hospodinova s radostí půjdeme. – Žalm 122
OL715 – Budu tě oslavovat na věky, můj Bože, králi. – Žalm 145
OL716 – Má duše žízní po tobě, Pane, Bože můj! – Žalm 42
OL717 – Budu tě chválit, Hospodine, ve velkém shromáždění. – Žalm 22
OL718 – Hospodin je mé světlo a má spása. – Žalm 27
OL719 – Ze srdce ať se radují, kdo hledají Hospodina. – Žalm 105
OL720 – Blaze muži, který se bojí Hospodina. – Žalm 112
OL721 – Ústa spravedlivého mluví moudře. – Žalm 37
OL722 – Duše má, chval Hospodina! – Žalm 146
OL723 – Blaze těm, kdo kráčejí v zákoně Hospodinově. – Žalm 119
OL724 – Svatý, svatý, svatý, Pán, Bůh vševládný. – Žalm 150
OL725 – Vytvořil jsi z nás našemu Bohu království a kněze. – Žalm 149
OL726 – Zpívejte Hospodinu píseň novou, protože učinil podivuhodné věci. – Žalm 98
OL727 – Hle, stánek Boží mezi lidmi! – Žalm 84
OL728 – Kéž byste dnes uposlechli jeho hlasu: „Nezatvrzujte svá srdce!“ – Žalm 95
"""

import re

exp = []
for l in alld.split("\n"):
	l = l.strip()
	if not l: continue
	d = l.split("–")
	if len(d) != 3:
		print("error", d)
		
	row = d[1].strip()
	if row not in exp:
		exp.append(row)
	
print(len(exp))

import json
json.dump(exp, open("zalm_cache.json", "wt"))
		
		

