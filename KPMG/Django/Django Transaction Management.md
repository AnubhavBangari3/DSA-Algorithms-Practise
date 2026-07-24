## Question 8: Django Transaction Management

### Problem Statement

Explain the purpose of using `transaction.atomic()` in Django.

Consider the following implementation and discuss:

1. Why transactions are used.
2. What happens if an exception occurs.
3. Why serializers are used inside the transaction.
4. Possible improvements to the code.

```python
from django.db import transaction

class PlanService:
    def save_plan(self, request_data, request_user):
        # All database operations inside this block are treated
        # as one transaction.
        with transaction.atomic():

            # Create the main plan record.
            plan = TransPlan.objects.create(
                plan_date=request_data["plan_date"],
                shift=request_data["shift"],
                created_by=request_user
            )

            # Process every mine-face parameter.
            for item in request_data["mine_face_parameters"]:

                # Connect the mine-face record with the created plan.
                item["plan"] = plan.pk

                # Store the user who created the record.
                item["created_by"] = request_user

                # Create a serializer with the mine-face data.
                serializer = MineFaceSerializer(data=item)

                # Validate the data.
                # If validation fails, an exception is raised.
                serializer.is_valid(raise_exception=True)

                # Save the mine-face record in the database.
                mine_face_obj = serializer.save()

                # Process all truck trips belonging to this mine face.
                for trip in item["truck_trips"]:

                    # Prepare the truck-trip data.
                    trip_data = {
                        "mine_face": mine_face_obj.pk,
                        "screening_plant": trip["screening_plant"],
                        "permissible_truck_trips": trip["permissible_trips"]
                    }

                    # Create the truck-trip serializer.
                    trip_serializer = TruckTripSerializer(data=trip_data)

                    # Validate the truck-trip data.
                    # Validation failure raises an exception.
                    trip_serializer.is_valid(raise_exception=True)

                    # Save the truck-trip record.
                    trip_serializer.save()

            # Return the plan after all records are successfully saved.
            return plan
```

## 1. Why are transactions used?

A transaction is used to ensure that all related database operations succeed or fail together.

In this code, the following records are created:

* One `TransPlan`
* Multiple mine-face records
* Multiple truck-trip records

These records are logically connected. Therefore, it would be incorrect to save only some of them.

For example, without a transaction:

```text
Plan created successfully
First mine-face created successfully
First truck trip created successfully
Second truck trip fails
```

The database would contain incomplete data.

Using:

```python
with transaction.atomic():
```

makes all operations part of one transaction.

If all operations succeed, Django commits the changes.

If any operation fails, Django rolls back all database changes made inside the block.

This maintains data consistency and prevents partial records from being saved.

## 2. What happens if an exception occurs?

If an exception occurs inside the `transaction.atomic()` block, Django rolls back all database operations performed inside that block.

For example:

```python
serializer.is_valid(raise_exception=True)
```

raises an exception when the input data is invalid.

Similarly:

```python
trip_serializer.is_valid(raise_exception=True)
```

raises an exception when truck-trip data is invalid.

If an exception occurs after the plan and some related records have already been created, Django removes those records during rollback.

Example:

```text
Plan created
Mine-face 1 created
Truck trip 1 created
Truck trip 2 validation fails
```

Result:

```text
Plan rolled back
Mine-face 1 rolled back
Truck trip 1 rolled back
Truck trip 2 not created
```

Therefore, either all records are saved or none of them are saved.

The exception continues to propagate unless it is caught outside the transaction block.

Example:

```python
try:
    plan = PlanService().save_plan(request_data, request_user)
except Exception as error:
    print(error)
```

## 3. Why are serializers used inside the transaction?

Serializers are used to validate incoming data and create model objects safely.

The serializers perform tasks such as:

* Field validation
* Required-field validation
* Type validation
* Custom validation
* Model creation
* Relationship validation

For example:

```python
serializer = MineFaceSerializer(data=item)
serializer.is_valid(raise_exception=True)
mine_face_obj = serializer.save()
```

The serializer first validates the mine-face data. Only valid data is saved.

The serializers are kept inside the transaction because serializer validation or saving may fail.

If a serializer fails after some records have already been created, the transaction rolls back those previously created records.

Without the transaction, serializer failure could leave partial data in the database.

Using `raise_exception=True` is important because it raises an exception, which causes `transaction.atomic()` to roll back the transaction.

## 4. Possible improvements to the code

### Improvement 1: Do not modify the original request data

The code directly modifies `item`:

```python
item["plan"] = plan.pk
item["created_by"] = request_user
```

This changes the original `request_data`.

A safer approach is to create a copy:

```python
item_data = item.copy()
item_data["plan"] = plan.pk
item_data["created_by"] = request_user
```

### Improvement 2: Remove nested data before passing it to the serializer

The `item` dictionary contains:

```python
item["truck_trips"]
```

If `truck_trips` is not a serializer field, it may cause validation errors.

It is better to remove it before passing the data to `MineFaceSerializer`.

```python
item_data = item.copy()
truck_trips = item_data.pop("truck_trips", [])
```

### Improvement 3: Use `.get()` for safer dictionary access

This code:

```python
request_data["mine_face_parameters"]
```

raises `KeyError` if the key is missing.

A safer approach is:

```python
mine_face_parameters = request_data.get("mine_face_parameters", [])
```

Similarly:

```python
truck_trips = item_data.pop("truck_trips", [])
```

### Improvement 4: Validate all input before creating database records

The current code creates the plan before validating all mine-face and truck-trip data.

Although the transaction will roll back on failure, validating everything first can reduce unnecessary database work.

A parent serializer with nested serializers could validate the complete request before saving anything.

### Improvement 5: Use nested serializers

Instead of manually creating mine-face and truck-trip serializers inside nested loops, a nested serializer can handle the complete structure.

For example:

```python
class TruckTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckTrip
        fields = "__all__"


class MineFaceSerializer(serializers.ModelSerializer):
    truck_trips = TruckTripSerializer(many=True)

    class Meta:
        model = MineFace
        fields = "__all__"
```

A parent plan serializer can then validate and save the complete nested structure.

### Improvement 6: Use `bulk_create()` when appropriate

If many truck-trip records are being created, calling `.save()` inside a loop causes multiple database queries.

`bulk_create()` can reduce the number of queries.

```python
TruckTrip.objects.bulk_create(trip_objects)
```

However, `bulk_create()` may bypass serializer logic, model `save()` methods and some signals, so it should only be used when appropriate.

### Improvement 7: Add explicit exception handling outside the atomic block

The service layer can allow the exception to propagate, while the view handles it and returns a proper API response.

```python
try:
    plan = PlanService().save_plan(request.data, request.user)
    return Response({"plan_id": plan.pk}, status=201)
except serializers.ValidationError as error:
    return Response(error.detail, status=400)
```

The exception should not be silently caught inside the `atomic()` block because doing so may prevent Django from rolling back correctly.

### Improvement 8: Use validated data instead of raw request data

Business logic should ideally receive already validated data rather than directly using raw `request_data`.

This avoids repeated validation and reduces the possibility of missing or malformed fields.

## Improved Version

```python
from django.db import transaction


class PlanService:

    @transaction.atomic
    def save_plan(self, request_data, request_user):
        # Create the main plan.
        plan = TransPlan.objects.create(
            plan_date=request_data["plan_date"],
            shift=request_data["shift"],
            created_by=request_user
        )

        # Safely get the mine-face list.
        mine_face_parameters = request_data.get(
            "mine_face_parameters",
            []
        )

        # Process every mine-face record.
        for item in mine_face_parameters:

            # Copy the dictionary so the original request data
            # is not modified.
            item_data = item.copy()

            # Remove nested truck-trip data before passing
            # the mine-face data to its serializer.
            truck_trips = item_data.pop("truck_trips", [])

            # Add related plan and user information.
            item_data["plan"] = plan.pk
            item_data["created_by"] = request_user.pk

            # Validate and save the mine-face record.
            mine_face_serializer = MineFaceSerializer(
                data=item_data
            )
            mine_face_serializer.is_valid(raise_exception=True)
            mine_face_obj = mine_face_serializer.save()

            # Process every truck trip.
            for trip in truck_trips:
                trip_data = {
                    "mine_face": mine_face_obj.pk,
                    "screening_plant": trip["screening_plant"],
                    "permissible_truck_trips": trip[
                        "permissible_trips"
                    ]
                }

                # Validate and save the truck-trip record.
                trip_serializer = TruckTripSerializer(
                    data=trip_data
                )
                trip_serializer.is_valid(raise_exception=True)
                trip_serializer.save()

        # Transaction is committed when this method
        # completes without an exception.
        return plan
```

## `with transaction.atomic()` vs `@transaction.atomic`

Both approaches provide the same transaction behavior.

Using a context manager:

```python
def save_plan(self, request_data, request_user):
    with transaction.atomic():
        # Database operations
        pass
```

Using a decorator:

```python
@transaction.atomic
def save_plan(self, request_data, request_user):
    # Database operations
    pass
```

Use the decorator when the whole method should run inside one transaction.

Use the context manager when only a specific part of the method should be transactional.

## Time Complexity

Let:

```text
m = number of mine-face records
t = total number of truck-trip records
```

The loop complexity is:

```text
O(m + t)
```

However, each serializer save performs database operations, so the total database-query cost depends on the number of records.

## Space Complexity

The additional space complexity is approximately:

```text
O(1)
```

excluding input data and created database objects.

If all objects are collected for `bulk_create()`, the space complexity may become:

```text
O(m + t)
```

## Final Interview Answer

`transaction.atomic()` ensures that all related database operations are executed as one unit. In this example, the plan, mine-face records and truck-trip records must all be created successfully. If any serializer validation or database operation raises an exception, Django rolls back every database change made inside the transaction, preventing partial or inconsistent data.

Serializers are used inside the transaction to validate input data and create model instances. Since `is_valid(raise_exception=True)` raises an exception on invalid data, it automatically triggers the transaction rollback.

The code can be improved by avoiding modification of the original request data, separating nested `truck_trips` before serializer validation, using `.get()` for optional fields, validating the full request before saving, using nested serializers and considering `bulk_create()` when large numbers of records are involved.
