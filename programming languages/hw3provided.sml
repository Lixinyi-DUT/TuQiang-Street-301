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

 


				  
				   
						
				       
	       
      
				     
		
 					  
				     
						    
						
					      
