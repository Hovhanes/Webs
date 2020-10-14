1. intro
	1. mez nerkayacnel, kurseri npatak@ inchi khasnen kurseric heto, xia dzri kurser@, inch petqa anenq ardzyunqi hasnelu hamar
	2. incha cragravorum@, cragravorman lezun u inchi hmar 
	3. xi henc python, vortexa ogtagorcvum python@ u inch haytni ynkerutyunnerum
	4. inch tesaki lezua python@, interpretatori u compeliatori tarberutyun@ tipizacian incha 
	5. practic ashxatanq, install python tpel hello world, mi 2 ban sarqel pythonov titizanalu hamar
	
												Tnayin
	1.stex karanq asenq vortexic enq menq informacia stanum,mi qani link tanq kam tekuz menak w3schools.(chgitem arji videourok asenq nayen? xosqi barisov)u asenq vor google anen misht
	2.karanq grqer xorhurd tanq ete haves unenan tox or@ mi qani ej kardan(prost@ documentacian mi qich chora grac im jogelov)

=================================================================================================================================================
								Types


2. Types
	1.popoxakanner, incha popoxakan@(tetev orinak urish lezuneri het tipizaciayi het kapvac)

		1.1 skzbum inch vor sovorakan orinak ` name="Hovlo"
		1.2 ka @ndunvac erku tesak popoxakan haytararelu hamar.arajin@ kochvuma CAMEL CASE (userName),isk erkrord@ UNDERSCORE NATION (user_name).stex uxaki mi qani barov kxosanq sra masin
		1.3 popoxakannerum chenq kara tanq annuner voronq pythonum unen hatuk nshanakutyunner `(True,False,if,else ...)
		1.4 python@ dinamik tipizacvac lezua,aysinqn mez petq chi naxoroq haytararel te inch type petq e iran veragrenq.(stex mi qani orinakner urish lezuneric)
			orinak erb menq grecink vor user="Hovlo" pyhton@ avtomat haskacav vor menq uzum enq string pahenq mer popoxakanum,nuyn@ karanq anenq urish type het.pyton@ dynamik bayc strong tipizacia uni,aysinqn chenq 
			kara stringin integer gumarenq vorovhetev python@ intuitiv chi haskana te inch petqa ani,isk pythoni grac kod@ misht nenca ashxatum vor ankaxateseli baner chlini. 
			orinak integer enq haytararum ` user_age=25(eqa txayes ay axper).
	2.(String,Integer,Float,List,Tuple,Dict,Set(frozenset),File,Bool) - slide `popoxvox u chpopoxvox https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747
		2.1 stex arden naxordneri orinakov tetev cuyc tvac klinenq mi qanis@. 	
	3.(String,Integer,Float) - intro (orinakner vor popxakaner@ poxvum en gorcoxutyunneric heto u pahvum en referance-i mijocov)
		3.0. referanci orinak 
			x = 1			
			y = x
			x = 7
			print(y)
		3.1 String pahelu hamar menq petqa @ndamen@ mer uzac arjeq@ grenq kam 1 kam 2 hatanoc chakertneri mej, vor interpretator@ haskana vor popoxakan chi.
		3.2 karanq arden print anenq sax u iranqel gren mer het.(stringer@ irar miacnelu orinaker)
		3.3 ete uzum enq toxadarc ogdagorcenq petqa text@ vercnenq 3 hat chakerti mej(eakan chi 1 te 2)
		3.4 string format.  orinak name = "Hovlo"            kam orinak senc print(f."Hello,{name}")(3.6 ic heto menak)
							print("Hello, {}".format(name))

			print("%s %d tarekana" % ('Hovlon',25.444) )
			
			%s - string
			
			%d - int(decimal - float@ kloracnuma)
			
		3.5 nuyn@ karanq asenq Integeri u Floiati hamar(Floati hamar mi qich aranzin kxosanq).meke mi qani orinakner (gumarum,hanum,random,meci u poqri nshanner u tenc inch hishenq)
	4.default funkcianeri orinakner (String,Integer,Float) hamar arandz bacatrelu te inch en u urduc(kasenq gorciqner kan senc)
		4.1 String  - 
					  str(55) - funkcian.
					  'string'.lower () mer tvac text@ sax sarcuma poqratar.
					  'string'.upper () mer tvac text@ sax sarquma mecatar.
					  'string'.replace('replaced_string','new_string',count_of_replaced_string) poxuma mer textum exac bar@(kam symbol@) mer uzacov.
					  'string#number#two'.split('separator') mer tvac text@ bajanuma @st mer tvac symboli u veradarcnuma list(stex tetev asac klinenq listeri masin)
					  'string'.find('r') ete gtnuma veradarcnuma mer uzac texti index@,isk ete chi gtnum veradarcnuma -1
	    4.2 Integer - 
					  x + y
					  x - y
					  x / y
					  x * y
					  x // y kloracnuma depi nerqev
					  x ** y
					  -x sarquma bacasakan
					  +x sarquma drakan
					  Int('5') - funkcian
	   
					  HISHENQ VOR CUYC TANQ STRINGI BAZMAPATKUM@

					  
	   4.3 Float - sra masin indz tvuma shat ban chkael xosalu prost@ mi qani orinak karanq cuyc tanq.
					#uxaki integer@ sarquma float
					print(float(10))

					# type@ mnuma eli float
					print(float(11.22))

					# string@ poxuma floata sarqum
					print(float("-13.33"))

					# spacer@ hasvi chen arnvum
					print(float("     -24.45\n"))

					# errora tali ete sxal parametr enq tali
					print(float("abc"))

					#float@ vor bajanum es integeri floata misht veradarcnum
					print(10.2 / 2)
	4.4 round(5.6, digits) tetev nerkayacnenq
		

	5.Integeri,stringi u floati default funkcianer@ cuyc tal orinaknerov te vortex en petq
		5.1 es indz tvuma arden arecinq
	6.berel orinak type() funkciayov
		6.1 String - type('55string')
					 type(str(1))
			Integer - type(1)
					  type(int('22'))
		    
			Float - type(55.77)
					type(float(22))
					type(float('22'))

3.List u Tuple
	1.bacatrenq vonc python kod@ grenq faileri mej u vonc run anenq mer arden modul@.
		1.1 bacatrumenq input@ - input@ funkciaya vor mez hnaravorutyuna talis stanal tvyalner mer ogtateric.asenq vor erb kod@ hasnuma et inputin,
	        heto user@ petqa inch vor ban gri u nor sharunaki kod@.
 		
		1.2 menq karanq useri grac tvyalner@ stananq mer input@ veragrelov popoxakani.

		1.3 misht string enq stanum useric, u heto karanq asxatenq voncvor sovorokan stringeri het.orinak ete petq lini sarqenq integer.
		
		1.4.uxaki orinak vonc stananq mer useri name@ u lastName u print anenq inch vor texti het.cuyt tanq vor karanq mer inputi label@ grenq nax
		dranic araj print anelov,heto aveli harmar dzevov(iran parametr talov)
		
	2.uzum enq grenq app vor kazmuma ashakertneri annunner@.
		2.1 skzbum cuyc ktanq dranq talov popxakannertin,heto nuyn@ bacatrelu enq vor aveli hesta listov u senc iravichaknerum aveli haramara list ogtagorcel.
			x = 'Hovo'     users_list = ['Hovo', 'Vazgen', 'Jarviz']
			y = 'Vazgen'
			z = 'Jarviz'
			listum karanq unenq tarber typeri valuner(orinak String,Integer, listi mej list ...)
		2.2 bacatrenq listum indexsavorum@, vor sksuma 0 ic, u vor index@ vonc karanq tpenq.
    	     orinak berenq te vonc karanq listi index@ stanalov iran urish tvyal veragrenq - users_list[0] = 'Tatul'
			slice -  users_list[0:2] - 'Hovo', 'Vazgen'
		      users_list[0:]
		      users_list[-1]
		      users_list[:]  - copy
		      users_list[::-1] - reverce
		      users_list[::1]
         
		2.3 operatorner 
			erku listeri irar gumarum@ users_list + ['25','35','&']
			list@ karas bazmapatkes -  users_list * 3
							 
		2.4 list mutable
					list@ hamarvuma popoxvox type, aysinqn 
						orinak ` x = [1, 2, 3]
									y = x
									hima ete x[0] = 100, u tpenq y apa ktesnenq vor ira mejnela poxvel arjeq@

		2.5 methodner
			append() - entadrenq mer mot nor ashakerta eke, uzumenq avelacnenq  iran mer mot. dra hamar ogtagorcum enq apend methodov vor@ misht mer listi verjuma avelacnum.
			pop() - kam orinak ete uzum enq pakasacnenq mer verjin ekac userin ogtagorcum enq pop, vor@ jnjuma listi verji arjeq@ u veradarcnum ayn.
			insert( 1, ''user') - ete uzum enq konkret indexov avelacnenq.
			remove(''value') - jnjum enq @st mer value - i
			reverce() - kstananq mer list@ hakarak uxxutyamb
			sort(reverse=True) - sortavorel list@ @st achman, isk ete reverse havasara True @st nvazman
		
		2.6 funkcianer
			copy()
			len()
			sorted() - chi poxum list@ ayl veradarcnuma nor@, veradarcnuma nor@

		
	3.tuple - asenq te inchna listi u tupli tarberutyunner@,berenq orinakner te te vonc karanq default funkcianerov(list(),tuple()) mi type poxenq miusov
		3.1 listi meji value - n karanq poxenq, isk tuplin@ che.
		3.2 tupl@ karanq ogdagorcenq en depqum ete mez petqa hamozvac linenq vor hetagayum sxalmamb chenq karox poxel ayn.

4.Dict u Set(frozenset)
	1.unenq xndir vor mer amen mi ashakerti hamar petqa lracnenq iranc tvyalner@(skzbum kasenq tox iranq mtacen,heto nor kbacatrenq).
		1.1 arden mer ancac typerov vonc et xndir@ lucenq ?  orinak karanq unenanq listum useri tvyalner@ ['"jorj","bush", "57"]. stex nax mez metqa angir hishenq te mer useri konkret vor tvyal@ vor indexova pahac.
			isk inch klini ete orinak user@ shat tvyalner unena? dra hamar mez aveli harmar klini unenal Dictionery.
		1.2 Dict@ 
	2.kberenq orinakner dict-ov,u vonc avelacnenq tvyalner kam jnjenq(naxord typeri orinaknerov).
	3.nerkayacnenq incha set@.
	4.set-i methodner@(union).
	5.kberenq orinak txeqi u axjikneri hamar set-um,heto union kanenq et set-er@ u kxosanq ardyunqneri masin.
	6.verjum random funkciayov k@ntrenq mi hogu u hajord dasin inq@ petqa kbacatri ira tnayinner@ bolorin.

5.File
	1.asenq vor pythonum faileri het ashxatum enq vonc vorpes obyektneri het(vonc vor mnacac typeri het).
	2.karanq tetev bacatrenq funkcianer@ u iranc parametrer@ vor karanq mi qani gorcoxutyunner anenq faileri het.
	3.
		3.1 arajin parametr@ et faili pathna minchev faili anun@ @st moduli(aysinq et path@ petqa tanq @st mer moduli pathi vortex vor ogtagorcum enq open() funkcian)
		3.2 erkrord parametr@ talis enq nra hamar vor asenq te inhc gorcoxutyunner enq uzum anenq faili het(et paraametr@ partadir chi u ete chtanq mer 
		funckian kashxati default r(read) parametrov)
		3.3 'r' - read uxxaki bacum enq fail@ kardalu hamar (default)(ete fail@ chka,exceptiona talis)

			"a" - append - bacum enq fail@ nra mej ban avelacnelu hamar,aysinqn menq arden exac texti verjic sksac arden karanqavelacnenq(ete fail@ chka stexcuma nor fail)
			
			"w" - write - eli bacum enq fail@ nra mej ban avelacnelu hamar,bayc amen angam menq jnjum enq failum exac text@ u avelacnum e miayn mer verjin text@(ete fail@ chka stexcuma nor fail)
			
			"x" - create - stexcel nor file (ete fail@ ka exceptiona tali)
			
			stex "t" u "b" parametrer kan bayc chem uzum dran vra xorananq."t" default sovorakan text veradarcnelu hamara isk "b" byte koda veradarcnum aran decode anelu.
	
	4.parameter@ nerkayacneluc heto cuyc tanq sovorakan operacianer faileri het ashxatelu hamar(kardal faili mej exac text@,nor text grel faileri mej,stexcel failer,....).

	5.karanq tetev asenq `with` instrukciayi masin,faileri het ashxatelu hamar.

==================================================================================================================================================
								Expressions


6.(if ,else, elif,) - orinak karanq mi toxov grneq karch linelu depqum

7.Ciklner - while u for (karch for)

8.Funckcianer,funkciai argumentner@, return

9.Rekursiv funkcianer()

10.tetev nerkayacnenq incha lambda,u funkciayi parametrer(default, args*, kwargs**)


===================================================================================================================================================
								Modulner




11.inch en modulner@,modulneri karevorutyun@ pythoni hamar





===================================================================================================================================================
								Exceptions

12.inch en exceptionner@ u vortex en ogtagorcvum(default exceptionner)


===================================================================================================================================================
								Advanced Pyton

13.Tesaneliutyan makardakner@
14.Generatorner
15.Funkcional cragravorman hamar gorciqner(map,reduce,filter....)


===================================================================================================================================================
								OOP ?






	


