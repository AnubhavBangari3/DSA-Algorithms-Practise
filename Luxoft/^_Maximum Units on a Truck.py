class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        # Sort box types in descending order
        # based on units per box.
        boxTypes.sort(key=lambda x: -x[1])

        # Stores the maximum units loaded onto the truck.
        total_units = 0

        # Process box types with the highest units first.
        for number_of_boxes, units_per_box in boxTypes:

            # Stop if the truck is already full.
            if truckSize == 0:
                break

            # Take as many boxes as possible from
            # the current box type.
            boxes_taken = min(truckSize, number_of_boxes)

            # Add the units contributed by these boxes.
            total_units += boxes_taken * units_per_box

            # Reduce the remaining truck capacity.
            truckSize -= boxes_taken

        return total_units
    
'''
Algorithm

1. Sort all box types in descending order of units per box.

2. Initialize total units as 0.

3. Traverse each box type.

4. If the truck is full:
   - Stop.

5. Take the maximum possible boxes from the current type:
   - boxes_taken = min(truckSize, number_of_boxes)

6. Add:
   - boxes_taken × units_per_box
   to the answer.

7. Reduce the remaining truck capacity.

8. Continue until the truck becomes full or all box types are processed.

9. Return the total units.

Pattern:
Greedy

Time Complexity: O(n log n)

Space Complexity: O(1)
'''