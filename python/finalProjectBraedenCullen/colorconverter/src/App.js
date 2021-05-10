import './App.css';

function ImageForm(props) {
  return (
    <div>
      <h1>
        test
      </h1>
      <label for="image">{props.name}</label>
      <input type="image" id="image" alt="Photo"/>

    </div>
  )
}

function App() {
  return (
    <div className="App">
      <ImageForm name="pp" />
    </div>
  );
}

export default App;
