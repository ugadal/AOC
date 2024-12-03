for pre in range(10):
	for post in range(10):
		pw="".join([str(x) for x in range(pre)])
		pw+="x"
		pw+="".join([chr(97+x) for x in range(post)])
		o=pw
		ps=pw.index("x")
		if ps>=4:ps+=2
		else:ps+=1
		# ~ print(ps)
		ps%=len(pw)
		# ~ print(ps)
		pw=pw[-ps:]+pw[:-ps]
		print(len(pw),pw.index("x"),"=>",o.index("x"),o,pw)
		
