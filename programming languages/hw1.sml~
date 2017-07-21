
fun is_older (date1:int*int*int, date2:int*int*int) =
  if #1 date1 < #1 date2
  then true
  else
      if #1 date1= #1 date2
      then
	  if #2 date1< #2 date2
	  then true
	  else
	      if #2 date1= #2 date2
	      then #3 date1< #3 date2
	      else false
      else false
	       
fun number_in_month (dates: (int*int*int) list, month:int)=
  if null dates
  then 0
  else
      if #2 (hd dates) = month
      then 1+number_in_month(tl dates,month)
      else number_in_month(tl dates,month)
	  
			     
fun number_in_months (dates:(int*int*int) list, months: int list)=
  if null months
  then 0
  else
      number_in_month(dates,hd months)+number_in_months(dates,tl months)
						      
fun dates_in_month (dates: (int*int*int) list, month:int)=
  if null dates
  then []
  else
      if #2 (hd dates)=month
      then hd dates::dates_in_month(tl dates,month)
      else dates_in_month(tl dates,month)

fun dates_in_months (dates: (int*int*int) list, months:int list)=
  if null months
  then []
  else dates_in_month(dates,hd months)@ dates_in_months(dates,tl months)

fun get_nth (strings:string list,pos:int)=
    if pos=1
    then hd strings
    else get_nth(tl strings,pos-1)

fun date_to_string (date:int*int*int)=
  let val names=["January", "February", "March", "April","May", "June", "July", "August", "September", "October","November", "December"]
  in get_nth(names,#2 date)^" "^Int.toString(#3 date)^", "^Int.toString(#1 date)
  end

fun number_before_reaching_sum (sum:int,nums:int list)=
  if hd nums>=sum
  then 0
  else 1+number_before_reaching_sum(sum-(hd nums),tl nums)
			       
fun what_month (day:int)=
  let val month=[31,28,31,30,31,30,31,31,30,31,30,31]
  in 1+number_before_reaching_sum(day,month)
  end

fun month_range (day1:int, day2:int)=
  if day1>day2
  then []
  else what_month(day1)::month_range(day1+1,day2)

fun oldest(dates:(int*int*int) list)=
  if null dates
  then NONE
  else
      let val ans=oldest(tl dates)
      in if isSome ans andalso is_older(valOf(ans),hd dates)
	 then ans
	 else SOME(hd dates)
      end

fun set(nums:int list)=
  let fun duplicate(x:int, l:int list)=
	if null l
	then false
	else hd l=x orelse duplicate(x,tl l)
  in
      if null nums
      then []
      else
	  let val s=set(tl nums)
	  in if duplicate(hd nums,s)
	     then s
	     else hd nums::s
	  end
  end
      
      
  
fun number_in_months_challenge (dates:(int*int*int) list,months:int list) =
  number_in_months(dates,set(months))

fun dates_in_months_challenge (dates:(int*int*int) list,months:int list)=
  dates_in_months(dates,set(months))

fun reasonable_date (date:(int*int*int))=
  if #1 date <0
  then false
  else
      if #2 date<0 orelse #2 date>12
      then false
      else
	  let val month=[31,28,31,30,31,30,31,31,30,31,30,31]
	      val  leap= #1 date mod 40=0 orelse (#1 date mod 4=0 andalso #1 date mod 100<>0)
	      fun get_nth_num (nums:int list,n:int)=
		if n=1 then hd nums
		else get_nth_num(tl nums,n-1)			
	  in if #2 date=2 andalso leap
	     then #3 date >0 andalso #3 date<=29
	     else #3 date>0 andalso #3 date<=get_nth_num(month,#2 date)
	  end
	      
						    
			      	  
     
