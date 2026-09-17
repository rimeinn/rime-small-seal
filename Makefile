.PHONY: all clean
all: opencc/small_seal.ocd2 opencc/small_seal.json

small_seal.txt small_seal.json NOMCJK.txt &: gen.py SealSources.txt
	python3 gen.py

opencc/small_seal.ocd2: small_seal.txt
	mkdir -p opencc
	opencc_dict -i $< -o $@ -f text -t ocd2

opencc/small_seal.json: small_seal.json
	mkdir -p opencc
	cp $< $@

clean:
	rm -f small_seal.txt small_seal.json NOMCJK.txt opencc/small_seal.ocd2 opencc/small_seal.json
