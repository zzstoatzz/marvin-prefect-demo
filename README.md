## `marvin` 🤝 `prefect`

### Following along
- Clone this repo
```bash
git clone https://github.com/zzstoatzz/marvin-prefect-demo.git
```

- Create a virtual environment
```bash
python3 -m venv venv
```

- Activate the virtual environment
```bash
source venv/bin/activate
```

- Install the dependencies
```bash
pip install -r requirements.txt
```
... which will install `marvin` and `prefect` and [some other stuff](https://github.com/PrefectHQ/marvin/blob/main/pyproject.toml#L56).

- Set your `OPENAI_API_KEY` in `~/.marvin/.env`
```
cat ~/.marvin/.env | grep OPENAI_API_KEY
    OPENAI_API_KEY=sk-...
```