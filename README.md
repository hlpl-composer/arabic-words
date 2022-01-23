
# hlpl_arabic_words

hlpl_arabic_words lists nouns, verbs, articles, nouns prefix, nouns suffix, verbs prefix, and verbs suffix in a readable database file. The package contains:  

> **active participle:**  List of all "أسماء-الأفعال" <br>  
> **passive participle:**  List of all "أسماء-المفعول"   
> **masdar:**  List of all "المصادر" 
> **verb:**  List of all "الأفعال" 
> **article:**  List of all "الأدوات" 
> **soun-suffix**  List of all "حروف-تلحق-الاسماء"  
> **noun-prefix:**  List of all "حروف-تسبق-الاسماء"  
> **verb-suffix:**  List of all "حروف-تلحق-الافعال"  
> **verb-prefix:**  List of all "حروف-تسبق-الاسماء" 


## Basic Usage: 

### Installation
This package can be installed from [PyPi](https://pypi.python.org/pypi/hlpl_arabic_words) by running:
```
pip install hlpl_arabic_words
```

### Command line: 

To get some info about the sofwtare, on console, execute the command line:
```
hlpl_arabic_words
```
To get the sofwtare version, on console, execute the command line:
```
hlpl_arabic_words version
```


### Basic usage: 

To return list of Arabic words list, execute:
```
from hlpl_arabic_words import arabic_words
hlpl_list=arabic_words.get(case)
```
`case` could be any element in the following list:
```
case=['فاعل','مفعول','مصدر','فعل','بداية-فعل','نهاية-فعل','بداية-اسم','نهاية-اسم','أداة','connection']
```
> **Note:** If `case==connection`, the returned value is the connection to database file

### License
hlpl_arabic_words is licensed under the [MIT license](https://opensource.org/licenses/MIT).



<p style="font-size:19px;color:green;font-weight:bold;">Contributions are welcome! Please make a pull request.</p>

#### Development pattern for contributors

1. [Create a fork](https://help.github.com/articles/fork-a-repo/) of the [main hlpl_arabic_words repository](https://github.com/hlpl/arabic-words) on GitHub.
2. Make your changes in a branch named something different from `master`, e.g. create a new branch `my-pull-request`.
3. [Create a pull request](https://help.github.com/articles/creating-a-pull-request/).

