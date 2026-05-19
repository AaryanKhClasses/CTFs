#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>

// Custom VM opcodes
#define OP_LOAD  0x42
#define OP_XOR   0x73
#define OP_ROL   0x91
#define OP_ADD   0xA5
#define OP_CHECK 0xC3

typedef struct {
    uint8_t opcode;
    uint32_t operand;
} VMInstruction;

// Obfuscated bytecode - encodes the validation logic
uint8_t vm_bytecode[] = {
    0x42, 0x13, 0x37, 0x42, 0x00,  // LOAD magic values
    0x73, 0xDE, 0xAD, 0xBE, 0xEF,  // XOR operations
    0x91, 0x07, 0x00, 0x00, 0x00,  // ROL 7
    0xA5, 0x42, 0x13, 0x00, 0x00,  // ADD
    0xC3, 0x00, 0x00, 0x00, 0x00   // CHECK
};

uint32_t hidden_key_parts[] = {
    0x13376942, 0xDEADBEEF, 0xCAFEBABE, 
    0x8BADF00D, 0xFEEDFACE
};

// VM state
typedef struct {
    uint32_t regs[8];
    uint32_t pc;
    uint8_t flag;
} VMState;

void init_vm(VMState *vm) {
    memset(vm, 0, sizeof(VMState));
}

// Obfuscated execution
uint32_t execute_vm(VMState *vm, uint8_t *code, size_t len, uint32_t input) {
    vm->regs[0] = input;
    
    for (size_t i = 0; i < len; i += 5) {
        uint8_t op = code[i];
        uint32_t operand = *(uint32_t*)(code + i + 1);
        
        switch(op) {
            case OP_LOAD:
                vm->regs[1] = operand;
                break;
            case OP_XOR:
                vm->regs[0] ^= operand;
                break;
            case OP_ROL:
                vm->regs[0] = (vm->regs[0] << operand) | (vm->regs[0] >> (32 - operand));
                break;
            case OP_ADD:
                vm->regs[0] += operand;
                break;
            case OP_CHECK:
                return vm->regs[0];
        }
    }
    return 0;
}

// Multi-stage validation
int validate_key(const char *key) {
    if (strlen(key) != 32) return 0;
    
    // Stage 1: Checksum
    uint32_t checksum = 0;
    for (int i = 0; i < 32; i++) {
        checksum = (checksum << 5) + checksum + key[i];
    }
    if (checksum != 0x7E4A8C9F) return 0;
    
    // Stage 2: VM validation on chunks
    VMState vm;
    uint32_t chunks[4];
    
    for (int i = 0; i < 4; i++) {
        uint32_t chunk = 0;
        for (int j = 0; j < 8; j++) {
            chunk = (chunk << 8) | key[i*8 + j];
        }
        init_vm(&vm);
        chunks[i] = execute_vm(&vm, vm_bytecode, sizeof(vm_bytecode), chunk);
    }
    
    // Stage 3: Cross-validation with hidden keys
    for (int i = 0; i < 4; i++) {
        if ((chunks[i] ^ hidden_key_parts[i]) != 0x42424242) return 0;
    }
    
    return 1;
}

int main(int argc, char **argv) {
    printf("╔══════════════════════════════════════╗\n");
    printf("║   CultRang VM License Validator     ║\n");
    printf("║   Inter IIT RE Challenge             ║\n");
    printf("╚══════════════════════════════════════╝\n\n");
    
    if (argc != 2) {
        printf("Usage: %s <license_key>\n", argv[0]);
        return 1;
    }
    
    printf("Validating key: %s\n", argv[1]);
    
    if (validate_key(argv[1])) {
        printf("\n✓ Valid license key!\n");
        printf("\nFlag: CultRang{%s}\n", argv[1]);
        return 0;
    } else {
        printf("\n✗ Invalid license key!\n");
        return 1;
    }
}