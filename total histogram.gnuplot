reset
n=300	#number of intervals
max=300.	#max value
min=0.	#min value
width=(max-min)/n	#interval width
#function used to map a value to the intervals
hist(x,width)=width*floor(x/width)+width/2.0
set term pngcairo size 1024,512	#output terminal and file
set output "scores.png"
set xrange [min:max]
set yrange [0:]
#to put an empty boundary around the
#data inside an autoscaled graph.
set offset graph 0.05,0.05,0.05,0.0
set xtics min,(max-min)/15,max
set boxwidth width
set style fill solid 0.5	#fillstyle
set tics out nomirror
set xlabel "score"
set ylabel "Frequency"
#count and plot
e = 2.71828
plot "finscores.dat" u (hist($1,width)):(1.0) smooth freq w boxes lc rgb"grey" notitle
