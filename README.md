# Unittest Ödevi

Bu repository, Taha Çağlar ,190722092  Tarafından yapılan Unittest kütüphanesi kullanılarak yazılmış basit bir Python test örneğini içerir.

## Test Özellikleri

1. **API 1: GET To Get User Information**
   - API URL: https://automationexercise.com/api/getUserInfo
   - Request Method: GET
   - Response Code: 200
   - Response Message: User information retrieved successfully!

2. **API 2: POST To Create User**
   - API URL: https://automationexercise.com/api/createUser
   - Request Method: POST
   - Request Parameters: name, email, password
   - Response Code: 201
   - Response Message: User created successfully!

3. **API 3: POST To Verify Login with Valid Details**
   - API URL: https://automationexercise.com/api/verifyLogin
   - Request Method: POST
   - Request Parameters: email, password
   - Response Code: 200
   - Response Message: User exists!

...

## Nasıl Çalıştırılır

1. Repoyu bilgisayarınıza klonlayın.
   ```bash
   git clone https://github.com/your-username/unittest-odevi.git
   ```

2. Proje dizinine gidin.
   ```bash
   cd unittest-odevi
   ```

3. Unit testleri çalıştırın.
   ```bash
   python -m unittest test_module.py
   ```
