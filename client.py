import click
import requests

@click.group()
def root():
    pass


@root.command()
@click.argument('url')
@click.option('--name',prompt='username')
@click.option('--password',prompt='password')
def login(url,name,password):
    payload={"userName":name,"password":password}
    r = requests.post(url+'/rating/login/',data=payload)
    if(r.status_code!=200):
        print("please check your url")
    else:
        print(r.text)

@root.command()
def loginout():
        r = requests.get('http://ml18b6h.pythonanywhere.com/rating/loginOut')
        print(r.text)

@root.command()
def list():
    r = requests.get('http://ml18b6h.pythonanywhere.com/rating/show')
    print(r.text)

@root.command()
def view():
    r = requests.get('http://ml18b6h.pythonanywhere.com/rating/showRatings/')
    print(r.text)
@root.command()
@click.argument('professor_id')
@click.argument('module_code')
def average(professor_id,module_code):
    payload = {"professor_id": professor_id, "module_code": module_code}
    r = requests.get('http://ml18b6h.pythonanywhere.com/rating/showRatings4Modules/', params=payload)
    print(r.text)

@root.command()
@click.argument('name')
@click.argument('password')
@click.argument('email')
def register(name,password,email):
    payload = {"userName": name, "password": password, "email":email}
    r = requests.post('http://ml18b6h.pythonanywhere.com/rating/register/', data=payload)
    print(r.text)

@root.command()
@click.argument('professor_id')
@click.argument('module_code')
@click.argument('year')
@click.argument('semester')
@click.argument('rating')
def rate(professor_id,module_code,year,semester,rating):
    payload = {"professor_id": professor_id, "module_code": module_code, "year":year,"semester":semester,"rating":rating}
    r = requests.post('http://ml18b6h.pythonanywhere.com/rating/rate/', data=payload)
    print(r.text)


if __name__ == '__main__':
    root()
