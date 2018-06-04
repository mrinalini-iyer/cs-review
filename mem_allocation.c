/* Metadata to be maintained for keeping track of freed memory, to resue for new malloc calls. */
struct block_meta {
size_t size;
struct block_meta *next;
int free;
int magic; // magic for debugging purpose
};

/* Malloc implementation using syscall sbrk. 
 * sbrk(0) - return the current top of stack.
 * sbrk(foo) - allocates foo size from the heap and returns previous top of heap.
 */  
void * malloc (size_t size)
{


}

void free (void *free_ptr)
{

}
