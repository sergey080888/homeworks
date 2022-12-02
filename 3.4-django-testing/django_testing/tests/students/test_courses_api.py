import pytest
from rest_framework.test import APIClient
from students.models import Course, Student
from model_bakery import baker


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def courses():
    return baker.make(Course, _quantity=10)


@pytest.fixture
def student():
    return Student.objects.create(name='Ivan', birth_date='2022-11-29')


@pytest.mark.django_db
def test_first_course_retrieve(client, course_factory,):
    course = course_factory()
    response = client.get(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 200
    data = response.json()
    assert len([data]) == len(Course.objects.all())
    assert data['name'] == Course.objects.first().name


@pytest.mark.django_db
def test_courses_list(client, courses):
    response = client.get(f'/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_courses_filter_id(client, courses):
    for i in range(len(courses)):
        response = client.get(f'/api/v1/courses/?id={(courses[i]).id}')
        data = response.json()
        assert response.status_code == 200
        assert data[0]['id'] == courses[i].id


@pytest.mark.django_db
def test_courses_filter_name(client, courses):
    for i in range(len(courses)):
        response = client.get(f'/api/v1/courses/?name={(courses[i]).name}')
        data = response.json()
        assert response.status_code == 200
        assert data[0]['name'] == courses[i].name


@pytest.mark.django_db
def test_courses_create_course(client, student):
    count = Course.objects.count()
    response = client.post(f'/api/v1/courses/', data={'name': 'Django', 'students': student.id})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_courses_update_course(client, courses):
    response = client.patch(f'/api/v1/courses/{courses[0].id}/', data={'name': 'Flask'})
    assert response.status_code == 200
    data = response.json()
    assert data['name'] != courses[0].name


@pytest.mark.django_db
def test_courses_delete_course(client, courses):
    response = client.delete(f'/api/v1/courses/{courses[0].id}/')
    assert response.status_code == 204
    response = client.get(f'/api/v1/courses/{courses[0].id}/')
    assert response.status_code == 404
