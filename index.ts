import { cc } from "bun:ffi";

export const {
  symbols: { myRandom },
} = cc({
  source: "./myRandom.c",
  symbols: {
    myRandom: {
      returns: "int",
      args: [],
    },
  },
});

console.log("myRandom() =", myRandom());