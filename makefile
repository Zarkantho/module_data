html dirhtml json: bootstrap
	@make -C docs $@
bootstrap:
	@cd docs; rm -rf docs; ln -s ../build
	@cd docs; python bootstrap.py safe
