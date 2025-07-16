
function predictDiabetes() {
      console.log("predictDiabetes called");
    var prg = document.getElementsByName('prg')[0].value;
    var glc = document.getElementsByName('glc')[0].value;
    var bp  = document.getElementsByName('bp')[0].value;
    var st  = document.getElementsByName('st')[0].value;
    var insulin = document.getElementsByName('insulin')[0].value;
    var bmi = document.getElementsByName('bmi')[0].value;
    var dpf = document.getElementsByName('Dpf')[0].value;
    var age = document.getElementsByName('age')[0].value;
    var resultDiv = document.getElementById('result');

     var url = "http://127.0.0.1:5000/predict"

    $.post(url, {
        prg: prg,
        glc: glc,
        bp: bp,
        st: st,
        insulin: insulin,
        bmi: bmi,
        Dpf: dpf,
        age: age
    }, function(data, status) {
        resultDiv.innerHTML = "<h2>Prediction: " + (data.prediction == 1 ? "Diabetic" : "Non-Diabetic") + "</h2>";
    }).fail(function(xhr, status, error) {
        resultDiv.innerHTML = "<h2 style='color:red;'>Error: " + error + "</h2>";
    });
}

