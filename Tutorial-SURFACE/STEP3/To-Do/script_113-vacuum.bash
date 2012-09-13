str="1 5 8"
for a in $str
do
mkdir 113-$a
cp HEAD input.xml
tail -12 113-"$a"Ang.exi | head -9 >> input.xml
cat TAIL >> input.xml
mv input.xml 113-$a
cd 113-$a
excitingser
cp input.xml input.xml.backup
head -16  input.xml > new.input
cat ../BAND_DOS.txt >> new.input
mv new.input input.xml
excitingser
xsltproc \$EXCITINGROOT/xml/visualizationtemplates/xmlband2agr.xsl bandstructure.xml 
xsltproc --stringparam ID "t///" \$EXCITINGROOT/xml/visualizationtemplates/xmldos2grace.xsl dos.xml >tdos.agr
cd ..

done
