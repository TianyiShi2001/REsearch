suppliers = {
  B: "Life Technologies",
  C: "Minotech Biotechnology",
  E: "Agilent Technologies",
  I: "SibEnzyme Ltd.",
  J: "Nippon Gene Co., Ltd.",
  K: "Takara Bio Inc.",
  M: "Roche Applied Science",
  N: "New England Biolabs",
  O: "Toyobo Biochemicals",
  Q: "Molecular Biology Resources - CHIMERx",
  R: "Promega Corporation",
  S: "Sigma Chemical Corporation",
  V: "Vivantis Technologies",
  X: "EURx Ltd.",
  Y: "SinaClon BioScience Co."
};

supplierKeys = Object.keys(suppliers);

// show legend
legendArray = [];
supplierKeys.forEach(function(key) {
  legendStr = `${key}: ${suppliers[key]}`;
  legendArray.push(legendStr);
});
document.getElementById("legend").innerText = legendArray.join("|");

// expand table
supplierKeys = Object.keys(suppliers);
for (let i = 0; i < supplierKeys.length; i++) {
  const e = supplierKeys[i];
  $("#result-header").append(`<th id="${e}">${e}</th>`);
  $("#result-body tr").append(`<td class="supplier-cell ${e}"></td>`);
}

// color suppliers
enzymeRows = document.querySelectorAll("#result-body tr");
for (let i = 0; i < enzymeRows.length; i++) {
  const row = enzymeRows[i];
  row.classList.forEach(
    c => (row.getElementsByClassName(c)[0].style.backgroundColor = "green")
  );
}
