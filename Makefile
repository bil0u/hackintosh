all: backup clean restore

backup:
	@python -Bc 'import tools.manage_config; tools.manage_config.backup_secrets()'

clean:
	@python -Bc 'import tools.manage_config; tools.manage_config.clean_config()'

restore:
	@python -Bc 'import tools.manage_config; tools.manage_config.restore_config()'
