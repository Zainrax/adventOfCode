const file = await Deno.readTextFile("./input.txt");
let input = file.split("\n");
const target = 2020;
const table = {};

input.forEach((item) => {
  const num = parseInt(item, 10);
  table[num] = target - num;
});
