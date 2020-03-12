import click
import requests
s = requests.session()
check_list = list()
@click.group()
def root():
    pass

@root.command()
def register():
    print("register")

@root.command()
@click.option('--name',prompt='username')
@click.option('--password',prompt='password')
def login(name,password):
    payload={"userName":name,"password":password}
    r = s.get('http://localhost:8000/rating/login',params=payload)
    if(r.status_code!=200):
        print("please check your url")
    else:
        print(r.text)

@root.command()
def loginout():
        r = s.get('http://localhost:8000/rating/loginOut')
        print(r.text)

@root.command()
def list():
    r = s.get('http://localhost:8000/rating/show')
    print(r.text)

@root.command()
def view():
    r = s.get('http://localhost:8000/rating/showRatings/')
    print(r.text)
@root.command()
@click.argument('professor_id')
@click.argument('module_code')
def average(professor_id,module_code):
    payload = {"professor_id": professor_id, "module_code": module_code}
    r = s.get('http://localhost:8000/rating/showRatings4Modules/', params=payload)
    print(r.text)

@root.command()
@click.argument('professor_id')
@click.argument('module_code')
@click.argument('year')
@click.argument('semester')
@click.argument('rating')
def rate(professor_id,module_code,year,semester,rating):
    payload = {"professor_id": professor_id, "module_code": module_code, "year":year,"semester":semester,"rating":rating}
    r = s.get('http://localhost:8000/rating/rate/', params=payload)
    print(r.text)


if __name__ == '__main__':
    root()
