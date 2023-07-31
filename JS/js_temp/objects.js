let test_object = {red:1,blue:2,green:3}
console.log(test_object)
console.log(test_object.red,test_object['blue'],test_object.green)

test_object['orange'] = 3
console.log('assigned new k/v pairs ',test_object)

test_object.red += 10
console.log('changing a value ',test_object)

keys = []
for (let key in test_object) keys.push(key)
console.log('keys ',keys)

keys2 = []
for (let key2 of Object.keys(test_object)) keys2.push(key2) ;
console.log('keys alt ',keys2)

key_value_pair = []
for (let [key,value] of Object.entries(test_object)) key_value_pair.push(key+' : '+value)
console.log('working with key/value pairs ',key_value_pair)

let test_object2 = structuredClone(test_object)
test_object2.red = 33
console.log(test_object,test_object2)
