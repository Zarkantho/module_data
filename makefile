html dirhtml json: bootstrap
	@make -C docs $@
bootstrap:
	@cd docs; python bootstrap.py safe
