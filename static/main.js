// console.log('Hello')

// // Fetch data from the data route defined in flask server
// fetch('./data').then((res) => {
//   // return res.json()
//   return res.text()
// }).then((text) => {
//   const json = JSON.parse(text)
//   const data = json.children.map((item) => ({
//     x: item.value, 
//     y: item.price, 
//     r: item.volume / 100000, 
//     label: item.name
//   }))
//   const labels = json.children.map((item) => item.name)
//   const h = 360 / data.length
//   const colors = json.children.map((item, i) => `hsl(${Math.round(h * i)}, 50%, 50%, 0.5)`)
//   console.log(colors)
//   makeChart(data, labels, colors)
// }).catch((err) => {
//   console.log('******** Error ********')
//   console.log(err.message)
// })


// var ctx = document.getElementById("myChart");

// function makeChart(x, labelsArray, colorsArray) {
//   var myChart = new Chart(ctx, {
//       type: 'bubble',
//       data: {
//           labels: labelsArray,
//           datasets: [{
//               label: 'Volume of shares',
//               data: x,
//               backgroundColor: colorsArray,
//               borderColor: colorsArray,
//               borderWidth: 1
//           }]
//       },
//       options: {
//           scales: {
//               yAxes: [{
//                   ticks: {
//                       beginAtZero:true
//                   }
//               }]
//           }
//       }
//   });
// }