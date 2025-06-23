import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Exponer a la red
    port: 5173,
    watch: {
      usePolling: true,
      interval: 1000, // revisa cada 1 segundo
    },
    proxy: {
      '/api/usuarios': {
        target: 'http://usuarios:8000',
        changeOrigin: true,
      },
      '/api/terrenos': {
        target: 'http://terrenos:8000',
        changeOrigin: true,
      },
      '/api/maquinaria': {
        target: 'http://maquinaria:8000',
        changeOrigin: true,
      },
      '/api/notificaciones': {
        target: 'http://notificaciones:8000',
        changeOrigin: true,
      },
    }
  }
})
