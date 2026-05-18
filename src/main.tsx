import React from 'react'
import ReactDOM from 'react-dom/client'
import './assets/main.css'
import App from './App'
import TooltipApp from './pages/TooltipApp'

const mode = new URLSearchParams(window.location.search).get('mode')

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    {mode === 'tooltip' ? <TooltipApp /> : <App />}
  </React.StrictMode>
)
