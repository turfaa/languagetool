# Language Tool
This is the https://languagetool.org/ API consumer. I added some hacks in the check function in the main program. You can remove it if you wish.

## Usage
### Get All Available Languages
```
./langTool.py languages
```

### Check A Text File
```
./langTool.py check <language-code> <path-to-file>
```

### Importing
```python
import langTool
LT = langTool.LanguageTool()
LT.getLanguages()
LT.check(language-code, path-to-file)
```
