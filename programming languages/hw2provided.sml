(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)

fun all_except_option (s,lst)=
  case lst of
      [] => NONE
    | x::l => case all_except_option(s,l) of
		    NONE => if same_string(x,s) then SOME l
			    else NONE
		  | SOME y => SOME (x::y)

fun get_substitutions1 (substitutions,s)=
  case substitutions of
      [] => []
    | x::xs =>  case all_except_option(s,x)  of
		      NONE => get_substitutions1 (xs,s)
		   |  SOME strings => strings @ get_substitutions1 (xs,s)

fun get_substitutions2 (substitutions,s)=
  let fun get_strings(sub,str,lst)=
	case sub of
	    []=>lst
	  | h::t => case all_except_option(str,h) of
			NONE => get_strings(t,str,lst)
			     | SOME re => get_strings(t,str,re@lst) 
  in get_strings (substitutions,s,[])
  end

fun similar_names(substitutions,fullname)=
  let fun name_generator(f,m,l)=
	case f of
	    [] =>[]
	  | h::t=> {first=h,last=l,middle=m}::name_generator(t,m,l)
  in case fullname of
	 {first=x,middle=y,last=z} => {first=x,middle=y,last=z}::name_generator(get_substitutions1(substitutions,x),y,z)
  end
      
  

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)
