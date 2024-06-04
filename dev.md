# Install dev

    python -m venv env
    source env/bin/activate
    pip install -e .
    pip install -r requirements/dev.txt


# Test as importable library

#### create project beside /ruption dir

    mkdir ruptiontest && cd ruptiontest
    python -m venv env
    source env/bin/activate
    pip install -e ../ruption
    mkdir .vscode/ && touch .vscode/settings.json
    echo "{\"python.autoComplete.extraPaths\": [\"./ruption\"],\"python.analysis.extraPaths\": [\"./ruption\"]}" >> .vscode/settings.json