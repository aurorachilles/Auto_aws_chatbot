def finalize(val: list[str]) -> bool or list[str]:
    instance_type = val[0]
    instance_image = val[1]
    storage_type = val[2]
    security_g = val[3]
    min_count = val[4]
    max_count = val[5]
    key_name = val[6]
    instance_name = val[7]

    print("You Instance details are as follows:")
    print("Instance Type: ", instance_type)
    print("Instance Image: ", instance_image)
    print("Storage Type: ", storage_type)
    print("Security Group: ", security_g)
    print("Min Count: ", min_count)
    print("Max Count: ", max_count)
    print("Key Name: ", key_name)
    print("Instance Name: ", instance_name)

    conf = input("Do you want to create this instance? (y/n): ")

    if conf.lower() == "y":
        return [instance_type, instance_image, storage_type, security_g, min_count, max_count, key_name, instance_name]
    else:
        print("Instance Creation Cancelled")
        print("Terminating the program")