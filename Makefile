%.pdf: %.md
	pandoc $< -o $@ \
		-V colorlinks=true \
		-V linkcolor=red \
		-V urlcolor=blue \
		-V citecolor=green
