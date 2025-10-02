#!/usr/bin/env python3
"""
Script de prueba para verificar la conectividad del backend
Ejecutar con: python test_backend_connectivity.py
"""

import requests
import json
import sys

# Configuración
BASE_URL = "http://127.0.0.1:8000/api"
CREDENTIALS = {
    "admin": {"username": "admin", "password": "admin123"},
    "residente1": {"username": "residente1", "password": "isaelOrtiz2"},
    "seguridad1": {"username": "seguridad1", "password": "guardia123"}
}

def test_api_root():
    """Test de conectividad básica"""
    print("🔍 Testing API Root...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ API Root accessible")
            return True
        else:
            print(f"❌ API Root failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

def test_login(username, password):
    """Test de login"""
    print(f"🔐 Testing login for {username}...")
    try:
        response = requests.post(f"{BASE_URL}/login/", 
                               json={"username": username, "password": password})
        if response.status_code == 200:
            data = response.json()
            token = data.get('token')
            print(f"✅ Login successful, token: {token[:20]}...")
            return token
        else:
            print(f"❌ Login failed: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Login error: {e}")
        return None

def test_authenticated_request(token, endpoint):
    """Test de request autenticada"""
    print(f"🔒 Testing authenticated request to {endpoint}...")
    try:
        headers = {"Authorization": f"Token {token}"}
        response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
        if response.status_code == 200:
            data = response.json()
            count = len(data.get('results', data)) if isinstance(data, dict) else len(data)
            print(f"✅ {endpoint} accessible, {count} items")
            return True
        else:
            print(f"❌ {endpoint} failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Request error: {e}")
        return False

def main():
    print("🚀 Backend Connectivity Test")
    print("="*50)
    
    # Test 1: API Root
    if not test_api_root():
        print("❌ Basic connectivity failed. Make sure server is running.")
        sys.exit(1)
    
    print()
    
    # Test 2: Login
    token = None
    for user_type, creds in CREDENTIALS.items():
        token = test_login(creds["username"], creds["password"])
        if token:
            print(f"✅ Login working for {user_type}")
            break
    
    if not token:
        print("❌ No login successful. Check credentials.")
        sys.exit(1)
    
    print()
    
    # Test 3: Authenticated endpoints
    endpoints_to_test = [
        "/usuarios/",
        "/condominio/propiedades/",
        "/finanzas/pagos/",
        "/seguridad/visitas/",
        "/mantenimiento/solicitudes/"
    ]
    
    successful_endpoints = 0
    for endpoint in endpoints_to_test:
        if test_authenticated_request(token, endpoint):
            successful_endpoints += 1
    
    print()
    print("📊 RESULTS:")
    print(f"✅ Successful endpoints: {successful_endpoints}/{len(endpoints_to_test)}")
    
    if successful_endpoints == len(endpoints_to_test):
        print("🎉 ALL TESTS PASSED! Your backend is ready for React frontend.")
    else:
        print("⚠️  Some endpoints failed. Check the server logs.")
    
    print("\n🔗 URLs to test in your React app:")
    print(f"API Root: {BASE_URL}/")
    print(f"Login: {BASE_URL}/login/")
    print(f"Docs: http://127.0.0.1:8000/api/schema/swagger-ui/")

if __name__ == "__main__":
    main()