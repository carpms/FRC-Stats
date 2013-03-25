scores = finscores.dat bptsscores.dat fptsscores.dat

all: scores.png stats

stats:
	./stats.py

scores.png: $(scores)
	gnuplot "./pyramid histogram.gnuplot"
	gnuplot "./total histogram.gnuplot"
	gnuplot "./foul histogram.gnuplot"

%scores.dat: frcspy.xml
	./scores.py $< $* > $@

frcspy.xml:
	wget http://www.chiefdelphi.com/forums/frcspy.php?xml=2 -O $@

clean:
	rm frcspy.xml $(scores) *.png
