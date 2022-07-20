.DEFAULT_GOAL := help

.PHONY: help install dev build lint type-check clean

help:
	@echo Available commands:
	@echo   install      - Install project dependencies
	@echo   dev          - Start development server (Electron + Vite)
	@echo   build        - Build the application for production
	@echo   lint         - Run ESLint
	@echo   type-check   - Run TypeScript type checking
	@echo   clean        - Remove build artifacts and cache

install:
	npm install

dev:
	npm run dev

build:
	npm run build

lint:
	npm run lint

type-check:
	npm run type-check

clean:
	rm -rf dist out node_modules/.cache
