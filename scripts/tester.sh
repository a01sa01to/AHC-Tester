# Write test script
# Runs in tools directory
../a.out < in/$1.txt 1> out/$1.txt 2> err/$1.txt
EXCODE=$?
if [ $EXCODE -gt 0 ]; then
  cat err/$1.txt
  exit $EXCODE
fi
echo "::group::stdout"
cat out/$1.txt
echo "::endgroup::"
echo "::group::stderr"
cat err/$1.txt
echo "::endgroup::"