function calc(arr){
    let operation;
    for (var i = arr.length; i > 0; i){
        if(arr[i] == '*'){
            arr.splice(i-1,3,(arr[i-1])*(arr[i+1]))
        }
        if(arr[i] == '/'){
            arr.splice(i-1,3,(arr[i-1])/(arr[i+1]))
        }
        if(arr[i] == '-'){
            arr.splice(i-1,3,(arr[i-1])-(arr[i+1]))
        }
        if(arr[i] == '+'){
            arr.splice(i-1,3,(arr[i-1])+(arr[i+1]))
        }
    }
    return arr
}

console.log(calc([1, '+', 2, '*', 5, '-', 3, '/', 2, '+', 1]))