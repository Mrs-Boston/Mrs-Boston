import radioactivedecay as rd

material=rd.Nuclide('Co-60')
material.half_life('y')
t0=rd.InventoryHP({'Co-60':100.0})
t1=t0.decay(1.0,'y')
print(t1)


def decay():
    material=input("enter the material (ie Co-60):")
    amount=input("enter the amount of the material: ")
    timeunit=input("enter the time unit (s for sec, y for year, etc): ")
    time=input("enter the length of time: ")
    to=rd.InventoryHP({material:amount})
    print(t0.decay(time,timeunit))

count=0
while count==0:

    try:
        decay()
        break
    except Exception:
        print("\n Something's not quite right!\n")
        yn=input("Do you want to try again? (y/n): \n")
        if yn.lower() != 'y':
            count==1

    