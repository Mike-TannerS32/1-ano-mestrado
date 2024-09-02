const zip = (a,b) => a.map((k,i)=> [k, b[i]])
let inputs = [1,2,3, 2.5];

let weights = [[0.2, 0.8, -0.5, 1.0],
                [0.5, -0.91, 0.26, -0.5],
                [-0.26, -0.27, 0.17, 0.87]];

let biases = [2, 3, 0.5];

let layer_outputs = []

let neuron_output;
for(let [neuron_weights, neuron_bias] of zip(weights, biases)){
    neuron_output = 0
    for(let [n_input, weight] of zip(inputs, neuron_weights)){
        neuron_output += n_input*weight;
    }
    neuron_output += neuron_bias;
    layer_outputs.push(neuron_output)
}
console.log(layer_outputs)