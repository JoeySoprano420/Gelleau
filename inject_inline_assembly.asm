.section .text
.global _start
_start:
    mov rax, 5    # Load value into register
    add rax, 10   # Add another value
    ret           # Return result
