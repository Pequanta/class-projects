import { useState } from 'react'
import './App.css'
import InputBox from './Components/InputBox.jsx'
import OutputBox from './Components/OutputBox'
function App() {

  return (
    <div className="main-page">
      <div className="sub-div">
        <InputBox boxLabel="Encrypt" keyType="Encryption" />
        <OutputBox />
        <button>Encrypt</button>
      </div>
      <div className="sub-div">
        <InputBox boxLabel="Decrypt" keyType="Decryption"/>
        <OutputBox />
        <button>Decrypt</button>
      </div>
    </div>
  )
}

export default App
