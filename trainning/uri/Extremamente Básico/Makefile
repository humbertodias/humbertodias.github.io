FILE_NAME=Main

run: compile

	@echo -n 'C = '
	@./"$(FILE_NAME)_c" < in.txt > out.txt
	@-diff ok.txt out.txt &> diff.txt
	@[ -s diff.txt ] || echo "OK"

	@echo -n 'CPP = '
	@./"$(FILE_NAME)_cpp" < in.txt > out.txt
	@-diff ok.txt out.txt &> diff.txt
	@[ -s diff.txt ] || echo "OK"
	
	@echo -n 'Java = '
	@java "$(FILE_NAME)" < in.txt > out.txt
	@-diff ok.txt out.txt &> diff.txt
	@[ -s diff.txt ] || echo "OK"

	@echo -n 'Python = '
	@python "$(FILE_NAME).pyc" < in.txt > diff.txt
	@-diff ok.txt out.txt &> diff.txt
	@[ -s diff.txt ] || echo "OK"

	@# @$(MAKE) clean

compile:
	@gcc "$(FILE_NAME).c" -o "$(FILE_NAME)_c"
	@g++ "$(FILE_NAME).cpp" -o "$(FILE_NAME)_cpp"
	@javac "$(FILE_NAME)".java
	@python -m py_compile "$(FILE_NAME).py"

clean:
	@rm -f diff.txt "$(FILE_NAME).class" "$(FILE_NAME).pyc" "$(FILE_NAME)_cpp" "$(FILE_NAME)_c"