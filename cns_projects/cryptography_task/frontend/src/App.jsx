import { useState } from 'react'
import './App.css'
import InputBox from './Components/InputBox.jsx'
import OutputBox from './Components/OutputBox.jsx'
function App() {
 
  const [algorithm, setAlgorithm] = useState("otp"); //holds the users seleection
  const [message, setMessage] = useState();
  const [outputMessage, setOutputMessage] = useState();
  const [encryptionOutput, setEncryptionOutput] = useState();
  const [encryptionKey, setEncryptionKey] = useState();

  const messageEncryptDecrypt = async (actionType)=>{  
    let request, response;
    switch(actionType){
      case "encrypt":
        request = await fetch(`http://0.0.0.0:8080/crypto/encrypt-message?message=${message}&key=${encryptionKey}&algorithm=${algorithm}`,
          {
            method: "POST"
          }
        );
        response = await request.json();
        setOutputMessage(response);
        console.log(response)
        break;
      case "decrypt":
        request = await fetch(`http://0.0.0.0:8080/crypto/decrypt-message`,
          {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            
            body:JSON.stringify({
              message: message,
              key: encryptionKey,
              algorithm: algorithm
            })
          }
        );
        response = await request.json();
        setEncryptionOutput(response);
        console.log(response)
        break;
      default:
        console.log("Invalid request")
    }
    
  }


  return (
    <div className="main-page">
      <div className="sub-div">
        <InputBox
          boxLabel="Encrypt"
          keyType="Encryption" 
          setAlgorithm = {setAlgorithm} 
          setMessage={setMessage}
          setEncryptionKey={setEncryptionKey}
        />
        <OutputBox message={outputMessage}/>
        <button onClick={()=>messageEncryptDecrypt("encrypt")}>Encrypt</button>
      </div>
      <div className="sub-div">
        <InputBox
          boxLabel="Decrypt"
          keyType="Decryption" 
          setAlgorithm = {setAlgorithm} 
          setMessage={setMessage}
          setEncryptionKey={setEncryptionKey}
        />
        <OutputBox message={encryptionOutput}/>
        <button onClick={()=>messageEncryptDecrypt("decrypt")}>Decrypt</button>

      </div>
    </div>
  )
}

export default App
