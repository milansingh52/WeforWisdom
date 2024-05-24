// var commonValues =
// {
//     Fruits: ["Apple", "Mango"],
//     Vegetables: ['Brinjal', 'Carrot'],
//     Countries: ["india", "US"]
// }
// function changeDropdownValue(value) {
//     if (value.length == 0) {
//         document.getElementById('category').innerHTML = "<option></option>";
//         alert("hello")
//     }
//     else {
//         var commonOptions = "";
//         for (categoryID in commonValues[value]) {
//             commonOptions += "<option>" + commonValues[value][categoryID] + "</option>"
//         }
//         document.getElementById('category').innerHTML = commonOptions
//     }
// }

// alert('hello')
// colsole.log("hello")

// To access the stars
// let stars = document.getElementsByClassName("star");
// let output = document.getElementById("output");
// let v = document.getElementById('value');

// // Funtion to update rating
// function gfg(n) {
//     remove();
//     for (let i = 0; i < n; i++) {
//         if (n == 1) {
//             cls = "one";
//             v.value = 1;
//         }
//         else if (n == 2) {
//             cls = "two";
//             v.value = 2;
//         }
//         else if (n == 3) {
//             cls = "three";
//             v.value = 3;
//         }
//         else if (n == 4) {
//             cls = "four";
//             v.value = 4;
//         }
//         else if (n == 5) {
//             cls = "five";
//             v.value = 5;
//         }
//         stars[i].className = "star " + cls;
//     }
//     output.innerText = "Rating is: " + n + "/5";
// }

// // To remove the pre-applied styling
// function remove() {
//     let i = 0;
//     while (i < 5) {
//         stars[i].className = "star";
//         i++;
//     }
// }
