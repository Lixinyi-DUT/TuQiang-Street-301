(* Coursera Programming Languages, Homework 3, Provided Code *)

exception NoAnswer

datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
    let 
	val r = g f1 f2 
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x
	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
	  | ConstructorP(_,p) => r p
	  | _                 => 0
    end

(**** for the challenge problem only ****)

datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string

			       (**** you can put all your code here ****)

fun only_capitals sl=
  List.filter (fn s => Char.isUpper(String.sub(s,0))) sl

fun longest_string1 sl=
  foldl (fn (x,cur) => if String.size(x)>String.size(cur) then x else cur) "" sl 
fun longest_string2 sl=
  foldl (fn (x,cur) => if String.size(x)>=String.size(cur) then x else cur) "" sl
	
fun longest_string_helper greater lst =
  foldl (fn (x,cur) => if greater(String.size(x),String.size(cur)) then x else cur) "" lst

val  longest_string3 = longest_string_helper (fn (x,y)=>x>y)

val  longest_string4 = longest_string_helper (fn (x,y) => x>=y)

val longest_capitalized  = longest_string1 o only_capitals

val rev_string = implode o rev o explode

fun first_answer f lst=
  case lst of
      [] => raise NoAnswer
    | h::tail => case f h  of
		     SOME v => v
		   | NONE => first_answer f tail

fun all_answers f lst= (*f:a'->b' list option, lst: a' list*,rtype: b' list option*)
  let fun answers g l acc= (*g:a' -> b' list option, l: a' list, acc:b' list rtype: b' list option*)
	case l of
	    [] => SOME acc
	  | h::tail => case g h of
			   SOME v =>  answers g tail (acc@v)
			 | NONE => NONE
  in answers f lst []
  end

val count_wildcards=g (fn ()=>1) (fn x=>0)

val count_wild_and_variable_lengths=g (fn ()=>1) (fn x=>String.size(x))

fun count_some_var (s,p)=g (fn ()=>0) (fn x=>if x=s then 1 else 0) p

fun check_pat p=
  let fun get_string_list p=
	  case p of
	      Variable x=>[x]
	   |  TupleP l=> foldl (fn (x,y)=>(get_string_list x)@y) [] l
	   |  ConstructorP (_,ps) => get_string_list ps
	   | _ => []
      fun is_distinct lst=
	  case lst of
		     [] => true
		   | h::t => (not (List.exists (fn x=>x=h) t)) andalso (is_distinct t)
  in is_distinct(get_string_list(p)) 
  end
      
	      
  
  
				      

 


				  
				   
						
				       
	       
      
				     
		
 					  
				     
						    
						
					      
