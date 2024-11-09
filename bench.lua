local ffi = require "ffi"

local mylib = ffi.load "myRandom"

ffi.cdef[[
    int myRandom();
]]

print("myRandom() = " .. mylib.myRandom())

local start = os.clock()
local n = 1000000
for i = 1, n do
    mylib.myRandom()
end
local t = os.clock() - start
print("Total time: " .. t .. "s (" .. n .. " iterations)")
print("" .. t/n * 1e9 .. " ns/iter")