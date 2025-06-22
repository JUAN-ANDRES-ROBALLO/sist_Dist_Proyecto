import React, { useState, useEffect } from 'react'
import { usuariosService, terrenosService, maquinariaService, notificacionesService } from '../services/api'

export default function TestConnection() {
  const [testResults, setTestResults] = useState({})
  const [loading, setLoading] = useState(false)

  const runTests = async () => {
    setLoading(true)
    const results = {}

    try {
      // Test 1: Health check de usuarios
      try {
        const usuariosHealth = await usuariosService.health()
        results.usuariosHealth = { success: true, data: usuariosHealth }
      } catch (error) {
        results.usuariosHealth = { success: false, error: error.message }
      }

      // Test 2: Health check de terrenos
      try {
        const terrenosHealth = await terrenosService.health()
        results.terrenosHealth = { success: true, data: terrenosHealth }
      } catch (error) {
        results.terrenosHealth = { success: false, error: error.message }
      }

      // Test 3: Health check de maquinaria
      try {
        const maquinariaHealth = await maquinariaService.health()
        results.maquinariaHealth = { success: true, data: maquinariaHealth }
      } catch (error) {
        results.maquinariaHealth = { success: false, error: error.message }
      }

      // Test 4: Health check de notificaciones
      try {
        const notificacionesHealth = await notificacionesService.health()
        results.notificacionesHealth = { success: true, data: notificacionesHealth }
      } catch (error) {
        results.notificacionesHealth = { success: false, error: error.message }
      }

      // Test 5: Listar usuarios
      try {
        const usuarios = await usuariosService.getAll()
        results.usuariosList = { success: true, data: usuarios }
      } catch (error) {
        results.usuariosList = { success: false, error: error.message }
      }

      // Test 6: Listar fincas
      try {
        const fincas = await terrenosService.getFincas()
        results.fincasList = { success: true, data: fincas }
      } catch (error) {
        results.fincasList = { success: false, error: error.message }
      }

      // Test 7: Listar maquinaria
      try {
        const maquinaria = await maquinariaService.getAll()
        results.maquinariaList = { success: true, data: maquinaria }
      } catch (error) {
        results.maquinariaList = { success: false, error: error.message }
      }

      // Test 8: Listar notificaciones
      try {
        const notificaciones = await notificacionesService.getAll()
        results.notificacionesList = { success: true, data: notificaciones }
      } catch (error) {
        results.notificacionesList = { success: false, error: error.message }
      }

    } catch (error) {
      console.error('Error running tests:', error)
    } finally {
      setLoading(false)
    }

    setTestResults(results)
  }

  useEffect(() => {
    runTests()
  }, [])

  const getStatusIcon = (success) => {
    return success ? '✅' : '❌'
  }

  const getStatusColor = (success) => {
    return success ? 'text-green-600' : 'text-red-600'
  }

  return (
    <div className="test-connection-container" style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
      <h2>🔍 Test de Conexión Frontend-Backend</h2>
      
      <button 
        onClick={runTests} 
        disabled={loading}
        style={{
          padding: '10px 20px',
          backgroundColor: '#007bff',
          color: 'white',
          border: 'none',
          borderRadius: '5px',
          cursor: loading ? 'not-allowed' : 'pointer',
          marginBottom: '20px'
        }}
      >
        {loading ? 'Ejecutando tests...' : 'Ejecutar Tests'}
      </button>

      <div className="test-results">
        <h3>Resultados de las Pruebas:</h3>
        
        <div className="test-section">
          <h4>🏥 Health Checks:</h4>
          <div className="test-item">
            <span>Usuarios: </span>
            <span className={getStatusColor(testResults.usuariosHealth?.success)}>
              {getStatusIcon(testResults.usuariosHealth?.success)} 
              {testResults.usuariosHealth?.success ? 'Conectado' : testResults.usuariosHealth?.error || 'Error'}
            </span>
          </div>
          <div className="test-item">
            <span>Terrenos: </span>
            <span className={getStatusColor(testResults.terrenosHealth?.success)}>
              {getStatusIcon(testResults.terrenosHealth?.success)} 
              {testResults.terrenosHealth?.success ? 'Conectado' : testResults.terrenosHealth?.error || 'Error'}
            </span>
          </div>
          <div className="test-item">
            <span>Maquinaria: </span>
            <span className={getStatusColor(testResults.maquinariaHealth?.success)}>
              {getStatusIcon(testResults.maquinariaHealth?.success)} 
              {testResults.maquinariaHealth?.success ? 'Conectado' : testResults.maquinariaHealth?.error || 'Error'}
            </span>
          </div>
          <div className="test-item">
            <span>Notificaciones: </span>
            <span className={getStatusColor(testResults.notificacionesHealth?.success)}>
              {getStatusIcon(testResults.notificacionesHealth?.success)} 
              {testResults.notificacionesHealth?.success ? 'Conectado' : testResults.notificacionesHealth?.error || 'Error'}
            </span>
          </div>
        </div>

        <div className="test-section">
          <h4>📊 Datos de Prueba:</h4>
          <div className="test-item">
            <span>Listar Usuarios: </span>
            <span className={getStatusColor(testResults.usuariosList?.success)}>
              {getStatusIcon(testResults.usuariosList?.success)} 
              {testResults.usuariosList?.success ? 'OK' : testResults.usuariosList?.error || 'Error'}
            </span>
          </div>
          <div className="test-item">
            <span>Listar Fincas: </span>
            <span className={getStatusColor(testResults.fincasList?.success)}>
              {getStatusIcon(testResults.fincasList?.success)} 
              {testResults.fincasList?.success ? 'OK' : testResults.fincasList?.error || 'Error'}
            </span>
          </div>
          <div className="test-item">
            <span>Listar Maquinaria: </span>
            <span className={getStatusColor(testResults.maquinariaList?.success)}>
              {getStatusIcon(testResults.maquinariaList?.success)} 
              {testResults.maquinariaList?.success ? 'OK' : testResults.maquinariaList?.error || 'Error'}
            </span>
          </div>
          <div className="test-item">
            <span>Listar Notificaciones: </span>
            <span className={getStatusColor(testResults.notificacionesList?.success)}>
              {getStatusIcon(testResults.notificacionesList?.success)} 
              {testResults.notificacionesList?.success ? 'OK' : testResults.notificacionesList?.error || 'Error'}
            </span>
          </div>
        </div>

        <div className="test-summary" style={{ marginTop: '20px', padding: '15px', backgroundColor: '#f8f9fa', borderRadius: '5px' }}>
          <h4>📋 Resumen:</h4>
          <p>
            <strong>Estado General:</strong> 
            {Object.values(testResults).every(result => result?.success) ? 
              '🟢 TODOS LOS SERVICIOS CONECTADOS CORRECTAMENTE' : 
              '🟡 ALGUNOS SERVICIOS TIENEN PROBLEMAS'
            }
          </p>
          <p>
            <strong>Servicios Funcionando:</strong> {
              Object.values(testResults).filter(result => result?.success).length
            } / {Object.keys(testResults).length}
          </p>
        </div>
      </div>

      <style jsx>{`
        .test-connection-container {
          font-family: Arial, sans-serif;
        }
        .test-section {
          margin: 20px 0;
          padding: 15px;
          border: 1px solid #ddd;
          border-radius: 5px;
        }
        .test-item {
          margin: 10px 0;
          padding: 5px 0;
        }
        .text-green-600 {
          color: #059669;
        }
        .text-red-600 {
          color: #dc2626;
        }
      `}</style>
    </div>
  )
} 