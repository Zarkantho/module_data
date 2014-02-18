html dirhtml json: bootstrap
	@make -C docs $@
bootstrap:
	@cd docs; rm -rf build; ln -s ../build
	@mkdir -p build
	@cd docs; python bootstrap.py safe
