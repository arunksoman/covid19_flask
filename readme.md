# Follow these steps:

1. Install any stable versions of python like 3.6.5/ 3.7.2/ 3.8.5.

Don't forget to add path to environmental variable

![img](https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png)

2. Navigate to directory using:
```
cd Covid19
```

3. Create virtual Environment
```
python -m venv venv
```

4. Activate virtual environmental

For Windows:
```
.\venv\Scripts\activate
```

For Ubuntu

```
source venv/bin/activate
```

5. Upgrade setuptools and pip:

```
python -m pip install --upgrade setuptools pip
```

6. Install requirements:

```
pip install -r requirements.txt
```
