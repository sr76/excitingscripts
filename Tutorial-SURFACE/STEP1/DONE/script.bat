str="3.3 3.38 3.43 3.5"
for a in $str;
do
str2="GGAPerdew-Burke-Ernzerhof LDA-X-alpha"
for c in $str2;
do
mkdir $a-$c
cd $a-$c

cat > input.xml<<EOF
<input>
  <title>Copper: Bulk Calculations</title>
  <structure speciespath="$EXCITINGROOT/species">
    <crystal scale="$a">
      <basevect> 1.0     1.0     0.0 </basevect>
      <basevect> 0.0     1.0     1.0 </basevect>
      <basevect> 1.0     0.0     1.0</basevect>
    </crystal>
    <species speciesfile="Cu.xml" >
      <atom coord="   0.0  0.0  0.0 "/>
    </species>
  </structure>
  <groundstate ngridk="10 10 10"
               xctype="$c"
               rgkmax="8.0d0">
  </groundstate>
    <properties>
    </properties>
</input>
EOF
excitingser 
tail -1 TOTENERGY.OUT >> ../$a-$c.dat
cd ..
done
done
grep "  " *alpha.dat >energy.latticeLDA-X-alpha
grep "  " *rhof.dat >energy.latticeGGAPerdew-Burke-Ernzerhof