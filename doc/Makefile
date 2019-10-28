_mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
I := $(patsubst %/,%,$(dir $(_mkfile_path)))
O ?= build/

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = $(I)/source
BUILDDIR      = build

help:
all:
.PHONY: all help

DEPDIR := $(O).deps
STAMPDIR := $(O).stamps
DOTDIRS := $(DEPDIR) $(STAMPDIR)
IGNORE_MANIFEST := $(I)/ignore.manifest

# Create the dependency directory
$(DEPDIR): ; @mkdir -p $@
$(STAMPDIR): ; @mkdir -p $@

# -----------------------------
# Bootstrap virtual environment
# -----------------------------
PYENV_DIR := $(O).pyenv
PYENV_WITNESS := $(STAMPDIR)/pyenv.witness
PYENV_WANT := $(STAMPDIR)/pyenv.want
PYENV_MANIFEST := $(STAMPDIR)/pyenv.manifest
PYENV_GLOB := $(shell cat $(PYENV_MANIFEST) 2>/dev/null | tr '\n' ' ' || true)

$(PYENV_WANT) $(PYENV_GLOB) $(PYENV_MANIFEST): | $(DOTDIRS)
	@echo 'missing glob: $@' >> $(PYENV_WANT)
	@touch $(PYENV_WANT)

$(PYENV_WITNESS): $(PYENV_WANT) | $(PYENV_GLOB) $(PYENV_MANIFEST)
	@head $(PYENV_WANT)
	truncate -s 0 $(PYENV_WANT)
	rm -rf $(PYENV_DIR)
	virtualenv -p python3 $(PYENV_DIR)
	find $(PYENV_DIR) -type l,f | sort > $(PYENV_MANIFEST).1
	comm -1 -3 $(IGNORE_MANIFEST) $(PYENV_MANIFEST).1 > $(PYENV_MANIFEST)
	touch $(PYENV_WITNESS)

all: $(PYENV_WITNESS)

# Activate the virtualenv for the remainder of the build
export PATH := $(PYENV_DIR)/bin:$(PATH)
export VIRTUALENV := $(PYENV_DIR)
export PYTHONDONTWRITEBYTECODE := 1

# ---------------------------
# Install python requirements
# ---------------------------
PYREQ_WITNESS := $(STAMPDIR)/pyreq.witness
PYREQ_WANT := $(STAMPDIR)/pyreq.want
PYREQ_MANIFEST := $(STAMPDIR)/pyreq.manifest
PYREQ_GLOB := $(shell cat $(PYREQ_MANIFEST) 2>/dev/null | tr '\n' ' ' || true)

$(PYREQ_WANT) $(PYREQ_GLOB) $(PYREQ_MANIFEST): | $(DOTDIRS)
	@echo 'missing glob: $@' >> $(PYREQ_WANT)
	@touch $(PYREQ_WANT)

$(PYREQ_WITNESS):  $(I)/requirements.txt $(PYENV_WITNESS) \
    $(PYREQ_WANT) | $(PYREQ_GLOB) $(PYREQ_MANIFEST)
	@head $(PYREQ_WANT)
	truncate -s 0 $(PYREQ_WANT)
	pip install -r $(I)/requirements.txt
	find $(PYENV_DIR) -type l,f | sort > $(PYREQ_MANIFEST).1
	comm -1 -3 $(IGNORE_MANIFEST) $(PYREQ_MANIFEST).1 > $(PYREQ_MANIFEST).2
	comm -1 -3 $(PYENV_MANIFEST) $(PYREQ_MANIFEST).2 > $(PYREQ_MANIFEST)
	touch $(PYREQ_WITNESS)

all: $(PYREQ_WITNESS)

# Put it first so that "make" without argument is like "make help".
help: $(PYREQ_WITNESS) Makefile
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
html: $(PYREQ_WITNESS) Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
