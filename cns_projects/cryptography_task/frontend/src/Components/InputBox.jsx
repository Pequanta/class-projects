import styles from "./components.module.css";
import { useState } from "react";
function InputBox(props){

    const changeAlgorithm = (event) =>{
        props.setAlgorithm(event.target.value);
        setAlgorithm(event.target.value) //To allow the local variable to change inorder to be accessed by the select-option tag
    }

    const handleMessageChange = (event) =>{
        props.setMessage(event.target.value);
        console.log(event.target.value)
    }

    const handleKeyChange = (event) =>{
        props.setEncryptionKey(event.target.value);
        console.log(event.target.value)
    }

    
    const [algorithm, setAlgorithm] = useState();
    return(
        <div className={styles.inputDiv}>
            <h1>Message to {props.boxLabel}</h1>
            <textarea onChange={(event) => handleMessageChange(event)}></textarea>
            <div className={styles.valuesDiv}>
                <div>
                    <span>{props.keyType} key</span>
                    <input type="text" id="encryption-key" onChange={event=>handleKeyChange(event)}/>
                </div>
                <span>Algorithm</span>
                <select name="algorithm" value={algorithm} onChange={(event) => {changeAlgorithm(event)}}>
                    <option value="otp" >OTP</option>
                    <option value="three_des">3DES</option>
                    <option value="aes">AES</option>
                    <option value="rsa">RSA</option>
                </select>
            </div>
        </div>
    );
}

export default InputBox;