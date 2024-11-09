local ffi = require "ffi"

local mylib = ffi.load "myRandom"

ffi.cdef[[
    int myRandom();
]]

print("myRandom() = " .. mylib.myRandom())