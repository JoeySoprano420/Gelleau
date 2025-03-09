from llvmlite import ir, binding

# Initialize LLVM
binding.initialize()
binding.initialize_native_target()
binding.initialize_native_asmprinter()

# LLVM Module Setup
module = ir.Module(name="gelleau")
fnty = ir.FunctionType(ir.IntType(64), [ir.IntType(64), ir.IntType(64)])
func = ir.Function(module, fnty, name="sum")

block = func.append_basic_block(name="entry")
builder = ir.IRBuilder(block)

# Implement sum function
a, b = func.args
result = builder.add(a, b)
builder.ret(result)

# Compile and print IR
print(module)


