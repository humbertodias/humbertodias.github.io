FILE_NAME=Main

run: run_c run_cpp run_java run_python2 run_python3

run_c: compile_c

	@echo -n 'C = '
	@./"$(FILE_NAME)_c" < in.txt > out.txt
	@-diff ok.txt out.txt &> diff.txt
	@[ -s diff.txt ] || echo "OK"

run_cpp: compile_cpp

	@echo -n 'CPP = '
	@./"$(FILE_NAME)_cpp" < in.txt > out.txt
	@-diff ok.txt out.txt &> diff.txt
	@[ -s diff.txt ] || echo "OK"

run_java: compile_java

	@echo -n 'Java = '
	@java "$(FILE_NAME)" < in.txt > out.txt
	@-diff ok.txt out.txt &> diff.txt
	@[ -s diff.txt ] || echo "OK"

run_python2: compile_python2

	@echo -n 'Python2 = '
	@python2 "$(FILE_NAME)2.pyc" < in.txt > out.txt
	@-diff ok.txt out.txt &> diff.txt
	@[ -s diff.txt ] || echo "OK"

run_python3: compile_python3

	@echo -n 'Python3 = '
	@python3 "$(FILE_NAME)3.py" < in.txt > out.txt
	@-diff ok.txt out.txt &> diff.txt
	@[ -s diff.txt ] || echo "OK"
	
compile_c:
	@gcc "$(FILE_NAME).c" -o "$(FILE_NAME)_c" -O2 -lm

compile_cpp:
	@g++ "$(FILE_NAME).cpp" -o "$(FILE_NAME)_cpp" -Wall -std=c++11 -O2 -lm

compile_java:
	@javac "$(FILE_NAME).java"

compile_python2:
	@python2 -m py_compile "$(FILE_NAME)2.py"

compile_python3:
	@python3 -m py_compile "$(FILE_NAME)3.py"

compile: compile_c compile_cpp compile_java compile_python2 compile_python3

clean:
	@rm -rf __pycache__ diff.txt *.class *.pyc "$(FILE_NAME)_cpp" "$(FILE_NAME)_c"
