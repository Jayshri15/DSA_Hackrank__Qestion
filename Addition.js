var number1 = [20, 45, 78, 6, 19];
var number2 = [2,6,9,7,0];
vb = [];
for(var i in number1) {  
    var so =(number1[i] += number2[i]);
    vb.push(so);
}
console.log(vb);