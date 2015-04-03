# Check that source code conforms to PEP8.
if pep8 --show-source opt_flow.py opt_flow_tests.py; then
	echo "No style errors found. You're so hip!"
else
	echo "Some style errors detected."
fi
echo ""

# Run unit tests.
if python opt_flow_tests.py; then
	echo "All unit tests passing. Congrats!"
else
	echo "Some unit tests failing."
fi
