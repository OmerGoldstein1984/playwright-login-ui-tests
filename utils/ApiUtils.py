import playwright
from playwright.sync_api import Playwright

class ApiUtils():
    baseUrl="http://127.0.0.1:5000"
    headers = {
        "Authorization": "secret_token",
        "Content-Type": "application/json"
    }

    def CreteCar(self,playwright:Playwright):
        apiRequestContext = playwright.request.new_context(base_url=self.baseUrl)
        newCar= {
            "make": "Box",
            "model": "AhC",
            "year": 2025,
            "color": "Green"
        }

        response=apiRequestContext.post('/cars',data=newCar,headers=self.headers)
        if response.status==200:
            return f"Car {response.json()} created"
        else:
            print(f"Failed to create car. Status code: {response.status}")
            print(response.text())  # Print the error message

    def UpdateCar(self,playwright:Playwright):
        apiRequestContext = playwright.request.new_context(base_url=self.baseUrl)
        newCar= {
            "make": "Box",
            "model": "AAAA",
            "year": 2025,
            "color": "YELLOW"
        }

        response=apiRequestContext.put('/cars/3',data=newCar,headers=self.headers)
        if response.status==200:
            return f"Car {response.json()} updated"
        else:
            print(f"Failed to update car. Status code: {response.status}")


    def getCar(self, playwright: Playwright, id):
        apiRequestContext = playwright.request.new_context(base_url=self.baseUrl)
        response = apiRequestContext.get(f'/cars/{id}', headers=self.headers)
        print(response.body())







