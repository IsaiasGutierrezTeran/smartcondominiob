#!/usr/bin/env python3
"""
Script para verificar que los CORS están configurados correctamente para React
"""

import requests
import json

def test_cors_headers():
    """Simula una petición CORS como la haría React"""
    
    base_url = "http://127.0.0.1:8000"
    
    print("🧪 VERIFICACIÓN DE CORS PARA REACT")
    print("=" * 50)
    
    # Test 1: Preflight Request (OPTIONS)
    print("\n1️⃣ Probando petición OPTIONS (preflight CORS)...")
    try:
        response = requests.options(
            f"{base_url}/api/usuarios/login/",
            headers={
                'Origin': 'http://localhost:3000',
                'Access-Control-Request-Method': 'POST',
                'Access-Control-Request-Headers': 'Content-Type',
            }
        )
        
        print(f"   Status: {response.status_code}")
        print(f"   Headers CORS recibidos:")
        cors_headers = {k: v for k, v in response.headers.items() if 'access-control' in k.lower()}
        for header, value in cors_headers.items():
            print(f"   - {header}: {value}")
            
        if response.status_code == 200:
            print("   ✅ Preflight CORS OK!")
        else:
            print(f"   ⚠️  Preflight status: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Petición real desde React
    print("\n2️⃣ Probando petición POST real con Origin...")
    try:
        response = requests.post(
            f"{base_url}/api/usuarios/login/",
            headers={
                'Origin': 'http://localhost:3000',
                'Content-Type': 'application/json',
            },
            json={
                "username": "admin",
                "password": "admin123"
            }
        )
        
        print(f"   Status: {response.status_code}")
        cors_header = response.headers.get('Access-Control-Allow-Origin', 'No encontrado')
        print(f"   Access-Control-Allow-Origin: {cors_header}")
        
        if cors_header == 'http://localhost:3000':
            print("   ✅ CORS configurado correctamente para React!")
        elif cors_header == '*':
            print("   ✅ CORS abierto (desarrollo)")
        else:
            print("   ⚠️  CORS podría tener problemas")
            
        # Mostrar respuesta si hay errores útiles
        if response.status_code >= 400:
            try:
                error_data = response.json()
                print(f"   Respuesta: {error_data}")
            except:
                print(f"   Respuesta texto: {response.text[:200]}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Verificar otros puertos de React
    print("\n3️⃣ Probando otros puertos de React (Vite - 5173)...")
    try:
        response = requests.options(
            f"{base_url}/api/usuarios/login/",
            headers={
                'Origin': 'http://localhost:5173',
                'Access-Control-Request-Method': 'POST',
            }
        )
        
        print(f"   Status: {response.status_code}")
        cors_header = response.headers.get('Access-Control-Allow-Origin', 'No encontrado')
        print(f"   Access-Control-Allow-Origin: {cors_header}")
        
        if response.status_code == 200:
            print("   ✅ Vite CORS OK!")
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Verificar endpoint de health check
    print("\n4️⃣ Probando endpoint básico (API disponible)...")
    try:
        response = requests.get(f"{base_url}/api/")
        print(f"   Status API base: {response.status_code}")
        
        # Probar admin panel
        response = requests.get(f"{base_url}/admin/")
        print(f"   Status Admin: {response.status_code}")
        
    except Exception as e:
        print(f"   ❌ Error: {e}")

if __name__ == "__main__":
    print("🚀 Asegúrate de que el servidor Django esté corriendo en el puerto 8000")
    print("   Comando: python manage.py runserver")
    input("\nPresiona Enter cuando el servidor esté listo...")
    
    test_cors_headers()
    
    print("\n" + "=" * 50)
    print("📋 RESUMEN:")
    print("- Si ves 'Access-Control-Allow-Origin: http://localhost:3000' ✅")
    print("- Si ves status 200 o 405 (método no permitido) está bien ✅") 
    print("- Si ves errores de conexión, revisar que el servidor esté corriendo ❌")
    print("\n🔗 Desde React, usa estas URLs:")
    print("   - Login: http://127.0.0.1:8000/api/usuarios/login/")
    print("   - API Base: http://127.0.0.1:8000/api/")