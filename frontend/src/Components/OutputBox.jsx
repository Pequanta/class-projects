import styles from './components.module.css'
function OutputBox(props){ 
    return(
        <div className={styles.outputMain}>
            <span>{props.message}</span>
        </div>
    );
}

export default OutputBox;