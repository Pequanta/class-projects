import styles from "./components.module.css"
function InputBox(props){
    return(
        <div className={styles.inputDiv}>
            <h1>Message to {props.boxLabel}</h1>
            <textarea></textarea>
            <div className={styles.valuesDiv}>
                <div>
                    <span>{props.keyType} key</span>
                    <input type="text" />
                </div>
                <span>Algorithm</span>
                <select name="algorithm" id="">
                    <option name="otp" id="">OTP</option>
                    <option name="des" id="">3DES</option>
                    <option name="aes" id="">AES</option>
                </select>
            </div>
        </div>
    );
}

export default InputBox;